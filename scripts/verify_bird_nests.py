import asyncio
from playwright.async_api import async_playwright

async def verify_everything():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    
    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    # 1. Desktop 1366x768
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')
    await page.wait_for_selector('.nest-satellite-node')
    await page.wait_for_timeout(1000)
    await page.screenshot(path=f'{out_dir}/live_bird_nests_1366.png')

    # Test tilt animation state
    tilt_style = await page.evaluate('''() => {
        const img = document.querySelector('.portal-core-avatar-img');
        const comp = window.getComputedStyle(img);
        return {
            animationName: comp.animationName,
            animationDuration: comp.animationDuration,
            transformOrigin: comp.transformOrigin
        };
    }''')
    print('Tilt animation computed style:', tilt_style)

    # 2. Desktop 1920x1080
    await page.set_viewport_size({'width': 1920, 'height': 1080})
    await page.wait_for_timeout(500)
    await page.screenshot(path=f'{out_dir}/live_bird_nests_1920.png')

    # 3. Mobile 375x812
    await page.set_viewport_size({'width': 375, 'height': 812})
    await page.wait_for_timeout(500)
    await page.screenshot(path=f'{out_dir}/live_bird_nests_375.png')

    # 4. Test clicking Course 1 (AI nest)
    await page.set_viewport_size({'width': 1366, 'height': 768})
    await page.locator('.node-slot-1').click()
    await page.wait_for_selector('.question-set-card')
    print('Successfully navigated into Course 1 (AI) from the bird nest!')
    await page.screenshot(path=f'{out_dir}/live_after_nest_click_course.png')

    await browser.close()
    await p.stop()
    print('All tests and screenshots completed successfully!')

asyncio.run(verify_everything())
