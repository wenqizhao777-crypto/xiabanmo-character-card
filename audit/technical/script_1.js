let registerMvuSchema;
try {
  ({ registerMvuSchema } = await import(
    'https://cdn.jsdelivr.net/gh/StageDog/tavern_resource/dist/util/mvu_zod.js'
  ));
} catch (error) {
  ({ registerMvuSchema } = await import(
    'https://testingcf.jsdelivr.net/gh/StageDog/tavern_resource/dist/util/mvu_zod.js'
  ));
}

// ---------- 辅助 ----------
function isPlainObject(value) {
  return value && typeof value === 'object' && !Array.isArray(value);
}
function cloneData(raw) {
  try { return JSON.parse(JSON.stringify(raw)); } catch (e) { return raw; }
}
const LooseString = (fallback = '') => z.preprocess(
  v => (v === undefined || v === null || v === '' ? fallback : String(v)),
  z.string()
).prefault(fallback);
const Num = (min, max, fallback) => z.coerce.number()
  .transform(v => _.clamp(Number.isFinite(v) ? v : fallback, min, max))
  .prefault(fallback);
const StrList = () => z.array(
  z.preprocess(v => (v === undefined || v === null ? '' : String(v)), z.string())
).prefault([]);
const EnumOr = (values, fallback) => z.enum(values).catch(fallback).prefault(fallback);

// ---------- 子结构 ----------
const 魔装Schema = z.object({
  名称: LooseString(),
  形态: LooseString(),
  完损: EnumOr(['', '完好', '受损', '严重受损', '崩毁'], ''),
}).passthrough().prefault({});

const 心核Schema = z.object({
  形态: EnumOr(['', '心之花', '心之种', '心之芽', '心之宝石'], ''),
  状态: EnumOr(['', '完好', '裂纹', '碎裂'], ''),
}).passthrough().prefault({});

const 人物Schema = z.object({
  本名: LooseString(),
  代号: LooseString(),
  阵营: LooseString(),
  身份: LooseString(),
  开华阶段: EnumOr(['无', '种', '芽', '叶', '蕾', '花'], '无'),
  变身状态: EnumOr(['未变身', '变身', '特殊形态'], '未变身'),
  魔力: Num(0, 100, 100),
  伤势: EnumOr(['无伤', '轻伤', '重伤', '濒危'], '无伤'),
  魔装: 魔装Schema,
  心核: 心核Schema,
  当前位置: LooseString(),
  当前行动: LooseString(),
  特殊状态: StrList(),
}).passthrough().prefault({});

const 敌人Schema = z.object({
  名称: LooseString(),
  等级: EnumOr(['卵', '蠖', '蛹', '蜕', '半蜕', '王蜕', '羽', '其他'], '其他'),
  状态: LooseString(),
}).passthrough().prefault({});

// ---------- 顶层归一化 ----------
function normalizeRoot(raw) {
  const root = cloneData(raw);
  if (!isPlainObject(root)) return raw;
  if (isPlainObject(root.玩家) && !isPlainObject(root.user)) {
    root.user = root.玩家;
    delete root.玩家;
  }
  if (isPlainObject(root.人物) && !isPlainObject(root.在场人物)) {
    root.在场人物 = root.人物;
    delete root.人物;
  }
  return root;
}

// ---------- 顶层 Schema(10 容器) ----------
export const Schema = z.preprocess(normalizeRoot, z.object({
  世界: z.object({
    日期: LooseString('女王历1999年·初春'),
    时段: LooseString('清晨'),
    地点: LooseString('方亭市'),
    场景: LooseString(),
    天气: LooseString('晴'),
  }).passthrough().prefault({}),

  主线: z.object({
    当前节点: LooseString('卷一·幕01·开端'),
    已达成节点: StrList(),
    篇章提要: LooseString(),
  }).passthrough().prefault({}),

  user: z.object({
    姓名: LooseString(),
    性别: LooseString(),
    年龄: LooseString(),
    身份: LooseString(),
    原作绑定: LooseString(),
    背景: LooseString(),
    外观: LooseString(),
    装束: LooseString(),
    代号: LooseString(),
    认证牌: EnumOr(['无', '白牌', '字牌', '花牌'], '无'),
    开华阶段: EnumOr(['无', '种', '芽', '叶', '蕾', '花'], '无'),
    变身状态: EnumOr(['未变身', '变身', '特殊形态'], '未变身'),
    魔力: Num(0, 100, 100),
    伤势: EnumOr(['无伤', '轻伤', '重伤', '濒危'], '无伤'),
    魔装: 魔装Schema,
    心核: 心核Schema,
    状态效果: StrList(),
  }).passthrough().prefault({}),

  在场人物: z.record(z.string(), 人物Schema).prefault({}),
  不在场人物: z.record(z.string(), 人物Schema).prefault({}),

  关系: z.record(z.string(), z.object({
    好感: Num(0, 200, 0),
    关系: LooseString('陌生'),
    称呼: LooseString(),
  }).passthrough().prefault({})).prefault({}),

  图鉴: z.object({
    已解锁CG: StrList(),
  }).passthrough().prefault({}),

  检定: z.object({
    本回合: z.object({
      行动: LooseString('无'),
      骰值: Num(0, 20, 0),
      判定: EnumOr(['无', '大成功', '成功', '勉强', '失败', '大失败'], '无'),
      缘由: LooseString(),
    }).passthrough().prefault({}),
    战斗中: z.coerce.boolean().prefault(false),
    敌人: z.array(敌人Schema).prefault([]),
  }).passthrough().prefault({}),

  事件: z.object({
    进行中: z.array(z.object({
      名称: LooseString(),
      进展: LooseString(),
    }).passthrough().prefault({})).prefault([]),
    大事记: StrList(),
  }).passthrough().prefault({}),

  持有物: z.record(z.string(), z.object({
    描述: LooseString(),
    数量: Num(0, 9999, 1),
  }).passthrough().prefault({})).prefault({}),
}).passthrough());

// ---------- 注册(必须等 DOM 就绪) ----------
$(() => {
  registerMvuSchema(Schema);
});
