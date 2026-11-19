import asyncio
from playwright.async_api import async_playwright

FONTS = [
    ('Calistoga', 'https://fonts.googleapis.com/css2?family=Calistoga&display=swap'),
    ('Caprasimo', 'https://fonts.googleapis.com/css2?family=Caprasimo&display=swap'),
    ('Pirata One', 'https://fonts.googleapis.com/css2?family=Pirata+One&display=swap'),
    ('MedievalSharp', 'https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap'),
    ('Cinzel Decorative', 'https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&display=swap'),
    ('Carter One', 'https://fonts.googleapis.com/css2?family=Carter+One&display=swap'),
    ('Kavoon', 'https://fonts.googleapis.com/css2?family=Kavoon&display=swap'),
    ('Fraunces', 'https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,700;9..144,800&display=swap'),
]

font_links = '\n'.join([f'<link href="{url}" rel="stylesheet">' for name, url in FONTS])

cards = ''
for name, url in FONTS:
    cards += f'''
    <div class="card">
      <div class="font-name">{name}</div>
      <div class="title-41" style="font-family: '{name}', cursive, serif;">4-1</div>
      <div class="title-sub" style="font-family: '{name}', cursive, serif;">Semester Final Preparation</div>
      <div class="subtitle">Explore 2023 &amp; 2024 Exam Questions, Solutions &amp; Term Tests</div>
    </div>
    '''

html = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
{font_links}
<style>
  body {{
    background: #fafafa;
    margin: 0;
    padding: 30px;
    font-family: sans-serif;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
  }}
  .card {{
    background: #ffffff;
    border: 1px solid #e0e8df;
    border-radius: 16px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(16, 69, 53, 0.05);
  }}
  .font-name {{
    font-size: 13px;
    font-weight: 700;
    color: #666;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 12px;
  }}
  .title-41 {{
    font-size: 34px;
    font-weight: 800;
    color: #104535;
    line-height: 1.1;
    margin-bottom: 4px;
  }}
  .title-sub {{
    font-size: 26px;
    font-weight: 700;
    color: #1F3818;
    line-height: 1.2;
    margin-bottom: 8px;
  }}
  .subtitle {{
    font-family: sans-serif;
    font-size: 13px;
    color: #4B6342;
  }}
</style>
</head>
<body>
{cards}
</body>
</html>
'''

with open('dev/font_showcase.html', 'w', encoding='utf-8') as f:
    f.write(html)

async def capture():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1200, 'height': 1200})
    await page.goto('file:///t:/Project/7th Semester/dev/font_showcase.html')
    await page.wait_for_timeout(2000)
    await page.screenshot(path='C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots/font_showcase.png', full_page=True)
    await browser.close()
    await p.stop()
    print('Showcase captured successfully!')

asyncio.run(capture())
