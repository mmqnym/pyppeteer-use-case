import asyncio
import os
from pyppeteer import launch
from pyppeteer_stealth import stealth
from env_logger import EnvLogger

class Tracker:
    def __init__(self) -> None:
        ''' Keep browser active and only use one page. '''

        self._browser_is_running = False
        self._browser = None
        self._page = None
        self._logger = EnvLogger('Tracker')
    # __init__()

    async def launch_browser(self) -> None:
        ''' Launch bowser and keep active. '''

        if self.__browser_is_running:
            self._logger.warning( 'Browser is executing.' )
            return
        # if

        # It is recommended to use the latest version of chromium browser.
        self._browser = await launch(
                            headless = True,
                            # executablePath = f'{os.getcwd()}\chromium\chrome.exe',
                            args = ['--start-maximized', '--no-sandbox', '--disable-infobars'],
                            autoClose = False 
        )

        self._page = await self._browser.newPage()
        await self._page.setViewport({'width': 2048, 'height': 1080})
        await self._page.evaluateOnNewDocument( 'delete navigator.__proto__.webdriver ;' )
        await self._page.setUserAgent(
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        )
        await stealth(self._page)
        self._browser_is_running = True
    # launch_browser()

    async def get_page_img(self):
        await self._page.goto('http://example.com')
        await self._page.screenshot({'path': 'example.png'})

    # get_page_img()

    async def close_browser(self) -> None:
        if not self._browser_is_running:
            self._logger.warning('Browser is closing.')
            return
        # if

        await self._browser.close()
        self._browser_is_running = False
    # close_browser()
# Tracker

async def main() -> None:
    ''' A series of script. '''

    tracker = Tracker()
    await tracker.launch_browser()
    await tracker.get_page_img()

    # ...

    await tracker.close_browser()
# main()

asyncio.get_event_loop().run_until_complete(main())
