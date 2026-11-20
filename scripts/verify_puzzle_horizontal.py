from playwright.sync_api import sync_playwright
import shutil

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1280, 'height': 800})
    page.goto('http://localhost:8000/#cse-4101')
    page.wait_for_selector('.question-set-card')
    page.wait_for_timeout(600)
    
    card = page.locator('#card-cse-4101-final-2023-set2')
    puzzle = card.locator('.puzzle-states-horizontal')
    print('Puzzle container count:', puzzle.count())
    
    cols = puzzle.locator('.puzzle-state-col').all()
    print('Columns count:', len(cols))
    if len(cols) >= 2:
        b1 = cols[0].bounding_box()
        b2 = cols[1].bounding_box()
        print('Initial State Box:', b1)
        print('Final State Box:', b2)
        is_horiz = (b2['x'] > b1['x']) and abs(b1['y'] - b2['y']) < 15
        print('Is Horizontally Aligned Side-by-Side:', is_horiz)
    
    # Clip to the puzzle container with padding
    pbox = puzzle.bounding_box()
    clip = {
        'x': max(0, pbox['x'] - 20),
        'y': max(0, pbox['y'] - 40),
        'width': pbox['width'] + 40,
        'height': pbox['height'] + 60
    }
    page.screenshot(path='screenshots/puzzle_horizontal_tables.png', clip=clip)
    browser.close()

shutil.copy('screenshots/puzzle_horizontal_tables.png', 'C:/Users/ahmed/.gemini/antigravity/brain/4fc4ec37-d310-498f-9ecb-cf74490ff70a/screenshots/puzzle_horizontal_tables.png')
print('Screenshot saved successfully!')
