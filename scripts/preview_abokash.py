import asyncio
from playwright.async_api import async_playwright

async def test_abokash():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')

    # Load handwritten fonts Caveat & Kalam
    await page.evaluate('''() => {
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = 'https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=Kalam:wght@700&display=swap';
        document.head.appendChild(link);

        const style = document.createElement('style');
        style.innerHTML = `
            /* Ultra-smooth organic breathing and gentle head sway */
            @keyframes avatarLiquidSmoothTilt {
                0% {
                    transform: rotate(0deg) translateY(0);
                }
                20% {
                    transform: rotate(-6deg) translateY(-2px);
                }
                40% {
                    transform: rotate(0deg) translateY(0);
                }
                60% {
                    transform: rotate(6deg) translateY(-2px);
                }
                80% {
                    transform: rotate(0deg) translateY(0);
                }
                100% {
                    transform: rotate(0deg) translateY(0);
                }
            }

            .portal-core-avatar-img {
                transform-origin: 50% 90% !important;
                animation: avatarLiquidSmoothTilt 7s cubic-bezier(0.45, 0.05, 0.55, 0.95) infinite !important;
                transition: transform 0.3s ease;
            }

            .core-avatar-badge {
                font-family: 'Caveat', cursive !important;
                font-size: 1.05rem !important;
                font-weight: 700 !important;
                padding: 1px 12px 3px 12px !important;
                letter-spacing: 0.03em !important;
                bottom: -10px !important;
                background: #104535 !important;
                border: 1px solid rgba(200, 217, 77, 0.35) !important;
                color: #FFFFFF !important;
                box-shadow: 0 4px 10px rgba(16, 69, 53, 0.3) !important;
            }
        `;
        document.head.appendChild(style);

        const badge = document.querySelector('.core-avatar-badge');
        if (badge) badge.textContent = 'Abokash';
    }''');

    await page.wait_for_timeout(1500);
    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'
    await page.screenshot(path=f'{out_dir}/test_abokash_caveat.png');

    # Also test Kalam font
    await page.evaluate('''() => {
        const badge = document.querySelector('.core-avatar-badge');
        badge.style.fontFamily = "'Kalam', cursive";
        badge.style.fontSize = '0.85rem';
    }''');
    await page.wait_for_timeout(500);
    await page.screenshot(path=f'{out_dir}/test_abokash_kalam.png');

    await browser.close()
    await p.stop()
    print('Both Abokash screenshots captured!')

asyncio.run(test_abokash())
