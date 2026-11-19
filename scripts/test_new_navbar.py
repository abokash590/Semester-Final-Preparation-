import asyncio
from playwright.async_api import async_playwright

async def preview():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 820})
    await page.goto('http://localhost:8000')
    await page.wait_for_timeout(1000)
    
    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'
    await page.screenshot(path=f'{out_dir}/current_home_before_navbar.png')
    
    # Enter course 1
    await page.locator('.node-slot-1').click()
    await page.wait_for_timeout(1000)
    await page.screenshot(path=f'{out_dir}/current_course_before_navbar.png')
    
    await browser.close()
    await p.stop()
    print("Baseline captured successfully!")

asyncio.run(preview())
