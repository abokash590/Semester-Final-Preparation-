from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page()
    page.goto('http://localhost:8000/#home')
    page.wait_for_timeout(600)
    
    print('Home Page Title:', page.title())
    print('OG Title:', page.evaluate("() => document.querySelector('meta[property=\"og:title\"]').content"))
    print('OG Description:', page.evaluate("() => document.querySelector('meta[property=\"og:description\"]').content"))
    print('OG Site Name:', page.evaluate("() => document.querySelector('meta[property=\"og:site_name\"]').content"))
    
    page.goto('http://localhost:8000/#cse-4101')
    page.wait_for_timeout(600)
    print('Course Page Title:', page.title())
    
    browser.close()
