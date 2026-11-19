import asyncio
from playwright.async_api import async_playwright

async def run():
    p = await async_playwright().start()
    browser = await p.chromium.launch(channel='chrome')
    out = 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots'

    page = await browser.new_page(viewport={'width': 1366, 'height': 820})
    await page.goto('http://localhost:8000')
    await page.wait_for_timeout(900)

    # Enter Course 1 (AI)
    await page.locator('.node-slot-1').click()
    await page.wait_for_selector('.question-set-card')
    await page.wait_for_timeout(800)

    # 1. Verify progress bar & question count bar is hidden/gone
    progress_visible = await page.locator('.progress-bar-strip').is_visible()
    header_bar_visible = await page.locator('.results-header-bar').is_visible()
    print('Progress bar visible:', progress_visible)
    print('Results header bar visible:', header_bar_visible)
    assert not progress_visible, "Error: Progress bar strip should be removed!"
    assert not header_bar_visible, "Error: Results header bar should be removed!"

    # 2. Verify Countdown Chip
    chip = page.locator('#examCountdownBtn')
    chip_visible = await chip.is_visible()
    chip_text = await chip.inner_text()
    print('Countdown chip visible:', chip_visible)
    print('Countdown chip text:', repr(chip_text))
    assert chip_visible, "Error: Exam countdown chip should be visible!"

    # Capture Header with Countdown Chip
    hdr = page.locator('.app-header')
    await hdr.screenshot(path=f'{out}/course_header_with_countdown.png')

    # Capture Course Full Page showing progress bar is gone
    await page.screenshot(path=f'{out}/course_page_no_progress_bar.png')

    # 3. Click Countdown Chip to open Exam Routine Popover
    await chip.click()
    await page.wait_for_timeout(400)
    popover = page.locator('#examSchedulePopover')
    popover_visible = await popover.is_visible()
    print('Popover visible on click:', popover_visible)
    assert popover_visible, "Error: Popover should be visible on click!"

    await page.screenshot(path=f'{out}/exam_schedule_popover_open.png')

    await browser.close()
    await p.stop()
    print('ALL CHECKS PASSED!')

asyncio.run(run())
