import asyncio
from playwright.async_api import async_playwright

FONTS_TEST = [
    ('Calistoga', 'https://fonts.googleapis.com/css2?family=Calistoga&display=swap', 'Calistoga'),
    ('Caprasimo', 'https://fonts.googleapis.com/css2?family=Caprasimo&display=swap', 'Caprasimo'),
    ('MedievalSharp', 'https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap', 'MedievalSharp'),
    ('Fraunces', 'https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700;9..144,800&display=swap', 'Fraunces'),
]

async def capture_live_home():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')

    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    for label, url, font_family in FONTS_TEST:
        # Inject Google font link
        await page.evaluate(f'''() => {{
            let link = document.getElementById('temp-font-link');
            if (!link) {{
                link = document.createElement('link');
                link.id = 'temp-font-link';
                link.rel = 'stylesheet';
                document.head.appendChild(link);
            }}
            link.href = '{url}';

            const pill = document.querySelector('.portal-badge-pill');
            if (pill) pill.style.display = 'none';

            const title = document.querySelector('.portal-title');
            title.style.fontFamily = "'{font_family}', cursive, serif";
            title.style.fontSize = '2.4rem';
            title.style.lineHeight = '1.15';
            title.style.color = '#104535';
            title.style.margin = '0 0 6px 0';
            title.innerHTML = '<span style="display:block; font-size: 2.2rem; margin-bottom: 2px;">4-1</span><span>Semester Final Preparation</span>';

            const sub = document.querySelector('.portal-subtitle');
            sub.textContent = 'Explore 2023 & 2024 Exam Questions, Solutions & Term Tests';
        }}''')
        await page.wait_for_timeout(1000)
        await page.screenshot(path=f'{out_dir}/live_home_{label.lower()}.png')
        print(f'Captured live_home_{label.lower()}.png')

    await browser.close()
    await p.stop()

asyncio.run(capture_live_home())
