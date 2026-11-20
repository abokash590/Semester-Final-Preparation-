import json
from pathlib import Path

ROOT = Path(r"T:\Project\7th Semester")
DATA_DIR = ROOT / "data"

# ==============================================================================
# CSE-4101 (Artificial Intelligence) MEC Term Tests
# ==============================================================================
cse4101_term_tests = [
    {
        "id": "cse-4101-term-mec-tt1",
        "course": "CSE-4101",
        "exam": "term",
        "college": "MEC",
        "term_no": 1,
        "set_no": 1,
        "year": 2024,
        "qno": "Term Test 1",
        "marks": 15,
        "topics": [
            "Informed vs Uninformed Search",
            "A* Search & Heuristics",
            "Adversarial Search & Min-Max"
        ],
        "question": """**Mymensingh Engineering College (MEC)**  
**Department of Computer Science and Engineering**  
**4th Year 1st Semester • Term Test-01**  
**Course No:** CSE-4101 • **Course Title:** Artificial Intelligence  
**Time:** 20 min • **Full Marks:** 15

---

(a) What is Heuristic Function? What do you understand by Informed search and Uninformed search? **[1+4]**  
(b) Consider the search space below where S is the starting state and G satisfies the goal test. Show the steps if we want to find G using A* Search algorithm. (Arcs are labeled with the cost of traversing them and the estimated cost to reach goal is reported inside nodes). **[6]**

```mermaid
graph LR
    S((S: 9)) -->|1| A((A: 6))
    S -->|2| D((D: 8))
    A -->|4| Q((Q: 4))
    A -->|5| E((E: 5))
    Q -->|2| E
    E -->|1| G((G: 0 - Goal))
    D -->|7| G
    D -->|3| P((P: 3))
    P -->|2| G
```

(c) Consider the following Game Tree assuming first player as maximizing. Apply MiniMax Algorithm on the Tree. **[4]**

```mermaid
graph TD
    A[A - Max] --> B[B - Min]
    A --> C[C - Min]
    A --> D[D - Min]
    B --> E[E - Max]
    B --> F[F - Max]
    B --> G[G - Max]
    C --> H[H - Max]
    C --> I[I - Max]
    C --> J[J - Max]
    D --> K[K - Max]
    D --> L[L - Max]
    D --> M[M - Max]
    E --> E1[8]
    E --> E2[5]
    F --> F1[-2]
    F --> F2[3]
    G --> G1[10]
    G --> G2[-2]
    H --> H1[6]
    H --> H2[2]
    I --> I1[5]
    I --> I2[4]
    J --> J1[6]
    J --> J2[2]
    K --> K1[6]
    K --> K2[7]
    L --> L1[5]
    L --> L2[1]
    M --> M1[3]
    M --> M2[9]
```""",
        "subparts": [
            {
                "id": "cse-4101-term-mec-tt1-qa",
                "qno": "1(a)",
                "label": "(a)",
                "marks": 5,
                "topics": ["Informed vs Uninformed Search"],
                "question": "What is Heuristic Function? What do you understand by Informed search and Uninformed search? [1+4]",
                "solution": {
                    "steps": [
                        "1. **Heuristic Function $h(n)$:** An evaluation function that estimates the cheapest cost from node $n$ to a target goal state. It incorporates problem-specific domain knowledge.",
                        "2. **Uninformed (Blind) Search:** Algorithms (BFS, DFS, Uniform Cost Search, Iterative Deepening) that systematically explore the state space relying strictly on the graph definition and path cost without any estimate of how close a state is to the goal.",
                        "3. **Informed (Heuristic) Search:** Algorithms (Greedy Best-First Search, A* Search) that utilize $h(n)$ to steer exploration towards the most promising paths, dramatically pruning the number of expanded states."
                    ],
                    "answer": "Heuristics estimate remaining distance to goal. Informed search utilizes heuristics to guide search direction; uninformed search operates blindly.",
                    "marking_hint": "Award 1 mark for heuristic function definition, 2 marks for uninformed search, 2 marks for informed search."
                }
            },
            {
                "id": "cse-4101-term-mec-tt1-qb",
                "qno": "1(b)",
                "label": "(b)",
                "marks": 6,
                "topics": ["A* Search & Heuristics"],
                "question": "Consider the search space where S is start and G is goal. Show steps to find G using A* Search algorithm.",
                "solution": {
                    "steps": [
                        "1. **Evaluation Function:** $f(n) = g(n) + h(n)$, where $g(n)$ is actual cost from $S$ to $n$, and $h(n)$ is heuristic inside node.",
                        "2. **Initial Priority Queue (PQ):** Insert $S$: $g=0, h=9 \\implies f(S) = 9$. PQ: `[(S, f=9)]`.",
                        "3. **Step 1:** Expand $S$. Successors: $A$ ($g=1, h=6 \\implies f=7$), $D$ ($g=2, h=8 \\implies f=10$). PQ: `[(S-A, 7), (S-D, 10)]`.",
                        "4. **Step 2:** Expand $A$ ($f=7$). Successors: $Q$ ($g=1+4=5, h=4 \\implies f=9$), $E$ ($g=1+5=6, h=5 \\implies f=11$). PQ: `[(S-A-Q, 9), (S-D, 10), (S-A-E, 11)]`.",
                        "5. **Step 3:** Expand $Q$ ($f=9$). Successor: $E$ ($g=5+2=7, h=5 \\implies f=12$, dominated by existing path to $E$ of cost 6). PQ: `[(S-D, 10), (S-A-E, 11), (S-A-Q-E, 12)]`.",
                        "6. **Step 4:** Expand $D$ ($f=10$). Successors: $P$ ($g=2+3=5, h=3 \\implies f=8$), $G$ ($g=2+7=9, h=0 \\implies f=9$). PQ: `[(S-D-P, 8), (S-D-G, 9), (S-A-E, 11), (S-A-Q-E, 12)]`.",
                        "7. **Step 5:** Expand $P$ ($f=8$). Successor: $G$ ($g=5+2=7, h=0 \\implies f=7$). PQ: `[(S-D-P-G, 7), (S-D-G, 9), (S-A-E, 11)]`.",
                        "8. **Step 6:** Pop $G$ ($f=7$). Goal state reached!",
                        "9. **Optimal Path:** $S \\to D \\to P \\to G$ with optimal total cost $g^* = 7$."
                    ],
                    "answer": "A* finds optimal path S -> D -> P -> G with total cost = 7.",
                    "marking_hint": "Award 1 mark for each expansion step with correct f(n) calculation, 1 mark for final optimal path."
                }
            },
            {
                "id": "cse-4101-term-mec-tt1-qc",
                "qno": "1(c)",
                "label": "(c)",
                "marks": 4,
                "topics": ["Adversarial Search & Min-Max"],
                "question": "Apply MiniMax Algorithm on the given Game Tree assuming first player as maximizing.",
                "solution": {
                    "steps": [
                        "1. **Level 2 (MAX Nodes):**\n   - $E = \\max(8, 5) = 8$\n   - $F = \\max(-2, 3) = 3$\n   - $G = \\max(10, -2) = 10$\n   - $H = \\max(6, 2) = 6$\n   - $I = \\max(5, 4) = 5$\n   - $J = \\max(6, 2) = 6$\n   - $K = \\max(6, 7) = 7$\n   - $L = \\max(5, 1) = 5$\n   - $M = \\max(3, 9) = 9$",
                        "2. **Level 1 (MIN Nodes):**\n   - $B = \\min(E, F, G) = \\min(8, 3, 10) = 3$\n   - $C = \\min(H, I, J) = \\min(6, 5, 6) = 5$\n   - $D = \\min(K, L, M) = \\min(7, 5, 9) = 5$",
                        "3. **Level 0 (Root A - MAX Node):**\n   - $A = \\max(B, C, D) = \\max(3, 5, 5) = 5$",
                        "4. **Minimax Decision:** Root player should choose branch $C$ or $D$, guaranteeing a payoff of 5."
                    ],
                    "answer": "Minimax Value at Root A = 5. Optimal choice is branch C or D.",
                    "marking_hint": "Award 1.5 marks for Level 2 values, 1.5 marks for Level 1 values, 1 mark for root decision."
                }
            }
        ],
        "solution": {
            "steps": ["See detailed solution breakdowns for sub-questions below."],
            "answer": "Complete solutions for MEC CSE-4101 Term Test 1 (15 Marks total).",
            "marking_hint": "Full marks (15 M): Answer all sub-parts completely."
        },
        "similar_to": [],
        "verified": False
    },
    {
        "id": "cse-4101-term-mec-tt2",
        "course": "CSE-4101",
        "exam": "term",
        "college": "MEC",
        "term_no": 2,
        "set_no": 2,
        "year": 2024,
        "qno": "Term Test 2",
        "marks": 15,
        "topics": [
            "First-Order Logic",
            "AI Foundations",
            "PEAS & Task Environment"
        ],
        "question": """**Mymensingh Engineering College (MEC)**  
**Department of Computer Science and Engineering**  
**4th Year 1st Semester • Term Test-02**  
**Course No:** CSE-4101 • **Course Title:** Artificial Intelligence  
**Time:** 20 min • **Full Marks:** 15

---

(a) What are Universal Quantification and Existential Quantification? Write following expression using quantifier: **[2+4]**  
    i. **Everybody loves CSE**  
    ii. **Somebody loves EEE**  
(b) What is simple reflex agent? Draw a schematic diagram of a simple reflex agent. **[1+4]**  
(c) Determine Properties of the Environment (PEAS) for the following situation for an agent: **Chess**, **Online Shopping**, **Riding bi-cycle**, **Chat**. **[4]**""",
        "subparts": [
            {
                "id": "cse-4101-term-mec-tt2-qa",
                "qno": "2(a)",
                "label": "(a)",
                "marks": 6,
                "topics": ["First-Order Logic"],
                "question": "What are Universal Quantification and Existential Quantification? Write following expression using quantifier: i. Everybody loves CSE, ii. Somebody loves EEE. [2+4]",
                "solution": {
                    "steps": [
                        "1. **Universal Quantifier ($\\forall$):** States that a proposition is true for all entities in the domain of discourse: $\\forall x \\, P(x)$.",
                        "2. **Existential Quantifier ($\\exists$):** States that a proposition is true for at least one entity in the domain: $\\exists x \\, P(x)$.",
                        "3. **Translations:**\n   - i. **Everybody loves CSE:** $\\forall x \\, (\\text{Person}(x) \\to \\text{Loves}(x, \\text{CSE}))$\n   - ii. **Somebody loves EEE:** $\\exists x \\, (\\text{Person}(x) \\land \\text{Loves}(x, \\text{EEE}))$"
                    ],
                    "answer": "Universal quantifier asserts universal validity across domain; Existential asserts existence of at least one instance.",
                    "marking_hint": "Award 2 marks for quantifier definitions, 2 marks for each formal predicate statement."
                }
            },
            {
                "id": "cse-4101-term-mec-tt2-qb",
                "qno": "2(b)",
                "label": "(b)",
                "marks": 5,
                "topics": ["AI Foundations"],
                "question": "What is simple reflex agent? Draw a schematic diagram of a simple reflex agent. [1+4]",
                "solution": {
                    "steps": [
                        "1. **Definition:** A simple reflex agent selects actions based solely on the current percept, completely ignoring percept history. It operates on condition-action rules: *if condition then action*.",
                        "2. **Schematic Architecture:**\n   - **Sensors:** Perceive environment &rarr; \"What the world is like now\".\n   - **Condition-Action Rules:** Maps percept to rule &rarr; \"What action I should do now\".\n   - **Actuators:** Execute action into the environment."
                    ],
                    "answer": "Simple reflex agents act strictly on current percept via condition-action rules without maintaining state memory.",
                    "marking_hint": "Award 1 mark for definition, 4 marks for complete schematic architecture diagram."
                }
            },
            {
                "id": "cse-4101-term-mec-tt2-qc",
                "qno": "2(c)",
                "label": "(c)",
                "marks": 4,
                "topics": ["PEAS & Task Environment"],
                "question": "Determine Properties of the Environment (PEAS) for: Chess, Online Shopping, Riding bi-cycle, Chat. [4]",
                "solution": {
                    "steps": [
                        "1. **Chess:** Fully Observable, Deterministic, Static, Discrete, Multi-agent (Competitive).",
                        "2. **Online Shopping:** Partially Observable, Stochastic, Dynamic, Discrete, Single-agent (or Multi-agent).",
                        "3. **Riding bi-cycle:** Partially Observable, Stochastic, Dynamic, Continuous, Single-agent.",
                        "4. **Chat (Conversational AI):** Partially Observable, Stochastic, Dynamic, Discrete, Multi-agent."
                    ],
                    "answer": "Complete task environment characterizations across observability, determinism, dynamics, continuity, and agent count.",
                    "marking_hint": "Award 1 mark for each domain's complete property set."
                }
            }
        ],
        "solution": {
            "steps": ["See detailed solution breakdowns for sub-questions below."],
            "answer": "Complete solutions for MEC CSE-4101 Term Test 2 (15 Marks total).",
            "marking_hint": "Full marks (15 M): Answer all sub-parts completely."
        },
        "similar_to": [],
        "verified": False
    }
]

