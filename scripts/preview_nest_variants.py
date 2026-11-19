import asyncio
from playwright.async_api import async_playwright

async def test_nest_variants():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')

    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    # Variant 1: Cute Egg in the Nest
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
                --r: clamp(140px, min(27vw, 22vh), 195px);
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
                ) scale(1.14);
            }

            .nest-wrapper {
                position: relative;
                width: 124px;
                height: 112px;
                display: flex;
                align-items: center;
                justify-content: center;
                filter: drop-shadow(0 6px 14px rgba(43, 27, 16, 0.18));
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
                width: 58px;
                height: 66px;
                margin-top: -8px;
                background: linear-gradient(145deg, #FFFDF8, #F3ECE0);
                border: 1.8px solid #C4A47C;
                border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
                box-shadow: 0 4px 10px rgba(70, 50, 30, 0.2), inset 0 -3px 6px rgba(196, 164, 124, 0.3), inset 0 2px 4px #FFFFFF;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                transition: all 0.2s ease;
            }

            .nest-satellite-node:hover .nest-egg {
                background: linear-gradient(145deg, #104535, #1B5E46);
                border-color: #0B2B21;
                box-shadow: 0 6px 16px rgba(16, 69, 53, 0.35);
            }

            .nest-slot-num {
                font-family: var(--font-mono);
                font-size: 0.65rem;
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
                font-size: 1.35rem;
                font-weight: 700;
                color: #104535;
                line-height: 1;
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
    }''');
    await page.wait_for_timeout(1000);
    await page.screenshot(path=f'{out_dir}/variant_egg_nest_1366.png');

    # Variant 2: Rustic Wooden Plaque across the nest
    await page.evaluate('''() => {
        let style = document.getElementById('nest-test-style');
        style.innerHTML = style.innerHTML.replace(/\\.nest-egg \\{[^\\}]+\\}/, `
            .nest-egg {
                position: relative;
                z-index: 2;
                padding: 4px 14px;
                margin-top: -6px;
                background: linear-gradient(180deg, #F9F5EA 0%, #E8DFC8 100%);
                border: 2px solid #5C3A21;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(45, 25, 10, 0.25), inset 0 1px 1px #FFF;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                transition: all 0.2s ease;
            }
            .nest-satellite-node:hover .nest-egg {
                background: linear-gradient(180deg, #104535 0%, #0A2F24 100%);
                border-color: #071E17;
            }
        `);
    }''');
    await page.wait_for_timeout(500);
    await page.screenshot(path=f'{out_dir}/variant_wooden_plaque_1366.png');

    await browser.close()
    await p.stop()
    print('Variants captured!')

asyncio.run(test_nest_variants())
