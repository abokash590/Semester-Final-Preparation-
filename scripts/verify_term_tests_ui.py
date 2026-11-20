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

        # Verify college pills in Term Test section
        pills = await page.locator(".term-college-pill").all_text_contents()
        print(f"College pills found: {pills}")
        assert pills == ["MEC", "FEC", "NITER", "ShEC", "SIMT"], f"Unexpected pills: {pills}"

        # Verify active pill is MEC
        active_pill = page.locator(".term-college-pill.active")
        active_text = await active_pill.text_content()
        assert active_text.strip() == "MEC", f"Active pill is {active_text}"
        
        # Check active pill style (background color #104535 -> rgb(16, 69, 53))
        bg_color = await active_pill.evaluate("el => window.getComputedStyle(el).backgroundColor")
        print(f"Active pill background color: {bg_color}")
        assert "16, 69, 53" in bg_color, f"Active pill background is not #104535! Got {bg_color}"

        # Scroll to Term Test section
        print("2. Scrolling to #year-section-term-test...")
        await page.locator("#year-section-term-test").scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)

        # Check left scrollspy active college node
        active_spy_college = page.locator(".college-thread-node.active-college")
        spy_text = await active_spy_college.text_content()
        print(f"Scrollspy active college: {spy_text}")
        spy_bg = await active_spy_college.evaluate("el => window.getComputedStyle(el).backgroundColor")
        print(f"Scrollspy active college bg: {spy_bg}")
        assert "16, 69, 53" in spy_bg, f"Scrollspy active college is not #104535! Got {spy_bg}"

        # Screenshot Term Test Section with MEC active
        await page.screenshot(path=str(SCREENSHOT_DIR / "term_test_mec_green.png"))
        print("Saved term_test_mec_green.png")

        # Click FEC
        print("3. Clicking FEC pill...")
        await page.locator(".term-college-pill", has_text="FEC").click()
        await page.wait_for_timeout(500)
        await page.screenshot(path=str(SCREENSHOT_DIR / "term_test_fec_placeholder.png"))
        print("Saved term_test_fec_placeholder.png")

        # Click back to MEC
        print("4. Clicking back to MEC pill...")
        await page.locator(".term-college-pill", has_text="MEC").click()
        await page.wait_for_timeout(500)

        # Reveal Solution for Term Test 1
        reveal_btn = page.locator("#termTestCardsContainer button:has-text('Reveal Solution for Term Test 1')")
        if await reveal_btn.count() > 0:
            print("5. Clicking Reveal Solution for Term Test 1...")
            await reveal_btn.click()
            await page.wait_for_timeout(1000)
            await page.screenshot(path=str(SCREENSHOT_DIR / "term_test_solution_revealed.png"))
            print("Saved term_test_solution_revealed.png")

        # Navigate to Math CSE-4102
        print("6. Navigating to Math CSE-4102...")
        await page.goto("http://localhost:8000/#cse-4102", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        await page.locator("#year-section-term-test").scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        
        # Check term test cards in Math
        math_cards = await page.locator("#termTestCardsContainer .question-card").count()
        print(f"Math term test cards count: {math_cards}")
        assert math_cards == 3, f"Expected 3 term test cards for Math, got {math_cards}"
        await page.screenshot(path=str(SCREENSHOT_DIR / "term_test_math_3_cards.png"))
        print("Saved term_test_math_3_cards.png")

        # Check DS CSE-4126
        print("7. Navigating to DS CSE-4126...")
        await page.goto("http://localhost:8000/#cse-4126", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        await page.locator("#year-section-term-test").scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        ds_cards = await page.locator("#termTestCardsContainer .question-card").count()
        print(f"DS term test cards count: {ds_cards}")
        assert ds_cards == 2, f"Expected 2 term test cards for DS, got {ds_cards}"

        # Check ML CSE-4125
        print("8. Navigating to ML CSE-4125...")
        await page.goto("http://localhost:8000/#cse-4125", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        await page.locator("#year-section-term-test").scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        ml_cards = await page.locator("#termTestCardsContainer .question-card").count()
        print(f"ML term test cards count: {ml_cards}")
        assert ml_cards == 2, f"Expected 2 term test cards for ML, got {ml_cards}"

        # Check ENT SS-4103
        print("9. Navigating to ENT SS-4103...")
        await page.goto("http://localhost:8000/#ss-4103", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        await page.locator("#year-section-term-test").scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        ent_cards = await page.locator("#termTestCardsContainer .question-card").count()
        print(f"ENT term test cards count: {ent_cards}")
        assert ent_cards == 2, f"Expected 2 term test cards for ENT, got {ent_cards}"

        print("ALL VERIFICATIONS PASSED SUCCESSFULLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
