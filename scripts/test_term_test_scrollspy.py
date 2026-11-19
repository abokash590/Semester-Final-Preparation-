import os
from playwright.sync_api import sync_playwright

SCREENSHOTS_DIR = r"C:\Users\ahmed\.gemini\antigravity\brain\4fc4ec37-d310-498f-9ecb-cf74490ff70a\screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        context = browser.new_context(viewport={"width": 1366, "height": 920})
        page = context.new_page()

        print("Opening http://localhost:8000 ...")
        page.goto("http://localhost:8000", wait_until="networkidle")

        # Wait for left sidebar
        page.wait_for_selector(".year-scrollspy-nav")

        # Click "SIMT" in Term Test left rail
        simt_btn = page.locator(".college-dot[data-college='SIMT']")
        simt_btn.click()
        page.wait_for_timeout(800)

        screenshot_simt = os.path.join(SCREENSHOTS_DIR, "scrollspy_term_test_simt.png")
        page.screenshot(path=screenshot_simt)
        print(f"Captured: {screenshot_simt}")

        browser.close()
        print("SIMT verification complete!")

if __name__ == "__main__":
    test()
