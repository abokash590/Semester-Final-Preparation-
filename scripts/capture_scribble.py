from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 1000})
    page.goto("http://localhost:8000/#cse-4101")
    page.wait_for_timeout(1000)
    page.evaluate("app.enterCourse('cse-4101')")
    page.wait_for_timeout(500)
    page.evaluate("app.scrollToSection('2023')")
    page.wait_for_timeout(600)

    card = page.locator("#card-cse-4101-final-2023-set1")
    btn = card.locator(".solution-toggle-btn")
    btn.click()
    page.wait_for_timeout(500)

    # Capture the transition between 1(a) and 1(b) showing the scribble underline
    divider = card.locator(".subpart-scribble-divider").first
    divider.scroll_into_view_if_needed()
    page.wait_for_timeout(300)

    # Screenshot area containing 1(a) bottom, scribble divider, and 1(b) top
    sub_a = card.locator(".subpart-solution-block").nth(0)
    sub_b = card.locator(".subpart-solution-block").nth(1)
    
    # Let's screenshot from sub_a through sub_b
    sub_a.screenshot(path="screenshots/scribble_1a_unboxed.png")
    divider.screenshot(path="screenshots/scribble_divider_only.png")

    # Take screenshot of the entire upper solution area
    sol_body = card.locator(".subparts-solutions-wrapper")
    page.evaluate("window.scrollTo(0, document.querySelector('#card-cse-4101-final-2023-set1 .solution-drawer-body').offsetTop - 60)")
    page.wait_for_timeout(400)
    page.screenshot(path="screenshots/scribble_in_action.png")

    print("Screenshots taken successfully!")
    browser.close()
