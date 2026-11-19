import os
from playwright.sync_api import sync_playwright

html = """<!DOCTYPE html>
<html>
<head>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
</head>
<body>
  <div id="target"></div>
  <script>
    mermaid.initialize({
      startOnLoad: false,
      theme: 'base',
      themeVariables: {
        primaryColor: '#EEF2FF',
        primaryTextColor: '#1E1B4B',
        primaryBorderColor: '#4F46E5',
        lineColor: '#475569',
        fontSize: '14px'
      }
    });

    async function run() {
      const graphDef = `graph TD
        A((A)) -->|5| B((B))
        A -->|4| C((C))
        A -->|3| D((D))
        B -->|2| E((E))
        B -->|2| F((F))
        C -->|1| G((G))
        D -->|4| H((H))
        D -->|2| K((K))
        G -->|3| I((I - Goal))
        H -->|4| J((J))
        classDef default fill:#EEF2FF,stroke:#4F46E5,stroke-width:2px,color:#1E1B4B,font-weight:bold;
        classDef goal fill:#DCFCE7,stroke:#16A34A,stroke-width:3px,color:#14532D,font-weight:bold;
        class I goal;`;
      
      const res = await mermaid.render('mermaid-diag-1', graphDef);
      document.getElementById('target').innerHTML = res.svg;
      window.renderDone = true;
    }
    run();
  </script>
</body>
</html>
"""

test_path = r"t:\Project\7th Semester\dev\test_render_api.html"
with open(test_path, "w", encoding="utf-8") as f:
    f.write(html)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, channel="chrome")
    page = browser.new_page()
    page.goto(f"file:///{test_path.replace(os.sep, '/')}")
    page.wait_for_function("window.renderDone === true")
    svg_len = page.evaluate("document.querySelector('svg') ? document.querySelector('svg').outerHTML.length : 0")
    print("SVG rendered length:", svg_len)
    browser.close()
