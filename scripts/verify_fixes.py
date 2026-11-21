from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.goto("http://localhost:8000/#cse-4101")
    page.wait_for_timeout(1000)
    page.evaluate("app.enterCourse('cse-4101')")
    page.wait_for_timeout(500)

    # 1. Test NITER 8-puzzle
    page.evaluate("app.selectTermTestCollege('NITER')")
    page.wait_for_timeout(600)
    niter_card = page.locator("#termTestCardsContainer .question-card").first
    puzzle = niter_card.locator(".puzzle-states-horizontal")
    assert puzzle.count() > 0, "NITER 8-puzzle should render as .puzzle-states-horizontal"
    puzzle.scroll_into_view_if_needed()
    page.wait_for_timeout(300)
    puzzle.screenshot(path="screenshots/niter_puzzle_fixed.png")
    print("NITER 8-puzzle side-by-side: Verified!")

    # 2. Test FEC Romania Map
    page.evaluate("app.selectTermTestCollege('FEC')")
    page.wait_for_timeout(600)
    fec_card = page.locator("#termTestCardsContainer .question-card").first
    svg_diag = fec_card.locator(".svg-diagram-wrapper")
    assert svg_diag.count() > 0, "FEC should render .svg-diagram-wrapper"
    svg_diag.scroll_into_view_if_needed()
    page.wait_for_timeout(300)
    fec_card.screenshot(path="screenshots/fec_romania_fixed.png")
    print("FEC Romania SVG Map: Verified!")

    browser.close()
    print("ALL VERIFICATIONS COMPLETED SUCCESSFULLY!")