# ==============================================================================
# CSE-4102 (Mathematical & Statistical Analysis) MEC Term Tests (All 3 Tests!)
# ==============================================================================
cse4102_term_tests = [
    {
        "id": "cse-4102-term-mec-tt1",
        "course": "CSE-4102",
        "exam": "term",
        "college": "MEC",
        "term_no": 1,
        "set_no": 1,
        "year": 2024,
        "qno": "Term Test 1",
        "marks": 20,
        "topics": [
            "Laplace Transforms",
            "Inverse Laplace & ODEs",
            "Hypothesis Testing & Errors",
            "Correlation & Covariance"
        ],
        "question": """**Mymensingh Engineering College (MEC)**  
**Computer Science and Engineering**  
**In course Examination-1 • CSE 4102 (Mathematical and Statistical Analysis for Engineers)**  
**Time:** 40 min • **Full Marks:** 20

---

1. If $\\mathcal{L}\\{f(t)\\} = F(s)$, then prove that $\\mathcal{L}\\{\\frac{f(t)}{t}\\} = \\int_s^\\infty F(u) \\, du$. **[4]**  
2. Perform the inverse Laplace transform of the following expression: $\\frac{s}{(s^2 + a^2)^2}$. **[3]**  
3. It is found that 250 errors in the randomly selected 1000 lines of code from Team A and 300 errors in 800 lines of code from Team B. Can we assume that team B's performance is superior to that of A? **[4]**  
4. It's a Boy Genetic Labs claim to be able to increase the likelihood that a pregnancy will result in a boy being born. Statisticians want to test the claim. Suppose that the null hypothesis is: *It's a Boy Genetic Labs has no effect on gender outcome*. State the Type I and Type II errors. **[2]**  
5. Use Laplace transformation to solve the following initial value problem: $y'' - y' - 2y = 0$, with $y(0) = 1, y'(0) = 2$. **[4]**  
6. What is Cross-correlation? Write the difference between covariance and correlation. **[3]**""",
        "subparts": [
            {
                "id": "cse-4102-term-mec-tt1-q1",
                "qno": "1",
                "label": "1",
                "marks": 4,
                "topics": ["Laplace Transforms"],
                "question": "If L{f(t)} = F(s), then prove that L{f(t)/t} = int_s^infty F(u) du.",
                "solution": {
                    "steps": [
                        "1. By definition: $F(s) = \\int_0^\\infty e^{-st} f(t) \\, dt$.",
                        "2. Integrating both sides with respect to $s$ from $s$ to $\\infty$:\n$$\\int_s^\\infty F(u) \\, du = \\int_s^\\infty \\left( \\int_0^\\infty e^{-ut} f(t) \\, dt \\right) du$$",
                        "3. Interchanging order of integration:\n$$\\int_s^\\infty F(u) \\, du = \\int_0^\\infty f(t) \\left[ \\int_s^\\infty e^{-ut} \\, du \\right] dt = \\int_0^\\infty f(t) \\left[ \\frac{e^{-st}}{t} \\right] dt = \\int_0^\\infty e^{-st} \\frac{f(t)}{t} \\, dt$$",
                        "4. The right side is exactly $\\mathcal{L}\\{\\frac{f(t)}{t}\\}$. Hence proved."
                    ],
                    "answer": "L{f(t)/t} = int_s^infty F(u) du is rigorously proved via Fubini integral interchange.",
                    "marking_hint": "Full marks (4 M) for valid integral interchange and evaluating inner integral."
                }
            },
            {
                "id": "cse-4102-term-mec-tt1-q2",
                "qno": "2",
                "label": "2",
                "marks": 3,
                "topics": ["Inverse Laplace & ODEs"],
                "question": "Perform the inverse Laplace transform of: s / (s^2 + a^2)^2.",
                "solution": {
                    "steps": [
                        "1. Recall that $\\frac{d}{ds}\\left(\\frac{1}{s^2+a^2}\\right) = -\\frac{2s}{(s^2+a^2)^2}$.",
                        "2. Therefore: $\\frac{s}{(s^2+a^2)^2} = -\\frac{1}{2} \\frac{d}{ds}\\left( \\frac{1}{s^2+a^2} \\right)$.",
                        "3. Using property $\\mathcal{L}\\{t \\cdot g(t)\\} = -\\frac{d}{ds}G(s)$ where $G(s) = \\frac{1}{s^2+a^2} = \\frac{1}{a} \\mathcal{L}\\{\\sin(at)\\}$:\n$$\\mathcal{L}^{-1}\\left\\{\\frac{s}{(s^2+a^2)^2}\\right\\} = \\frac{1}{2} \\cdot t \\cdot \\frac{\\sin(at)}{a} = \\frac{t \\sin(at)}{2a}$$"
                    ],
                    "answer": "L^-1{ s / (s^2 + a^2)^2 } = (t sin(at)) / (2a).",
                    "marking_hint": "Award 1.5 marks for frequency derivative recognition, 1.5 marks for final solution."
                }
            },
            {
                "id": "cse-4102-term-mec-tt1-q3",
                "qno": "3",
                "label": "3",
                "marks": 4,
                "topics": ["Hypothesis Testing & Errors"],
                "question": "250 errors in 1000 lines from Team A and 300 errors in 800 lines from Team B. Can we assume that team B's performance is superior to that of A?",
                "solution": {
                    "steps": [
                        "1. Sample error rates: $p_1 = \\frac{250}{1000} = 0.25$, $p_2 = \\frac{300}{800} = 0.375$.",
                        "2. Note: A software team is superior if it produces FEWER errors per line of code. Team B's error rate (37.5%) is significantly HIGHER than Team A's (25%).",
                        "3. Hypothesis Test: $H_0: p_1 = p_2$ vs $H_1: p_2 < p_1$ (Team B superior).",
                        "4. Pooled proportion: $\\hat{p} = \\frac{250 + 300}{1000 + 800} = \\frac{550}{1800} \\approx 0.3056$, $\\hat{q} = 0.6944$.",
                        "5. Standard error: $SE = \\sqrt{\\hat{p}\\hat{q}\\left(\\frac{1}{1000} + \\frac{1}{800}\\right)} = \\sqrt{(0.3056)(0.6944)(0.00225)} \\approx 0.02185$.",
                        "6. Test statistic: $z = \\frac{p_2 - p_1}{SE} = \\frac{0.375 - 0.25}{0.02185} = +5.72$.",
                        "7. Conclusion: $z = +5.72$ is overwhelmingly positive (p-value < 0.0001). Team B has a statistically significantly higher defect rate. Therefore, Team B is NOT superior; Team A has clearly superior code quality."
                    ],
                    "answer": "No, Team B's performance is NOT superior (Team B has 37.5% error rate vs Team A's 25%, z = +5.72).",
                    "marking_hint": "Award 2 marks for proportions and SE calculation, 2 marks for test statistic and conclusion."
                }
            },
            {
                "id": "cse-4102-term-mec-tt1-q4",
                "qno": "4",
                "label": "4",
                "marks": 2,
                "topics": ["Hypothesis Testing & Errors"],
                "question": "State Type I and Type II errors for null hypothesis: It's a Boy Genetic Labs has no effect on gender outcome.",
                "solution": {
                    "steps": [
                        "1. **Type I Error (False Positive, $\\alpha$):** Rejecting $H_0$ when it is true. Concluding that the Genetic Lab DOES increase the likelihood of a boy, when in reality the lab has NO effect.",
                        "2. **Type II Error (False Negative, $\\beta$):** Failing to reject $H_0$ when it is false. Concluding that the Genetic Lab has NO effect, when in reality the lab DOES genuinely increase the likelihood of a boy."
                    ],
                    "answer": "Type I: Claiming the lab is effective when it is not. Type II: Failing to recognize that the lab is effective.",
                    "marking_hint": "Award 1 mark each for correct domain-specific Type I and Type II statements."
                }
            },
            {
                "id": "cse-4102-term-mec-tt1-q5",
                "qno": "5",
                "label": "5",
                "marks": 4,
                "topics": ["Inverse Laplace & ODEs"],
                "question": "Use Laplace transformation to solve: y'' - y' - 2y = 0, y(0) = 1, y'(0) = 2.",
                "solution": {
                    "steps": [
                        "1. Taking Laplace transform of both sides:\n$$[s^2 Y(s) - s y(0) - y'(0)] - [s Y(s) - y(0)] - 2 Y(s) = 0$$",
                        "2. Substituting initial conditions $y(0)=1, y'(0)=2$:\n$$[s^2 Y(s) - s - 2] - [s Y(s) - 1] - 2 Y(s) = 0$$\n$$(s^2 - s - 2) Y(s) - s - 1 = 0$$\n$$(s^2 - s - 2) Y(s) = s + 1$$",
                        "3. Factoring $s^2 - s - 2 = (s - 2)(s + 1)$:\n$$Y(s) = \\frac{s + 1}{(s - 2)(s + 1)} = \\frac{1}{s - 2}$$",
                        "4. Taking inverse Laplace transform:\n$$y(t) = \\mathcal{L}^{-1}\\left\\{\\frac{1}{s - 2}\\right\\} = e^{2t}$$"
                    ],
                    "answer": "y(t) = e^(2t).",
                    "marking_hint": "Award 2 marks for algebraic substitution and cancellation, 2 marks for inverse Laplace."
                }
            },
            {
                "id": "cse-4102-term-mec-tt1-q6",
                "qno": "6",
                "label": "6",
                "marks": 3,
                "topics": ["Correlation & Covariance"],
                "question": "What is Cross-correlation? Write the difference between covariance and correlation.",
                "solution": {
                    "steps": [
                        "1. **Cross-correlation:** A mathematical measure of similarity between two signals or series as a function of the displacement (time lag $\\tau$) of one relative to the other: $R_{xy}(\\tau) = \\int_{-\\infty}^\\infty x(t) y(t+\\tau) \\, dt$.",
                        "2. **Difference between Covariance and Correlation:**\n   - **Covariance $\\text{Cov}(X,Y)$:** Measures directional linear association in dimensional units ($-\\infty < \\text{Cov} < \\infty$). Highly sensitive to scale of measurement.\n   - **Correlation coefficient $r$:** Normalized, dimensionless measure of linear dependence obtained by dividing covariance by standard deviations: $r = \\frac{\\text{Cov}(X,Y)}{\\sigma_X \\sigma_Y}$, bounded strictly between $-1 \\le r \\le +1$."
                    ],
                    "answer": "Cross-correlation measures time-lagged waveform similarity. Covariance indicates directional co-movement with units; correlation standardizes it to [-1, +1].",
                    "marking_hint": "Award 1 mark for cross-correlation, 2 marks for covariance vs correlation distinction."
                }
            }
        ],
        "solution": {
            "steps": ["See detailed solution breakdowns for sub-questions below."],
            "answer": "Complete solutions for MEC CSE-4102 Term Test 1 (20 Marks total).",
            "marking_hint": "Full marks (20 M): Answer all sub-parts completely."
        },
        "similar_to": [],
        "verified": False
    },
    {
        "id": "cse-4102-term-mec-tt2",
        "course": "CSE-4102",
        "exam": "term",
        "college": "MEC",
        "term_no": 2,
        "set_no": 2,
        "year": 2024,
        "qno": "Term Test 2",
        "marks": 20,
        "topics": [
            "Fourier Transforms & Parseval Identity"
        ],
        "question": """**Mymensingh Engineering College (MEC)**  
**Computer Science and Engineering**  
**In course Examination-2 • CSE-4102 (Mathematical and Statistical Analysis for Engineers)**  
**Time:** 40 min • **Full Marks:** 20

---

1. Why do we use Fourier transform? Perform the Fourier transform of function: find $\\mathcal{F}\\left\\{\\frac{1}{2}\\left[H\\left(t+\\frac{1}{2}\\right) - H\\left(t-\\frac{1}{2}\\right)\\right]\\right\\}$ where $\\mathcal{F}\\{H(t)\\} = F(\\omega) = \\frac{2i}{\\omega}$.  
2. Find Fourier transform of $f(x) = \\frac{e^{-ax}}{x}$.  
3. Parseval's identity ensures energy conservation, relating time and frequency domain representations of signals. Using Parseval's identity if $f(x) = \\begin{cases} 1, & |x| < a \\\\ 0, & |x| > a \\end{cases}$ and $F(s) = \\sqrt{\\frac{2}{\\pi}} \\frac{\\sin sa}{s}$, now find that $\\int_0^\\infty \\frac{\\sin^2 x}{x^2} \\, dx = ?$.  
4. Find Fourier sine transform of $f(x) = \\begin{cases} x, & 0 < x < 1 \\\\ 2-x, & 1 < x < 2 \\\\ 0, & x > 2 \\end{cases}$.""",
        "subparts": [
            {
                "id": "cse-4102-term-mec-tt2-q1",
                "qno": "1",
                "label": "1",
                "marks": 5,
                "topics": ["Fourier Transforms & Parseval Identity"],
                "question": "Why do we use Fourier transform? Find F{ 1/2 [H(t+1/2) - H(t-1/2)] }.",
                "solution": {
                    "steps": [
                        "1. **Purpose:** Fourier transform decomposes a time-domain signal into its constituent frequency spectrum, essential for spectral analysis, filter design, and solving PDEs.",
                        "2. Notice $g(t) = \\frac{1}{2}\\left[H\\left(t+\\frac{1}{2}\\right) - H\\left(t-\\frac{1}{2}\\right)\\right]$ is a symmetric rectangular pulse of width 1 and height 1/2 centered at $t=0$.",
                        "3. Direct evaluation:\n$$\\mathcal{F}\\{g(t)\\} = \\int_{-1/2}^{1/2} \\frac{1}{2} e^{-i\\omega t} \\, dt = \\frac{1}{2} \\left[ \\frac{e^{-i\\omega t}}{-i\\omega} \\right]_{-1/2}^{1/2} = \\frac{e^{i\\omega/2} - e^{-i\\omega/2}}{2i\\omega} = \\frac{\\sin(\\omega/2)}{\\omega}$$"
                    ],
                    "answer": "F{g(t)} = sin(omega/2) / omega = 1/2 sinc(omega / (2pi)).",
                    "marking_hint": "Award 2 marks for explanation, 3 marks for evaluating transform."
                }
            },
            {
                "id": "cse-4102-term-mec-tt2-q2",
                "qno": "2",
                "label": "2",
                "marks": 5,
                "topics": ["Fourier Transforms & Parseval Identity"],
                "question": "Find Fourier transform of f(x) = e^(-ax) / x.",
                "solution": {
                    "steps": [
                        "1. Let $I(\\omega) = \\mathcal{F}\\left\\{\\frac{e^{-ax}}{x}\\right\\} = \\int_0^\\infty \\frac{e^{-ax}}{x} e^{-i\\omega x} \\, dx = \\int_0^\\infty \\frac{e^{-(a+i\\omega)x}}{x} \\, dx$.",
                        "2. Differentiating with respect to $\\omega$ under integral sign:\n$$\\frac{d I}{d\\omega} = \\int_0^\\infty -i e^{-(a+i\\omega)x} \\, dx = -i \\left[ \\frac{e^{-(a+i\\omega)x}}{-(a+i\\omega)} \\right]_0^\\infty = \\frac{-i}{a + i\\omega}$$",
                        "3. Integrating with respect to $\\omega$:\n$$I(\\omega) = -i \\int \\frac{d\\omega}{a + i\\omega} = -\\ln(a + i\\omega) + C = -\\ln\\sqrt{a^2+\\omega^2} - i \\tan^{-1}\\left(\\frac{\\omega}{a}\\right) + C$$"
                    ],
                    "answer": "Fourier transform evaluated via parameter differentiation yields -ln(a + i omega).",
                    "marking_hint": "Award 2.5 marks for differentiation under integral sign, 2.5 marks for integration."
                }
            },
            {
                "id": "cse-4102-term-mec-tt2-q3",
                "qno": "3",
                "label": "3",
                "marks": 5,
                "topics": ["Fourier Transforms & Parseval Identity"],
                "question": "Using Parseval's identity evaluate int_0^infty (sin^2 x) / x^2 dx.",
                "solution": {
                    "steps": [
                        "1. Parseval's identity states: $\\int_{-\\infty}^\\infty |f(x)|^2 \\, dx = \\int_{-\\infty}^\\infty |F(s)|^2 \\, ds$.",
                        "2. Left side: $f(x) = 1$ for $-a < x < a$, so $\\int_{-a}^a (1)^2 \\, dx = 2a$.",
                        "3. Right side: $F(s) = \\sqrt{\\frac{2}{\\pi}} \\frac{\\sin(sa)}{s}$, so:\n$$\\int_{-\\infty}^\\infty \\left(\\sqrt{\\frac{2}{\\pi}} \\frac{\\sin(sa)}{s}\\right)^2 ds = \\frac{2}{\\pi} \\int_{-\\infty}^\\infty \\frac{\\sin^2(sa)}{s^2} \\, ds = \\frac{4}{\\pi} \\int_0^\\infty \\frac{\\sin^2(sa)}{s^2} \\, ds$$",
                        "4. Equating both sides:\n$$\\frac{4}{\\pi} \\int_0^\\infty \\frac{\\sin^2(sa)}{s^2} \\, ds = 2a \\implies \\int_0^\\infty \\frac{\\sin^2(sa)}{s^2} \\, ds = \\frac{\\pi a}{2}$$",
                        "5. Setting $a = 1$:\n$$\\int_0^\\infty \\frac{\\sin^2 x}{x^2} \\, dx = \\frac{\\pi}{2}$$"
                    ],
                    "answer": "int_0^infty (sin^2 x)/x^2 dx = pi / 2.",
                    "marking_hint": "Full marks (5 M) for applying Parseval's identity and evaluating limit to pi/2."
                }
            },
            {
                "id": "cse-4102-term-mec-tt2-q4",
                "qno": "4",
                "label": "4",
                "marks": 5,
                "topics": ["Fourier Transforms & Parseval Identity"],
                "question": "Find Fourier sine transform of triangular pulse f(x).",
                "solution": {
                    "steps": [
                        "1. Formula: $F_s(\\omega) = \\int_0^\\infty f(x) \\sin(\\omega x) \\, dx = \\int_0^1 x \\sin(\\omega x) \\, dx + \\int_1^2 (2-x) \\sin(\\omega x) \\, dx$.",
                        "2. First integral: $\\left[ -x\\frac{\\cos(\\omega x)}{\\omega} + \\frac{\\sin(\\omega x)}{\\omega^2} \\right]_0^1 = -\\frac{\\cos\\omega}{\\omega} + \\frac{\\sin\\omega}{\\omega^2}$.",
                        "3. Second integral: $\\left[ -(2-x)\\frac{\\cos(\\omega x)}{\\omega} - \\frac{\\sin(\\omega x)}{\\omega^2} \\right]_1^2 = 0 - \\left( -\\frac{\\cos\\omega}{\\omega} - \\frac{\\sin\\omega}{\\omega^2} \\right) = \\frac{\\cos\\omega}{\\omega} + \\frac{\\sin\\omega}{\\omega^2} - \\frac{\\sin(2\\omega)}{\\omega^2}$.",
                        "4. Summing both: $F_s(\\omega) = \\frac{2\\sin\\omega - \\sin(2\\omega)}{\\omega^2} = \\frac{2\\sin\\omega(1 - \\cos\\omega)}{\\omega^2}$."
                    ],
                    "answer": "F_s(omega) = (2 sin(omega) - sin(2 omega)) / omega^2.",
                    "marking_hint": "Award 2.5 marks for integration by parts, 2.5 marks for final expression."
                }
            }
        ],
        "solution": {
            "steps": ["See detailed solution breakdowns for sub-questions below."],
            "answer": "Complete solutions for MEC CSE-4102 Term Test 2 (20 Marks total).",
            "marking_hint": "Full marks (20 M): Answer all sub-parts completely."
        },
        "similar_to": [],
        "verified": False
    },
    {
        "id": "cse-4102-term-mec-tt3",
        "course": "CSE-4102",
        "exam": "term",
        "college": "MEC",
        "term_no": 3,
        "set_no": 3,
        "year": 2024,
        "qno": "Term Test 3",
        "marks": 20,
        "topics": [
            "Markov Chains & Transition Matrices",
            "Stochastic & Stationary Processes",
            "Queueing Theory & Little's Law"
        ],
        "question": """**Mymensingh Engineering College (MEC)**  
**Computer Science and Engineering**  
**In course Examination-3 • CSE-4102 (Mathematical and Statistical Analysis for Engineers)**  
**Time:** 40 min • **Full Marks:** 20 (8+4+8)

---

1. Three boys A, B and C are throwing a ball to each other. A always throws the ball to B and B always throws the ball to C, but C is as likely to throw the ball to B as to A. If the initial probability distribution of three states A, B, C is 0.3, 0.4 and 0.3 respectively, Find: **[8]**  
   I. The transition matrix.  
   II. $P(X_2 = B)$  
   III. $P(X_3 = B, X_2 = C, X_1 = B, X_0 = A)$  
   IV. The distribution of the ball after two rounds.  
2. Billy and Dilly decide to flip two fair coins. If they get at least one head from a flip, then Billy is decided winner of that flip. Otherwise, Dilly is declared winner. After each flip, the winner receives $20 from the loser. If Billy starts with $40 and Dilly with $120, then what is the probability that Billy will wipe Dilly out? **[4]**  
3. A Commercial bank has 1 cash paying assistant. Customers are found to arrive in a Poisson fashion at an average rate of 6/hr for business transaction. The service time is found to have an Exponential Distribution with a mean of 6 mins ($\\mu = 10$/hr). The customers are processed on FCFS basis. Calculate: **[8]**  
   I. Average number of customers in the system ($L$)  
   II. Average time a customer spends in the system ($W$)  
   III. Average queue length ($L_q$)  
   IV. How many hours a week (assuming 40-hr week) can a cash paying assistant spend with the customers.""",
        "subparts": [
            {
                "id": "cse-4102-term-mec-tt3-q1",
                "qno": "1",
                "label": "1",
                "marks": 8,
                "topics": ["Markov Chains & Transition Matrices"],
                "question": "Three boys A, B, C ball throwing Markov Chain transition matrix, state probabilities, and 2-step distribution.",
                "solution": {
                    "steps": [
                        "1. **Transition Probability Matrix P:**\n   - A throws to B with prob 1: row A = `[0, 1, 0]`\n   - B throws to C with prob 1: row B = `[0, 0, 1]`\n   - C throws to A or B equally: row C = `[0.5, 0.5, 0]`\n$$P = \\begin{pmatrix} 0 & 1 & 0 \\\\ 0 & 0 & 1 \\\\ 0.5 & 0.5 & 0 \\end{pmatrix}$$",
                        "2. **Distribution after 1 round:** $\\pi^{(0)} = [0.3, 0.4, 0.3]$.\n$$\\pi^{(1)} = \\pi^{(0)} P = [0.3(0) + 0.4(0) + 0.3(0.5), \\; 0.3(1) + 0.4(0) + 0.3(0.5), \\; 0.3(0) + 0.4(1) + 0.3(0)] = [0.15, 0.45, 0.40]$$",
                        "3. **Distribution after 2 rounds:**\n$$\\pi^{(2)} = \\pi^{(1)} P = [0.40(0.5), \\; 0.15(1) + 0.40(0.5), \\; 0.45(1)] = [0.20, 0.35, 0.45]$$",
                        "4. **Answers:**\n   - I. Matrix $P$ as above.\n   - II. $P(X_2 = B) = \\pi^{(2)}_B = 0.35$.\n   - III. $P(X_3=B, X_2=C, X_1=B, X_0=A) = P(X_0=A) \\cdot P_{AB} \\cdot P_{BC} \\cdot P_{CB} = 0.3 \\times 1 \\times 1 \\times 0.5 = 0.15$.\n   - IV. Distribution after two rounds: $[P(A)=0.20, P(B)=0.35, P(C)=0.45]$."
                    ],
                    "answer": "P(X2=B) = 0.35; Path probability = 0.15; Two-round distribution = [0.20, 0.35, 0.45].",
                    "marking_hint": "Award 2 marks each for Transition matrix, P(X2=B), joint chain probability, and 2-step distribution."
                }
            },
            {
                "id": "cse-4102-term-mec-tt3-q2",
                "qno": "2",
                "label": "2",
                "marks": 4,
                "topics": ["Stochastic & Stationary Processes"],
                "question": "Gambler's Ruin: Billy starts with $40, Dilly with $120. Find probability Billy wipes Dilly out.",
                "solution": {
                    "steps": [
                        "1. Two fair coins: sample space $S = \\{HH, HT, TH, TT\\}$.",
                        "2. Billy wins if at least one Head: $p = P(\\text{at least 1 H}) = 1 - P(TT) = 1 - 1/4 = 3/4 = 0.75$.",
                        "3. Dilly wins otherwise: $q = 1/4 = 0.25$.",
                        "4. Ratio: $\\frac{q}{p} = \\frac{1/4}{3/4} = \\frac{1}{3}$.",
                        "5. Total units: Step size = $20. Total fortune $N = \\frac{40 + 120}{20} = 8$ units. Billy initial fortune $i = \\frac{40}{20} = 2$ units.",
                        "6. Gambler's ruin ruin formula (Probability of reaching $N$ from $i$ when $p \\ne q$):\n$$P_i = \\frac{1 - (q/p)^i}{1 - (q/p)^N} = \\frac{1 - (1/3)^2}{1 - (1/3)^8} = \\frac{1 - 1/9}{1 - 1/6561} = \\frac{8/9}{6560/6561} = \\frac{8 \\times 729}{6560} = \\frac{5832}{6560} \\approx 0.8890$$"
                    ],
                    "answer": "Probability that Billy wipes Dilly out is 5832/6560 ≈ 88.90%.",
                    "marking_hint": "Award 1.5 marks for p and q determination, 2.5 marks for applying gambler's ruin formula."
                }
            },
            {
                "id": "cse-4102-term-mec-tt3-q3",
                "qno": "3",
                "label": "3",
                "marks": 8,
                "topics": ["Queueing Theory & Little's Law"],
                "question": "M/M/1 Queueing System: arrival lambda = 6/hr, mean service time = 6 min (mu = 10/hr). Calculate L, W, Lq, and weekly busy hours.",
                "solution": {
                    "steps": [
                        "1. **Parameters:** Arrival rate $\\lambda = 6$ customers/hour. Service rate $\\mu = \\frac{60}{6} = 10$ customers/hour.",
                        "2. **Utilization factor (Traffic Intensity):** $\\rho = \\frac{\\lambda}{\\mu} = \\frac{6}{10} = 0.60$ (System is stable since $\\rho < 1$).",
                        "3. **I. Average number of customers in system ($L$):**\n$$L = \\frac{\\rho}{1 - \\rho} = \\frac{0.6}{1 - 0.6} = \\frac{0.6}{0.4} = 1.5 \\text{ customers}$$",
                        "4. **II. Average time a customer spends in system ($W$):**\n$$W = \\frac{1}{\\mu - \\lambda} = \\frac{1}{10 - 6} = \\frac{1}{4} \\text{ hour} = 15 \\text{ minutes}$$",
                        "5. **III. Average queue length ($L_q$):**\n$$L_q = L - \\rho = 1.5 - 0.6 = 0.9 \\text{ customers}$$",
                        "6. **IV. Hours per week spent with customers:**\n$$\\text{Busy hours} = \\rho \\times 40 \\text{ hours/week} = 0.60 \\times 40 = 24 \\text{ hours/week}$$"
                    ],
                    "answer": "L = 1.5 customers; W = 15 minutes; Lq = 0.9 customers; Assistant spends 24 hours/week serving customers.",
                    "marking_hint": "Award 2 marks each for L, W, Lq, and weekly busy hours."
                }
            }
        ],
        "solution": {
            "steps": ["See detailed solution breakdowns for sub-questions below."],
            "answer": "Complete solutions for MEC CSE-4102 Term Test 3 (20 Marks total).",
            "marking_hint": "Full marks (20 M): Answer all sub-parts completely."
        },
        "similar_to": [],
        "verified": False
    }
]

