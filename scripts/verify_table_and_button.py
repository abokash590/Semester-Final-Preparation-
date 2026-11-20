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

        # 1. Verify button text
        buttons = await page.locator(".solution-toggle-btn span").all_text_contents()
        print(f"First 3 button labels: {buttons[:3]}")
        for b in buttons:
            assert b == "Reveal Solution", f"Expected 'Reveal Solution', got '{b}'"
        print("All buttons now strictly show 'Reveal Solution'!")

        # 2. Check Question 3 with heuristic table
        q3_card = page.locator("#card-cse-4101-final-2023-set3")
        await q3_card.scroll_into_view_if_needed()
        await page.wait_for_timeout(500)

        table = q3_card.locator("table.data-table")
        assert await table.count() > 0, "Heuristic table not found in Q3!"

        # Check thead styling
        th = table.locator("th").first
        th_bg = await th.evaluate("el => window.getComputedStyle(el).backgroundColor")
        print(f"Header th background: {th_bg}")
        assert "241, 245, 249" in th_bg, f"Expected rgb(241, 245, 249), got: {th_bg}"

        # Check zebra striping on tbody rows
        rows = table.locator("tbody tr")
        row_count = await rows.count()
        print(f"Table row count: {row_count}")
        assert row_count > 1, f"Expected multiple rows, got {row_count}"

        row1_bg = await rows.nth(0).evaluate("el => window.getComputedStyle(el).backgroundColor")
        row2_bg = await rows.nth(1).evaluate("el => window.getComputedStyle(el).backgroundColor")
        print(f"Row 1 bg (odd): {row1_bg}")
        print(f"Row 2 bg (even): {row2_bg}")
        assert row1_bg != row2_bg, "Zebra striping failed: row 1 and row 2 have same color!"
        assert "248, 250, 252" in row2_bg or "255, 255, 255" in row1_bg, "Zebra striping color mismatch!"

        # Screenshot normal table state
        await q3_card.screenshot(path=str(SCREENSHOT_DIR / "table_zebra_striping.png"))
        print("Saved table_zebra_striping.png")

        # Hover over row 2 and verify hover color
        await rows.nth(1).hover()
        await page.wait_for_timeout(300)
        hover_bg = await rows.nth(1).evaluate("el => window.getComputedStyle(el).backgroundColor")
        print(f"Row 2 hover bg: {hover_bg}")
        assert "240, 253, 244" in hover_bg, f"Expected hover rgb(240, 253, 244), got {hover_bg}"

        # Screenshot hovered table state
        await q3_card.screenshot(path=str(SCREENSHOT_DIR / "table_row_hovered.png"))
        print("Saved table_row_hovered.png")

        print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
