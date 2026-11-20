import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(r"T:\Project\7th Semester")
SCREENSHOT_DIR = ROOT / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=True)
        context = await browser.new_context(viewport={"width": 1440, "height": 900})
        page = await context.new_page()

        print("1. Loading http://localhost:8000/#cse-4101...")
        await page.goto("http://localhost:8000/#cse-4101", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # Check 2024 Final scrollspy nodes: should strictly be Q1-Q7!
        spy_2024_nodes = await page.locator('.scrollspy-item[data-year="2024"] .scrollspy-thread-node').all_text_contents()
        print(f"2024 Final Scrollspy Nodes: {spy_2024_nodes}")
        assert spy_2024_nodes == ["Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7"], f"2024 nodes still contain term tests: {spy_2024_nodes}"

        # Scroll to Term Test section
        print("2. Scrolling to Term Test section...")
        await page.locator("#year-section-term-test").scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)

        # Check Term Test scrollspy nodes under MEC
        sub_tt_nodes = await page.locator('.college-node-group .college-subthread .scrollspy-sub-tt-node').all_text_contents()
        print(f"Term Test Sub-nodes under MEC: {sub_tt_nodes}")
        assert sub_tt_nodes == ["Term Test 01", "Term Test 02"], f"Unexpected MEC subnodes: {sub_tt_nodes}"

        # Take screenshot of the clean scrollspy with MEC subthread
        await page.screenshot(path=str(SCREENSHOT_DIR / "clean_scrollspy_mec_subnodes.png"))
        print("Saved clean_scrollspy_mec_subnodes.png")

        # Verify that Question Card body NO LONGER contains redundant paper header
        card_text = await page.locator("#termTestCardsContainer .question-card").first.locator(".question-set-body").text_content()
        print(f"First card body preview: {repr(card_text[:120])}")
        assert "Mymensingh Engineering College (MEC)" not in card_text, "Redundant header still present!"
        assert "Course No: CSE-4101" not in card_text, "Redundant course code still present!"
        assert card_text.strip().startswith("(a) What is Heuristic Function?"), f"Card doesn't start with question! Starts with: {repr(card_text[:60])}"

        # Take screenshot of clean question card
        await page.screenshot(path=str(SCREENSHOT_DIR / "clean_term_test_card_no_header.png"))
        print("Saved clean_term_test_card_no_header.png")

        # Check Math CSE-4102
        print("3. Checking Math CSE-4102 for 3 Term Tests...")
        await page.goto("http://localhost:8000/#cse-4102", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        await page.locator("#year-section-term-test").scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)

        math_sub_tt_nodes = await page.locator('.college-node-group .college-subthread .scrollspy-sub-tt-node').all_text_contents()
        print(f"Math Term Test Sub-nodes under MEC: {math_sub_tt_nodes}")
        assert math_sub_tt_nodes == ["Term Test 01", "Term Test 02", "Term Test 03"], f"Expected 3 subnodes for Math, got: {math_sub_tt_nodes}"

        # Take screenshot of Math Term Test scrollspy
        await page.screenshot(path=str(SCREENSHOT_DIR / "math_scrollspy_3_subnodes.png"))
        print("Saved math_scrollspy_3_subnodes.png")

        print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
