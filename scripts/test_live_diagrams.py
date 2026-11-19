import os
from playwright.sync_api import sync_playwright

SCREENSHOTS_DIR = r"C:\Users\ahmed\.gemini\antigravity\brain\4fc4ec37-d310-498f-9ecb-cf74490ff70a\screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        context = browser.new_context(viewport={"width": 1280, "height": 950})
        page = context.new_page()

        print("Opening http://localhost:8000 ...")
        page.goto("http://localhost:8000", wait_until="networkidle")

        # Wait for diagrams to render
        page.wait_for_selector(".diagram-render-target svg", timeout=8000)

        # 1. Scroll specifically to the diagram wrapper in Question 1
        diagram_el = page.locator(".diagram-wrapper").first
        diagram_el.scroll_into_view_if_needed()
        page.wait_for_timeout(500)

        screenshot_path = os.path.join(SCREENSHOTS_DIR, "live_diagram_search_tree_2024.png")
        page.screenshot(path=screenshot_path)
        print(f"Captured: {screenshot_path}")

        # 2. Toggle to 2023 to check 2023 diagrams
        btn_2023 = page.locator(".year-toggle-btn[data-year='2023']")
        btn_2023.click()
        page.wait_for_timeout(1000)

        # Wait for 2023 diagram
        page.wait_for_selector(".diagram-render-target svg", timeout=8000)
        diagram_2023 = page.locator(".diagram-wrapper").first
        diagram_2023.scroll_into_view_if_needed()
        page.wait_for_timeout(500)

        screenshot_2023 = os.path.join(SCREENSHOTS_DIR, "live_diagram_2023_astar.png")
        page.screenshot(path=screenshot_2023)
        print(f"Captured: {screenshot_2023}")

        # 3. Test Dark Mode diagram rendering
        theme_btn = page.locator("#themeToggleBtn")
        theme_btn.click()
        page.wait_for_timeout(800)

        screenshot_dark = os.path.join(SCREENSHOTS_DIR, "live_diagram_dark_mode.png")
        page.screenshot(path=screenshot_dark)
        print(f"Captured: {screenshot_dark}")

        browser.close()
        print("Live diagram visual verification complete!")

if __name__ == "__main__":
    run()
