import asyncio
import http.server
import socketserver
import threading
import os
from playwright.async_api import async_playwright

def main():
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(('127.0.0.1', 8089), Handler)
    server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    server_thread.start()
    print('HTTP server started on port 8089')

    async def run():
        artifacts_dir = r"C:\Users\ahmed\.gemini\antigravity\brain\4fc4ec37-d310-498f-9ecb-cf74490ff70a\screenshots"
        os.makedirs(artifacts_dir, exist_ok=True)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(channel='chrome')
            
            # 1. Desktop View (1280x800) - AI Course with Year Toggle
            page = await browser.new_page(viewport={'width': 1280, 'height': 800})
            await page.goto('http://127.0.0.1:8089/index.html')
            await page.wait_for_timeout(800)
            await page.screenshot(path=os.path.join(artifacts_dir, 'clean_plain_ui_ai.png'))
            print('Captured clean_plain_ui_ai.png')

            # 2. Click 2023 Final Toggle
            await page.click('button.year-toggle-btn[data-year="2023"]')
            await page.wait_for_timeout(500)
            await page.screenshot(path=os.path.join(artifacts_dir, 'toggle_2023_ai.png'))
            print('Captured toggle_2023_ai.png')

            # 3. Click 2024 Final Toggle
            await page.click('button.year-toggle-btn[data-year="2024"]')
            await page.wait_for_timeout(500)
            await page.screenshot(path=os.path.join(artifacts_dir, 'toggle_2024_ai.png'))
            print('Captured toggle_2024_ai.png')

            # 4. Switch to ML (Machine Learning)
            await page.click('button.course-nav-btn[data-code="CSE-4125"]')
            await page.wait_for_timeout(600)
            await page.screenshot(path=os.path.join(artifacts_dir, 'clean_plain_ui_ml.png'))
            print('Captured clean_plain_ui_ml.png')

            # 5. Mobile Phone View (375x812)
            mobile_page = await browser.new_page(viewport={'width': 375, 'height': 812})
            await mobile_page.goto('http://127.0.0.1:8089/index.html')
            await mobile_page.wait_for_timeout(800)
            await mobile_page.screenshot(path=os.path.join(artifacts_dir, 'clean_mobile_phone_375px.png'))
            print('Captured clean_mobile_phone_375px.png')

            await browser.close()
        httpd.shutdown()

    asyncio.run(run())

if __name__ == '__main__':
    main()
