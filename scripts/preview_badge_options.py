import asyncio
from playwright.async_api import async_playwright

async def test_badge_positions():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')

    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    # Option 1: Badge cleanly moved BELOW the circle (bottom: -22px) so 100% of chin/face is visible
    await page.evaluate('''() => {
        const badge = document.querySelector('.core-avatar-badge');
        badge.style.bottom = '-20px';
        badge.style.zIndex = '30';
    }''')
    await page.wait_for_timeout(500)
    avatar = page.locator('.portal-avatar-core')
    await avatar.screenshot(path=f'{out_dir}/option1_badge_below_circle.png')

    # Option 2: Pure handwritten signature floating below the circle (no pill background)
    await page.evaluate('''() => {
        const badge = document.querySelector('.core-avatar-badge');
        badge.style.background = 'transparent';
        badge.style.border = 'none';
        badge.style.boxShadow = 'none';
        badge.style.color = '#104535';
        badge.style.fontSize = '1.35rem';
        badge.style.bottom = '-26px';
        badge.style.fontWeight = '700';
        badge.style.textShadow = '0 1px 2px rgba(255, 255, 255, 0.9)';
    }''')
    await page.wait_for_timeout(500)
    await avatar.screenshot(path=f'{out_dir}/option2_floating_signature.png')

    # Option 3: Avatar image scaled slightly & shifted up, badge at bottom: -14px
    await page.evaluate('''() => {
        const badge = document.querySelector('.core-avatar-badge');
        badge.style.background = '#104535';
        badge.style.border = '1px solid rgba(200, 217, 77, 0.4)';
        badge.style.boxShadow = '0 3px 8px rgba(16, 69, 53, 0.28)';
        badge.style.color = '#FFFFFF';
        badge.style.fontSize = '1.05rem';
        badge.style.bottom = '-18px';

        const img = document.querySelector('.portal-core-avatar-img');
        img.style.marginTop = '-8px';
    }''')
    await page.wait_for_timeout(500)
    await avatar.screenshot(path=f'{out_dir}/option3_shifted_img_badge.png')

    # Full home view with Option 1
    await page.evaluate('''() => {
        const badge = document.querySelector('.core-avatar-badge');
        badge.style.bottom = '-19px';
        const img = document.querySelector('.portal-core-avatar-img');
        img.style.marginTop = '-6px';
    }''')
    await page.wait_for_timeout(500)
    await page.screenshot(path=f'{out_dir}/full_home_with_perfect_avatar.png')

    await browser.close()
    await p.stop()
    print('All options captured!')

asyncio.run(test_badge_positions())
