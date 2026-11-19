import asyncio
from playwright.async_api import async_playwright

FONTS_TEST2 = [
    ('Carter_One', 'https://fonts.googleapis.com/css2?family=Carter+One&display=swap', 'Carter One'),
    ('Shrikhand', 'https://fonts.googleapis.com/css2?family=Shrikhand&display=swap', 'Shrikhand'),
    ('Kavoon', 'https://fonts.googleapis.com/css2?family=Kavoon&display=swap', 'Kavoon'),
    ('Cinzel_Decorative', 'https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&display=swap', 'Cinzel Decorative'),
]

async def capture_more():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 768})
    await page.goto('http://localhost:8000/#home')
    await page.wait_for_selector('.portal-avatar-core')

    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    for label, url, font_family in FONTS_TEST2:
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
            title.style.fontSize = '2.3rem';
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

asyncio.run(capture_more())
