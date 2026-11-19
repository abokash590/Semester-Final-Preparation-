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
            page = await browser.new_page(viewport={'width': 1280, 'height': 850})
            
            await page.goto('http://127.0.0.1:8089/index.html')
            await page.wait_for_timeout(1000)
            
            # 1. Default View with Topic-Wise Navbar visible
            await page.screenshot(path=os.path.join(artifacts_dir, 'topic_navbar_view.png'))
            print('Captured topic_navbar_view.png')
            
            # 2. Click Group by Topic toggle
            await page.click('#viewModeTopicBtn')
            await page.wait_for_timeout(600)
            await page.screenshot(path=os.path.join(artifacts_dir, 'group_by_topic_view.png'))
            print('Captured group_by_topic_view.png')
            
            # 3. Test clicking a topic on the topic navbar
            buttons = await page.query_selector_all('.topic-nav-btn')
            if len(buttons) > 1:
                # click the second button (first specific topic)
                await buttons[1].click()
                await page.wait_for_timeout(600)
                await page.screenshot(path=os.path.join(artifacts_dir, 'topic_filtered_view.png'))
                print('Captured topic_filtered_view.png')
            
            await browser.close()
        httpd.shutdown()

    asyncio.run(run())

if __name__ == '__main__':
    main()
