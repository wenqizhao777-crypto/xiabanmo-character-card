const ACT_ENTRY_RE = /剧情·卷一(幕\d{2}|终章)/;

function actKeyOf(node) {
  const m = /卷一·(幕\d{2}|终章)/.exec(String(node || ''));
  return m ? m[1] : null;
}

let lastKey = null;
let busy = false;

async function waitForMvuReady() {
  if (typeof waitGlobalInitialized === 'function') {
    try { return await waitGlobalInitialized('Mvu'); } catch (e) { /* 转轮询 */ }
  }
  const started = Date.now();
  while (!window.Mvu && Date.now() - started < 10000) {
    await new Promise(r => setTimeout(r, 80));
  }
  return window.Mvu;
}

function resolveWorldbookName() {
  try {
    const names = TavernHelper.getCharWorldbookNames('current');
    if (names && names.primary) return names.primary;
  } catch (e) { /* 落到全量扫描 */ }
  try {
    const all = TavernHelper.getWorldbookNames();
    if (Array.isArray(all)) {
      const hit = all.find(n => /魔法少女/.test(String(n)));
      if (hit) return hit;
    }
  } catch (e) { /* 无法定位 */ }
  return null;
}

async function syncActEntries(reason) {
  if (busy) return;
  busy = true;
  try {
    const mvu = window.Mvu;
    if (!mvu || typeof mvu.getMvuData !== 'function') return;
    let node = '';
    try {
      const data = mvu.getMvuData({ type: 'message', message_id: 'latest' });
      node = data && data.stat_data && data.stat_data.主线 ? data.stat_data.主线.当前节点 : '';
    } catch (e) { return; }
    const key = actKeyOf(node);
    if (!key || key === lastKey) return;

    const book = resolveWorldbookName();
    if (!book || typeof TavernHelper.updateWorldbookWith !== 'function') return;

    await TavernHelper.updateWorldbookWith(book, entries => {
      const list = Array.isArray(entries) ? entries : [];
      for (const entry of list) {
        if (!entry || typeof entry.name !== 'string') continue;
        const m = ACT_ENTRY_RE.exec(entry.name);
        if (!m) continue;
        const want = m[1] === key;
        if (entry.enabled !== want) entry.enabled = want;
      }
      return list;
    });
    lastKey = key;
    if (typeof console !== 'undefined') console.info('[主线推进器] 当前轨道:卷一·' + key + '(' + (reason || 'sync') + ')');
  } catch (e) {
    if (typeof console !== 'undefined') console.warn('[主线推进器] 同步失败:', e);
  } finally {
    busy = false;
  }
}

(async () => {
  const mvu = await waitForMvuReady();
  if (!mvu) return;
  await syncActEntries('startup');
  if (typeof eventOn === 'function' && mvu.events) {
    eventOn(mvu.events.VARIABLE_UPDATE_ENDED, () => { syncActEntries('update'); });
    eventOn(mvu.events.VARIABLE_INITIALIZED, () => { lastKey = null; syncActEntries('init'); });
  }
  if (typeof eventOn === 'function' && typeof tavern_events !== 'undefined' && tavern_events.CHAT_CHANGED) {
    eventOn(tavern_events.CHAT_CHANGED, () => { lastKey = null; syncActEntries('chat-changed'); });
  }
})();
