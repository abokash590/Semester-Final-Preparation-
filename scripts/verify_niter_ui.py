import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel="msedge")
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        print("Navigating to http://localhost:8000/ ...")
        await page.goto("http://localhost:8000/", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        # Test 1: Select NITER under CSE-4101
        print("Scrolling to term test section...")
        await page.evaluate("app.scrollToSection('term-test')")
        await page.wait_for_timeout(1000)
        
        print("Selecting NITER...")
        await page.evaluate("app.selectTermTestCollege('NITER')")
        await page.wait_for_timeout(1000)
        
        # Capture screenshot of CSE-4101 NITER term tests
        await page.screenshot(path="screenshots/niter_cse4101_view.png", full_page=False)
        print("Saved screenshots/niter_cse4101_view.png")
        
        # Reveal solution of first subpart
        reveal_btn = page.locator("#cse-4101-term-niter-tt1 .solution-toggle-btn").first
        if await reveal_btn.count() > 0:
            print("Clicking Reveal Solution...")
            await reveal_btn.click()
            await page.wait_for_timeout(500)
            await page.screenshot(path="screenshots/niter_solution_revealed.png")
            print("Saved screenshots/niter_solution_revealed.png")
            
        # Check Term Test 2 with Alpha-Beta tree
        tt2_card = page.locator("#cse-4101-term-niter-tt2")
        if await tt2_card.count() > 0:
            await tt2_card.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await page.screenshot(path="screenshots/niter_cse4101_tt2_tree.png")
            print("Saved screenshots/niter_cse4101_tt2_tree.png")

        # Test Course 2: CSE-4102 (Math)
        print("Switching to CSE-4102...")
        await page.evaluate("app.loadCourse('CSE-4102')")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.selectTermTestCollege('NITER')")
        await page.evaluate("app.scrollToSection('term-test')")
        await page.wait_for_timeout(500)
        await page.screenshot(path="screenshots/niter_cse4102_math.png")
        print("Saved screenshots/niter_cse4102_math.png")
        
        # Test Course 3: CSE-4125 (ML)
        print("Switching to CSE-4125...")
        await page.evaluate("app.loadCourse('CSE-4125')")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.selectTermTestCollege('NITER')")
        await page.evaluate("app.scrollToSection('term-test')")
        await page.wait_for_timeout(500)
        await page.screenshot(path="screenshots/niter_cse4125_ml.png")
        print("Saved screenshots/niter_cse4125_ml.png")

        # Test Course 4: CSE-4126 (DS)
        print("Switching to CSE-4126...")
        await page.evaluate("app.loadCourse('CSE-4126')")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.selectTermTestCollege('NITER')")
        await page.evaluate("app.scrollToSection('term-test')")
        await page.wait_for_timeout(500)
        await page.screenshot(path="screenshots/niter_cse4126_ds.png")
        print("Saved screenshots/niter_cse4126_ds.png")

        # Test Course 5: SS-4103 (ENT)
        print("Switching to SS-4103...")
        await page.evaluate("app.loadCourse('SS-4103')")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.selectTermTestCollege('NITER')")
        await page.evaluate("app.scrollToSection('term-test')")
        await page.wait_for_timeout(500)
        await page.screenshot(path="screenshots/niter_ss4103_ent.png")
        print("Saved screenshots/niter_ss4103_ent.png")

        await browser.close()
        print("All visual verification tests completed successfully!")

if __name__ == "__main__":
    asyncio.run(main())
