import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';

const root = path.dirname(fileURLToPath(import.meta.url));
const project = path.dirname(root);
const hash = data => crypto.createHash('sha256').update(data).digest('hex');
function local(name) {
  assert(!path.isAbsolute(name) && !name.split(/[\\/]/).includes('..'), 'Unsafe local path');
  const target = path.resolve(root, name);
  assert(target.startsWith(root + path.sep), 'Output outside prototype');
  let parent = target;
  while (parent !== root) {
    if (fs.existsSync(parent)) assert(!fs.lstatSync(parent).isSymbolicLink(), 'Symlinks are not supported');
    parent = path.dirname(parent);
  }
  return target;
}
const read = name => fs.readFileSync(local(name), 'utf8').replace(/^\uFEFF/, '');
const json = name => JSON.parse(read(name));
function writeNew(name, data) {
  const target = local(name);
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.writeFileSync(target, data, { encoding: 'utf8', flag: 'wx' });
}
function tree(dir) {
  const rows = [];
  function walk(folder) {
    for (const entry of fs.readdirSync(folder, { withFileTypes: true }).sort((a,b) => a.name.localeCompare(b.name, 'en'))) {
      const full = path.join(folder, entry.name);
      assert(!entry.isSymbolicLink(), 'Protected source symlink: ' + full);
      if (entry.isDirectory()) walk(full);
      else if (entry.isFile()) rows.push([path.relative(project, full).replaceAll('\\', '/'), hash(fs.readFileSync(full))]);
    }
  }
  walk(path.join(project, dir));
  return { files: rows.length, sha256: hash(JSON.stringify(rows)) };
}
const protectedSnapshot = () => Object.fromEntries(['source','current','audit','canon','final'].map(dir => [dir, tree(dir)]));
function assemble() {
  const config = json('source/card.json');
  assert.equal(config.primaryType, 'text');
  const data = { ...config.data };
  for (const [field, source] of Object.entries(config.fields)) data[field] = read(source).trim();
  data.alternate_greetings = config.alternates.map(source => read(source).trim());
  return { config, card: { spec: 'chara_card_v2', spec_version: '2.0', data } };
}
function parseRecord(message) {
  assert.equal(message.split('【行程记录】').length - 1, 1, 'Exactly one state record');
  assert.equal(message.split('【记录结束】').length - 1, 1, 'Exactly one state terminator');
  const block = message.split('【行程记录】')[1].split('【记录结束】')[0];
  const entries = block.trim().split(/\r?\n/).map(line => {
    const separator = line.indexOf('：');
    assert(separator > 0, 'State line requires a key');
    return [line.slice(0, separator), line.slice(separator + 1).trim()];
  });
  assert.equal(new Set(entries.map(([key]) => key)).size, entries.length, 'Duplicate state field');
  const record = Object.fromEntries(entries);
  for (const key of ['路线','阶段','时地','玩家','伤势','魔力','本领','关系','已知','纪要','下步']) assert(record[key], 'Missing state field: ' + key);
  assert.equal(entries.length, 11, 'Unexpected state fields');
  return record;
}
function validate(card, config) {
  assert.equal(card.spec, 'chara_card_v2');
  assert.equal(card.spec_version, '2.0');
  for (const field of ['name','description','personality','scenario','first_mes','mes_example','creator_notes','system_prompt','post_history_instructions','creator','character_version']) assert.equal(typeof card.data[field], 'string', field);
  assert(Array.isArray(card.data.tags));
  assert.equal(card.data.alternate_greetings.length, 1);
  assert.equal(card.data.character_version, config.version);
  assert.deepEqual(card.data.extensions, {});
  assert.equal(card.data.system_prompt, '');
  assert.equal(card.data.post_history_instructions, '');
  assert(!('character_book' in card.data), 'This text prototype does not use conditional worldbook routing');
  const all = JSON.stringify(card);
  assert(!/<script|<iframe|https?:\/\/|<initvar>|<UpdateVariable>|\bfetch\s*\(|\beval\s*\(/i.test(all), 'Unexpected runtime or remote dependency');
  assert(!/tavernweave-guidance-preference|TW_GUIDANCE_LEVEL|[A-Z]:\\\\/.test(all), 'Client preference or local path leaked into card');
  assert(!/\{\{(?!user\}\}|char\}\})/.test(all), 'Unsupported/unresolved macro');
  const rose = parseRecord(card.data.first_mes);
  const oc = parseRecord(card.data.alternate_greetings[0]);
  assert.equal(rose['路线'], '原作·白玫');
  assert.equal(rose['玩家'], '林小璐／白玫');
  assert.equal(oc['路线'], 'OC·改编支线');
  assert.equal(oc['阶段'], '建角待确认');
  assert.equal(oc['玩家'], '待确认');
  assert(oc['纪要'].includes('尚未发生'));
  assert(!rose['已知'].includes('林昀'));
  assert(rose['伤势'].includes('摩可'));
  assert(rose['魔力'].includes('未知'));
  assert(!rose['本领'].includes('掌握运动防御'));
  assert(!oc['本领'].includes('已掌握'));
  const records = json('source/claims.json');
  assert.equal(new Set(records.claims.map(x => x.id)).size, records.claims.length);
  const events = JSON.parse(fs.readFileSync(path.join(project, 'canon/events/records.json'), 'utf8'));
  const eventIDs = new Set(events.map(x => x.id));
  const novelPath = path.join(project, 'source/下班，然后变成魔法少女_第1-282章.txt');
  const novel = fs.readFileSync(novelPath, 'utf8').split(/\r?\n/);
  for (const claim of records.claims) {
    assert(claim.statement && claim.targets.length);
    for (const target of claim.targets) assert(fs.existsSync(local(target)), 'Missing claim consumer');
    if (claim.layer === 'NOVEL_TEXT') {
      assert(claim.ranges.length && claim.anchor);
      const excerpts = claim.ranges.map(([start,end]) => {
        assert(start >= 1 && end >= start && end <= novel.length, 'Invalid source range');
        return novel.slice(start - 1, end).join('\n');
      }).join('\n');
      assert(excerpts.includes(claim.anchor), 'Source anchor mismatch: ' + claim.id);
      for (const id of claim.events) assert(eventIDs.has(id), 'Unknown event reference');
    } else assert(['USER_IF','USER_DESIGN','RP_RULE'].includes(claim.layer));
  }
  const baseline = json('evidence/input-baseline.json');
  assert.deepEqual(protectedSnapshot(), baseline.directories, 'Protected source/current/audit/canon/final changed');
  // Adversarial checks of the state-envelope validator, not simulated model behavior.
  for (const invalid of [card.data.first_mes.replace('魔力：', '能量：'), card.data.first_mes + '\n【行程记录】', card.data.first_mes.replace('路线：原作·白玫', '路线：原作·白玫\n路线：OC·改编支线')]) assert.throws(() => parseRecord(invalid));
  return {
    structuralChecks: 'passed', sourceAnchors: records.claims.filter(x => x.layer === 'NOVEL_TEXT').length,
    totalClaims: records.claims.length, initialStates: 'two-distinct-branches-passed',
    invalidStateEnvelopesRejected: 3, protectedInputs: 'unchanged',
    primaryType: 'text', capabilityFlags: [], hostExtensionsRequired: [], remoteRuntime: [],
    characterBook: 'absent-by-design', fullReasoningOutput: 'not-requested',
    runtime: process.version, modelTokens: 'not-measured',
    promptCharacters: Object.fromEntries(['description','personality','scenario','mes_example'].map(key => [key, [...card.data[key]].length])),
    limitations: ['Source anchors prove references exist, not full semantic fidelity.', 'No model generation, client import, character portrayal, state persistence, or human acceptance has been tested.']
  };
}
const mode = process.argv[2] || '--help';
if (mode === '--help') {
  console.log('node prototype/build.mjs --baseline | --inspect | --check | --build | --verify\n--baseline creates evidence/input-baseline.json once. --inspect/--check/--verify are read-only. --build creates the declared JSON and report once; existing different outputs are refused. No install, network, PNG, deployment or live import.');
} else if (mode === '--baseline') {
  writeNew('evidence/input-baseline.json', JSON.stringify({ capturedAt: new Date().toISOString(), directories: protectedSnapshot() }, null, 2) + '\n');
  console.log('Protected input baseline saved.');
} else {
  assert(['--inspect','--check','--build','--verify'].includes(mode), 'Unknown mode');
  const {config,card} = assemble();
  const output = local(config.output);
  if (mode === '--inspect') console.log(JSON.stringify({ mode, output: config.output, sourceFiles: [...Object.values(config.fields), ...config.alternates], exists: fs.existsSync(output), primaryType: config.primaryType }, null, 2));
  else {
    const checks = validate(card, config);
    const body = JSON.stringify(card, null, 2) + '\n';
    if (mode === '--build') {
      assert(!fs.existsSync(output), 'Output exists; choose a new version for a changed build');
      assert(!fs.existsSync(local(config.report)), 'Evidence report exists');
      writeNew(config.output, body);
      assert.equal(fs.readFileSync(output,'utf8'), body);
      const report = { status: 'offline-artifact-passed', version: config.version, date: new Date().toISOString(), output: config.output, bytes: Buffer.byteLength(body), sha256: hash(body), ...checks, realHost: 'pending-user-import-third-party-client', driver: 'pending' };
      writeNew(config.report, JSON.stringify(report, null, 2) + '\n');
      console.log(JSON.stringify(report, null, 2));
    } else if (mode === '--verify') {
      assert.equal(fs.readFileSync(output,'utf8'), body, 'Artifact/source mismatch');
      assert.equal(json(config.report).sha256, hash(body));
      console.log(JSON.stringify({ status: 'passed', artifactParity: true, sha256: hash(body), ...checks }, null, 2));
    } else console.log(JSON.stringify({ status: 'passed', predictedOutput: config.output, ...checks }, null, 2));
  }
}
