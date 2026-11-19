#!/usr/bin/env python3
"""
scripts/generate_synthetic.py
Generates 400 realistic questions with equations, tables, and varying marks/years
to stress-test virtualized chunked rendering and performance under 4x CPU throttling.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

TOPICS = [
    "AI Foundations",
    "Informed vs Uninformed Search",
    "A* Search & Heuristics",
    "Alpha-Beta Pruning",
    "Constraint Satisfaction Problems",
    "Genetic Algorithms",
    "First-Order Logic",
    "Neural Networks & Backpropagation"
]

def generate():
    questions = []
    years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
    exams = ["final", "term"]
    
    # Precompute IDs
    ids = [f"synth-400-{exams[i % len(exams)]}-{years[i % len(years)]}-q{i+1}" for i in range(400)]
    
    for i in range(400):
        year = years[i % len(years)]
        exam = exams[i % len(exams)]
        t1 = TOPICS[i % len(TOPICS)]
        t2 = TOPICS[(i + 3) % len(TOPICS)]
        topics = [t1] if t1 == t2 else [t1, t2]
        
        sim = []
        # Link every 10th question symmetrically to question i-5
        if i >= 10 and i % 10 == 0:
            sim.append(ids[i - 5])
        elif i >= 5 and (i + 5) < 400 and (i + 5) % 10 == 0:
            sim.append(ids[i + 5])
            
        q = {
            "id": ids[i],
            "course": "SYNTH-400",
            "exam": exam,
            "year": year,
            "qno": f"{(i % 7) + 1}({chr(97 + (i % 4))})",
            "marks": (i % 6 + 2),
            "topics": topics,
            "question": f"Synthetic Test Question #{i+1}: Analyze the algorithmic time and space complexity of function $f_{{{i+1}}}(x) = \\sum_{{k=1}}^{{n}} \\frac{{\\alpha_k \\cdot x^k}}{{k!}}$ when applied to the following dataset:\n\n<div class=\"scroll-container\"><table class=\"data-table\"><thead><tr><th>Node ID</th><th>Cost $g(n)$</th><th>Heuristic $h(n)$</th><th>Evaluation $f(n)$</th></tr></thead><tbody><tr><td>N_{{{i+1}}}A</td><td>{(i+1) * 2}</td><td>{i + 6}</td><td>{(i+1) * 3 + 5}</td></tr><tr><td>N_{{{i+1}}}B</td><td>{(i+1) * 2 + 3}</td><td>{i + 3}</td><td>{(i+1) * 3 + 5}</td></tr></tbody></table></div>",
            "solution": {
              "steps": [
                f"Step 1: Compute the partial derivatives $\\frac{{\\partial f_{{{i+1}}}}}{{\\partial x}}$ with respect to each input parameter.",
                f"Step 2: Apply gradient descent update $\\theta_{{t+1}} = \\theta_t - \\eta \\cdot \\nabla J(\\theta)$ with learning rate $\\eta = 0.01$.",
                "Step 3: Verify the numerical bounds and verify convergence within tolerance $\\epsilon = 10^{-5}$."
              ],
              "answer": f"The optimal minimum for system #{i+1} converges in $O(n \\log n)$ time with asymptotic space $O(k)$.",
              "marking_hint": "Award 50% for mathematical derivation and 50% for asymptotic runtime justification."
            },
            "similar_to": sim,
            "verified": False
        }
        questions.append(q)

    out_file = DATA_DIR / "synthetic-400.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2)
    print(f"Generated {len(questions)} synthetic questions at {out_file}")

if __name__ == "__main__":
    generate()