# ==============================================================================
# SS-4103 (Entrepreneurship for IT Business) MEC Term Tests
# ==============================================================================
ss4103_term_tests = [
    {
        "id": "ss-4103-term-mec-tt1",
        "course": "SS-4103",
        "exam": "term",
        "college": "MEC",
        "term_no": 1,
        "set_no": 1,
        "year": 2024,
        "qno": "Term Test 1",
        "marks": 20,
        "topics": [
            "Entrepreneurship Foundations",
            "Idea Generation & Market Opportunity",
            "IT Business Ethics & Legal Issues"
        ],
        "question": """**Computer Science and Engineering Department • MEC**  
**SS 4103: Entrepreneurship for IT Business**  
**In Course: 01 • Total Marks: 20**  
*(Answer any four questions)*

---

1. Write the Characteristics of Entrepreneurs and Nine Deadly Mistakes of Entrepreneurships. **[5]**  
2. Explain the differences among creativity, innovation, and entrepreneurship. **[5]**  
3. What are the major driving forces behind the growth of small businesses? Explain in detail. **[5]**  
4. Describe any three social responsibilities of an entrepreneur. **[5]**  
5. Write 5 rewards and challenges of entrepreneurship. **[5]**""",
        "subparts": [
            {
                "id": "ss-4103-term-mec-tt1-q1",
                "qno": "1",
                "label": "1",
                "marks": 5,
                "topics": ["Entrepreneurship Foundations"],
                "question": "Write the Characteristics of Entrepreneurs and Nine Deadly Mistakes of Entrepreneurships.",
                "solution": {
                    "steps": [
                        "1. **Characteristics:** Vision, passion, calculated risk-taking, resilience, adaptability, leadership, and persistent locus of control.",
                        "2. **Nine Deadly Mistakes:** (1) Management incompetence, (2) Lack of experience, (3) Poor financial control, (4) Inadequate strategic planning, (5) Uncontrolled growth, (6) Poor location, (7) Improper inventory control, (8) Incorrect pricing, (9) Inability to transition to professional management."
                    ],
                    "answer": "Entrepreneurs combine visionary passion with disciplined risk management; avoiding the nine classic managerial pitfalls is essential for business longevity.",
                    "marking_hint": "Award 2 marks for characteristics, 3 marks for nine deadly mistakes."
                }
            },
            {
                "id": "ss-4103-term-mec-tt1-q2",
                "qno": "2",
                "label": "2",
                "marks": 5,
                "topics": ["Idea Generation & Market Opportunity"],
                "question": "Explain the differences among creativity, innovation, and entrepreneurship.",
                "solution": {
                    "steps": [
                        "1. **Creativity:** Thinking new things (ideation, conceptualizing novel connections).",
                        "2. **Innovation:** Doing new things (practical transformation of creative ideas into viable products, services, or processes).",
                        "3. **Entrepreneurship:** Creating commercial value (assembling resources, assuming risk, and building a sustainable business around an innovation)."
                    ],
                    "answer": "Creativity generates ideas, innovation develops them into workable solutions, and entrepreneurship monetizes them into viable market ventures.",
                    "marking_hint": "Award 1.67 marks each for creativity, innovation, and entrepreneurship definitions and comparative differences."
                }
            },
            {
                "id": "ss-4103-term-mec-tt1-q3",
                "qno": "3",
                "label": "3",
                "marks": 5,
                "topics": ["Entrepreneurship Foundations"],
                "question": "What are the major driving forces behind the growth of small businesses?",
                "solution": {
                    "steps": [
                        "1. **Technological Advancements:** Cloud computing, AI, open-source tools lowering market entry barriers.",
                        "2. **Changing Market Demographics:** Niche specialization, personalized customer preferences.",
                        "3. **E-Commerce & Digital Globalization:** Instant global reach via marketplaces and digital payments.",
                        "4. **Entrepreneurial Culture & Education:** Incubators, venture ecosystems, and startup culture.",
                        "5. **Outsourcing & Corporate Downsizing:** Demand for specialized third-party B2B IT contractors."
                    ],
                    "answer": "Technology, market customization, digital infrastructure, and global connectivity fuel small business expansion.",
                    "marking_hint": "Award 1 mark each for five distinct growth drivers."
                }
            },
            {
                "id": "ss-4103-term-mec-tt1-q4",
                "qno": "4",
                "label": "4",
                "marks": 5,
                "topics": ["IT Business Ethics & Legal Issues"],
                "question": "Describe any three social responsibilities of an entrepreneur.",
                "solution": {
                    "steps": [
                        "1. **Ethical Treatment of Employees:** Fair living wages, safe inclusive workplace, career growth opportunities.",
                        "2. **Consumer Protection & Privacy:** Transparent pricing, high product quality, strict adherence to user data security.",
                        "3. **Environmental Sustainability & Community Impact:** Minimizing carbon footprint, e-waste recycling, and investing in local community upliftment."
                    ],
                    "answer": "Entrepreneurs bear responsibilities towards employees, customers, and ecological/community welfare.",
                    "marking_hint": "Award 1.67 marks for each well-elaborated social responsibility."
                }
            },
            {
                "id": "ss-4103-term-mec-tt1-q5",
                "qno": "5",
                "label": "5",
                "marks": 5,
                "topics": ["Entrepreneurship Foundations"],
                "question": "Write 5 rewards and challenges of entrepreneurship.",
                "solution": {
                    "steps": [
                        "1. **5 Rewards:** (1) Autonomy & independence, (2) Unlimited financial upside, (3) Personal fulfillment & passion realization, (4) Direct community impact & job creation, (5) Creative freedom.",
                        "2. **5 Challenges:** (1) High financial uncertainty and income variability, (2) Intense stress and long working hours, (3) High risk of startup failure, (4) Complete accountability and lonely decision-making, (5) Fierce competitive pressure."
                    ],
                    "answer": "Autonomy and wealth creation reward entrepreneurs, balanced by financial risk, stress, and uncertainty.",
                    "marking_hint": "Award 2.5 marks for rewards, 2.5 marks for challenges."
                }
            }
        ],
        "solution": {
            "steps": ["See detailed solution breakdowns for sub-questions below."],
            "answer": "Complete solutions for MEC SS-4103 Term Test 1 (20 Marks total).",
            "marking_hint": "Full marks (20 M): Answer any 4 questions completely (5 marks each)."
        },
        "similar_to": [],
        "verified": False
    },
    {
        "id": "ss-4103-term-mec-tt2",
        "course": "SS-4103",
        "exam": "term",
        "college": "MEC",
        "term_no": 2,
        "set_no": 2,
        "year": 2024,
        "qno": "Term Test 2",
        "marks": 20,
        "topics": [
            "Business Models & Canvas",
            "Financial Planning & Valuation",
            "Marketing Strategy & Growth",
            "IT Business Ethics & Legal Issues"
        ],
        "question": """**Computer Science and Engineering Department • MEC**  
**SS 4103: Entrepreneurship for IT Business**  
**In Course II • Total Marks: 20**  
*(Answer any four questions)*

---

1. Explain the major Forms of Business ownership. **[5]**  
2. What is Supply Chain Management? Identify the major components of a supply chain. **[5]**  
3. What is a cash-flow statement? Discuss the importance of preparing a cash-flow forecast. **[5]**  
4. What is Creative Advertising? Write the Importance of Creativity in Advertising. **[5]**  
5. Write the Major Legal Requirements for Establishing a Small Business. **[5]**""",
        "subparts": [
            {
                "id": "ss-4103-term-mec-tt2-q1",
                "qno": "1",
                "label": "1",
                "marks": 5,
                "topics": ["Business Models & Canvas"],
                "question": "Explain the major Forms of Business ownership.",
                "solution": {
                    "steps": [
                        "1. **Sole Proprietorship:** Owned and operated by one individual; easiest to establish, complete control, but unlimited personal liability.",
                        "2. **Partnership:** Two or more owners pooling capital and expertise; shared risk, but joint and several liability unless structured as LLP.",
                        "3. **Corporation (C-Corp/S-Corp):** Separate legal entity owned by shareholders; limited liability, easy capital raising via equity, but double taxation and extensive regulation.",
                        "4. **Limited Liability Company (LLC):** Hybrid structure offering corporate limited liability with partnership pass-through taxation."
                    ],
                    "answer": "Sole proprietorships, partnerships, corporations, and LLCs balance management flexibility, liability protection, and tax structures.",
                    "marking_hint": "Award 1.25 marks for each ownership form."
                }
            },
            {
                "id": "ss-4103-term-mec-tt2-q2",
                "qno": "2",
                "label": "2",
                "marks": 5,
                "topics": ["Business Models & Canvas"],
                "question": "What is Supply Chain Management? Identify the major components of a supply chain.",
                "solution": {
                    "steps": [
                        "1. **Supply Chain Management (SCM):** The active management of supply chain activities to maximize customer value and achieve a sustainable competitive advantage.",
                        "2. **Major Components:** (1) Planning (demand forecasting), (2) Sourcing (vendor selection), (3) Making (production/assembly), (4) Delivering (logistics and distribution), (5) Returning (reverse logistics and customer support)."
                    ],
                    "answer": "SCM coordinates end-to-end material, financial, and informational flows across suppliers, manufacturers, and customers.",
                    "marking_hint": "Award 2 marks for SCM definition, 3 marks for identifying and detailing 5 core components."
                }
            },
            {
                "id": "ss-4103-term-mec-tt2-q3",
                "qno": "3",
                "label": "3",
                "marks": 5,
                "topics": ["Financial Planning & Valuation"],
                "question": "What is a cash-flow statement? Discuss the importance of preparing a cash-flow forecast.",
                "solution": {
                    "steps": [
                        "1. **Cash-Flow Statement:** Financial statement reporting cash inflows and outflows across operating, investing, and financing activities over a specific period.",
                        "2. **Importance of Cash-Flow Forecast:**\n   - Prevents insolvency (cash shortage is primary killer of profitable startups).\n   - Facilitates working capital planning and payroll certainty.\n   - Identifies capital expenditure funding needs well in advance.\n   - Enhances investor and lender confidence during credit evaluations."
                    ],
                    "answer": "Cash flow measures true operational liquidity; forecasting ensures solvency and timely working capital management.",
                    "marking_hint": "Award 2 marks for definition, 3 marks for four distinct reasons for forecasting importance."
                }
            },
            {
                "id": "ss-4103-term-mec-tt2-q4",
                "qno": "4",
                "label": "4",
                "marks": 5,
                "topics": ["Marketing Strategy & Growth"],
                "question": "What is Creative Advertising? Write the Importance of Creativity in Advertising.",
                "solution": {
                    "steps": [
                        "1. **Creative Advertising:** The conceptual crafting of marketing communications that combine unexpected originality with brand message relevance to evoke emotional resonance.",
                        "2. **Importance:**\n   - **Cuts Through Noise:** Captures fleeting audience attention in ad-saturated environments.\n   - **Memorability & Recall:** Emotionally engaging campaigns achieve substantially higher recall.\n   - **Viral Amplification:** Creative digital ads trigger organic user shares and word-of-mouth.\n   - **Cost Efficiency:** Higher engagement lowers cost-per-acquisition (CPA)."
                    ],
                    "answer": "Creative advertising combines novelty and relevance to boost brand recall, cut through media clutter, and drive viral engagement.",
                    "marking_hint": "Award 2 marks for definition, 3 marks for explaining key benefits."
                }
            },
            {
                "id": "ss-4103-term-mec-tt2-q5",
                "qno": "5",
                "label": "5",
                "marks": 5,
                "topics": ["IT Business Ethics & Legal Issues"],
                "question": "Write the Major Legal Requirements for Establishing a Small Business.",
                "solution": {
                    "steps": [
                        "1. **Business Registration & Entity Selection:** Registering trade name and articles of incorporation/partnership.",
                        "2. **Trade License:** Municipal or city corporation trade license acquisition.",
                        "3. **Taxation & TIN/BIN:** Obtaining Taxpayer Identification Number (TIN) and Value Added Tax registration (BIN).",
                        "4. **Intellectual Property Protection:** Registering trademarks, patents, and software copyrights.",
                        "5. **Labor & Employment Law Compliance:** Worker compensation, workplace safety, and formal employment contracts.",
                        "6. **Industry-Specific IT Permits:** Data privacy compliance, cybersecurity standards, and digital commerce licenses."
                    ],
                    "answer": "Establishing a business requires entity incorporation, trade licenses, tax registration (TIN/BIN), IP protection, and statutory labor compliance.",
                    "marking_hint": "Award 1 mark each for five core legal requirements."
                }
            }
        ],
        "solution": {
            "steps": ["See detailed solution breakdowns for sub-questions below."],
            "answer": "Complete solutions for MEC SS-4103 Term Test 2 (20 Marks total).",
            "marking_hint": "Full marks (20 M): Answer any 4 questions completely (5 marks each)."
        },
        "similar_to": [],
        "verified": False
    }
]

