import asyncio
from playwright.async_api import async_playwright

async def run():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    out = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    page = await browser.new_page(viewport={'width': 1366, 'height': 820})
    # wait a bit longer for web fonts to load
    await page.goto('http://localhost:8000')
    await page.wait_for_timeout(2500)

    # Capture home portal full
    await page.screenshot(path=f'{out}/home_jungle_title.png')

    # Capture just the title area
    title = page.locator('.portal-title.jungle-title')
    await title.screenshot(path=f'{out}/jungle_title_closeup.png')

    # Also check what font is actually loading
    font_check = await page.evaluate("""() => {
        const el = document.querySelector('.jungle-eyebrow');
        return window.getComputedStyle(el).fontFamily;
    }""")
    print('Font family on .jungle-eyebrow:', font_check)

    font_check2 = await page.evaluate("""() => {
        const el = document.querySelector('.jungle-main');
        return window.getComputedStyle(el).fontFamily;
    }""")
    print('Font family on .jungle-main:', font_check2)

    await browser.close()
    await p.stop()
    print('Done!')

asyncio.run(run())
