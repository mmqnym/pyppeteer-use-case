# Pyppeteer usecase

## Set up

``` sh
pip install pyppeteer
```

<br />

This package is used to hide some webdrive attributes

``` sh
pip install pyppeteer_stealth
```

## Experience

- You can use https://bot.sannysoft.com/ to check if you are being detected as a bot.
- There are several Chromium arguments for reference in the `Reference` section below.
- Most of the problems can be solved by the discussions in `puppetter` or the related docs.
- **Some of the situations detected as bot may not be caused by the code, just don't use the default Chronium download the latest version of chromium, copy-paste that package in your main file and use `executablePath = f'{os.getcwd()}\chromium\chrome.exe'` in lunch, most of them can be solved.**
- You can refer to the `troubleshooting.md` of [Nodejs puppeteer docs](https://github.com/puppeteer/puppeteer/tree/main/docs), which has a record of some common problems.

<br />

## Reference

- ##### [Python Asyncio Guide](https://docs.python.org/3/library/asyncio-dev.html)
- ##### [Chromium Command Line Switches](https://peter.sh/experiments/chromium-command-line-switches/)
- ##### [Nodejs puppeteer docs](https://github.com/puppeteer/puppeteer/tree/main/docs)
- ##### [Pyppeteer](https://github.com/pyppeteer/pyppeteer)
- ##### [Pyppeteer Docs](https://miyakogi.github.io/pyppeteer/)
- ##### [Hide webdrive attributes](https://github.com/MeiK2333/pyppeteer_stealth)

<br />

> ### 中文補充資料 (Guide in Mandarin)

- ##### [Asyncio 從頭入門](https://ithelp.ithome.com.tw/articles/10199385)
- ##### [Asyncio 架構探討](https://www.ithome.com.tw/voice/138875)

<br />

## License

[MIT](LICENSE)