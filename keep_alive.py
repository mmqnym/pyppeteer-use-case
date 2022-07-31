import asyncio
import os
from pyppeteer import launch
from pyppeteer_stealth import stealth
from env_logger import EnvLogger

class Tracker:
    def __init__(self) -> None:
        ''' Keep browser active and only use one page. '''

        self.__browser_is_running = False
        self.__browser = None
        self.__page = None
        self.__logger = EnvLogger('Tracker')
    # __init__()

    async def launch_browser(self) -> None:
        ''' Launch bowser and keep active. '''

        if self.__browser_is_running:
            self.__logger.warning( 'Browser is executing.' )
            return
        # if

        # It is recommended to use the latest version of chromium browser.
        self.__browser = await launch(headless = True,
                                      # executablePath = f'{os.getcwd()}\chromium\chrome.exe',
                                      args = ['--start-maximized', '--no-sandbox', '--disable-infobars'],
                                      autoClose = False )

        self.__page = await self.__browser.newPage()
        await self.__page.setViewport({'width': 2048, 'height': 1080})
        await self.__page.evaluateOnNewDocument( 'delete navigator.__proto__.webdriver ;' )
        await self.__page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36' )
        await stealth(self.__page)
        self.__browser_is_running = True
    # launch_browser()

    async def get_page_img(self):
        await self.__page.goto('http://example.com')
        await self.__page.screenshot({'path': 'example.png'})

    # get_page_img()

    async def close_browser(self) -> None:
        if not self.__browser_is_running:
            self.__logger.warning('Browser 已處於未啟用狀態。')
            return
        # if

        await self.__browser.close()
        self.__browser_is_running = False
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