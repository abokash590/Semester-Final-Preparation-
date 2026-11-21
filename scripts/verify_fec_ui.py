import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, channel="msedge")
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        
        # 1. CSE-4101 (AI) - FEC Term Test 1
        print("Navigating to CSE-4101 with FEC...")
        await page.goto("http://localhost:8000/#cse-4101", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.enterCourse('CSE-4101')")
        await page.wait_for_timeout(500)
        await page.evaluate("app.selectTermTestCollege('FEC')")
        await page.wait_for_timeout(1000)
        
        tt1 = page.locator("#card-cse-4101-term-fec-tt1")
        if await tt1.count() > 0:
            await tt1.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await tt1.screenshot(path="screenshots/fec_ai_tt1.png")
            print("Saved screenshots/fec_ai_tt1.png")
            
            # Reveal solution
            btn = tt1.locator(".solution-toggle-btn").first
            await btn.click()
            await page.wait_for_timeout(500)
            await tt1.screenshot(path="screenshots/fec_ai_tt1_revealed.png")
            print("Saved screenshots/fec_ai_tt1_revealed.png")

        # 2. CSE-4101 (AI) - FEC Term Test 2
        tt2 = page.locator("#card-cse-4101-term-fec-tt2")
        if await tt2.count() > 0:
            await tt2.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await tt2.screenshot(path="screenshots/fec_ai_tt2.png")
            print("Saved screenshots/fec_ai_tt2.png")

        # 3. CSE-4125 (ML) - FEC Term Test 2 (PCA & Entropy)
        print("Switching to CSE-4125 FEC...")
        await page.evaluate("app.enterCourse('CSE-4125')")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.selectTermTestCollege('FEC')")
        await page.wait_for_timeout(500)
        
        ml_tt2 = page.locator("#card-cse-4125-term-fec-tt2")
        if await ml_tt2.count() > 0:
            await ml_tt2.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await ml_tt2.screenshot(path="screenshots/fec_ml_tt2.png")
            print("Saved screenshots/fec_ml_tt2.png")

        # 4. CSE-4126 (DS) - FEC Term Test 1 (KNN & Chi-Square)
        print("Switching to CSE-4126 FEC...")
        await page.evaluate("app.enterCourse('CSE-4126')")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.selectTermTestCollege('FEC')")
        await page.wait_for_timeout(500)
        
        ds_tt1 = page.locator("#card-cse-4126-term-fec-tt1")
        if await ds_tt1.count() > 0:
            await ds_tt1.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await ds_tt1.screenshot(path="screenshots/fec_ds_tt1.png")
            print("Saved screenshots/fec_ds_tt1.png")

        # 5. SS-4103 (ENT) - FEC Term Test 1 & 2
        print("Switching to SS-4103 FEC...")
        await page.evaluate("app.enterCourse('SS-4103')")
        await page.wait_for_timeout(1000)
        await page.evaluate("app.selectTermTestCollege('FEC')")
        await page.wait_for_timeout(500)
        
        ent_tt1 = page.locator("#card-ss-4103-term-fec-tt1")
        if await ent_tt1.count() > 0:
            await ent_tt1.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await ent_tt1.screenshot(path="screenshots/fec_ent_tt1.png")
            print("Saved screenshots/fec_ent_tt1.png")

        await browser.close()
        print("All FEC verification screenshots captured successfully!")

if __name__ == "__main__":
    asyncio.run(main())
