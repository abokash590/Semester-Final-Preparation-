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

    # 1. Screenshot 1(b)
    sub_b = card.locator(".subpart-solution-block").nth(1)
    sub_b.scroll_into_view_if_needed()
    page.wait_for_timeout(300)
    sub_b.screenshot(path="screenshots/human_style_1b.png")

    # 2. Screenshot 1(c)
    sub_c = card.locator(".subpart-solution-block").nth(2)
    sub_c.scroll_into_view_if_needed()
    page.wait_for_timeout(300)
    sub_c.screenshot(path="screenshots/human_style_1c.png")

    # 3. Screenshot end marker
    end_marker = card.locator(".solution-set-end-tag")
    if end_marker.count() > 0:
        end_marker.scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        end_marker.screenshot(path="screenshots/human_style_end_marker.png")

    # Full drawer bottom screenshot
    card.screenshot(path="screenshots/human_style_full_card.png")
    print("Screenshots taken successfully!")
    browser.close()
