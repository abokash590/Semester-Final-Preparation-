from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 900})
    page.goto("http://localhost:8000/#cse-4101")
    page.wait_for_timeout(1000)
    page.evaluate("app.enterCourse('cse-4101')")
    page.wait_for_timeout(500)

    # 1. Test Final Exam 2024 Question 1 -> Should have step-by-step solution
    final_card = page.locator("#year-section-2024 .question-card").first
    btn_final = final_card.locator(".solution-toggle-btn")
    btn_final.click()
    page.wait_for_timeout(400)
    sol_text = final_card.locator(".solution-drawer-body").inner_text()
    assert "STEP-BY-STEP SOLUTION" in sol_text.upper(), f"Final exam should still have solutions. Got: {sol_text[:200]}"
    print("Final Exam 2024 has step-by-step solution: Verified!")

    # 2. Test FEC Term Test
    page.evaluate("app.selectTermTestCollege('FEC')")
    page.wait_for_timeout(500)
    fec_card = page.locator("#termTestCardsContainer .question-card").first
    fec_btn = fec_card.locator(".solution-toggle-btn")
    fec_btn.click()
    page.wait_for_timeout(400)
    fec_sol_text = fec_card.locator(".solution-drawer-body").inner_text()
    assert "Solution still cooking" in fec_sol_text, f"FEC should show cooking placeholder. Got: {fec_sol_text[:200]}"
    assert "STEP-BY-STEP SOLUTION" not in fec_sol_text.upper(), "FEC should NOT have AI solution"
    fec_card.screenshot(path="screenshots/fec_clean_cooking.png")
    print("FEC Term Test shows cooking placeholder without solutions: Verified!")

    # 3. Test MEC Term Test
    page.evaluate("app.selectTermTestCollege('MEC')")
    page.wait_for_timeout(500)
    mec_card = page.locator("#termTestCardsContainer .question-card").first
    mec_btn = mec_card.locator(".solution-toggle-btn")
    mec_btn.click()
    page.wait_for_timeout(400)
    mec_sol_text = mec_card.locator(".solution-drawer-body").inner_text()
    assert "Solution still cooking" in mec_sol_text, f"MEC should show cooking placeholder. Got: {mec_sol_text[:200]}"
    assert "STEP-BY-STEP SOLUTION" not in mec_sol_text.upper(), "MEC should NOT have AI solution"
    mec_card.screenshot(path="screenshots/mec_clean_cooking.png")
    print("MEC Term Test shows cooking placeholder without solutions: Verified!")

    # 4. Test NITER Term Test
    page.evaluate("app.selectTermTestCollege('NITER')")
    page.wait_for_timeout(500)
    niter_card = page.locator("#termTestCardsContainer .question-card").first
    niter_btn = niter_card.locator(".solution-toggle-btn")
    niter_btn.click()
    page.wait_for_timeout(400)
    niter_sol_text = niter_card.locator(".solution-drawer-body").inner_text()
    assert "Solution still cooking" in niter_sol_text, f"NITER should show cooking placeholder. Got: {niter_sol_text[:200]}"
    assert "STEP-BY-STEP SOLUTION" not in niter_sol_text.upper(), "NITER should NOT have AI solution"
    niter_card.screenshot(path="screenshots/niter_clean_cooking.png")
    print("NITER Term Test shows cooking placeholder without solutions: Verified!")

    browser.close()
    print("ALL CHECKS PASSED SUCCESSFULLY!")
