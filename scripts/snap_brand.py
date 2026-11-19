import asyncio
from playwright.async_api import async_playwright

async def run():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    out = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    page = await browser.new_page(viewport={'width': 1366, 'height': 820})
    await page.goto('http://localhost:8000')
    await page.wait_for_timeout(900)

    # Enter course to see navbar
    await page.locator('.node-slot-1').click()
    await page.wait_for_selector('.question-set-card')
    await page.wait_for_timeout(700)

    hdr = page.locator('.app-header')
    await hdr.screenshot(path=f'{out}/brand_new_header.png')

    brand = page.locator('.brand-group')
    await brand.screenshot(path=f'{out}/brand_new_closeup.png')

    # Also full page
    await page.screenshot(path=f'{out}/brand_new_fullpage.png')

    await browser.close()
    await p.stop()
    print('Done!')

asyncio.run(run())
