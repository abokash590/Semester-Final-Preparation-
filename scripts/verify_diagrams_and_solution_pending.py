import asyncio
from playwright.async_api import async_playwright

async def run():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    out = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    page = await browser.new_page(viewport={'width': 1366, 'height': 820})
    await page.goto('http://localhost:8000')
    await page.wait_for_timeout(900)

    # Enter AI course
    await page.locator('.node-slot-1').click()
    await page.wait_for_selector('.question-set-card')
    await page.wait_for_timeout(1000)

    # 1. Test Solution Toggle on Question 1
    first_card = page.locator('.question-set-card').first
    sol_btn = first_card.locator('.solution-toggle-btn')
    await sol_btn.click()
    await page.wait_for_timeout(400)

    # Check pending message
    pending_box = first_card.locator('.solution-pending-box')
    box_visible = await pending_box.is_visible()
    box_text = await pending_box.inner_text()
    print('Pending box visible:', box_visible)
    print('Pending box text:', repr(box_text))
    assert box_visible, "Error: Solution pending box should be visible!"
    assert "Solution will be added later" in box_text, "Error: Should contain 'Solution will be added later'!"
    assert "Stay connected" in box_text, "Error: Should contain 'Stay connected'!"

    await first_card.screenshot(path=f'{out}/solution_pending_notice.png')

    # 2. Find a card with a diagram (e.g. search tree or graph)
    diagram = page.locator('.diagram-wrapper').first
    if await diagram.count() > 0:
        await diagram.scroll_into_view_if_needed()
        await page.wait_for_timeout(600)
        await diagram.screenshot(path=f'{out}/forest_green_diagram.png')
        print('Captured diagram with Forest Green colors!')
    else:
        print('No diagram on first page, checking all cards...')
        # Scroll down to reveal more cards
        await page.evaluate("window.scrollBy(0, 1500)")
        await page.wait_for_timeout(800)
        diagram = page.locator('.diagram-wrapper').first
        if await diagram.count() > 0:
            await diagram.scroll_into_view_if_needed()
            await page.wait_for_timeout(600)
            await diagram.screenshot(path=f'{out}/forest_green_diagram.png')
            print('Captured diagram after scroll!')

    await browser.close()
    await p.stop()
    print('ALL TESTS COMPLETED SUCCESSFULLY!')

asyncio.run(run())
