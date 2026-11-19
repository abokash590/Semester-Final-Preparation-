import asyncio
from playwright.async_api import async_playwright

async def verify_abokash():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')
    await page.wait_for_timeout(1000)

    # Check anchor attributes
    anchor_info = await page.evaluate('''() => {
        const a = document.querySelector('.portal-avatar-core');
        const badge = document.querySelector('.core-avatar-badge');
        const img = document.querySelector('.portal-core-avatar-img');
        const compBadge = window.getComputedStyle(badge);
        const compImg = window.getComputedStyle(img);
        return {
            tagName: a.tagName,
            href: a.href,
            target: a.target,
            badgeText: badge.innerText.trim(),
            badgeFontFamily: compBadge.fontFamily,
            badgeFontSize: compBadge.fontSize,
            animationName: compImg.animationName,
            animationDuration: compImg.animationDuration,
            animationTiming: compImg.animationTimingFunction
        };
    }''')
    print('Verified Anchor & Badge Info:', anchor_info)

    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'
    await page.screenshot(path=f'{out_dir}/live_abokash_avatar_1366.png')

    # Zoom in on center avatar
    avatar_elem = page.locator('.portal-avatar-core')
    await avatar_elem.screenshot(path=f'{out_dir}/live_abokash_avatar_closeup.png')

    await browser.close()
    await p.stop()
    print('Screenshots captured successfully!')

asyncio.run(verify_abokash())
