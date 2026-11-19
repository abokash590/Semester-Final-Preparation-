import asyncio
from playwright.async_api import async_playwright

async def run():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    
    out_dir = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'
    
    # Test 1: Desktop 1366x820 - Home Page
    page = await browser.new_page(viewport={'width': 1366, 'height': 820})
    await page.goto('http://localhost:8000')
    await page.wait_for_timeout(1000)
    
    # Verify header is hidden on Home page
    header_is_hidden = await page.locator('.app-header').is_hidden()
    print('Header is hidden on Home page:', header_is_hidden)
    assert header_is_hidden, "Error: Header should be hidden on Home page!"
    
    # Capture Home View
    await page.screenshot(path=f'{out_dir}/home_page_no_navbar.png')
    
    # Test 2: Enter Course 1 (AI) via Bird Nest
    await page.locator('.node-slot-1').click()
    await page.wait_for_selector('.question-set-card')
    await page.wait_for_timeout(800)
    
    # Verify header is now visible on Course page
    header_is_visible = await page.locator('.app-header').is_visible()
    print('Header is visible on Course page:', header_is_visible)
    assert header_is_visible, "Error: Header should be visible on Course page!"
    
    # Capture Course View with New Navbar
    await page.screenshot(path=f'{out_dir}/course_page_with_navbar.png')
    
    # Capture Header Closeup
    header = page.locator('.app-header')
    await header.screenshot(path=f'{out_dir}/course_header_closeup.png')
    
    active_pill = await page.locator('.course-nav-pill.active').inner_text()
    print('Active nav pill on AI course page:', repr(active_pill))
    
    # Test 3: Click Course 2 (MSA)
    await page.locator('.course-nav-pill[data-code="CSE-4102"]').click()
    await page.wait_for_timeout(600)
    active_pill_msa = await page.locator('.course-nav-pill.active').inner_text()
    print('Active nav pill on MSA course page:', repr(active_pill_msa))
    
    # Test 4: Click 'Home' pill in navbar to return to Home page
    await page.locator('.course-nav-pill', has_text='Home').click()
    await page.wait_for_timeout(800)
    
    header_hidden_again = await page.locator('.app-header').is_hidden()
    print('Header is hidden after returning to Home:', header_hidden_again)
    assert header_hidden_again, "Error: Header should be hidden after returning to Home!"
    await page.screenshot(path=f'{out_dir}/returned_home_no_navbar.png')
    
    # Test 5: Mobile (375x812)
    mobile_page = await browser.new_page(viewport={'width': 375, 'height': 812})
    await mobile_page.goto('http://localhost:8000')
    await mobile_page.wait_for_timeout(1000)
    
    mobile_home_hidden = await mobile_page.locator('.app-header').is_hidden()
    print('Mobile Home header hidden:', mobile_home_hidden)
    assert mobile_home_hidden, "Error: Header should be hidden on mobile Home!"
    
    # Enter course on mobile
    await mobile_page.locator('.node-slot-1').click()
    await mobile_page.wait_for_selector('.question-set-card')
    await mobile_page.wait_for_timeout(800)
    
    mobile_course_visible = await mobile_page.locator('.app-header').is_visible()
    print('Mobile Course header visible:', mobile_course_visible)
    assert mobile_course_visible, "Error: Header should be visible on mobile Course!"
    
    await mobile_page.screenshot(path=f'{out_dir}/mobile_course_page_navbar.png')
    await mobile_page.locator('.app-header').screenshot(path=f'{out_dir}/mobile_header_closeup.png')
    
    await browser.close()
    await p.stop()
    print('ALL TESTS PASSED! Home has no navbar, Course has new navbar!')

asyncio.run(run())
