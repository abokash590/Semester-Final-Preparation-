#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(r"T:\Project\7th Semester")
DATA_DIR = ROOT / "data"

# ==============================================================================
# 1. BUILD SVG FOR SEARCH TREE (2024 Question 1c)
# ==============================================================================
def generate_search_tree_svg():
    return """<div class="svg-diagram-wrapper"><svg viewBox="0 0 520 310" class="responsive-diagram" role="img" aria-label="Search tree graph for Informed and Uninformed search"><defs><marker id="arrow" viewBox="0 0 10 10" refX="21" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#104535"/></marker></defs><g stroke="#104535" stroke-width="1.8" fill="none"><line x1="260" y1="35" x2="105" y2="100" marker-end="url(#arrow)"/><line x1="260" y1="35" x2="260" y2="100" marker-end="url(#arrow)"/><line x1="260" y1="35" x2="415" y2="100" marker-end="url(#arrow)"/><line x1="105" y1="100" x2="105" y2="180" marker-end="url(#arrow)"/><line x1="260" y1="100" x2="210" y2="180" marker-end="url(#arrow)"/><line x1="260" y1="100" x2="310" y2="180" marker-end="url(#arrow)"/><line x1="415" y1="100" x2="415" y2="180" marker-end="url(#arrow)"/><line x1="310" y1="180" x2="310" y2="260" marker-end="url(#arrow)"/><line x1="415" y1="180" x2="370" y2="260" marker-end="url(#arrow)"/><line x1="415" y1="180" x2="465" y2="260" marker-end="url(#arrow)"/></g><g font-size="12" font-weight="bold" fill="#104535" text-anchor="middle"><rect x="170" y="55" width="18" height="16" rx="3" fill="#F4F8F5"/><text x="179" y="68">5</text><rect x="264" y="60" width="18" height="16" rx="3" fill="#F4F8F5"/><text x="273" y="73">4</text><rect x="330" y="55" width="18" height="16" rx="3" fill="#F4F8F5"/><text x="339" y="68">3</text><rect x="85" y="132" width="18" height="16" rx="3" fill="#F4F8F5"/><text x="94" y="145">2</text><rect x="215" y="132" width="18" height="16" rx="3" fill="#F4F8F5"/><text x="224" y="145">2</text><rect x="295" y="132" width="18" height="16" rx="3" fill="#F4F8F5"/><text x="304" y="145">1</text><rect x="420" y="132" width="18" height="16" rx="3" fill="#F4F8F5"/><text x="429" y="145">4</text><rect x="315" y="212" width="18" height="16" rx="3" fill="#F4F8F5"/><text x="324" y="225">3</text><rect x="375" y="212" width="18" height="16" rx="3" fill="#F4F8F5"/><text x="384" y="225">4</text><rect x="445" y="212" width="18" height="16" rx="3" fill="#F4F8F5"/><text x="454" y="225">2</text></g><g fill="#ffffff" stroke="#104535" stroke-width="2"><circle cx="260" cy="35" r="17"/><circle cx="105" cy="100" r="17"/><circle cx="260" cy="100" r="17"/><circle cx="415" cy="100" r="17"/><circle cx="105" cy="180" r="17"/><circle cx="210" cy="180" r="17"/><circle cx="310" cy="180" r="17"/><circle cx="415" cy="180" r="17"/><circle cx="370" cy="260" r="17"/><circle cx="465" cy="260" r="17"/><circle cx="310" cy="260" r="22" fill="#DCFCE7" stroke="#104535" stroke-width="2.5"/></g><g font-size="12" font-weight="900" fill="#104535" text-anchor="middle" dominant-baseline="central"><text x="260" y="35">A</text><text x="105" y="100">B</text><text x="260" y="100">C</text><text x="415" y="100">D</text><text x="105" y="180">E</text><text x="210" y="180">F</text><text x="310" y="180">G</text><text x="415" y="180">H</text><text x="370" y="260">J</text><text x="465" y="260">K</text><text x="310" y="254" font-size="11">I</text><text x="310" y="268" font-size="9" fill="#104535">GOAL</text></g></svg></div>"""

