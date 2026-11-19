import asyncio
from playwright.async_api import async_playwright

async def test_nests():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')

    # Inject test styles and nest elements
    await page.evaluate('''() => {
        // 1. Add head tilt animation to avatar
        const avatarImg = document.querySelector('.portal-core-avatar-img');
        if (avatarImg) {
            avatarImg.style.transformOrigin = '50% 85%';
            avatarImg.style.animation = 'avatarIdleTilt 5.5s ease-in-out infinite';
        }

        // Add keyframes
        const style = document.createElement('style');
        style.innerHTML = `
            @keyframes avatarIdleTilt {
                0%, 100% { transform: rotate(0deg) translateY(0); }
                15% { transform: rotate(-7deg) translateY(-2px); }
                28% { transform: rotate(0deg) translateY(0); }
                42% { transform: rotate(7deg) translateY(-2px); }
                55% { transform: rotate(0deg) translateY(0); }
            }

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
                ) scale(1.12);
            }

            .nest-wrapper {
                position: relative;
                width: clamp(100px, 11vw, 128px);
                height: clamp(90px, 10vw, 115px);
                display: flex;
                align-items: center;
                justify-content: center;
                filter: drop-shadow(0 6px 12px rgba(43, 27, 16, 0.16));
            }

            .nest-img {
                position: absolute;
                inset: 0;
                width: 100%;
                height: 100%;
                object-fit: contain;
                pointer-events: none;
                transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
            }

            .nest-satellite-node:hover .nest-img {
                filter: drop-shadow(0 8px 16px rgba(16, 69, 53, 0.25));
            }

            .nest-course-badge {
                position: relative;
                z-index: 2;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin-top: -6px; /* align with the inner bowl */
                background: rgba(255, 255, 255, 0.92);
                backdrop-filter: blur(4px);
                border: 1.5px solid #2D4A22;
                border-radius: 20px;
                padding: 2px 12px 3px 12px;
                box-shadow: 0 3px 8px rgba(45, 74, 34, 0.15);
                transition: all 0.2s ease;
            }

            .nest-satellite-node:hover .nest-course-badge {
                background: #104535;
                border-color: #104535;
                box-shadow: 0 4px 12px rgba(16, 69, 53, 0.3);
            }

            .nest-slot-num {
                font-family: var(--font-mono);
                font-size: 0.62rem;
                font-weight: 700;
                color: #2D4A22;
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
                line-height: 1.05;
                letter-spacing: -0.01em;
            }

            .nest-satellite-node:hover .nest-short-title {
                color: #ffffff;
            }
        `;
        document.head.appendChild(style);

        // Replace satellites with nest markup
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
                    <div class="nest-course-badge">
                        <span class="nest-slot-num">${c.slot}</span>
                        <span class="nest-short-title">${c.short}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }''');

    await page.wait_for_timeout(1000);
    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'
    await page.screenshot(path=f'{out_dir}/test_nests_badge_1366.png')

    # Also test Variant 2: Nest text sitting directly inside the bowl WITHOUT a white box
    # like a natural golden/creamy wooden carved text inside the bowl!
    await page.evaluate('''() => {
        document.querySelectorAll('.nest-course-badge').forEach(badge => {
            badge.style.background = 'transparent';
            badge.style.border = 'none';
            badge.style.boxShadow = 'none';
            badge.style.backdropFilter = 'none';
            badge.style.textShadow = '0 1px 3px rgba(0,0,0,0.5), 0 0 8px rgba(255,255,255,0.4)';
            badge.querySelector('.nest-slot-num').style.color = '#c8d94d';
            badge.querySelector('.nest-slot-num').style.fontSize = '0.7rem';
            badge.querySelector('.nest-short-title').style.color = '#ffffff';
            badge.querySelector('.nest-short-title').style.fontSize = '1.6rem';
        });
    }''')
    await page.wait_for_timeout(500);
    await page.screenshot(path=f'{out_dir}/test_nests_direct_1366.png')

    await browser.close()
    await p.stop()
    print('Both nest variants captured!')

asyncio.run(test_nests())
