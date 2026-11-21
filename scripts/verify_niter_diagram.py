from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.goto("http://localhost:8000/#cse-4101")
    page.wait_for_timeout(1000)
    page.evaluate("app.enterCourse('cse-4101')")
    page.wait_for_timeout(500)

    # Select NITER
    page.evaluate("app.selectTermTestCollege('NITER')")
    page.wait_for_timeout(800)

    # Find the diagram in NITER Term Test 1
    card = page.locator("#termTestCardsContainer .question-card").first
    diag = card.locator(".mermaid-wrapper")
    if diag.count() > 0:
        diag.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        diag.screenshot(path="screenshots/niter_diagram_fixed.png")
        print("Diagram screenshot saved to screenshots/niter_diagram_fixed.png")
    else:
        card.screenshot(path="screenshots/niter_diagram_fixed.png")
        print("Card screenshot saved to screenshots/niter_diagram_fixed.png")

    browser.close()
