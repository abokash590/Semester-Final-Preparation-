from playwright.sync_api import sync_playwright

def debug():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="chrome")
        page = browser.new_page()
        page.on("console", lambda msg: print(f"[CONSOLE {msg.type}] {msg.text}"))
        page.on("pageerror", lambda err: print(f"[PAGE ERROR] {err}"))

        page.goto("http://localhost:8000", wait_until="networkidle")
        page.wait_for_timeout(2000)

        html_snippets = page.evaluate("""() => {
            const el = document.querySelector('.diagram-wrapper');
            return {
                wrapperExists: !!el,
                wrapperHTML: el ? el.outerHTML.substring(0, 500) : 'none',
                mermaidLoaded: typeof window.mermaid !== 'undefined',
                renderTargets: document.querySelectorAll('.diagram-render-target').length,
                rawSources: document.querySelectorAll('.mermaid-raw-source').length
            };
        }""")
        print("DOM State:", html_snippets)
        browser.close()

if __name__ == "__main__":
    debug()
