import os
from playwright.sync_api import sync_playwright

SCREENSHOTS_DIR = r"C:\Users\ahmed\.gemini\antigravity\brain\4fc4ec37-d310-498f-9ecb-cf74490ff70a\screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def test_scrollspy():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        context = browser.new_context(viewport={"width": 1366, "height": 900})
        page = context.new_page()

        print("Navigating to http://localhost:8000 ...")
        page.goto("http://localhost:8000", wait_until="networkidle")

        # Wait for left sidebar scrollspy to render
        page.wait_for_selector(".year-scrollspy-nav .scrollspy-item")

        # 1. Capture Desktop Initial View (2024 active with elongated line on left)
        screenshot_initial = os.path.join(SCREENSHOTS_DIR, "scrollspy_desktop_2024_active.png")
        page.screenshot(path=screenshot_initial)
        print(f"Captured: {screenshot_initial}")

        # 2. Scroll down to 2023 section to test automatic Scrollspy activation
        sec_2023 = page.locator("#year-section-2023")
        sec_2023.scroll_into_view_if_needed()
        page.wait_for_timeout(800)

        screenshot_scrolled_2023 = os.path.join(SCREENSHOTS_DIR, "scrollspy_scrolled_to_2023.png")
        page.screenshot(path=screenshot_scrolled_2023)
        print(f"Captured: {screenshot_scrolled_2023}")

        # Verify 2023 item is now active
        is_2023_active = page.locator(".scrollspy-item[data-year='2023']").evaluate("el => el.classList.contains('active')")
        print(f"Is 2023 item active after scroll? {is_2023_active}")

        # 3. Test clicking 2024 item to scroll back up
        btn_2024 = page.locator(".scrollspy-item[data-year='2024']")
        btn_2024.click()
        page.wait_for_timeout(800)

        # 4. Test Mobile view (375px)
        mobile_ctx = browser.new_context(viewport={"width": 375, "height": 812})
        mobile_page = mobile_ctx.new_page()
        mobile_page.goto("http://localhost:8000", wait_until="networkidle")
        mobile_page.wait_for_selector(".mobile-scrollspy-bar")

        screenshot_mobile = os.path.join(SCREENSHOTS_DIR, "scrollspy_mobile_375px.png")
        mobile_page.screenshot(path=screenshot_mobile)
        print(f"Captured: {screenshot_mobile}")

        browser.close()
        print("Scrollspy verification complete!")

if __name__ == "__main__":
    test_scrollspy()
