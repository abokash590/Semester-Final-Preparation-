import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / "data" / "cse-4101.json"

with open(FILE, "r", encoding="utf-8") as f:
    questions = json.load(f)

# Filter out q6c if already present
questions = [q for q in questions if q["id"] != "cse-4101-final-2024-q6c"]

q6c = {
    "id": "cse-4101-final-2024-q6c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "6(c)",
    "marks": 7,
    "topics": ["Machine Learning in AI", "Neural Networks & Backpropagation"],
    "question": "Consider a single neuron with parameters: $x_1 = 1.0, x_2 = 0.5$, weights $w_1 = 0.4, w_2 = -0.6$, bias $b = 0.1$, activation function $\\sigma(z) = \\frac{1}{1 + e^{-z}}$, target $t = 1$, learning rate $\\eta = 0.2$.\n\nCompute the error and backpropagation weight update:\n\n<div class=\"scroll-container\"><div class=\"katex-display\">$$\\Delta w_j = -\\eta \\frac{\\partial E}{\\partial w_j} = \\eta (t - y) \\cdot \\sigma(z)(1 - \\sigma(z)) \\cdot x_j = 0.2 \\cdot (1 - 0.5744) \\cdot 0.2444 \\cdot x_j$$</div></div>",
    "solution": {
      "steps": [
        "1. Net input: $z = w_1 x_1 + w_2 x_2 + b = (0.4)(1.0) + (-0.6)(0.5) + 0.1 = 0.4 - 0.3 + 0.1 = 0.20$.",
        "2. Neuron output: $y = \\sigma(0.20) = \\frac{1}{1 + e^{-0.20}} \\approx 0.5498$.",
        "3. Mean Squared Error: $E = \\frac{1}{2}(t - y)^2 = \\frac{1}{2}(1 - 0.5498)^2 = 0.1013$.",
        "4. Error gradient factor: $\\delta = (t - y) \\cdot y(1 - y) = (0.4502)(0.5498)(0.4502) \\approx 0.1114$.",
        "5. Weight updates: $\\Delta w_1 = \\eta \\delta x_1 = 0.2 \\cdot 0.1114 \\cdot 1.0 = +0.0223$. New $w_1 = 0.4223$."
      ],
      "answer": "Net input z = 0.20, output y = 0.5498, MSE error = 0.1013, delta w1 = +0.0223, delta w2 = +0.0111, delta b = +0.0223.",
      "marking_hint": "Award 2 marks for net input & output, 2 marks for MSE error, 3 marks for backpropagation gradient weight updates."
    },
    "similar_to": [],
    "verified": False
}

questions.append(q6c)

with open(FILE, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Successfully updated cse-4101.json with wide KaTeX equation. Total questions: {len(questions)}")
