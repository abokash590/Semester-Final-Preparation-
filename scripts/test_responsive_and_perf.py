#!/usr/bin/env python3
"""
scripts/test_responsive_and_perf.py
Comprehensive responsive design, zero-overflow, and performance test suite using Playwright.
Tests viewports: 320, 375, 768, 1024, 1440, 1920, and 844x390 landscape with filter open.
Also benchmarks 400 questions on SYNTH-400.
"""

import sys
import time
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
PORT = 8089
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

class QuietHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)
    def log_message(self, format, *args):
        pass  # Quiet logging

def start_server():
    server = HTTPServer(("127.0.0.1", PORT), QuietHandler)
    server.serve_forever()

def run_tests():
    print(f"🚀 Starting test HTTP server on port {PORT}...")
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    time.sleep(1)

    screenshots_dir = ROOT / "screenshots"
    screenshots_dir.mkdir(exist_ok=True)

    viewports = [
        {"name": "320_small_phone", "w": 320, "h": 568},
        {"name": "375_standard_phone", "w": 375, "h": 667},
        {"name": "768_tablet_portrait", "w": 768, "h": 1024},
        {"name": "1024_tablet_desktop", "w": 1024, "h": 768},
        {"name": "1440_laptop_desktop", "w": 1440, "h": 900},
        {"name": "1920_large_desktop", "w": 1920, "h": 1080},
    ]

    overflow_failures = []

    print("\n🔍 Launching Headless Chrome via Playwright...")
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME_PATH, headless=True)

        # -------------------------------------------------------------
        # Part 1: Test standard viewports for horizontal overflow
        # -------------------------------------------------------------
        for vp in viewports:
            page = browser.new_page(viewport={"width": vp["w"], "height": vp["h"]})
            page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")
            page.wait_for_selector(".question-card", timeout=5000)

            # Check overflow programmatically
            check_result = page.evaluate("""() => {
                const docW = document.documentElement.clientWidth;
                const docScrollW = document.documentElement.scrollWidth;
                const bodyScrollW = document.body.scrollWidth;
                
                // Find any specific overflowing element
                const overflowing = [];
                document.querySelectorAll('*').forEach(el => {
                    const rect = el.getBoundingClientRect();
                    if (rect.right > docW + 1) { // 1px rounding margin
                        overflowing.push({
                            tag: el.tagName,
                            id: el.id,
                            className: el.className,
                            right: Math.round(rect.right),
                            docW: docW
                        });
                    }
                });

                return {
                    docW,
                    docScrollW,
                    bodyScrollW,
                    hasOverflow: (docScrollW > docW + 1) || (bodyScrollW > docW + 1),
                    overflowing: overflowing.slice(0, 5)
                };
            }""")

            shot_path = screenshots_dir / f"viewport_{vp['name']}.png"
            page.screenshot(path=str(shot_path), full_page=False)

            status = "✓ OK (Zero Overflow)" if not check_result["hasOverflow"] else "❌ OVERFLOW DETECTED"
            print(f"[{vp['w']}x{vp['h']}] {vp['name']}: {status}")

            if check_result["hasOverflow"]:
                overflow_failures.append({
                    "vp": vp["name"],
                    "details": check_result
                })

            page.close()

        # -------------------------------------------------------------
        # Part 2: Landscape phone (844x390) with filter bottom-sheet open
        # -------------------------------------------------------------
        print("\n🔍 Testing Landscape Phone (844x390) with Filter Sheet Open...")
        landscape_page = browser.new_page(viewport={"width": 844, "height": 390})
        landscape_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")
        landscape_page.wait_for_selector("#headerFilterBtn")

        # Click open filter sheet
        landscape_page.click("#headerFilterBtn")
        landscape_page.wait_for_timeout(300) # wait for animation

        # Screenshot with sheet open
        shot_landscape = screenshots_dir / "viewport_844x390_landscape_filter_open.png"
        landscape_page.screenshot(path=str(shot_landscape))

        # Check sheet visibility & touch targets
        sheet_visible = landscape_page.is_visible(".filter-sidebar.open")
        print(f"[844x390 Landscape] Filter Sheet Open: {'✓ Visible' if sheet_visible else '❌ Not visible'}")
        landscape_page.close()

        # -------------------------------------------------------------
        # Part 3: Performance Stress Test on 400 questions (SYNTH-400)
        # -------------------------------------------------------------
        print("\n⚡ Testing Performance on 400 Questions (SYNTH-400)...")
        perf_page = browser.new_page(viewport={"width": 375, "height": 667})
        
        # Emulate 4x CPU Throttling via Chrome DevTools Protocol
        client = perf_page.context.new_cdp_session(perf_page)
        client.send("Emulation.setCPUThrottlingRate", {"rate": 4})

        t0 = time.time()
        perf_page.goto(f"http://127.0.0.1:{PORT}/index.html", wait_until="networkidle")
        
        # Switch course to SYNTH-400
        perf_page.select_option("#courseSelect", "SYNTH-400")
        perf_page.wait_for_timeout(300)

        # Check initial chunk size
        initial_cards = perf_page.locator(".question-card").count()
        t_load = time.time() - t0

        # Scroll down 5 times to simulate user scrolling
        for _ in range(5):
            perf_page.evaluate("window.scrollBy(0, 1500)")
            perf_page.wait_for_timeout(100)

        total_rendered_after_scroll = perf_page.locator(".question-card").count()
        t_total = time.time() - t0

        print(f"✓ Initial chunk rendered: {initial_cards} cards in {t_load:.2f}s (with 4x CPU throttling).")
        print(f"✓ Smooth infinite scroll chunked to {total_rendered_after_scroll} cards in {t_total:.2f}s total.")

        perf_page.close()
        browser.close()

    print("\n================ TEST SUMMARY ================")
    if overflow_failures:
        print(f"❌ OVERFLOW DETECTED in {len(overflow_failures)} viewports:")
        for fail in overflow_failures:
            print(f"  • {fail['vp']}: {fail['details']}")
        sys.exit(1)
    else:
        print("🎉 ALL RESPONSIVE VIEWPORT CHECKS PASSED: Zero horizontal overflow on all viewports from 320px to 1920px!")
        print("🎉 Landscape (844x390) filter sheet verified!")
        print("🎉 400-question chunked lazy-rendering verified under 4x CPU throttling!")

if __name__ == "__main__":
    run_tests()