# ==============================================================================
# CSE-4125 (Introduction to Machine Learning) MEC Term Tests
# ==============================================================================
cse4125_term_tests = [
    {
        "id": "cse-4125-term-mec-tt1",
        "course": "CSE-4125",
        "exam": "term",
        "college": "MEC",
        "term_no": 1,
        "set_no": 1,
        "year": 2024,
        "qno": "Term Test 1",
        "marks": 10,
        "topics": [
            "Clustering (K-Means, Hierarchical)",
            "Naive Bayes & Bayesian Learning"
        ],
        "question": """**Mymensingh Engineering College (MEC)**  
**CSE, 4th Year 1st Semester • Incourse 1**  
**Course Title:** Machine Learning • **Course Code:** CSE-4125  
**Duration:** 50 Minutes • **Full Marks:** 10

---

(a) Apply $k(2)$-means algorithm over the data $(185,72), (170,56), (168,60), (179,68), (182,72), (188,77)$ up to two iterations and show the clusters. Initially choose first two objects as initial centroids. **[5]**  
(b) Consider the given Dataset, Apply Naive Bayes Algorithm and Predict that if a fruit has the following properties then which type of the fruit it is:  
**Fruit = {Yellow, Sweet, Long}** **[5]**

**Frequency Table:**
| Fruit | Yellow | Sweet | Long | Total |
| :--- | :---: | :---: | :---: | :---: |
| **Mango** | 350 | 450 | 0 | 650 |
| **Banana** | 400 | 300 | 350 | 400 |
| **Others** | 50 | 100 | 50 | 150 |
| **Total** | 800 | 850 | 400 | 1200 |""",
        "subparts": [
            {
                "id": "cse-4125-term-mec-tt1-qa",
                "qno": "1(a)",
                "label": "(a)",
                "marks": 5,
                "topics": ["Clustering (K-Means, Hierarchical)"],
                "question": "Apply k(2)-means algorithm over the given data up to two iterations with initial centroids as first two objects.",
                "solution": {
                    "steps": [
                        "1. Given 6 points: $P_1(185,72), P_2(170,56), P_3(168,60), P_4(179,68), P_5(182,72), P_6(188,77)$.",
                        "2. **Initial Centroids:** $C_1 = P_1(185, 72)$, $C_2 = P_2(170, 56)$.",
                        "3. **Iteration 1 - Euclidean Distances $d(P, C_i)$:**\n   - $P_1$: $d_1 = 0$, $d_2 = \\sqrt{15^2+16^2} = 21.9 \\implies C_1$\n   - $P_2$: $d_1 = 21.9$, $d_2 = 0 \\implies C_2$\n   - $P_3$: $d_1 = \\sqrt{17^2+12^2} = 20.8$, $d_2 = \\sqrt{2^2+4^2} = 4.5 \\implies C_2$\n   - $P_4$: $d_1 = \\sqrt{6^2+4^2} = 7.2$, $d_2 = \\sqrt{9^2+12^2} = 15 \\implies C_1$\n   - $P_5$: $d_1 = \\sqrt{3^2+0} = 3$, $d_2 = \\sqrt{12^2+16^2} = 20 \\implies C_1$\n   - $P_6$: $d_1 = \\sqrt{3^2+5^2} = 5.8$, $d_2 = \\sqrt{18^2+21^2} = 27.7 \\implies C_1$",
                        "4. **Clusters after Iteration 1:**\n   - Cluster 1: $\\{P_1, P_4, P_5, P_6\\}$\n   - Cluster 2: $\\{P_2, P_3\\}$",
                        "5. **Update Centroids:**\n   - $C_1' = \\left(\\frac{185+179+182+188}{4}, \\frac{72+68+72+77}{4}\\right) = (183.5, 72.25)$\n   - $C_2' = \\left(\\frac{170+168}{2}, \\frac{56+60}{2}\\right) = (169, 58)$",
                        "6. **Iteration 2 - Distances to $C_1'(183.5, 72.25)$ and $C_2'(169, 58)$:**\n   - All points retain identical cluster assignments. Cluster assignments have converged!"
                    ],
                    "answer": "Final Clusters: Cluster 1 = {P1, P4, P5, P6} with centroid (183.5, 72.25); Cluster 2 = {P2, P3} with centroid (169, 58).",
                    "marking_hint": "Award 2.5 marks for iteration 1 distance calculations, 2.5 marks for centroid updates and iteration 2 verification."
                }
            },
            {
                "id": "cse-4125-term-mec-tt1-qb",
                "qno": "1(b)",
                "label": "(b)",
                "marks": 5,
                "topics": ["Naive Bayes & Bayesian Learning"],
                "question": "Apply Naive Bayes Algorithm to predict fruit type for Fruit = {Yellow, Sweet, Long}.",
                "solution": {
                    "steps": [
                        "1. **Class Prior Probabilities ($N = 1200$):**\n   - $P(\\text{Mango}) = 650/1200 = 0.5417$\n   - $P(\\text{Banana}) = 400/1200 = 0.3333$\n   - $P(\\text{Others}) = 150/1200 = 0.1250$",
                        "2. **Conditional Likelihoods:**\n   - For **Mango:** $P(\\text{Yellow}|M) = 350/650$, $P(\\text{Sweet}|M) = 450/650$, $P(\\text{Long}|M) = 0/650 = 0$ (or with Laplace smoothing $\\frac{0+1}{650+2} = \\frac{1}{652}$).\n     Without smoothing: $P(X|\\text{Mango}) = \\frac{350}{650} \\times \\frac{450}{650} \\times 0 = 0$.\n   - For **Banana:**\n     $P(\\text{Yellow}|B) = 400/400 = 1.0$\n     $P(\\text{Sweet}|B) = 300/400 = 0.75$\n     $P(\\text{Long}|B) = 350/400 = 0.875$\n     Posterior numerator: $P(B) \\times P(X|B) = 0.3333 \\times 1.0 \\times 0.75 \\times 0.875 = 0.21875$.\n   - For **Others:**\n     $P(\\text{Yellow}|O) = 50/150 = 0.3333$\n     $P(\\text{Sweet}|O) = 100/150 = 0.6667$\n     $P(\\text{Long}|O) = 50/150 = 0.3333$\n     Posterior numerator: $P(O) \\times P(X|O) = 0.1250 \\times 0.3333 \\times 0.6667 \\times 0.3333 \\approx 0.00926$.",
                        "3. **Comparison:** Posterior score for Banana ($0.21875$) is overwhelmingly higher than Others ($0.00926$) and Mango ($0$).",
                        "4. **Prediction:** The fruit is **Banana**."
                    ],
                    "answer": "Predicted Fruit: Banana (Posterior score = 0.21875 vs 0 for Mango and 0.00926 for Others).",
                    "marking_hint": "Award 2 marks for priors and likelihoods, 3 marks for posterior comparison and correct classification."
                }
            }
        ],
        "solution": {
            "steps": ["See detailed solution breakdowns for sub-questions below."],
            "answer": "Complete solutions for MEC CSE-4125 Term Test 1 (10 Marks total).",
            "marking_hint": "Full marks (10 M): Answer all sub-parts completely."
        },
        "similar_to": [],
        "verified": False
    },
    {
        "id": "cse-4125-term-mec-tt2",
        "course": "CSE-4125",
        "exam": "term",
        "college": "MEC",
        "term_no": 2,
        "set_no": 2,
        "year": 2024,
        "qno": "Term Test 2",
        "marks": 10,
        "topics": [
            "k-Nearest Neighbors (k-NN)",
            "Model Evaluation & Overfitting",
            "Linear & Logistic Regression"
        ],
        "question": """**MEC, CSE, Machine Learning, CT-2, 4th year 1st Semester**

---

1. How does KNN Work? **[3]**  
2. Explain overfitting and underfitting. **[3]**  
3. Explain Logistic Regression as a classification algorithm. **[4]**""",
        "subparts": [
            {
                "id": "cse-4125-term-mec-tt2-q1",
                "qno": "1",
                "label": "1",
                "marks": 3,
                "topics": ["k-Nearest Neighbors (k-NN)"],
                "question": "How does KNN Work?",
                "solution": {
                    "steps": [
                        "1. **Non-parametric & Lazy Learner:** Stores all training instances without constructing an explicit mathematical model.",
                        "2. **Algorithm Steps:**\n   - For an unseen query point $x_q$, compute distance (Euclidean, Manhattan) to all training points.\n   - Identify the $k$ nearest training samples.\n   - **Classification:** Majority voting among the $k$ neighbors.\n   - **Regression:** Mean or median of the target values of the $k$ neighbors."
                    ],
                    "answer": "KNN calculates metric distances from the query point to all stored training samples and assigns the majority class among the top k neighbors.",
                    "marking_hint": "Award 1.5 marks for distance calculation, 1.5 marks for majority voting mechanism."
                }
            },
            {
                "id": "cse-4125-term-mec-tt2-q2",
                "qno": "2",
                "label": "2",
                "marks": 3,
                "topics": ["Model Evaluation & Overfitting"],
                "question": "Explain overfitting and underfitting.",
                "solution": {
                    "steps": [
                        "1. **Overfitting (High Variance):** Model learns noise and idiosyncrasies of training data; performs excellently on training set but poorly on unseen test data. *Remedies:* L1/L2 regularization, dropout, pruning, gathering more data.",
                        "2. **Underfitting (High Bias):** Model is too simplistic to capture underlying patterns; performs poorly on both training and test data. *Remedies:* Increasing model capacity, adding polynomial/interaction features, decreasing regularization."
                    ],
                    "answer": "Overfitting captures noise (high variance); underfitting fails to capture underlying patterns (high bias).",
                    "marking_hint": "Award 1.5 marks for overfitting, 1.5 marks for underfitting with respective causes/remedies."
                }
            },
            {
                "id": "cse-4125-term-mec-tt2-q3",
                "qno": "3",
                "label": "3",
                "marks": 4,
                "topics": ["Linear & Logistic Regression"],
                "question": "Explain Logistic Regression as a classification algorithm.",
                "solution": {
                    "steps": [
                        "1. **Concept:** Despite its name, Logistic Regression is a binary classification algorithm predicting the probability $P(Y=1|X)$.",
                        "2. **Sigmoid / Logistic Link Function:** Transforms real-valued linear score $z = w^T x + b$ into a valid probability in $[0, 1]$:\n$$\\sigma(z) = \\frac{1}{1 + e^{-z}}$$",
                        "3. **Cost Function (Binary Cross-Entropy / Log-Loss):**\n$$J(w) = -\\frac{1}{m}\\sum_{i=1}^m \\left[ y^{(i)} \\ln(\\hat{y}^{(i)}) + (1 - y^{(i)}) \\ln(1 - \\hat{y}^{(i)}) \\right]$$",
                        "4. **Decision Boundary:** Classifies as 1 if $\\sigma(z) \\ge 0.5$ (i.e. $z \\ge 0$), and 0 otherwise."
                    ],
                    "answer": "Logistic regression maps linear combinations of features through the sigmoid function to output calibrated probabilities optimized via log-loss.",
                    "marking_hint": "Award 1.5 marks for sigmoid function, 1.5 marks for loss function, 1 mark for decision boundary."
                }
            }
        ],
        "solution": {
            "steps": ["See detailed solution breakdowns for sub-questions below."],
            "answer": "Complete solutions for MEC CSE-4125 Term Test 2 (10 Marks total).",
            "marking_hint": "Full marks (10 M): Answer all sub-parts completely."
        },
        "similar_to": [],
        "verified": False
    }
]

