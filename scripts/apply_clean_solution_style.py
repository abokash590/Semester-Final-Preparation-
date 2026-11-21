import re

# 1. Update app.js
with open("app.js", "r", encoding="utf-8") as f:
    app_js = f.read()

# Replace marking guide and answer box in subparts
old_subpart_pattern = r'<strong class="solution-heading">Step-by-Step Solution:</strong>\s*<ol class="solution-steps-list">\$\{subSteps\}</ol>[\s\S]*?</div>\s*</div>\s*`;\s*}\)\.join\("<hr class=\'subpart-solution-divider\'>"[\s\S]*?const solutionContentHtml = hasValidSolution\s*\?\s*`<div class="subparts-solutions-wrapper">\$\{subpartsSolutionsHtml\}</div>`'

# Let's inspect the exact lines in app.js
start_marker = '<div class="subpart-derivation">'
end_marker = 'const solutionContentHtml = hasValidSolution'
s_idx = app_js.find(start_marker)
e_idx = app_js.find(end_marker)

print("s_idx:", s_idx, "e_idx:", e_idx)
section = app_js[s_idx:e_idx]
print("Section:\n", section)

new_section = """<div class="subpart-derivation">
              <strong class="solution-heading">Solution:</strong>
              <div class="subpart-steps-content">${subSteps}</div>
              ${sub.solution?.answer ? `<div class="solution-answer-box"><strong>Final Result:</strong> ${this.formatMarkdownText(sub.solution.answer)}</div>` : ""}
            </div>
          </div>
        `;
      }).join("<hr class='subpart-solution-divider'>");
    } else {
      const stepsHtml = (q.solution?.steps || [])
        .map(s => `<div class="subpart-step-item">${this.formatMarkdownText(s)}</div>`)
        .join("");
      subpartsSolutionsHtml = `
        <div class="subpart-steps-content">${stepsHtml}</div>
        ${q.solution?.answer ? `<div class="solution-answer-box"><strong>Final Result:</strong> ${this.formatMarkdownText(q.solution.answer)}</div>` : ""}
      `;
    }

    const endMarkerHtml = `
      <div class="solution-set-end-tag" aria-hidden="true">
        <span class="end-tag-line"></span>
        <span class="end-tag-badge">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
          <span>End of Solution</span>
        </span>
        <span class="end-tag-line"></span>
      </div>
    `;

    const hasValidSolution = (Array.isArray(q.subparts) && q.subparts.some(s => s.solution?.steps?.length > 0)) ||
                             (q.solution?.steps?.length > 0);

    const solutionContentHtml = hasValidSolution
      ? `<div class="subparts-solutions-wrapper">${subpartsSolutionsHtml}${endMarkerHtml}</div>`
"""

# Let's verify and replace
updated_app_js = app_js[:s_idx] + new_section + app_js[app_js.find(":\n          <div class=\"solution-chat-bubble-container\">", e_idx):]

with open("app.js", "w", encoding="utf-8") as f:
    f.write(updated_app_js)

print("Updated app.js successfully!")

# 2. Update style.css with styled end marker
with open("style.css", "r", encoding="utf-8") as f:
    style_css = f.read()

end_tag_css = """
/* Styled Minimalist End of Solution Marker */
.solution-set-end-tag {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  margin: 28px 0 6px 0;
  padding: 0 4px;
}

.end-tag-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(to right, transparent, #E4E4E7, #D4D4D8);
}

.solution-set-end-tag .end-tag-line:last-child {
  background: linear-gradient(to left, transparent, #E4E4E7, #D4D4D8);
}

.end-tag-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 5px 14px;
  background: #F4F8F5;
  border: 1px solid rgba(16, 69, 53, 0.22);
  border-radius: 9999px;
  font-family: var(--font-sans);
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #104535;
  box-shadow: 0 1px 2px rgba(16, 69, 53, 0.05);
}

.end-tag-badge svg {
  color: #104535;
  stroke-width: 2.5px;
}

.subpart-steps-content {
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
  margin-top: 4px;
  line-height: 1.65;
}

.subpart-step-item {
  line-height: 1.65;
}
"""

if ".solution-set-end-tag" not in style_css:
    style_css += "\n" + end_tag_css
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(style_css)
    print("Added solution end tag CSS to style.css!")
else:
    print("CSS already present.")
