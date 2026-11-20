import os
import shutil
from playwright.sync_api import sync_playwright

SCREENSHOTS_DIR = r"C:\Users\ahmed\.gemini\antigravity\brain\4fc4ec37-d310-498f-9ecb-cf74490ff70a\screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, channel="chrome")
    page = browser.new_page(viewport={"width": 1280, "height": 900})

    print("Opening http://localhost:8000/#cse-4101 ...")
    page.goto("http://localhost:8000/#cse-4101")
    page.wait_for_selector(".question-set-card", timeout=8000)
    page.wait_for_timeout(1000)

    # 1. 2024 Set 6 (Neuron parameters math block)
    card_q6 = page.locator("#card-cse-4101-final-2024-set6")
    card_q6.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    card_q6.screenshot(path="screenshots/check_2024_q6.png")
    shutil.copy("screenshots/check_2024_q6.png", os.path.join(SCREENSHOTS_DIR, "check_2024_q6.png"))
    print("✓ Saved check_2024_q6.png")

    # 2. 2024 Set 4 (5 Bold FOL statements)
    card_q4 = page.locator("#card-cse-4101-final-2024-set4")
    card_q4.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    card_q4.screenshot(path="screenshots/check_2024_q4.png")
    shutil.copy("screenshots/check_2024_q4.png", os.path.join(SCREENSHOTS_DIR, "check_2024_q4.png"))
    print("✓ Saved check_2024_q4.png")

    # 3. 2024 Set 7 (E connected to I, D to H)
    card_q7 = page.locator("#card-cse-4101-final-2024-set7")
    card_q7.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    card_q7.screenshot(path="screenshots/check_2024_q7.png")
    shutil.copy("screenshots/check_2024_q7.png", os.path.join(SCREENSHOTS_DIR, "check_2024_q7.png"))
    print("✓ Saved check_2024_q7.png")

    # 4. 2023 Set 7 (Romania Map SVG)
    card_2023_q7 = page.locator("#card-cse-4101-final-2023-set7")
    card_2023_q7.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    card_2023_q7.screenshot(path="screenshots/check_2023_q7.png")
    shutil.copy("screenshots/check_2023_q7.png", os.path.join(SCREENSHOTS_DIR, "check_2023_q7.png"))
    print("✓ Saved check_2023_q7.png")

    browser.close()
    print("All checks completed!")