# ==============================================================================
# 2. BUILD SVG FOR ROMANIA MAP (2023 Question 7d)
# ==============================================================================
def generate_romania_map_svg():
    cities = {
        "Oradea": (115, 45),
        "Zerind": (75, 110),
        "Arad": (60, 185),
        "Timisoara": (65, 275),
        "Lugoj": (140, 315),
        "Mehadia": (145, 370),
        "Drobeta": (140, 425),
        "Sibiu": (220, 185),
        "Rimnicu Vilcea": (250, 255),
        "Craiova": (265, 425),
        "Fagaras": (335, 185),
        "Pitesti": (345, 315),
        "Bucharest": (445, 350),
        "Giurgiu": (420, 425),
        "Urziceni": (525, 320),
        "Hirsova": (615, 320),
        "Eforie": (645, 385),
        "Vaslui": (575, 205),
        "Iasi": (540, 125),
        "Neamt": (455, 75)
    }

    edges = [
        ("Oradea", "Zerind", 71),
        ("Oradea", "Sibiu", 151),
        ("Zerind", "Arad", 75),
        ("Arad", "Sibiu", 140),
        ("Arad", "Timisoara", 118),
        ("Timisoara", "Lugoj", 111),
        ("Lugoj", "Mehadia", 70),
        ("Mehadia", "Drobeta", 75),
        ("Drobeta", "Craiova", 120),
        ("Sibiu", "Fagaras", 99),
        ("Sibiu", "Rimnicu Vilcea", 80),
        ("Rimnicu Vilcea", "Craiova", 146),
        ("Rimnicu Vilcea", "Pitesti", 97),
        ("Craiova", "Pitesti", 138),
        ("Fagaras", "Bucharest", 211),
        ("Pitesti", "Bucharest", 101),
        ("Bucharest", "Giurgiu", 90),
        ("Bucharest", "Urziceni", 85),
        ("Urziceni", "Hirsova", 98),
        ("Hirsova", "Eforie", 86),
        ("Urziceni", "Vaslui", 142),
        ("Vaslui", "Iasi", 92),
        ("Iasi", "Neamt", 87)
    ]

    lines_svg = []
    badges_svg = []

    for c1, c2, dist in edges:
        x1, y1 = cities[c1]
        x2, y2 = cities[c2]
        lines_svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
        # Midpoint for badge
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        badges_svg.append(f'<g transform="translate({mx},{my})"><rect x="-13" y="-8" width="26" height="16" rx="4" fill="#F4F8F5" stroke="#CBD5E1" stroke-width="0.8"/><text x="0" y="3.5" font-size="10" font-weight="700" fill="#104535" text-anchor="middle">{dist}</text></g>')

    nodes_svg = []
    labels_svg = []

    for name, (x, y) in cities.items():
        is_start = (name == "Arad")
        is_goal = (name == "Bucharest")

        if is_start:
            nodes_svg.append(f'<circle cx="{x}" cy="{y}" r="8" fill="#FEF3C7" stroke="#D97706" stroke-width="2.5"/>')
            labels_svg.append(f'<text x="{x}" y="{y-12}" font-size="11" font-weight="900" fill="#92400E" text-anchor="middle">{name} (Start)</text>')
        elif is_goal:
            nodes_svg.append(f'<circle cx="{x}" cy="{y}" r="9" fill="#DCFCE7" stroke="#104535" stroke-width="2.8"/>')
            labels_svg.append(f'<text x="{x}" y="{y-13}" font-size="11" font-weight="900" fill="#104535" text-anchor="middle">{name} (Goal)</text>')
        else:
            nodes_svg.append(f'<circle cx="{x}" cy="{y}" r="5.5" fill="#FFFFFF" stroke="#104535" stroke-width="2"/>')
            offset_y = -10
            anchor = "middle"
            if name in ["Lugoj", "Mehadia", "Drobeta", "Timisoara"]:
                anchor = "end"
                offset_y = 4
                labels_svg.append(f'<text x="{x-9}" y="{y+offset_y}" font-size="10" font-weight="700" fill="#1E293B" text-anchor="{anchor}">{name}</text>')
            elif name in ["Hirsova", "Eforie", "Vaslui", "Iasi"]:
                anchor = "start"
                offset_y = 4
                labels_svg.append(f'<text x="{x+9}" y="{y+offset_y}" font-size="10" font-weight="700" fill="#1E293B" text-anchor="{anchor}">{name}</text>')
            elif name in ["Giurgiu", "Craiova"]:
                labels_svg.append(f'<text x="{x}" y="{y+16}" font-size="10" font-weight="700" fill="#1E293B" text-anchor="{anchor}">{name}</text>')
            else:
                labels_svg.append(f'<text x="{x}" y="{y+offset_y}" font-size="10" font-weight="700" fill="#1E293B" text-anchor="{anchor}">{name}</text>')

    svg_content = f"""<div class="svg-diagram-wrapper"><svg viewBox="0 0 720 460" class="responsive-diagram" role="img" aria-label="Map of Romania road network with distances between cities"><g stroke="#94A3B8" stroke-width="1.8" fill="none">{''.join(lines_svg)}</g><g>{''.join(badges_svg)}</g><g>{''.join(nodes_svg)}</g><g>{''.join(labels_svg)}</g></svg></div>"""
    return svg_content

