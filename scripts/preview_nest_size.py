import asyncio
from playwright.async_api import async_playwright

async def test_size():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')

    await page.evaluate('''() => {
        let style = document.getElementById('nest-test-style');
        if (!style) {
            style = document.createElement('style');
            style.id = 'nest-test-style';
            document.head.appendChild(style);
        }
        style.innerHTML = `
            .nest-satellite-node {
                position: absolute;
                top: 50%;
                left: 50%;
                --r: clamp(145px, min(28vw, 23vh), 205px);
                transform: translate(
                    calc(-50% + cos(var(--angle)) * var(--r)),
                    calc(-50% + sin(var(--angle)) * var(--r))
                );
                cursor: pointer;
                user-select: none;
                transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
                z-index: 26;
            }

            .nest-satellite-node:hover {
                transform: translate(
                    calc(-50% + cos(var(--angle)) * var(--r)),
                    calc(-50% + sin(var(--angle)) * var(--r))
                ) scale(1.15);
            }

            .nest-wrapper {
                position: relative;
                width: 144px;
                height: 130px;
                display: flex;
                align-items: center;
                justify-content: center;
                filter: drop-shadow(0 8px 16px rgba(43, 27, 16, 0.22));
            }

            .nest-img {
                position: absolute;
                inset: 0;
                width: 100%;
                height: 100%;
                object-fit: contain;
                pointer-events: none;
            }

            .nest-egg {
                position: relative;
                z-index: 2;
                width: 64px;
                height: 72px;
                margin-top: -10px;
                background: linear-gradient(150deg, #FFFFFF 0%, #F5EFE4 100%);
                border: 2px solid #C4A47C;
                border-radius: 50% 50% 50% 50% / 62% 62% 38% 38%;
                box-shadow: 0 4px 12px rgba(60, 40, 20, 0.22), inset 0 -3px 6px rgba(196, 164, 124, 0.35), inset 0 2px 4px #FFFFFF;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                transition: all 0.22s ease;
            }

            .nest-satellite-node:hover .nest-egg {
                background: linear-gradient(145deg, #104535, #1B5E46);
                border-color: #071E17;
                box-shadow: 0 6px 18px rgba(16, 69, 53, 0.4);
            }

            .nest-slot-num {
                font-family: var(--font-mono);
                font-size: 0.68rem;
                font-weight: 700;
                color: #8C6A48;
                line-height: 1;
                margin-bottom: 1px;
            }

            .nest-satellite-node:hover .nest-slot-num {
                color: #c8d94d;
            }

            .nest-short-title {
                font-family: 'Calistoga', Georgia, serif;
                font-size: 1.45rem;
                font-weight: 700;
                color: #104535;
                line-height: 1;
                letter-spacing: -0.01em;
            }

            .nest-satellite-node:hover .nest-short-title {
                color: #FFFFFF;
            }
        `;

        const group = document.getElementById('orbitalSatellitesGroup');
        const courses = [
            { code: 'CSE-4101', short: 'AI', angle: -90, slot: 1 },
            { code: 'CSE-4102', short: 'MSA', angle: -18, slot: 2 },
            { code: 'SS-4103', short: 'ENT', angle: 54, slot: 3 },
            { code: 'CSE-4125', short: 'ML', angle: 126, slot: 4 },
            { code: 'CSE-4126', short: 'DS', angle: 198, slot: 5 }
        ];

        group.innerHTML = courses.map(c => `
            <div class="nest-satellite-node node-slot-${c.slot}" style="--angle: ${c.angle}deg;">
                <div class="nest-wrapper">
                    <img src="assets/bird_nest.png" alt="" class="nest-img">
                    <div class="nest-egg">
                        <span class="nest-slot-num">${c.slot}</span>
                        <span class="nest-short-title">${c.short}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }''')

    await page.wait_for_timeout(1000);
    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'
    await page.screenshot(path=f'{out_dir}/test_nest_144px_1366.png')
    await browser.close()
    await p.stop()
    print('144px test captured successfully!')

asyncio.run(test_size())