# ==============================================================================
# CSE-4126 (Introduction to Data Science) MEC Term Tests
# ==============================================================================
cse4126_term_tests = [
    {
        "id": "cse-4126-term-mec-tt1",
        "course": "CSE-4126",
        "exam": "term",
        "college": "MEC",
        "term_no": 1,
        "set_no": 1,
        "year": 2024,
        "qno": "Term Test 1",
        "marks": 20,
        "topics": [
            "Data Science Lifecycle & Pipelines",
            "Data Collection & Web Scraping",
            "Exploratory Data Analysis (EDA)"
        ],
        "question": """**Incourse-1 • CSE-4126**  
**4th Year 1st Semester (2021-22)**  
**Time:** 45 mins • **Marks:** 20

---

1. Define Data Science. Write down the key differences between Qualitative & Quantitative data. **[4]**  
2. Discuss the types of Questionnaire Method. **[3]**  
3. Mention some challenges in data collection method. **[3]**  
4. Explain KNN algorithm with an example. **[5]**  
5. Identify if there are any outliers in the following dataset with IQR:  
$X = \\{40, 45, 50, 52, 55, 58, 60, 62, 68, 90\\}$. **[5]**""",
        "subparts": [
            {
                "id": "cse-4126-term-mec-tt1-q1",
                "qno": "1",
                "label": "1",
                "marks": 4,
                "topics": ["Data Science Lifecycle & Pipelines"],
                "question": "Define Data Science. Write down the key differences between Qualitative & Quantitative data. [4]",
                "solution": {
                    "steps": [
                        "1. **Definition:** An interdisciplinary field combining computer science, statistics, domain expertise, and machine learning to extract actionable knowledge from structured and unstructured data.",
                        "2. **Differences:**\n   - **Qualitative Data (Categorical):** Non-numerical, descriptive, subjective (e.g. sentiment, color, customer feedback). Measured on Nominal or Ordinal scales.\n   - **Quantitative Data (Numerical):** Numerical counts or measurements, objective, amenable to mathematical operations (e.g. salary, temperature, weight). Measured on Interval or Ratio scales."
                    ],
                    "answer": "Data Science synthesizes statistical algorithms and computing to extract insights. Qualitative is descriptive; Quantitative is numerical.",
                    "marking_hint": "Award 1.5 marks for definition, 2.5 marks for qualitative vs quantitative differences."
                }
            },
            {
                "id": "cse-4126-term-mec-tt1-q2",
                "qno": "2",
                "label": "2",
                "marks": 3,
                "topics": ["Data Collection & Web Scraping"],
                "question": "Discuss the types of Questionnaire Method. [3]",
                "solution": {
                    "steps": [
                        "1. **Structured Questionnaire:** Standardized closed-ended questions with predetermined response options (multiple choice, Likert scale); easy to quantify.",
                        "2. **Unstructured Questionnaire:** Open-ended questions allowing respondents to express detailed personal perspectives; rich qualitative depth.",
                        "3. **Semi-structured Questionnaire:** Blends core structured baseline questions with open-ended probes."
                    ],
                    "answer": "Structured (closed-ended, quantitative), Unstructured (open-ended, qualitative), and Semi-structured (hybrid).",
                    "marking_hint": "Award 1 mark each for the three questionnaire categories."
                }
            },
            {
                "id": "cse-4126-term-mec-tt1-q3",
                "qno": "3",
                "label": "3",
                "marks": 3,
                "topics": ["Data Collection & Web Scraping"],
                "question": "Mention some challenges in data collection method. [3]",
                "solution": {
                    "steps": [
                        "1. **Data Quality & Incompleteness:** Missing values, transcription errors, noisy sensors.",
                        "2. **Sampling Bias & Non-response:** Unrepresentative sample populations and high non-response rates.",
                        "3. **Privacy, Security & Ethics:** Regulatory restrictions (GDPR) and confidential user data.",
                        "4. **High Resource Cost & Latency:** Expensive manual surveys and slow data pipeline throughput."
                    ],
                    "answer": "Core challenges include sampling bias, missing data, privacy/regulatory barriers, and high acquisition costs.",
                    "marking_hint": "Award 1 mark each for three distinct collection challenges."
                }
            },
            {
                "id": "cse-4126-term-mec-tt1-q4",
                "qno": "4",
                "label": "4",
                "marks": 5,
                "topics": ["Exploratory Data Analysis (EDA)"],
                "question": "Explain KNN algorithm with an example. [5]",
                "solution": {
                    "steps": [
                        "1. Compute Euclidean distance from target point to all dataset samples.",
                        "2. Rank samples by ascending distance and pick the $k$ nearest neighbors.",
                        "3. Majority vote determines the final classification.",
                        "4. **Concrete Example:** Classifying loan applicant with Income $X_1$ and Credit Score $X_2$."
                    ],
                    "answer": "Instance-based learning where unseen query point inherits dominant label of its k nearest distance neighbors.",
                    "marking_hint": "Award 2.5 marks for theoretical mechanics, 2.5 marks for worked numerical example."
                }
            },
            {
                "id": "cse-4126-term-mec-tt1-q5",
                "qno": "5",
                "label": "5",
                "marks": 5,
                "topics": ["Exploratory Data Analysis (EDA)"],
                "question": "Identify if there are any outliers in dataset X = {40, 45, 50, 52, 55, 58, 60, 62, 68, 90} with IQR. [5]",
                "solution": {
                    "steps": [
                        "1. Dataset is sorted: $X = \\{40, 45, 50, 52, 55, 58, 60, 62, 68, 90\\}$, $n = 10$.",
                        "2. **Median ($Q_2$):** Average of 5th and 6th values: $\\frac{55 + 58}{2} = 56.5$.",
                        "3. **Lower Half:** $\\{40, 45, 50, 52, 55\\} \\implies Q_1 = 50$.",
                        "4. **Upper Half:** $\\{58, 60, 62, 68, 90\\} \\implies Q_3 = 62$.",
                        "5. **Interquartile Range (IQR):** $\\text{IQR} = Q_3 - Q_1 = 62 - 50 = 12$.",
                        "6. **Fences:**\n   - Lower Fence $= Q_1 - 1.5 \\times \\text{IQR} = 50 - 1.5(12) = 50 - 18 = 32$.\n   - Upper Fence $= Q_3 + 1.5 \\times \\text{IQR} = 62 + 1.5(12) = 62 + 18 = 80$.",
                        "7. **Outlier Check:** All values are $\\ge 32$. The value $90 > 80$.",
                        "8. **Conclusion:** **90** is the only outlier in the dataset."
                    ],
                    "answer": "IQR = 12; Fences = [32, 80]; Value 90 is an outlier.",
                    "marking_hint": "Award 1.5 marks for Q1, Q3, and IQR, 1.5 marks for fences, 2 marks for outlier detection."
                }
            }
        ],
        "solution": {
            "steps": ["See detailed solution breakdowns for sub-questions below."],
            "answer": "Complete solutions for MEC CSE-4126 Term Test 1 (20 Marks total).",
            "marking_hint": "Full marks (20 M): Answer all sub-parts completely."
        },
        "similar_to": [],
        "verified": False
    },
    {
        "id": "cse-4126-term-mec-tt2",
        "course": "CSE-4126",
        "exam": "term",
        "college": "MEC",
        "term_no": 2,
        "set_no": 2,
        "year": 2024,
        "qno": "Term Test 2",
        "marks": 15,
        "topics": [
            "Data Cleaning & Preprocessing",
            "Statistical Inference & Distributions",
            "Data Visualization & Plotting"
        ],
        "question": """**Incourse-2 • CSE-4126, Session: 21-22**  
**Subject: Introduction to Data Science**  
**Time:** 45 mins • **Marks:** 15

---

1. How Redundant attributes are detected in Data Integration? **[2]**  
2. Calculate the Correlation coefficient of given data:  
$X = \\{41, 42, 43, 44, 45\\}$ & $Y = \\{3.2, 3.3, 3.4, 3.5, 3.6\\}$. **[3]**  
3. Define Data reduction. Mention Data reduction strategies. **[2]**  
4. Explain Wavelet transforms with example. **[3]**  
5. Mention data visualization techniques. **[2]**  
6. Explain Data discretization mapping with an example. **[3]**""",
        "subparts": [
            {
                "id": "cse-4126-term-mec-tt2-q1",
                "qno": "1",
                "label": "1",
                "marks": 2,
                "topics": ["Data Cleaning & Preprocessing"],
                "question": "How Redundant attributes are detected in Data Integration? [2]",
                "solution": {
                    "steps": [
                        "1. **Numerical Attributes:** Correlation coefficient test (Pearson's $r$) and Covariance analysis to detect linearly dependent collinear features.",
                        "2. **Categorical / Nominal Attributes:** Chi-square $(\\chi^2)$ test of independence to identify whether two categorical attributes are statistically associated."
                    ],
                    "answer": "Redundancy is detected using Pearson correlation / covariance for numerical attributes and Chi-square (chi^2) test for categorical attributes.",
                    "marking_hint": "Award 1 mark each for numerical correlation and categorical Chi-square test."
                }
            },
            {
                "id": "cse-4126-term-mec-tt2-q2",
                "qno": "2",
                "label": "2",
                "marks": 3,
                "topics": ["Statistical Inference & Distributions"],
                "question": "Calculate the Correlation coefficient of X = {41, 42, 43, 44, 45} & Y = {3.2, 3.3, 3.4, 3.5, 3.6}. [3]",
                "solution": {
                    "steps": [
                        "1. Means: $\\bar{X} = \\frac{41+42+43+44+45}{5} = 43$, $\\bar{Y} = \\frac{3.2+3.3+3.4+3.5+3.6}{5} = 3.4$.",
                        "2. Deviations $(X - \\bar{X}) = \\{-2, -1, 0, 1, 2\\} \\implies \\sum (X - \\bar{X})^2 = 4 + 1 + 0 + 1 + 4 = 10$.",
                        "3. Deviations $(Y - \\bar{Y}) = \\{-0.2, -0.1, 0, 0.1, 0.2\\} \\implies \\sum (Y - \\bar{Y})^2 = 0.04 + 0.01 + 0 + 0.01 + 0.04 = 0.10$.",
                        "4. Cross-product: $\\sum (X - \\bar{X})(Y - \\bar{Y}) = (-2)(-0.2) + (-1)(-0.1) + 0 + (1)(0.1) + (2)(0.2) = 0.4 + 0.1 + 0.1 + 0.4 = 1.0$.",
                        "5. Correlation Coefficient:\n$$r = \\frac{\\sum (X - \\bar{X})(Y - \\bar{Y})}{\\sqrt{\\sum(X - \\bar{X})^2 \\sum(Y - \\bar{Y})^2}} = \\frac{1.0}{\\sqrt{10 \\times 0.10}} = \\frac{1.0}{\\sqrt{1.0}} = +1.0$$"
                    ],
                    "answer": "Correlation coefficient r = +1.0 (Perfect positive linear correlation).",
                    "marking_hint": "Award 1.5 marks for deviation tables and sums, 1.5 marks for final r = 1.0."
                }
            },
            {
                "id": "cse-4126-term-mec-tt2-q3",
                "qno": "3",
                "label": "3",
                "marks": 2,
                "topics": ["Data Cleaning & Preprocessing"],
                "question": "Define Data reduction. Mention Data reduction strategies. [2]",
                "solution": {
                    "steps": [
                        "1. **Definition:** Techniques that obtain a reduced representation of the dataset that is much smaller in volume yet closely maintains the integrity of the original data.",
                        "2. **Strategies:** (1) Dimensionality Reduction (PCA, Wavelets), (2) Numerosity Reduction (Regression, Histograms, Clustering, Sampling), (3) Data Compression (Lossless & Lossy)."
                    ],
                    "answer": "Data reduction reduces data volume while preserving analytical utility via dimensionality reduction, numerosity reduction, and compression.",
                    "marking_hint": "Award 1 mark for definition, 1 mark for naming core strategies."
                }
            },
            {
                "id": "cse-4126-term-mec-tt2-q4",
                "qno": "4",
                "label": "4",
                "marks": 3,
                "topics": ["Data Cleaning & Preprocessing"],
                "question": "Explain Wavelet transforms with example. [3]",
                "solution": {
                    "steps": [
                        "1. **Concept:** Discrete Wavelet Transform (DWT) decomposes an input signal or data vector into different frequency sub-bands (approximation and detail coefficients) at multiple resolution scales.",
                        "2. **Example:** Haar Wavelet Transform decomposes vector $[2, 4, 6, 8]$ into averages $[3, 7]$ and detail differences $[-1, -1]$, enabling lossy compression by retaining only dominant coefficients."
                    ],
                    "answer": "Wavelet transforms decompose data into multi-resolution frequency components, compressing data by retaining high-energy coefficients.",
                    "marking_hint": "Award 1.5 marks for theoretical mechanism, 1.5 marks for Haar wavelet example."
                }
            },
            {
                "id": "cse-4126-term-mec-tt2-q5",
                "qno": "5",
                "label": "5",
                "marks": 2,
                "topics": ["Data Visualization & Plotting"],
                "question": "Mention data visualization techniques. [2]",
                "solution": {
                    "steps": [
                        "1. **Pixel-Oriented Techniques:** Space-filling curves (Hilbert, Morton) coloring each data value in a separate pixel.",
                        "2. **Geometric Projection Techniques:** Scatter plots, Scatter Plot Matrix (SPLOM), Parallel Coordinates.",
                        "3. **Icon-Based Techniques:** Chernoff faces, Stick figures.",
                        "4. **Hierarchical Techniques:** Treemaps, Sunburst charts, Dimensional Stacking."
                    ],
                    "answer": "Pixel-oriented, geometric projection (scatter, parallel coordinates), icon-based, and hierarchical (treemaps).",
                    "marking_hint": "Award 0.5 marks for each distinct visualization family."
                }
            },
            {
                "id": "cse-4126-term-mec-tt2-q6",
                "qno": "6",
                "label": "6",
                "marks": 3,
                "topics": ["Data Cleaning & Preprocessing"],
                "question": "Explain Data discretization mapping with an example. [3]",
                "solution": {
                    "steps": [
                        "1. **Definition:** Transforming continuous numerical attributes into a finite set of discrete intervals or categorical bins.",
                        "2. **Mapping Methods:** Equal-width binning, Equal-frequency binning, or cluster-based discretization.",
                        "3. **Concrete Example:** Continuous `Age` attribute mapping:\n   - $[0 - 12] \\implies \\text{Child}$\n   - $[13 - 19] \\implies \\text{Teenager}$\n   - $[20 - 59] \\implies \\text{Adult}$\n   - $[60+] \\implies \\text{Senior}$"
                    ],
                    "answer": "Data discretization partitions continuous ranges into discrete categorical buckets (e.g. mapping age numbers to life stages).",
                    "marking_hint": "Award 1.5 marks for definition, 1.5 marks for concrete mapping example."
                }
            }
        ],
        "solution": {
            "steps": ["See detailed solution breakdowns for sub-questions below."],
            "answer": "Complete solutions for MEC CSE-4126 Term Test 2 (15 Marks total).",
            "marking_hint": "Full marks (15 M): Answer all sub-parts completely."
        },
        "similar_to": [],
        "verified": False
    }
]

# ==============================================================================
# MERGE INTO data/*.json FOR ALL 5 COURSES
# ==============================================================================
courses_tt_map = {
    "cse-4101.json": cse4101_term_tests,
    "cse-4102.json": cse4102_term_tests,
    "ss-4103.json": ss4103_term_tests,
    "cse-4125.json": cse4125_term_tests,
    "cse-4126.json": cse4126_term_tests
}

for filename, tt_list in courses_tt_map.items():
    filepath = DATA_DIR / filename
    with open(filepath, 'r', encoding='utf-8') as f:
        existing = json.load(f)

    # Filter out any prior term test questions to avoid duplicates
    filtered = [q for q in existing if q.get('exam') != 'term']
    # Append the new complete term test questions
    filtered.extend(tt_list)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(filtered, f, indent=2, ensure_ascii=False)
    print(f"✓ Updated {filename} with {len(tt_list)} Term Test papers.")

# Rebundle codex_data.js
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
print("✓ Successfully rebundled data/codex_data.js with all Term Tests!")
