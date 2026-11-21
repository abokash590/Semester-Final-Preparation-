import re
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='msedge', headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    page.goto('http://localhost:8000/#cse-4101')
    page.wait_for_timeout(1000)

    # Let's find all tables on the page
    tables = page.locator('table')
    print('Total tables on page:', tables.count())
    for i in range(tables.count()):
        tbl = tables.nth(i)
        txt = tbl.inner_text()
        print(f"Table {i}: {txt[:40].replace(chr(10), ' ')}")
        if 'Node' in txt or 'h(n)' in txt:
            print(f"Found Node table at index {i}")
            tbl.scroll_into_view_if_needed()
            page.wait_for_timeout(300)
            # Take screenshot of wrapper and table
            wrapper = tbl.locator('xpath=ancestor::div[contains(@class, "table-scroll-wrapper")]')
            if wrapper.count() > 0:
                wrapper.screenshot(path='screenshots/node_table_wrapper.png')
            else:
                tbl.screenshot(path='screenshots/node_table_wrapper.png')
            
            # Hover on row 3
            rows = tbl.locator('tr')
            if rows.count() > 5:
                rows.nth(4).hover()
                page.wait_for_timeout(300)
                if wrapper.count() > 0:
                    wrapper.screenshot(path='screenshots/node_table_hover.png')
                else:
                    tbl.screenshot(path='screenshots/node_table_hover.png')
            break

    browser.close()
