import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(r"T:\Project\7th Semester")
SCREENSHOT_DIR = ROOT / "screenshots"

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome", headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:8000/#cse-4101", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # 1. Verify Drive button exists
        drive_btn = page.locator("#driveLinksBtn")
        assert await drive_btn.count() == 1, "Drive button not found!"
        print("Drive button found in header.")

        # 2. Click Drive button and verify popover opens
        await drive_btn.click()
        await page.wait_for_timeout(300)
        drive_pop = page.locator("#driveLinksPopover")
        is_hidden = await drive_pop.get_attribute("hidden")
        assert is_hidden is None, f"Drive popover should be visible but hidden={is_hidden}"
        print("Drive popover opened successfully.")

        # 3. Verify 4 drive cards in 2x2 grid
        cards = await page.locator(".drive-card").all_text_contents()
        print(f"Drive cards: {cards}")
        assert len(cards) == 4, f"Expected 4 drive cards, got {len(cards)}"

        # 4. Verify card labels
        labels = await page.locator(".drive-card-label").all_text_contents()
        print(f"Drive card labels: {labels}")
        assert labels == ["MEC", "NITER", "FEC", "SIMT"], f"Unexpected labels: {labels}"

        # 5. Verify correct hrefs
        mec_href = await page.locator(".drive-card").first.get_attribute("href")
        assert "1nU4SPxKwUr5Mhvd57NwVb_G65nsdZ6Tj" in mec_href, f"MEC href wrong: {mec_href}"
        print("All drive links verified correctly.")

        # 6. Screenshot with popover open
        await page.screenshot(path=str(SCREENSHOT_DIR / "drive_links_popover_open.png"))
        print("Saved drive_links_popover_open.png")

        # 7. Click outside to close
        await page.click("body", position={"x": 700, "y": 400})
        await page.wait_for_timeout(300)
        is_hidden_after = await drive_pop.get_attribute("hidden")
        assert is_hidden_after is not None, "Drive popover should be hidden after clicking outside"
        print("Drive popover closed by clicking outside.")

        print("ALL DRIVE LINK VERIFICATIONS PASSED!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
