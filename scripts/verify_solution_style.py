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

        # Click Reveal Solution on Question 1
        reveal_btn = page.locator(".question-card").first.locator(".solution-toggle-btn")
        await reveal_btn.click()
        await page.wait_for_timeout(500)

        # Screenshot the revealed solution
        await page.screenshot(path=str(SCREENSHOT_DIR / "solution_outer_box_removed.png"))
        print("Saved screenshots/solution_outer_box_removed.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
