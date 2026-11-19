import asyncio
from playwright.async_api import async_playwright

async def verify_course_bg():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 820})
    
    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    # 1. Course 1 (AI)
    await page.goto('http://localhost:8000/#cse-4101')
    await page.wait_for_selector('.question-set-card')
    await page.wait_for_timeout(1000)
    
    # Check body background style
    bg_style = await page.evaluate('''() => {
        const bodyStyle = window.getComputedStyle(document.body);
        return {
            bgColor: bodyStyle.backgroundColor,
            bgImage: bodyStyle.backgroundImage,
            bgSize: bodyStyle.backgroundSize
        };
    }''')
    print('Course page body background:', bg_style)

    await page.screenshot(path=f'{out_dir}/course_ai_bg_dots_1366.png')

    # 2. Course 2 (MSA)
    await page.goto('http://localhost:8000/#cse-4102')
    await page.wait_for_selector('.question-set-card')
    await page.wait_for_timeout(600)
    await page.screenshot(path=f'{out_dir}/course_msa_bg_dots_1366.png')

    # 3. Mobile Course 1 (375x812)
    await page.set_viewport_size({'width': 375, 'height': 812})
    await page.goto('http://localhost:8000/#cse-4101')
    await page.wait_for_selector('.question-set-card')
    await page.wait_for_timeout(600)
    await page.screenshot(path=f'{out_dir}/course_ai_bg_dots_375.png')

    await browser.close()
    await p.stop()
    print('All course bg screenshots captured successfully!')

asyncio.run(verify_course_bg())
