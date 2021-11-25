from os import PathLike
from pathlib import Path
from playwright.sync_api import Page, ChromiumBrowserContext, sync_playwright


# We could also support custom namespaces for the KWs
def execute_user_keyword(page: Page, kw_name: str, *args):
    return page.evaluate(f"rfbrowser_kw.{kw_name}", [page, args])

# IF we do this at library import like with the current style we can probably also put the KW names in some list
def import_js_extension(context: ChromiumBrowserContext, filename: PathLike):
    with open(filename, 'r', encoding='UTF-8') as f:
        script = f.read()

    # Do this for every context that the library opens. We will need an implementation of PlaywrightState anyway to keep our current auto closing / opening
    context.add_init_script(script)

with sync_playwright() as p:
    browser_type = p.chromium
    browser = browser_type.launch()
    context = browser.new_context()
    
    # In RFBrowser we will handle this automatically for contexts. User gives extension modules at library import time or some other time and then they will affect all current and future contexts.
    import_js_extension(context, Path("funky.js"))
    page = context.new_page()
    page.goto('http://whatsmyuseragent.org/')
    print(execute_user_keyword(page, "myFunkyKeyword", "My IP Address"))
    
    page.screenshot(path=f'example-{browser_type.name}.png')
    browser.close()
