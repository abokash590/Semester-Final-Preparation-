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

        # 1. Check Question 3 with heuristic table
        q3_card = page.locator("#card-cse-4101-final-2023-set3")
        await q3_card.scroll_into_view_if_needed()
        await page.wait_for_timeout(500)

        wrapper = q3_card.locator(".table-scroll-wrapper")
        assert await wrapper.count() > 0, "Table wrapper not found!"

        # Check outer border on wrapper
        border = await wrapper.evaluate("el => window.getComputedStyle(el).border")
        print(f"Wrapper border: {border}")
        assert "solid" in border, f"Wrapper missing border: {border}"

        table = q3_card.locator("table.data-table")
        # Check thead th: 1st row green accent tune
        th = table.locator("th").first
        th_bg = await th.evaluate("el => window.getComputedStyle(el).backgroundColor")
        th_color = await th.evaluate("el => window.getComputedStyle(el).color")
        print(f"Header th bg: {th_bg}, color: {th_color}")
        assert "235, 244, 240" in th_bg, f"Expected #EBF4F0, got: {th_bg}"
        assert "16, 69, 53" in th_color, f"Expected #104535, got: {th_color}"

        # Check zebra striping: White then Ash (chai color)
        rows = table.locator("tbody tr")
        row1_bg = await rows.nth(0).evaluate("el => window.getComputedStyle(el).backgroundColor")
        row2_bg = await rows.nth(1).evaluate("el => window.getComputedStyle(el).backgroundColor")
        print(f"Row 1 bg (odd, white): {row1_bg}")
        print(f"Row 2 bg (even, ash): {row2_bg}")
        assert "255, 255, 255" in row1_bg, f"Expected white for row 1, got: {row1_bg}"
        assert "241, 243, 245" in row2_bg, f"Expected ash #F1F3F5 for row 2, got: {row2_bg}"

        # Screenshot normal table state
        await q3_card.screenshot(path=str(SCREENSHOT_DIR / "table_perfect_style.png"))
        print("Saved table_perfect_style.png")

        # Hover over row 2 and verify hover color
        await rows.nth(1).hover()
        await page.wait_for_timeout(300)
        hover_bg = await rows.nth(1).evaluate("el => window.getComputedStyle(el).backgroundColor")
        print(f"Row 2 hover bg: {hover_bg}")
        assert "226, 239, 233" in hover_bg, f"Expected hover rgb(226, 239, 233), got {hover_bg}"

        # Screenshot hovered table state
        await q3_card.screenshot(path=str(SCREENSHOT_DIR / "table_perfect_hovered.png"))
        print("Saved table_perfect_hovered.png")

        print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