def generate_heuristic_table_md():
    return """\n\n**Straight-line distance to Bucharest ($h_{SLD}$ in km):**\n\n| City | $h_{SLD}$ | City | $h_{SLD}$ |\n| :--- | :---: | :--- | :---: |\n| **Arad** | 366 | **Mehadia** | 241 |\n| **Bucharest** | 0 | **Neamt** | 234 |\n| **Craiova** | 160 | **Oradea** | 380 |\n| **Drobeta** | 242 | **Pitesti** | 100 |\n| **Eforie** | 161 | **Rimnicu Vilcea** | 193 |\n| **Fagaras** | 176 | **Sibiu** | 253 |\n| **Giurgiu** | 77 | **Timisoara** | 329 |\n| **Hirsova** | 151 | **Urziceni** | 80 |\n| **Iasi** | 226 | **Vaslui** | 199 |\n| **Lugoj** | 244 | **Zerind** | 374 |"""

# ==============================================================================
# 3. UPDATE ALL DATA IN data/cse-4101.json
# ==============================================================================
def update_all():
    json_path = DATA_DIR / "cse-4101.json"
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    search_tree_svg = generate_search_tree_svg()
    romania_svg = generate_romania_map_svg()
    heuristic_table = generate_heuristic_table_md()

    for s in data:
        # 1. 2024 Set 1: Search tree (F under C, D only H, H to J and K)
        if s.get('id') == 'cse-4101-final-2024-set1':
            s['question'] = """(a) Define Artificial Intelligence. List five problems that cannot be currently aided/solved by AI. **[4]**  
(b) Give a PEAS description of the following task environment and characterize it in terms of task environment. **[4]**  
    i. Automated taxi driver  
    ii. Vacuum cleaner  
(c) For the following tree, show the order of nodes visited for i) breadth-first search, ii) depth-first search, iii) uniform cost search, and iv) iterative deepening search. The goal node is I and the numbers next to the edges indicate the associated cost. **[6]**

**Search Tree (Mermaid):**
```mermaid
graph TD
    A((A)) -->|5| B((B))
    A -->|4| C((C))
    A -->|3| D((D))
    B -->|2| E((E))
    C -->|2| F((F))
    C -->|1| G((G))
    G -->|3| I((I - Goal))
    D -->|4| H((H))
    H -->|4| J((J))
    H -->|2| K((K))
```"""
            for sub in s.get('subparts', []):
                if sub.get('id') == 'cse-4101-final-2024-q1c':
                    sub['question'] = f"For the following tree, show the order of nodes visited for i) breadth-first search, ii) depth-first search, iii) uniform cost search, and iv) iterative deepening search. The goal node is I and the numbers next to the edges indicate the associated cost.\n\n{search_tree_svg}"
                    sub['solution'] = {
                        "steps": [
                            "1. **Breadth-First Search (BFS) [FIFO Queue]:** Level 0: A &rarr; Level 1: B, C, D &rarr; Level 2: E, F, G, H &rarr; Level 3: I (Goal reached). Order visited: **A, B, C, D, E, F, G, H, I** (9 nodes).",
                            "2. **Depth-First Search (DFS) [LIFO Stack]:** Explores down leftmost path first: A &rarr; B &rarr; E (backtracks to A) &rarr; C &rarr; F (backtracks to C) &rarr; G &rarr; I (Goal reached). Order visited: **A, B, E, C, F, G, I** (7 nodes). Nodes D, H, J, K are never visited.",
                            "3. **Uniform Cost Search (UCS) [Priority Queue ordered by path cost g(n)]:**\n   - Step 1: Pop A (g=0). Fringe: {D(3), C(4), B(5)}\n   - Step 2: Pop D (g=3). Add H(7). Fringe: {C(4), B(5), H(7)}\n   - Step 3: Pop C (g=4). Add G(5), F(6). Fringe: {B(5), G(5), F(6), H(7)}\n   - Step 4: Pop B (g=5). Add E(7). Fringe: {G(5), F(6), E(7), H(7)}\n   - Step 5: Pop G (g=5). Add I(8). Fringe: {F(6), E(7), H(7), I(8)}\n   - Step 6: Pop F (g=6). Fringe: {E(7), H(7), I(8)}\n   - Step 7: Pop E (g=7). Fringe: {H(7), I(8)}\n   - Step 8: Pop H (g=7). Add K(9), J(11). Fringe: {I(8), K(9), J(11)}\n   - Step 9: Pop I (g=8). Goal reached!\n   Order of node expansion: **A (0) &rarr; D (3) &rarr; C (4) &rarr; B (5) &rarr; G (5) &rarr; F (6) &rarr; E (7) &rarr; H (7) &rarr; I (8)**.\n   Optimal Path: **A &rarr; C &rarr; G &rarr; I** with minimum cost **8**.",
                            "4. **Iterative Deepening Search (IDS):**\n   - Limit 0: [A]\n   - Limit 1: [A, B, C, D]\n   - Limit 2: [A, B, E, C, F, G, D, H]\n   - Limit 3: [A, B, E, C, F, G, I] (Goal I reached at depth 3!)."
                        ],
                        "answer": "BFS visits 9 nodes (A, B, C, D, E, F, G, H, I); DFS visits 7 nodes (A, B, E, C, F, G, I); UCS expands 9 nodes finding optimal path A-C-G-I of cost 8; IDS reaches goal at depth limit 3.",
                        "marking_hint": "Award 1.5 marks each for BFS, DFS, UCS, and IDS sequences."
                    }

        # 2. 2024 Set 4: Bold the 5 FOL statements
        if s.get('id') == 'cse-4101-final-2024-set4':
            s['question'] = """(a) Explain the components of the A* evaluation function $f(n) = g(n) + h(n)$. Write down the application of A* search. **[4]**  
(b) Convert the following English statement into FOL: **[5]**  
    i. **Every man respects his parent**  
    ii. **There is somebody whom everybody loves**  
    iii. **Not all students like both Mathematics and Science**  
    iv. **Mahmud has never sent an e-mail message to Abdullah**  
    v. **Everybody loves somebody**  
(c) Write short note on two types of quantifiers in FOL with example? **[3]**  
(d) Write down the application of AI in robotics. **[2]**"""
            for sub in s.get('subparts', []):
                if sub.get('id') == 'cse-4101-final-2024-q4b':
                    sub['question'] = """Convert the following English statement into FOL:
i. **Every man respects his parent**
ii. **There is somebody whom everybody loves**
iii. **Not all students like both Mathematics and Science**
iv. **Mahmud has never sent an e-mail message to Abdullah**
v. **Everybody loves somebody**"""

        # 3. 2024 Set 6: Neuron parameters compact math block
        if s.get('id') == 'cse-4101-final-2024-set6':
            s['question'] = """(a) A disease affects 1% of the population. A test is 95% accurate for both positive and negative results. If a person tests positive, what's the probability they have the disease? **[4]**  
(b) Write down the equation for Conditional Probability and Bayes Theorem. **[3]**  
(c) Consider a single neuron with the following parameters: **[7]**  
$$\\begin{aligned}
\\text{Inputs: } & x_1 = 1.0, \\; x_2 = 0.5 \\\\
\\text{Weights: } & w_1 = 0.4, \\; w_2 = -0.6 \\\\
\\text{Bias: } & b = 0.1 \\\\
\\text{Activation function: } & \\text{Sigmoid} \\\\
\\text{Target output: } & t = 1 \\\\
\\text{Learning rate: } & \\eta = 0.2
\\end{aligned}$$

Now,  
a) Compute the **net input** and the **output of the neuron**.  
b) Calculate the **error** using Mean Squared Error (MSE).  
c) Using **backpropagation**, compute the **weight and bias updates** for one training step."""

        # 4. 2024 Set 7: I is connected with E, NOT D!
        if s.get('id') == 'cse-4101-final-2024-set7':
            s['question'] = """(a) Write down the Limitation of Hill Climbing Search with explanation? **[4]**  
(b) Which heuristics are admissible for the 8-puzzle problem and why? **[4]**  
(c) Perform Iterative Deepening Search based on the following graph to reach goal node G. **[4]**

**Graph Structure (Mermaid):**
```mermaid
graph TD
    A((A)) --> B((B))
    A --> C((C))
    B --> D((D))
    B --> E((E))
    C --> F((F))
    C --> G((G - Goal))
    D --> H((H))
    E --> I((I))
```

(d) What is an ontology? How does it differ from a taxonomy or a database schema? **[2]**

---"""
            for sub in s.get('subparts', []):
                if sub.get('id') == 'cse-4101-final-2024-q7c':
                    sub['question'] = "Perform Iterative Deepening Search based on the following graph to reach goal node G:\nTree structure: Root A has children B, C; B has children D, E; C has children F, G; D has child H; E has child I."
                    sub['solution'] = {
                        "steps": [
                            "1. **Depth Limit 0:** Visit root [A]. (Goal G not reached).",
                            "2. **Depth Limit 1:** Visit A &rarr; B, C. (Goal G not reached).",
                            "3. **Depth Limit 2:** Visit A &rarr; B &rarr; D, E &rarr; C &rarr; F, G. (Goal G reached at depth 2!).",
                            "4. **Search Behavior:** Iterative Deepening Search (IDS) combines DFS memory efficiency O(bd) with BFS completeness. Since Goal G is located at Depth 2 on node C's right branch, search terminates successfully during iteration Limit = 2 without needing to explore leaves H (under D) or I (under E) at Depth 3."
                        ],
                        "answer": "IDS visits [A] at Limit 0, [A, B, C] at Limit 1, and reaches Goal G at Limit 2 in order [A, B, D, E, C, F, G].",
                        "marking_hint": "Award 1 mark for each depth limit iteration (0, 1, 2) and 1 mark for correct goal termination."
                    }

        # 5. 2023 Set 7: Romania 2D SVG map & heuristic table
        if s.get('id') == 'cse-4101-final-2023-set7':
            s['question'] = f"""(a) What is Natural language Processing (NLP)? Explain Phases of NLP. **[4]**  
(b) How to build an NLP pipeline? **[4]**  
(c) Differentiate between informed and uninformed search. **[2]**  
(d) Using Greedy best-first search find the cost and show the steps from the source Arad to the destination Bucharest. **[4]**

**Map of Romania (Road Distances between Cities):**
{romania_svg}
{heuristic_table}

---"""
            for sub in s.get('subparts', []):
                if sub.get('id') == 'cse-4101-final-2023-q7d':
                    sub['question'] = f"Using Greedy best-first search find the cost and show the steps from the source Arad to the destination Bucharest in the Romania road network.\n\n{romania_svg}\n{heuristic_table}"

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("✓ Successfully updated data/cse-4101.json with all 5 fixes.")

