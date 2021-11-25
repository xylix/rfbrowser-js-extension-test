// HAS to match the file name without the .js extension
const funky = {
  myFunkyKeyword: async function (page, args) {
    // TODO: uncomment when figure out how to get this workign
    // const h = await page.$(args[0]);
    // logger("Logging something funky");
    // return await h.evaluate((e) => e.textContent = "Funk yeah!");
    return "simple"
  },
  createRemoteBrowser: async function (page, args, logger, playwright) {
      logger("Launching chromium server");
      let browserServer = await playwright.chromium.launchServer({headless: false});
      logger("Returning server address");
      return browserServer.wsEndpoint();
  },

  closeRemoteBrowser: async function () {
    return browserServer.kill();
  },

  crashKeyword: function () {
    throw Error("Crash");
  }

}

if (!window.rfbrowser_kw) {
  window.rfbrowser_kw = {}
}

Object.assign(window.rfbrowser_kw, funky)
