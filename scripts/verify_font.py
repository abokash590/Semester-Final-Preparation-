import asyncio
from playwright.async_api import async_playwright

async def check_font():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel="chrome", headless=True)
        page = await b.new_page(viewport={"width": 1440, "height": 900})
        await page.goto("http://localhost:8000/#cse-4101", wait_until="networkidle")
        await page.wait_for_timeout(1000)

        body_font = await page.evaluate("() => window.getComputedStyle(document.body).fontFamily")
        print(f"Body computed font-family: {body_font}")
        assert "Inter" in body_font, f"Expected Inter in body font, got: {body_font}"

        card_font = await page.evaluate("() => window.getComputedStyle(document.querySelector('.question-set-body')).fontFamily")
        print(f"Question set body computed font-family: {card_font}")
        assert "Inter" in card_font, f"Expected Inter in card body font, got: {card_font}"

        pill_font = await page.evaluate("() => window.getComputedStyle(document.querySelector('.term-college-pill')).fontFamily")
        print(f"College pill computed font-family: {pill_font}")
        assert "Inter" in pill_font, f"Expected Inter in pill font, got: {pill_font}"

        label_font = await page.evaluate("() => window.getComputedStyle(document.querySelector('.scrollspy-label')).fontFamily")
        print(f"Scrollspy label computed font-family: {label_font}")
        assert "Inter" in label_font, f"Expected Inter in scrollspy label, got: {label_font}"

        await page.screenshot(path="screenshots/inter_font_typography.png")
        print("Saved screenshots/inter_font_typography.png")
        await b.close()

if __name__ == "__main__":
    asyncio.run(check_font())
