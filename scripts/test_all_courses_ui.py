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
            
            # 1. Desktop View (1440x900) - AI Course
            page = await browser.new_page(viewport={'width': 1440, 'height': 900})
            await page.goto('http://127.0.0.1:8089/index.html')
            await page.wait_for_timeout(1000)
            await page.screenshot(path=os.path.join(artifacts_dir, 'all_courses_navbar_ai.png'))
            print('Captured all_courses_navbar_ai.png')

            # 2. Switch to CSE-4102 (Mathematical & Statistical Analysis)
            await page.click('button.course-nav-btn[data-code="CSE-4102"]')
            await page.wait_for_timeout(800)
            await page.screenshot(path=os.path.join(artifacts_dir, 'course_cse4102_msa.png'))
            print('Captured course_cse4102_msa.png')

            # 3. Filter CSE-4102 to 2024 only
            await page.click('#resultsYearPills button[data-year="2024"]')
            await page.wait_for_timeout(500)
            await page.screenshot(path=os.path.join(artifacts_dir, 'course_cse4102_2024_filtered.png'))
            print('Captured course_cse4102_2024_filtered.png')

            # 4. Switch to CSE-4125 (Machine Learning)
            await page.click('button.course-nav-btn[data-code="CSE-4125"]')
            await page.wait_for_timeout(800)
            await page.screenshot(path=os.path.join(artifacts_dir, 'course_cse4125_ml.png'))
            print('Captured course_cse4125_ml.png')

            # 5. Mobile Phone View (375x812) - iPhone style
            mobile_page = await browser.new_page(viewport={'width': 375, 'height': 812})
            await mobile_page.goto('http://127.0.0.1:8089/index.html')
            await mobile_page.wait_for_timeout(1000)
            await mobile_page.screenshot(path=os.path.join(artifacts_dir, 'mobile_all_courses_375px.png'))
            print('Captured mobile_all_courses_375px.png')

            await browser.close()
        httpd.shutdown()

    asyncio.run(run())

if __name__ == '__main__':
    main()
