import os
import sys
from playwright.sync_api import sync_playwright

SCREENSHOTS_DIR = r"C:\Users\ahmed\.gemini\antigravity\brain\4fc4ec37-d310-498f-9ecb-cf74490ff70a\screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        context = browser.new_context(viewport={"width": 1280, "height": 900})
        page = context.new_page()

        print("Navigating to http://localhost:8000 ...")
        page.goto("http://localhost:8000", wait_until="networkidle")

        # Wait for questions to render
        page.wait_for_selector(".question-set-card")

        # 1. Capture Initial 2024 Final View (CSE-4101 AI)
        screenshot_2024 = os.path.join(SCREENSHOTS_DIR, "question_sets_2024_ai.png")
        page.screenshot(path=screenshot_2024, full_page=False)
        print(f"Captured: {screenshot_2024}")

        # Check total cards rendered
        cards_2024 = page.locator(".question-set-card").count()
        print(f"2024 Question Sets rendered: {cards_2024}")

        # 2. Reveal Question 1 Solution to inspect question prompt above solution
        first_reveal_btn = page.locator(".solution-toggle-btn").first
        first_reveal_btn.click()
        page.wait_for_timeout(500)

        screenshot_solution = os.path.join(SCREENSHOTS_DIR, "question_set_solution_revealed.png")
        page.screenshot(path=screenshot_solution, full_page=False)
        print(f"Captured: {screenshot_solution}")

        # 3. Toggle to 2023 Final
        btn_2023 = page.locator(".year-toggle-btn[data-year='2023']")
        btn_2023.click()
        page.wait_for_timeout(500)

        cards_2023 = page.locator(".question-set-card").count()
        print(f"2023 Question Sets rendered: {cards_2023}")

        screenshot_2023 = os.path.join(SCREENSHOTS_DIR, "question_sets_2023_ai.png")
        page.screenshot(path=screenshot_2023, full_page=False)
        print(f"Captured: {screenshot_2023}")

        # 4. Switch Course to ML (CSE-4125)
        btn_ml = page.locator(".course-nav-btn:has-text('ML')")
        btn_ml.click()
        page.wait_for_timeout(500)

        screenshot_ml = os.path.join(SCREENSHOTS_DIR, "question_sets_ml.png")
        page.screenshot(path=screenshot_ml, full_page=False)
        print(f"Captured: {screenshot_ml}")

        # 5. Mobile Viewport (375px)
        mobile_context = browser.new_context(viewport={"width": 375, "height": 812})
        mobile_page = mobile_context.new_page()
        mobile_page.goto("http://localhost:8000", wait_until="networkidle")
        mobile_page.wait_for_selector(".question-set-card")

        screenshot_mobile = os.path.join(SCREENSHOTS_DIR, "question_sets_mobile_375px.png")
        mobile_page.screenshot(path=screenshot_mobile, full_page=False)
        print(f"Captured mobile: {screenshot_mobile}")

        browser.close()
        print("Playwright visual verification complete!")

if __name__ == "__main__":
    verify()