# ==============================================================================
# 5. UPDATE Questions_2024.md
# ==============================================================================
def update_questions_2024_md():
    md_path = ROOT / "Questions_2024.md"
    content = md_path.read_text(encoding='utf-8')

    # Update Question 1(c) Mermaid
    old_q1_mermaid = """graph TD
    A((A)) -->|5| B((B))
    A -->|4| C((C))
    A -->|3| D((D))
    B -->|2| E((E))
    B -->|2| F((F))
    C -->|1| G((G))
    D -->|4| H((H))
    D -->|2| K((K))
    G -->|3| I((I - Goal))
    H -->|4| J((J))"""

    new_q1_mermaid = """graph TD
    A((A)) -->|5| B((B))
    A -->|4| C((C))
    A -->|3| D((D))
    B -->|2| E((E))
    C -->|2| F((F))
    C -->|1| G((G))
    G -->|3| I((I - Goal))
    D -->|4| H((H))
    H -->|4| J((J))
    H -->|2| K((K))"""

    content = content.replace(old_q1_mermaid, new_q1_mermaid)

    # Update Question 7(c) Mermaid
    old_q7_mermaid = """graph TD
    A((A)) --> B((B))
    A --> C((C))
    B --> D((D))
    B --> E((E))
    C --> F((F))
    C --> G((G - Goal))
    D --> H((H))
    D --> I((I))"""

    new_q7_mermaid = """graph TD
    A((A)) --> B((B))
    A --> C((C))
    B --> D((D))
    B --> E((E))
    C --> F((F))
    C --> G((G - Goal))
    D --> H((H))
    E --> I((I))"""

    content = content.replace(old_q7_mermaid, new_q7_mermaid)

    # Update FOL bolds
    content = content.replace("i. Every man respects his parent", "i. **Every man respects his parent**")
    content = content.replace("ii. There is somebody whom everybody loves", "ii. **There is somebody whom everybody loves**")
    content = content.replace("iii. Not all students like both Mathematics and Science", "iii. **Not all students like both Mathematics and Science**")
    content = content.replace("iv. Mahmud has never sent an e-mail message to Abdullah", "iv. **Mahmud has never sent an e-mail message to Abdullah**")
    content = content.replace("v. Everybody loves somebody", "v. **Everybody loves somebody**")

    # Update Question 6 neuron block
    old_neuron = """$$\\text{Inputs: } x_1 = 1.0, \\; x_2 = 0.5$$  
$$\\text{Weights: } w_1 = 0.4, \\; w_2 = -0.6$$  
$$\\text{Bias: } b = 0.1$$  
$$\\text{Activation function: Sigmoid}$$  
$$\\text{Target output: } t = 1$$  
$$\\text{Learning rate: } \\eta = 0.2$$"""

    new_neuron = """$$\\begin{aligned}
\\text{Inputs: } & x_1 = 1.0, \\; x_2 = 0.5 \\\\
\\text{Weights: } & w_1 = 0.4, \\; w_2 = -0.6 \\\\
\\text{Bias: } & b = 0.1 \\\\
\\text{Activation function: } & \\text{Sigmoid} \\\\
\\text{Target output: } & t = 1 \\\\
\\text{Learning rate: } & \\eta = 0.2
\\end{aligned}$$"""

    content = content.replace(old_neuron, new_neuron)

    md_path.write_text(content, encoding='utf-8')
    print("✓ Successfully updated Questions_2024.md")

# ==============================================================================
# 6. RE-BUNDLE data/codex_data.js
# ==============================================================================
def rebundle_codex_data():
    manifest_path = DATA_DIR / "manifest.json"
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    courses_dict = {}
    for c in manifest.get('courses', []):
        c_file = DATA_DIR / c['file']
        if c_file.exists():
            with open(c_file, 'r', encoding='utf-8') as f:
                courses_dict[c['code']] = json.load(f)

    bundle = {
        "manifest": manifest,
        "courses": courses_dict
    }

    bundle_js_path = DATA_DIR / "codex_data.js"
    with open(bundle_js_path, 'w', encoding='utf-8') as f:
        f.write("window.__CODEX_DATA__ = " + json.dumps(bundle, ensure_ascii=False) + ";\n")
    print("✓ Successfully rebundled data/codex_data.js")

if __name__ == "__main__":
    update_all()
    update_questions_2024_md()
    rebundle_codex_data()
