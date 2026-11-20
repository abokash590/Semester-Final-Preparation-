import re

text = """
(c) Consider a single neuron with the following parameters: **[7]**  
$$\\begin{aligned}
\\text{Inputs: } & x_1 = 1.0, \\; x_2 = 0.5 \\\\
\\text{Weights: } & w_1 = 0.4, \\; w_2 = -0.6 \\\\
\\text{Bias: } & b = 0.1 \\\\
\\text{Activation function: } & \\text{Sigmoid} \\\\
\\text{Target output: } & t = 1 \\\\
\\text{Learning rate: } & \\eta = 0.2
\\end{aligned}$$

<div class="svg-diagram-wrapper"><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="40"/></svg></div>

i. **Every man respects his parent**
"""

# 1. Placeholders
svg_blocks = []
def save_svg(m):
    idx = len(svg_blocks)
    svg_blocks.append(m.group(0))
    return f'@@SVG_BLOCK_{idx}@@'

out = re.sub(r'<div class="svg-diagram-wrapper"[\s\S]*?</div>|<svg[\s\S]*?</svg>', save_svg, text)

math_blocks = []
def save_math(m):
    idx = len(math_blocks)
    math_blocks.append(m.group(0))
    return f'@@MATH_BLOCK_{idx}@@'

# Save display math first, then inline math
out = re.sub(r'\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]', save_math, out)
out = re.sub(r'(?<!\\)\$([^\$\n]+?)(?<!\\)\$|\\\([^\)]+?\\\)', save_math, out)

# 2. Escape HTML on prose
out = out.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# 3. Bold
out = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', out)

# 4. Newlines
out = re.sub(r'\n\n+', '<div class="set-subpart-gap"></div>', out)
out = re.sub(r'\n(?!\s*<)', '<br>', out)

# 5. Restore
for idx, m in enumerate(math_blocks):
    out = out.replace(f'@@MATH_BLOCK_{idx}@@', m)

for idx, s in enumerate(svg_blocks):
    out = out.replace(f'@@SVG_BLOCK_{idx}@@', s)

print("RESULT SUCCESSFUL!")
print(out)
