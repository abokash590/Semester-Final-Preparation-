import asyncio
from playwright.async_api import async_playwright

async def test_realistic_nests():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')

    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    # Design 1: Direct Pure Typography nestled in the bowl (no egg, full nest visible)
    await page.evaluate('''() => {
        let style = document.getElementById('nest-realistic-style');
        if (!style) {
            style = document.createElement('style');
            style.id = 'nest-realistic-style';
            document.head.appendChild(style);
        }
        style.innerHTML = `
            .nest-satellite-node {
                position: absolute;
                top: 50%;
                left: 50%;
                --r: clamp(144px, min(27vw, 23vh), 205px);
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
                width: 140px;
                height: 126px;
                display: flex;
                align-items: center;
                justify-content: center;
                filter: drop-shadow(0 6px 14px rgba(43, 27, 16, 0.22));
            }

            .nest-img {
                position: absolute;
                inset: 0;
                width: 100%;
                height: 100%;
                object-fit: contain;
                pointer-events: none;
            }

            /* Direct Text inside the bowl - Organic & 100% visible nest */
            .nest-direct-label {
                position: relative;
                z-index: 2;
                margin-top: -8px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                pointer-events: none;
            }

            .nest-direct-num {
                font-family: var(--font-mono);
                font-size: 0.72rem;
                font-weight: 800;
                color: #c8d94d;
                line-height: 1;
                margin-bottom: 0px;
                text-shadow: 0 1px 3px rgba(0, 0, 0, 0.9), 0 0 6px rgba(0, 0, 0, 0.7);
            }

            .nest-direct-title {
                font-family: 'Calistoga', Georgia, serif;
                font-size: 1.75rem;
                font-weight: 800;
                color: #FFFFFF;
                line-height: 1;
                letter-spacing: 0.02em;
                text-shadow: 
                    0 2px 4px rgba(18, 10, 5, 0.95),
                    0 4px 10px rgba(18, 10, 5, 0.8),
                    0 0 12px rgba(16, 69, 53, 0.6);
                transition: transform 0.2s ease, color 0.2s ease;
            }

            .nest-satellite-node:hover .nest-direct-title {
                color: #c8d94d;
                transform: scale(1.08);
            }

            /* Soft cozy depth in the nest bowl */
            .nest-bowl-shadow {
                position: absolute;
                width: 64px;
                height: 48px;
                margin-top: -6px;
                border-radius: 50%;
                background: radial-gradient(ellipse at center, rgba(30, 16, 8, 0.65) 0%, rgba(30, 16, 8, 0.25) 60%, transparent 100%);
                z-index: 1;
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
                    <div class="nest-bowl-shadow"></div>
                    <div class="nest-direct-label">
                        <span class="nest-direct-num">${c.slot}</span>
                        <span class="nest-direct-title">${c.short}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }''');

    await page.wait_for_timeout(1000);
    await page.screenshot(path=f'{out_dir}/realistic_nest_direct_text.png');

    # Design 2: Wooden Branch Cross-Slice (Tree ring wood disc sitting inside the nest)
    await page.evaluate('''() => {
        let style = document.getElementById('nest-realistic-style');
        style.innerHTML += `
            .nest-wood-slice {
                position: relative;
                z-index: 2;
                width: 62px;
                height: 48px;
                margin-top: -8px;
                background: radial-gradient(ellipse at 45% 45%, #EADBBE 0%, #D8C39E 65%, #C2A77E 100%);
                border: 2px solid #5C3A21;
                border-radius: 48% 52% 49% 51% / 51% 48% 52% 49%;
                box-shadow: 0 4px 8px rgba(35, 20, 10, 0.4), inset 0 0 8px rgba(120, 75, 40, 0.35);
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                transition: all 0.2s ease;
            }
            .nest-satellite-node:hover .nest-wood-slice {
                background: radial-gradient(ellipse at 45% 45%, #104535 0%, #0B3327 100%);
                border-color: #051A13;
                transform: scale(1.08);
            }
            .wood-slice-num {
                font-family: var(--font-mono);
                font-size: 0.62rem;
                font-weight: 800;
                color: #7A5330;
                line-height: 1;
            }
            .nest-satellite-node:hover .wood-slice-num {
                color: #c8d94d;
            }
            .wood-slice-title {
                font-family: 'Calistoga', Georgia, serif;
                font-size: 1.35rem;
                font-weight: 800;
                color: #2D1B0E;
                line-height: 1;
                letter-spacing: -0.01em;
            }
            .nest-satellite-node:hover .wood-slice-title {
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
                    <div class="nest-wood-slice">
                        <span class="wood-slice-num">${c.slot}</span>
                        <span class="wood-slice-title">${c.short}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }''');

    await page.wait_for_timeout(1000);
    await page.screenshot(path=f'{out_dir}/realistic_nest_wood_slice.png');

    await browser.close()
    await p.stop()
    print('Both realistic variants captured!')

asyncio.run(test_realistic_nests())
