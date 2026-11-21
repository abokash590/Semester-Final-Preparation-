import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel="msedge")
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        await page.goto("http://localhost:8000/#cse-4101", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        # 1. CSE-4101 NITER
        print("Selecting NITER on CSE-4101...")
        await page.evaluate("app.enterCourse('CSE-4101')")
        await page.wait_for_timeout(500)
        await page.evaluate("app.selectTermTestCollege('NITER')")
        await page.wait_for_timeout(1000)
        
        tt1 = page.locator("#card-cse-4101-term-niter-tt1")
        if await tt1.count() > 0:
            await tt1.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await tt1.screenshot(path="screenshots/niter_ai_tt1.png")
            print("Saved screenshots/niter_ai_tt1.png")
            
            # Click reveal solution
            btn = tt1.locator(".solution-toggle-btn").first
            await btn.click()
            await page.wait_for_timeout(500)
            await tt1.screenshot(path="screenshots/niter_ai_tt1_revealed.png")
            print("Saved screenshots/niter_ai_tt1_revealed.png")
            
        tt2 = page.locator("#card-cse-4101-term-niter-tt2")
        if await tt2.count() > 0:
            await tt2.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await tt2.screenshot(path="screenshots/niter_ai_tt2.png")
            print("Saved screenshots/niter_ai_tt2.png")
            
        # 2. CSE-4102 Math
        print("Selecting CSE-4102 NITER...")
        await page.evaluate("app.enterCourse('CSE-4102')")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.selectTermTestCollege('NITER')")
        await page.wait_for_timeout(500)
        
        math_tt1 = page.locator("#card-cse-4102-term-niter-tt1")
        if await math_tt1.count() > 0:
            await math_tt1.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await math_tt1.screenshot(path="screenshots/niter_math_tt1.png")
            print("Saved screenshots/niter_math_tt1.png")

        # 3. CSE-4125 ML
        print("Selecting CSE-4125 NITER...")
        await page.evaluate("app.enterCourse('CSE-4125')")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.selectTermTestCollege('NITER')")
        await page.wait_for_timeout(500)
        
        ml_tt1 = page.locator("#card-cse-4125-term-niter-tt1")
        if await ml_tt1.count() > 0:
            await ml_tt1.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await ml_tt1.screenshot(path="screenshots/niter_ml_tt1.png")
            print("Saved screenshots/niter_ml_tt1.png")

        # 4. CSE-4126 DS
        print("Selecting CSE-4126 NITER...")
        await page.evaluate("app.enterCourse('CSE-4126')")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.selectTermTestCollege('NITER')")
        await page.wait_for_timeout(500)
        
        ds_tt1 = page.locator("#card-cse-4126-term-niter-tt1")
        if await ds_tt1.count() > 0:
            await ds_tt1.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await ds_tt1.screenshot(path="screenshots/niter_ds_tt1.png")
            print("Saved screenshots/niter_ds_tt1.png")

        # 5. SS-4103 ENT
        print("Selecting SS-4103 NITER...")
        await page.evaluate("app.enterCourse('SS-4103')")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.selectTermTestCollege('NITER')")
        await page.wait_for_timeout(500)
        
        ent_tt2 = page.locator("#card-ss-4103-term-niter-tt2")
        if await ent_tt2.count() > 0:
            await ent_tt2.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await ent_tt2.screenshot(path="screenshots/niter_ent_tt2.png")
            print("Saved screenshots/niter_ent_tt2.png")

        await browser.close()
        print("All cards captured successfully!")

if __name__ == "__main__":
    asyncio.run(main())
