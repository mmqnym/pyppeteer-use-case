import asyncio
import os
from pyppeteer import launch
from pyppeteer_stealth import stealth

async def normal() -> None:
    ''' Normal case. '''

    # It is recommended to use the latest version of chromium browser.
    browser = await launch(
                    headless = False,
                    # defaultViewport = None,
                    # executablePath = f'{os.getcwd()}\chromium\chrome.exe',
                    args = ['--start-maximized', '--no-sandbox', '--disable-infobars'],
                    autoClose = False
              )
    page = await browser.newPage()

    # It can use `defaultViewport = None` to always get maximized page viewport.
    # await page.setViewport({'width': 2048, 'height': 1080})

    # These block for anti-bot.
    await page.evaluateOnNewDocument('delete navigator.__proto__.webdriver ;')
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    )
    await stealth(page)
    
    await page.goto('http://example.com')
    await page.screenshot({'path': 'example.png'})
    
    # element = await page.waitForSelector(id_selector or css_selector, timeout = 6000)
    # element = await page.waitForXPath(xpath, timeout = 6000)

    # element_text = await (await element.getProperty('textContent')).jsonValue()

    await browser.close()
# normal()

asyncio.get_event_loop().run_until_complete(normal())
