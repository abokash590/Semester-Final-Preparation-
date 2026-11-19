# Project Rules & Architecture Guidelines: Semester Final Codex (DU CSE 4-1)

## 1. Strict UI & Design Rules
- **NEVER use emojis anywhere in the website:**
  - No emojis in UI buttons, banners, error handlers, badges, cards, placeholder text, or question solutions.
  - Always use crisp, accessible inline SVG vector icons (e.g. `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" ...>`) or pure typography.
- **Theme standard:** Strict Light Theme Only (no theme switcher, no dark mode).
- **Icon standard:** Clean line/stroke vector icons with consistent stroke-width (2px or 2.2px) matching GitHub/Lucide/Feather icon aesthetic.

## 2. Header & Course Navigation
- Single-tier top navbar containing:
  - Left: Smiling Voxel Avatar Head brand mark icon, Title (`Semester Final Codex`), and Active Course subtitle.
  - Right: Minecraft Hotbar course selection slots (`1: AI CSE-4101`, `2: MSA CSE-4102`, `3: ENT SS-4103`, `4: ML CSE-4125`, `5: DS CSE-4126`) with keyboard number shortcuts (1–5).
- **Favicon:** Smiling Voxel Avatar Head (`assets/avatar.png`).
- **No search bar** in header.
- **No theme changer** button in header.

## 3. Left-Rail Sticky Scrollspy Navigation
- Desktop Left-Rail Sticky Scrollspy Navigation:
  - Positioned centrally on the left rail (`left-side middle`), synchronizing in real time with question sets as the user scrolls.
  - Strict order:
    1. **`2023 FINAL`**
    2. **`2024 FINAL`**
    3. **`TERM TEST`**
  - **Subsection Layout & Accordion Visibility:**
    - Subsections use an ultra-compact vertical drop-line thread (`.scrollspy-thread`) along a 1.5px vertical line to minimize horizontal footprint.
    - **Active-only visibility:** Only the currently active section expands its subsection thread; non-active sections remain cleanly collapsed with zero clutter.
  - Term Test Sub-options (Affiliated Engineering Colleges):
    - **`MEC`**, **`FEC`**, **`NITER`**, **`ShEC`**, **`SIMT`** *(Note: Always `SIMT`, never SIMR)*.

## 4. Question Cards & Solutions
- Visual question paper diagrams (Search trees, state spaces, network graphs, UML diagrams) must be rendered as real diagrams (using Mermaid.js or SVG) as depicted in the original question papers.
- Complete Question Sets (all subparts: a, b, c, d) are grouped together on a single card.
- Solution drawers are collapsed by default behind accessible toggle buttons (`Reveal Solution for {Qno}`).
- Minimalist question presentation: No distracting horizontal line artifacts (`---`), no bulky practice textareas, and **NO unverified badges**.
- Mathematical equations rendered via KaTeX with math delimiters (`$`, `\(`).
