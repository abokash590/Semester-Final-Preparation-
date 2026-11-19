import asyncio
from playwright.async_api import async_playwright

async def capture_final_avatar():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')
    await page.wait_for_timeout(1000)

    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'
    
    # Closeup of avatar core
    avatar = page.locator('.portal-avatar-core')
    await avatar.screenshot(path=f'{out_dir}/avatar_chin_clear_closeup.png')
    
    # Full desktop
    await page.screenshot(path=f'{out_dir}/avatar_chin_clear_1366.png')

    # Mobile 375
    await page.set_viewport_size({'width': 375, 'height': 812})
    await page.wait_for_timeout(500)
    await page.screenshot(path=f'{out_dir}/avatar_chin_clear_375.png')

    await browser.close()
    await p.stop()
    print('All chin-clear screenshots captured!')

asyncio.run(capture_final_avatar())
