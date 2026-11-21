from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 1000})
    page.goto("http://localhost:8000/#cse-4101")
    page.wait_for_timeout(1000)
    page.evaluate("app.enterCourse('cse-4101')")
    page.wait_for_timeout(500)

    # Click on 2023 FINAL in scrollspy
    page.evaluate("app.scrollToSection('2023')")
    page.wait_for_timeout(600)

    # Locate card for cse-4101-final-2023-set1
    card = page.locator("#card-cse-4101-final-2023-set1")
    assert card.count() > 0, "Card cse-4101-final-2023-set1 should exist"

    # Click reveal solution
    btn = card.locator(".solution-toggle-btn")
    btn.click()
    page.wait_for_timeout(500)

    # Screenshot subpart 1(a) & 1(b)
    sub_b = card.locator(".subpart-solution-block").nth(1)
    sub_b.scroll_into_view_if_needed()
    page.wait_for_timeout(300)
    sub_b.screenshot(path="screenshots/ui_2023_q1_b_table.png")
    print("Screenshot 1(b) saved!")

    # Screenshot subpart 1(c)
    sub_c = card.locator(".subpart-solution-block").nth(2)
    sub_c.scroll_into_view_if_needed()
    page.wait_for_timeout(300)
    sub_c.screenshot(path="screenshots/ui_2023_q1_c_peas.png")
    print("Screenshot 1(c) saved!")

    browser.close()
    print("Verification completed successfully!")
