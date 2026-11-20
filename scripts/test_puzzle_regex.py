import re
import json

with open('data/cse-4101.json', encoding='utf-8') as f:
    data = json.load(f)

q = data[1]['question'] # Card 2

# Step 1: Escape
out = q.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# Step 2: Tables
def format_table(match):
    rows = match.group(0).strip().split('\n')
    if len(rows) < 2: return match.group(0)
    html = '<div class="table-scroll-wrapper"><table class="data-table">'
    for idx, row in enumerate(rows):
        if '---' in row: continue
        cells = [c.strip() for i, c in enumerate(row.split('|')) if 0 < i < len(row.split('|')) - 1]
        tag = 'th' if idx == 0 else 'td'
        html += '<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>'
    html += '</table></div>'
    return html

out = re.sub(r'((?:\|[^\n]+\|\n?)+)', format_table, out)

# Step 3: gaps and breaks
out = re.sub(r'\n\n+', '<div class="set-subpart-gap"></div>', out)
out = re.sub(r'\n(?!\s*<)', '<br>', out)
out = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', out)

print("Before puzzle pair:")
print(out)

# Step 4: Puzzle pairing regex
pattern = r'(?:<strong>\s*Initial State:?\s*<\/strong>|Initial State:?)\s*(?:<br>|\s)*<div class="table-scroll-wrapper"><table class="data-table">([\s\S]*?)<\/table><\/div>\s*(?:<div class="set-subpart-gap"><\/div>|<br>|\s)*(?:<strong>\s*Final State:?\s*<\/strong>|Final State:?)\s*(?:<br>|\s)*<div class="table-scroll-wrapper"><table class="data-table">([\s\S]*?)<\/table><\/div>'

m = re.search(pattern, out, re.I)
print("\nMatched:", bool(m))
if m:
    replacement = f'''
    <div class="puzzle-states-horizontal">
      <div class="puzzle-state-col">
        <span class="puzzle-state-title">Initial State:</span>
        <div class="table-scroll-wrapper"><table class="data-table">{m.group(1)}</table></div>
      </div>
      <div class="puzzle-state-arrow">&rarr;</div>
      <div class="puzzle-state-col">
        <span class="puzzle-state-title">Final State:</span>
        <div class="table-scroll-wrapper"><table class="data-table">{m.group(2)}</table></div>
      </div>
    </div>
    '''
    final_out = re.sub(pattern, replacement, out, flags=re.I)
    print("\nAfter puzzle pair:")
    print(final_out)
