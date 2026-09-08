const DEFAULTS = Object.freeze({
  reprocessVariables: true,
  rereadInitialVariables: true,
  retryExtraModelParse: true,
  '重新处理变量': true,
  '重新读取初始变量': true,
  '重试额外模型解析': true,
});

async function loadBundle() {
  try {
    await import('https://cdn.jsdelivr.net/gh/MagicalAstrogy/MagVarUpdate/artifact/bundle.js');
  } catch (error) {
    await import('https://testingcf.jsdelivr.net/gh/MagicalAstrogy/MagVarUpdate/artifact/bundle.js');
  }
}

async function waitForMvuReady() {
  if (typeof waitGlobalInitialized === 'function') {
    return await waitGlobalInitialized('Mvu');
  }
  const started = Date.now();
  while (!window.Mvu && Date.now() - started < 8000) {
    await new Promise(resolve => setTimeout(resolve, 50));
  }
  return window.Mvu;
}

function applyMvuDefaults(mvu) {
  if (!mvu || typeof mvu !== 'object') return;
  try {
    mvu.settings = Object.assign({}, mvu.settings || {}, DEFAULTS);
  } catch (e) { /* settings 注入失败不阻断运行 */ }
}

await loadBundle();
const Mvu = await waitForMvuReady();
applyMvuDefaults(Mvu);
