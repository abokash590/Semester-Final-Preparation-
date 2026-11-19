import asyncio
from playwright.async_api import async_playwright

async def verify_realistic():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    
    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    # Desktop 1366
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')
    await page.wait_for_selector('.nest-satellite-node')
    await page.wait_for_timeout(1000)
    await page.screenshot(path=f'{out_dir}/real_nests_live_1366.png')

    # Desktop 1920
    await page.set_viewport_size({'width': 1920, 'height': 1080})
    await page.wait_for_timeout(500)
    await page.screenshot(path=f'{out_dir}/real_nests_live_1920.png')

    # Mobile 375
    await page.set_viewport_size({'width': 375, 'height': 812})
    await page.wait_for_timeout(500)
    await page.screenshot(path=f'{out_dir}/real_nests_live_375.png')

    # Course navigation click check
    await page.set_viewport_size({'width': 1366, 'height': 768})
    await page.locator('.node-slot-1').click()
    await page.wait_for_selector('.question-set-card')
    print('Course navigation verified!')

    await browser.close()
    await p.stop()
    print('All realistic nest verification completed!')

asyncio.run(verify_realistic())
