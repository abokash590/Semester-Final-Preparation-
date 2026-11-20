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
        await page.wait_for_timeout(600)

        # 1. Initial cards in view should be revealed
        first_card = page.locator(".question-set-card").first
        first_class = await first_card.get_attribute("class")
        print(f"First card classes: {first_class}")
        assert "reveal-on-scroll" in first_class
        assert "is-revealed" in first_class, "First card should be revealed in initial viewport!"

        # 2. Card far down (e.g. 2024 Q7)
        q7_card = page.locator("#card-cse-4101-final-2024-set7")
        if await q7_card.count() > 0:
            q7_class = await q7_card.get_attribute("class")
            print(f"2024 Q7 card classes before scroll: {q7_class}")
            # Should not yet be revealed if far below viewport
            # Now scroll it into view
            await q7_card.scroll_into_view_if_needed()
            await page.wait_for_timeout(600)
            q7_class_after = await q7_card.get_attribute("class")
            print(f"2024 Q7 card classes after scroll: {q7_class_after}")
            assert "is-revealed" in q7_class_after, "Q7 should receive is-revealed after scrolling into view!"

        # 3. Screenshot after scrolling
        await page.screenshot(path=str(SCREENSHOT_DIR / "scroll_reveal_active.png"))
        print("Saved screenshots/scroll_reveal_active.png")

        print("GENTLE SCROLL REVEAL VERIFICATION PASSED!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
