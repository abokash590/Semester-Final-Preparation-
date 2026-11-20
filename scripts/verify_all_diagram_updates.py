import os
import shutil
from playwright.sync_api import sync_playwright

SCREENSHOTS_DIR = r"C:\Users\ahmed\.gemini\antigravity\brain\4fc4ec37-d310-498f-9ecb-cf74490ff70a\screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, channel="chrome")
    page = browser.new_page(viewport={"width": 1280, "height": 900})

    print("Opening http://localhost:8000/#cse-4101 ...")
    page.goto("http://localhost:8000/#cse-4101")
    page.wait_for_selector(".question-set-card", timeout=8000)
    page.wait_for_timeout(1000)

    # 1. 2024 Set 7 (I connected with E, D with H)
    card_q7 = page.locator("#card-cse-4101-final-2024-set7")
    card_q7.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    p1 = "screenshots/verified_2024_q7_diagram.png"
    card_q7.screenshot(path=p1)
    shutil.copy(p1, os.path.join(SCREENSHOTS_DIR, "verified_2024_q7_diagram.png"))
    print(f"✓ 2024 Q7 screenshot: {p1}")

    # 2. 2024 Set 6 (Neuron parameters compact math block)
    card_q6 = page.locator("#card-cse-4101-final-2024-set6")
    card_q6.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    p2 = "screenshots/verified_2024_q6_gap_fixed.png"
    card_q6.screenshot(path=p2)
    shutil.copy(p2, os.path.join(SCREENSHOTS_DIR, "verified_2024_q6_gap_fixed.png"))
    print(f"✓ 2024 Q6 screenshot: {p2}")

    # 3. 2024 Set 4 (5 Bold FOL statements)
    card_q4 = page.locator("#card-cse-4101-final-2024-set4")
    card_q4.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    p3 = "screenshots/verified_2024_q4_bold_fol.png"
    card_q4.screenshot(path=p3)
    shutil.copy(p3, os.path.join(SCREENSHOTS_DIR, "verified_2024_q4_bold_fol.png"))
    print(f"✓ 2024 Q4 screenshot: {p3}")

    # 4. 2024 Set 1 (Search tree: F under C, D only to H, H to J and K)
    card_q1 = page.locator("#card-cse-4101-final-2024-set1")
    card_q1.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    p4 = "screenshots/verified_2024_q1_search_tree.png"
    card_q1.screenshot(path=p4)
    shutil.copy(p4, os.path.join(SCREENSHOTS_DIR, "verified_2024_q1_search_tree.png"))
    print(f"✓ 2024 Q1 screenshot: {p4}")

    # 5. 2023 Set 7 (Romania Map)
    card_2023_q7 = page.locator("#card-cse-4101-final-2023-set7")
    card_2023_q7.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    p5 = "screenshots/verified_2023_q7_romania_map.png"
    card_2023_q7.screenshot(path=p5)
    shutil.copy(p5, os.path.join(SCREENSHOTS_DIR, "verified_2023_q7_romania_map.png"))
    print(f"✓ 2023 Q7 screenshot: {p5}")

    browser.close()
    print("ALL SCREENSHOTS CAPTURED SUCCESSFULLY!")
