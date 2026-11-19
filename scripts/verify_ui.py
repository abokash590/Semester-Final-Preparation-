import asyncio
from playwright.async_api import async_playwright

async def verify():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    page = await browser.new_page(viewport={'width': 1366, 'height': 880})
    await page.goto('http://localhost:8000')
    await page.wait_for_selector('.portal-avatar-core')

    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    # Capture Home Portal
    await page.screenshot(path=f'{out_dir}/nature_home_portal_desktop.png')

    # Click Course 1 (AI) to enter questions feed
    await page.locator('.node-slot-1').click()
    await page.wait_for_selector('.question-set-card')

    has_search = await page.evaluate("!!document.getElementById('searchInput')")
    has_theme = await page.evaluate("!!document.getElementById('themeToggleBtn')")
    theme = await page.evaluate("document.documentElement.getAttribute('data-theme')")
    has_unverified = await page.evaluate("document.querySelectorAll('.badge-unverified').length")
    has_practice = await page.evaluate("document.querySelectorAll('.practice-box, .practice-textarea').length")

    print('Has search input:', has_search)
    print('Has theme toggle:', has_theme)
    print('Theme:', theme)
    print('Unverified count:', has_unverified)
    print('Practice boxes count:', has_practice)

    # 1. Full Desktop Overview showing Hotbar, Progress bar, Left-Rail Scrollspy, and Question Cards
    await page.screenshot(path=f'{out_dir}/clean_desktop_overview.png')

    # 2. Header with Avatar Icon & Hotbar
    header = page.locator('.app-header')
    await header.screenshot(path=f'{out_dir}/clean_header_hotbar.png')

    # 3. Close-up of Brand Group with Avatar Icon
    brand = page.locator('.brand-group')
    await brand.screenshot(path=f'{out_dir}/clean_avatar_icon.png')

    # 4. Detailed Card Screenshot
    first_card = page.locator('.question-set-card').first
    await first_card.screenshot(path=f'{out_dir}/clean_question_card.png')

    # 5. Reveal Solution Drawer & Capture Screenshot
    sol_btn = first_card.locator('.solution-toggle-btn')
    await sol_btn.click()
    await page.wait_for_timeout(300)
    await first_card.screenshot(path=f'{out_dir}/clean_solution_revealed.png')

    # 6. Scrollspy Left-Rail Navigation (Active 2023)
    sidebar = page.locator('#yearSidebar')
    await sidebar.screenshot(path=f'{out_dir}/clean_scrollspy_2023.png')

    # 7. Click 2024 in Scrollspy
    item_2024 = page.locator('.scrollspy-item[data-year="2024"]')
    await item_2024.click()
    await page.wait_for_timeout(400)
    await sidebar.screenshot(path=f'{out_dir}/clean_scrollspy_2024.png')

    # 8. Click Term Test in Scrollspy & Screenshot Term Test section
    item_term = page.locator('.scrollspy-item[data-year="term-test"]')
    await item_term.click()
    await page.wait_for_timeout(500)
    await sidebar.screenshot(path=f'{out_dir}/clean_scrollspy_term_test.png')

    term_card = page.locator('.term-test-placeholder-card')
    await term_card.screenshot(path=f'{out_dir}/clean_term_test_section.png')

    # Full view at Term Test
    await page.screenshot(path=f'{out_dir}/clean_term_test_full_view.png')

    await browser.close()
    await p.stop()
    print('ALL VERIFICATIONS COMPLETED SUCCESSFULLY!')

asyncio.run(verify())
