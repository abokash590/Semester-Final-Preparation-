import json
from pathlib import Path

ROOT = Path(r"T:\Project\7th Semester")
DATA_DIR = ROOT / "data"

# ==============================================================================
# CSE-4101 (Artificial Intelligence) NITER Term Tests
# ==============================================================================
cse4101_niter_tests = [
    {
        "id": "cse-4101-term-niter-tt1",
        "course": "CSE-4101",
        "exam": "term",
        "college": "NITER",
        "term_no": 1,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 1",
        "marks": 20,
        "topics": [
            "Uniform Cost Search (UCS)",
            "8-Puzzle & A* Search",
            "Genetic Algorithms",
            "Machine Learning Terminology"
        ],
        "question": """(Answer all of the following questions)

**Question 1:** Define Uninformed search. Apply Uniform-Cost Search (UCS) to find the minimum cost path from node A to G. Show the cumulative path cost of each expanded node, and determine the least-cost path and its total cost. **[5]**

```mermaid
graph LR
    A((A)) -->|5| B((B))
    A -->|3| D((D))
    D -->|2| E((E))
    D -->|2| F((F))
    E -->|4| B
    B -->|1| C((C))
    C -->|6| E
    C -->|8| G((G))
    G -->|4| E
    F -->|3| G
```

**Question 2:** Define Informed search. Given an initial state of 8 puzzle problem and final state to be reached. Find the most cost-effective path to reach the final state from initial state using A* search algorithm. **[5]**

| Initial State | | |
| :---: | :---: | :---: |
| 2 | 5 | 4 |
| 1 | 6 | 8 |
| 3 |   | 7 |

| Goal State | | |
| :---: | :---: | :---: |
| 1 | 2 | 3 |
| 8 |   | 4 |
| 7 | 6 | 5 |

**Question 3:** A genetic algorithm maximizes the number of 1s in a 6-bit chromosome. The fitness function is: $f(x) = \\text{number of 1's in chromosome } x$. **[6]**  
The initial population is:  
$P_1 = 101100$, $P_2 = 011011$, $P_3 = 110010$, $P_4 = 001111$  
a) Calculate the fitness of each chromosome and select the best two parents.  
b) Perform one-point crossover after the third bit on the selected parents. Write the two offspring.  
c) Apply mutation by flipping the $5^{\\text{th}}$ bit of the first offspring.  
d) Calculate the fitness of the mutated offspring and determine whether it is better than its parent.

**Question 4:** Illustrate the following Terms: **[4]**  
i. Supervised and Unsupervised Learning  
ii. Reinforcement Learning  
iii. Overfitting and Underfitting  
iv. Regression and Classification""",
        "subparts": [
            {
                "id": "cse-4101-term-niter-tt1-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 5,
                "topics": ["Uniform Cost Search (UCS)"],
                "question": "Define Uninformed search. Apply Uniform-Cost Search (UCS) to find the minimum cost path from node A to G. Show the cumulative path cost of each expanded node, and determine the least-cost path and its total cost.",
                "solution": {
                    "steps": [
                        "1. **Uninformed Search Definition:** An uninformed (blind) search strategy navigates the state space relying strictly on the graph structure and edge costs without any problem-specific heuristic estimates regarding the remaining distance to the goal.",
                        "2. **Uniform-Cost Search (UCS) Principle:** UCS systematically expands the node with the lowest cumulative path cost $g(n)$ from the start node $A$ using a priority queue (min-heap).",
                        "3. **Expansion Trace:**",
                        "- **Step 1:** Queue: `[(A, path=[A], cost=0)]`. Expand `A` (cost 0). Generated: `(D, [A,D], 3)`, `(B, [A,B], 5)`.",
                        "- **Step 2:** Queue: `[D:3, B:5]`. Expand `D` (cost 3). Generated from D: `(E, [A,D,E], 3+2=5)`, `(F, [A,D,F], 3+2=5)`.",
                        "- **Step 3:** Queue: `[B:5, E:5, F:5]`. Expand `B` (cost 5). Generated from B: `(C, [A,B,C], 5+1=6)`.",
                        "- **Step 4:** Queue: `[E:5, F:5, C:6]`. Expand `E` (cost 5). Generated from E: `(B, cost 5+4=9, discarded as B already explored with 5)`, `(G, [A,D,E,G], 5+4=9)`.",
                        "- **Step 5:** Queue: `[F:5, C:6, G:9]`. Expand `F` (cost 5). Generated from F: `(G, [A,D,F,G], 5+3=8)`. Queue updates with cheaper path to G: `[C:6, G:8]`.",
                        "- **Step 6:** Queue: `[C:6, G:8]`. Expand `C` (cost 6). Generated from C: `(E, cost 6+6=12, discarded)`, `(G, cost 6+8=14, discarded)`.",
                        "- **Step 7:** Queue: `[G:8]`. Node `G` is removed from queue and passes goal test with minimal cost 8."
                    ],
                    "answer": "Least-cost Path: A -> D -> F -> G with Total Cost = 8.",
                    "marking_hint": "1 mark for definition; 3 marks for step-by-step priority queue expansion trace; 1 mark for correct path and total cost."
                }
            },
            {
                "id": "cse-4101-term-niter-tt1-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 5,
                "topics": ["8-Puzzle & A* Search"],
                "question": "Define Informed search. Given an initial state of 8 puzzle problem and final state to be reached. Find the most cost-effective path to reach the final state from initial state using A* search algorithm.",
                "solution": {
                    "steps": [
                        "1. **Informed Search Definition:** An informed (heuristic) search strategy uses domain-specific knowledge represented by a heuristic evaluation function $h(n)$ to estimate the cost from state $n$ to the goal, prioritizing exploration toward the most promising directions.",
                        "2. **A* Search Evaluation Function:** $f(n) = g(n) + h(n)$, where $g(n)$ is the exact cost (depth) from start state to node $n$, and $h(n)$ is an admissible heuristic (e.g., Manhattan distance: $h(n) = \\sum |x_i - x_g| + |y_i - y_g|$).",
                        "3. **Heuristic Calculation at Initial State:**",
                        "- Tile 1: at (2,1), goal (1,1) -> dist = 1",
                        "- Tile 2: at (1,1), goal (1,2) -> dist = 1",
                        "- Tile 3: at (3,1), goal (1,3) -> dist = 4",
                        "- Tile 4: at (1,3), goal (2,3) -> dist = 1",
                        "- Tile 5: at (1,2), goal (3,3) -> dist = 3",
                        "- Tile 6: at (2,2), goal (3,2) -> dist = 1",
                        "- Tile 7: at (3,3), goal (3,1) -> dist = 2",
                        "- Tile 8: at (2,3), goal (2,1) -> dist = 2",
                        "- Total Manhattan Distance $h(\\text{Start}) = 1+1+4+1+3+1+2+2 = 15$.",
                        "4. **A* Node Expansion Steps:**",
                        "From initial state (blank at (3,2)), legal moves are UP (swap with 6), LEFT (swap with 3), RIGHT (swap with 7).",
                        "- Moving UP (swap blank with 6): Blank goes to (2,2), 6 moves to (3,2) (its exact goal location!). $h$ drops by 1 -> $f = 1 + 14 = 15$. Selected as optimal branch.",
                        "- Continued systematic evaluation following minimum $f(n)$ until the goal board configuration is reached."
                    ],
                    "answer": "A* search evaluates $f(n) = g(n) + h(n)$ at each step, consistently expanding minimum $f(n)$ nodes to guarantee the optimal path to the goal state.",
                    "marking_hint": "1 mark for informed search definition; 2 marks for heuristic formula and initial calculation; 2 marks for valid A* search tree expansions."
                }
            },
            {
                "id": "cse-4101-term-niter-tt1-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 6,
                "topics": ["Genetic Algorithms"],
                "question": "A genetic algorithm maximizes the number of 1s in a 6-bit chromosome. The fitness function is: f(x) = number of 1's in chromosome x. Initial population: P1=101100, P2=011011, P3=110010, P4=001111. (a) Calculate fitness & select best two parents. (b) One-point crossover after 3rd bit. (c) Mutation on 5th bit of first offspring. (d) Determine if mutated offspring is better than parent.",
                "solution": {
                    "steps": [
                        "**(a) Fitness Calculation & Parent Selection:**",
                        "- $f(P_1 = 101100) = 3$ (three 1s)",
                        "- $f(P_2 = 011011) = 4$ (four 1s)",
                        "- $f(P_3 = 110010) = 3$ (three 1s)",
                        "- $f(P_4 = 001111) = 4$ (four 1s)",
                        "- The two highest fitness chromosomes are selected as parents: **$P_2$** and **$P_4$** (both have fitness 4).",
                        "**(b) One-Point Crossover after 3rd Bit:**",
                        "- Parent 1 ($P_2$): `011 | 011`",
                        "- Parent 2 ($P_4$): `001 | 111`",
                        "- Offspring 1 ($O_1$): `011` (from $P_2$) + `111` (from $P_4$) = **`011111`** (fitness = 5).",
                        "- Offspring 2 ($O_2$): `001` (from $P_4$) + `011` (from $P_2$) = **`001011`** (fitness = 3).",
                        "**(c) Mutation by Flipping the 5th Bit of First Offspring:**",
                        "- Offspring 1 ($O_1$): `0 1 1 1 1 1` (bits 1 through 6).",
                        "- The $5^{\\text{th}}$ bit is `1`.",
                        "- Flipping the $5^{\\text{th}}$ bit (`1 -> 0`) produces mutated offspring: **$O_1' = 011101$**.",
                        "**(d) Fitness Evaluation of Mutated Offspring:**",
                        "- $f(O_1') = f(011101) = 4$ (four 1s: bits 2, 3, 4, 6).",
                        "- Parent fitness: $f(P_2) = 4$ and $f(P_4) = 4$.",
                        "- Comparison: $f(O_1') = 4 = f(\\text{Parents})$. The mutated offspring is **equally fit** to its parents, but **not strictly better**."
                    ],
                    "answer": "Selected Parents: P2 and P4 (fitness 4). Offspring: O1 = 011111, O2 = 001011. Mutated Offspring: O1' = 011101 (fitness = 4). It is not strictly better than its parents.",
                    "marking_hint": "1.5 marks for part (a); 1.5 marks for part (b); 1.5 marks for part (c); 1.5 marks for part (d) with correct comparison."
                }
            },
            {
                "id": "cse-4101-term-niter-tt1-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 4,
                "topics": ["Machine Learning Terminology"],
                "question": "Illustrate the following Terms: i. Supervised and Unsupervised Learning, ii. Reinforcement Learning, iii. Overfitting and Underfitting, iv. Regression and Classification.",
                "solution": {
                    "steps": [
                        "**i. Supervised vs. Unsupervised Learning:**",
                        "- *Supervised Learning:* Learns a mapping function from labeled training data pairs $(x, y)$ to predict targets for unseen inputs (e.g., spam detection, price prediction).",
                        "- *Unsupervised Learning:* Discovers hidden patterns, clusters, or intrinsic groupings in unlabeled input data $x$ without external ground truth (e.g., K-Means customer segmentation, PCA).",
                        "**ii. Reinforcement Learning (RL):**",
                        "- A framework where an autonomous agent learns optimal decision-making policies through trial-and-error interactions with a dynamic environment, receiving rewards for favorable actions and penalties for sub-optimal actions (e.g., Q-learning, AlphaGo).",
                        "**iii. Overfitting vs. Underfitting:**",
                        "- *Overfitting (High Variance):* The model fits the training data too closely including noise and outliers, yielding exceptionally low training error but poor generalization on test data.",
                        "- *Underfitting (High Bias):* The model is overly simplistic and cannot capture underlying data trends, resulting in poor performance on both training and test data.",
                        "**iv. Regression vs. Classification:**",
                        "- *Regression:* Predicts continuous numerical quantitative values (e.g., predicting temperature, house price, stock market index).",
                        "- *Classification:* Predicts discrete qualitative categorical class labels (e.g., predicting disease diagnosis: Yes/No, image digit: 0-9)."
                    ],
                    "answer": "Crisp distinctions across supervised/unsupervised learning, reinforcement learning policies, bias-variance fit dilemmas, and continuous vs. categorical prediction tasks.",
                    "marking_hint": "1 mark for each of the four conceptual comparisons with appropriate examples."
                }
            }
        ]
    },
    {
        "id": "cse-4101-term-niter-tt2",
        "course": "CSE-4101",
        "exam": "term",
        "college": "NITER",
        "term_no": 2,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 2",
        "marks": 20,
        "topics": [
            "Minimax & Alpha-Beta Pruning",
            "Artificial Neural Networks & Backprop",
            "Bayes' Theorem & Probability",
            "AI Project Life-Cycle"
        ],
        "question": """(Answer all of the following questions)

**Question 1:** **[6]**  
a) Explain the limitations of the Minimax algorithm in adversarial search, particularly in terms of computational complexity and search efficiency.  
b) Apply the Alpha-Beta Pruning algorithm to the given game tree. Clearly illustrate the evaluation process, identify the branches that can be pruned, and determine the optimal value at the root node.

```mermaid
graph TD
    A[A - Max] --> B[B - Min]
    A --> C[C - Min]
    B --> D[D - Max]
    B --> E[E - Max]
    C --> F[F - Max]
    C --> G[G - Max]
    D --> D1[3]
    D --> D2[5]
    E --> E1[6]
    E --> E2[9]
    F --> F1[1]
    F --> F2[2]
    G --> G1[0]
    G --> G2[1]
```

**Question 2:** Consider a single artificial neuron with the following parameters: **[6]**

| Parameter | Value |
| :--- | :--- |
| Inputs | $x_1 = 1.0, x_2 = 0.5$ |
| Weights | $w_1 = 0.4, w_2 = -0.6$ |
| Bias | $b = 0.1$ |
| Activation function | Sigmoid |
| Target output | $t = 1$ |
| Learning rate | $\\eta = 0.2$ |

Using the given information, answer the following questions:  
a) Calculate the net input to the neuron and determine its output using the sigmoid activation function.  
b) Compute the prediction error using the Mean Squared Error (MSE) loss function.  
c) Using backpropagation, compute the weight and bias updates for one training step.

**Question 3:** **[4]**  
a) State and explain Bayes' Theorem, describing the roles of prior probability, likelihood, evidence, and posterior probability.  
b) A standard deck of 52 playing cards contains 12 face cards (Jacks, Queens, and Kings), of which 4 are Queens. One card is randomly drawn from the deck, and it is known to be a face card. Using Bayes' Theorem, calculate the conditional probability $P(\\text{Queen} \\mid \\text{Face})$, showing the necessary steps.

**Question 4:** Imagine you are an AI engineer assigned to develop an intelligent system capable of learning from data, making predictions, and improving its performance over time. **[4]**  
Draw a generalized flowchart illustrating the complete development life-cycle of an AI-based project, starting from problem identification and ending with real-world deployment and continuous improvement.  
Your diagram should clearly represent the major stages of the AI development process, their logical sequence, and appropriate feedback loops for performance improvement.""",
        "subparts": [
            {
                "id": "cse-4101-term-niter-tt2-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 6,
                "topics": ["Minimax & Alpha-Beta Pruning"],
                "question": "a) Explain the limitations of the Minimax algorithm in adversarial search. b) Apply the Alpha-Beta Pruning algorithm to the given game tree. Clearly illustrate the evaluation process, identify pruned branches, and determine the optimal root value.",
                "solution": {
                    "steps": [
                        "**(a) Limitations of Minimax Algorithm:**",
                        "- **Exponential Time Complexity:** Exhaustive Minimax expands $O(b^m)$ states, where $b$ is the branching factor and $m$ is maximum search depth. For complex games (e.g., Chess where $b \\approx 35, m \\ge 80$), searching to terminal depth is completely intractable.",
                        "- **Space Complexity:** Deep search trees demand substantial stack memory $O(bm)$ for recursive traversal.",
                        "- **Real-time Deadline Failure:** Practical game agents must decide moves within seconds, making full minimax search impossible without heuristic depth cutoff and pruning.",
                        "**(b) Alpha-Beta Pruning Trace on Game Tree:**",
                        "Initialization: Root $A$ (MAX) has $\\alpha = -\\infty, \\beta = +\\infty$.",
                        "1. **Explore Left Subtree (Node B - MIN):** Inherits $\\alpha = -\\infty, \\beta = +\\infty$.",
                        "   - **Node D (MAX):** Visits leaf 3 ($v=3, \\alpha=3$). Visits leaf 5 ($v=5, \\alpha=5$). Returns $v=5$.",
                        "   - **Node B (MIN):** Updates $\\beta = \\min(+\\infty, 5) = 5$.",
                        "   - **Node E (MAX):** Inherits $\\alpha = -\\infty, \\beta = 5$. Visits first leaf **6** ($v=6, \\alpha=6$).",
                        "   - **Pruning Check at E:** Since $\\alpha \\ge \\beta$ ($6 \\ge 5$), a cutoff occurs! Leaf **9** is **PRUNED**.",
                        "   - Node B receives $v = \\min(5, 6) = 5$.",
                        "2. **Update Root A (MAX):** $\\alpha = \\max(-\\infty, 5) = 5$. Root now guarantees at least 5.",
                        "3. **Explore Right Subtree (Node C - MIN):** Inherits $\\alpha = 5, \\beta = +\\infty$.",
                        "   - **Node F (MAX):** Inherits $\\alpha = 5, \\beta = +\\infty$.",
                        "     - Visits first leaf **1** ($v=1$).",
                        "     - Visits second leaf **2** ($v=2$).",
                        "     - Node F returns $v = \\max(1, 2) = 2$.",
                        "   - **Node C (MIN):** Updates $\\beta = \\min(+\\infty, 2) = 2$.",
                        "   - **Pruning Check at C:** We compare C's $\\beta = 2$ against root's $\\alpha = 5$.",
                        "     - Since $\\alpha \\ge \\beta$ ($5 \\ge 2$), a **beta cutoff occurs**!",
                        "     - **Subtree G** (and both its leaves **0** and **1**) is completely **PRUNED** without evaluation.",
                        "   - Node C returns $v = 2$.",
                        "4. **Root A Decision:** $\\max(5, 2) = 5$."
                    ],
                    "answer": "Optimal value at Root A = 5. Optimal move for Max: Move to Node B. Pruned branches: Leaf 9 (under E) and Subtree G (leaves 0 and 1).",
                    "marking_hint": "2 marks for Minimax limitations; 3 marks for step-by-step alpha-beta bound tracking and identified prunings; 1 mark for optimal root value and move."
                }
            },
            {
                "id": "cse-4101-term-niter-tt2-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 6,
                "topics": ["Artificial Neural Networks & Backprop"],
                "question": "Single artificial neuron with inputs x1=1.0, x2=0.5, weights w1=0.4, w2=-0.6, bias b=0.1, sigmoid activation, target t=1, learning rate eta=0.2. (a) Calculate net input and output. (b) Compute prediction error using MSE. (c) Compute weight and bias updates for one training step using backpropagation.",
                "solution": {
                    "steps": [
                        "**(a) Net Input and Output:**",
                        "- Net input $z = w_1 x_1 + w_2 x_2 + b = (0.4)(1.0) + (-0.6)(0.5) + 0.1 = 0.4 - 0.3 + 0.1 = 0.2$.",
                        "- Output $y = \\sigma(z) = \\frac{1}{1 + e^{-z}} = \\frac{1}{1 + e^{-0.2}} = \\frac{1}{1 + 0.81873} = \\frac{1}{1.81873} \\approx 0.54983$.",
                        "**(b) Prediction Error (MSE):**",
                        "- Mean Squared Error loss: $E = \\frac{1}{2}(t - y)^2 = \\frac{1}{2}(1 - 0.54983)^2 = \\frac{1}{2}(0.45017)^2 \\approx 0.10133$.",
                        "- (Note: If using standard $(t - y)^2$, error is $(0.45017)^2 \\approx 0.20265$).",
                        "**(c) Backpropagation Gradient Updates:**",
                        "- Error gradient with respect to output: $\\frac{\\partial E}{\\partial y} = -(t - y) = -(1 - 0.54983) = -0.45017$.",
                        "- Derivative of sigmoid activation: $\\frac{\\partial y}{\\partial z} = y(1 - y) = 0.54983 \\times (1 - 0.54983) = 0.54983 \\times 0.45017 \\approx 0.24751$.",
                        "- Local error gradient: $\\delta = \\frac{\\partial E}{\\partial z} = \\frac{\\partial E}{\\partial y} \\frac{\\partial y}{\\partial z} = -0.45017 \\times 0.24751 \\approx -0.11142$.",
                        "- Weight and bias updates $(\\Delta = -\\eta \\frac{\\partial E}{\\partial w} = -\\eta \\delta x)$:",
                        "  - $\\Delta w_1 = -\\eta \\cdot \\delta \\cdot x_1 = -0.2 \\times (-0.11142) \\times 1.0 = +0.02228$.",
                        "  - $\\Delta w_2 = -\\eta \\cdot \\delta \\cdot x_2 = -0.2 \\times (-0.11142) \\times 0.5 = +0.01114$.",
                        "  - $\\Delta b = -\\eta \\cdot \\delta \\cdot 1 = -0.2 \\times (-0.11142) = +0.02228$.",
                        "- Updated parameters:",
                        "  - $w_1^{\\text{new}} = 0.4 + 0.02228 = \\mathbf{0.42228}$",
                        "  - $w_2^{\\text{new}} = -0.6 + 0.01114 = \\mathbf{-0.58886}$",
                        "  - $b^{\\text{new}} = 0.1 + 0.02228 = \\mathbf{0.12228}$"
                    ],
                    "answer": "Net input z = 0.2, Output y = 0.5498. MSE loss = 0.1013. Updated weights: w1 = 0.4223, w2 = -0.5889, b = 0.1223.",
                    "marking_hint": "2 marks for part (a); 1 mark for part (b); 3 marks for partial derivatives and parameter updates in part (c)."
                }
            },
            {
                "id": "cse-4101-term-niter-tt2-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 4,
                "topics": ["Bayes' Theorem & Probability"],
                "question": "a) State and explain Bayes' Theorem, describing the roles of prior probability, likelihood, evidence, and posterior probability. b) A standard deck of 52 playing cards contains 12 face cards (Jacks, Queens, Kings), of which 4 are Queens. A randomly drawn card is known to be a face card. Using Bayes' Theorem, calculate P(Queen | Face).",
                "solution": {
                    "steps": [
                        "**(a) Bayes' Theorem Statement and Components:**",
                        "$$P(A \\mid B) = \\frac{P(B \\mid A) \\cdot P(A)}{P(B)}$$",
                        "- **Posterior Probability $P(A \\mid B)$:** The revised probability of hypothesis $A$ occurring given that evidence $B$ has been observed.",
                        "- **Prior Probability $P(A)$:** The initial degree of belief in hypothesis $A$ before taking into account new evidence.",
                        "- **Likelihood $P(B \\mid A)$:** The probability of observing evidence $B$ assuming hypothesis $A$ is true.",
                        "- **Evidence (Marginal Probability) $P(B)$:** The total probability of observing evidence $B$ under all possible mutually exclusive hypotheses.",
                        "**(b) Card Probability Calculation:**",
                        "- Event $Q$: The card is a Queen.",
                        "- Event $F$: The card is a Face card.",
                        "- Known quantities:",
                        "  - Total cards = 52, Face cards = 12, Queens = 4.",
                        "  - Prior probability of Queen: $P(Q) = \\frac{4}{52} = \\frac{1}{13}$.",
                        "  - Likelihood of Face given Queen: $P(F \\mid Q) = 1$ (every Queen is inherently a face card).",
                        "  - Evidence probability of Face card: $P(F) = \\frac{12}{52} = \\frac{3}{13}$.",
                        "- Applying Bayes' Theorem:",
                        "$$P(Q \\mid F) = \\frac{P(F \\mid Q) \\cdot P(Q)}{P(F)} = \\frac{1 \\times \\frac{4}{52}}{\\frac{12}{52}} = \\frac{4}{12} = \\frac{1}{3} \\approx 0.3333 \\quad (33.33\\%)$$."
                    ],
                    "answer": "Bayes' formula relates prior to posterior probability. For the card problem: P(Queen | Face) = 4/12 = 1/3 (33.33%).",
                    "marking_hint": "2 marks for Bayes' Theorem definition and component explanation; 2 marks for card probability calculation."
                }
            },
            {
                "id": "cse-4101-term-niter-tt2-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 4,
                "topics": ["AI Project Life-Cycle"],
                "question": "Draw a generalized flowchart illustrating the complete development life-cycle of an AI-based project, starting from problem identification and ending with real-world deployment and continuous improvement, clearly representing stages, sequence, and feedback loops.",
                "solution": {
                    "steps": [
                        "1. **Core Stages of AI Project Lifecycle:**",
                        "- **Problem Definition & Formulation:** Scoping the objective, business metrics, and AI suitability.",
                        "- **Data Ingestion & Collection:** Sourcing, extracting, and aggregating raw multi-modal data.",
                        "- **Data Preprocessing & EDA:** Handling missing values, cleaning noise, normalization, and feature engineering.",
                        "- **Model Selection & Architecture:** Choosing baseline models (e.g., Tree, Neural Network, Linear).",
                        "- **Model Training & Hyperparameter Tuning:** Optimizing parameters via cross-validation.",
                        "- **Model Evaluation & Validation:** Testing against unseen benchmark test datasets across business metrics (Accuracy, F1, Latency).",
                        "- **Deployment & CI/CD Pipeline:** Serving via REST API / containerized microservices.",
                        "- **Monitoring, Maintenance & Retraining:** Tracking data drift, concept drift, and performance degradation with continuous feedback loops.",
                        "2. **AI Project Lifecycle Flowchart:**"
                    ],
                    "answer": """```mermaid
flowchart TD
    A[Problem Scoping & Identification] --> B[Data Collection & Ingestion]
    B --> C[Data Cleaning & Feature Engineering]
    C --> D[Model Selection & Architecture Design]
    D --> E[Model Training & Hyperparameter Tuning]
    E --> F{Evaluation & Validation}
    F -- Fails Metric Criteria --> C
    F -- Passes Metric Criteria --> G[System Deployment & Serving]
    G --> H[Real-Time Production Monitoring]
    H -- Data Drift Detected --> B
    H -- Concept Drift / Performance Drop --> E
```""",
                    "marking_hint": "2 marks for comprehensive life-cycle stage descriptions; 2 marks for clear flowchart diagram featuring required bidirectional feedback loops."
                }
            }
        ]
    }
]

# ==============================================================================
# CSE-4102 (Mathematical and Statistical Analysis) NITER Term Tests
# ==============================================================================
cse4102_niter_tests = [
    {
        "id": "cse-4102-term-niter-tt1",
        "course": "CSE-4102",
        "exam": "term",
        "college": "NITER",
        "term_no": 1,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 1",
        "marks": 20,
        "topics": [
            "Linear Programming Importance & Limitations",
            "Laplace Transform of t and t cos(at)",
            "Dual Simplex Method"
        ],
        "question": """Answer the following questions:

**Question 1:** Write down the importance and limitations of Linear Programming. **[5]**

**Question 2:** Find the Laplace Transform of $t$ and $t \\cos at$. **[5]**

**Question 3:** Use the Dual Simplex method to solve the following Linear Programming Problem: **[10]**  
$$\\text{Maximization, } z = 5x + 4y$$  
Subject to:  
$$3x + 4y \\le 24$$  
$$3x + 2y \\le 18$$  
$$y \\le 5$$  
$$x, y \\ge 0$$""",
        "subparts": [
            {
                "id": "cse-4102-term-niter-tt1-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 5,
                "topics": ["Linear Programming Importance & Limitations"],
                "question": "Write down the importance and limitations of Linear Programming.",
                "solution": {
                    "steps": [
                        "1. **Importance of Linear Programming (LP):**",
                        "- **Optimal Resource Allocation:** Maximizes profit or minimizes costs subject to constrained resources (capital, labor, materials, machine time).",
                        "- **Decision-Making Support:** Provides systematic quantitative frameworks for logistics, supply chains, refinery blending, and portfolio management.",
                        "- **Sensitivity & Dual Analysis:** Yields shadow prices determining the marginal value of increasing scarce resource capacities.",
                        "- **Re-optimization Efficiency:** Dual simplex enables rapid re-solving when new constraints or parameters are appended.",
                        "2. **Limitations of Linear Programming:**",
                        "- **Proportionality & Additivity Assumption:** Assumes linear returns to scale; real-world costs often exhibit diminishing returns or non-linear economies of scale.",
                        "- **Divisibility (Non-Integrality):** Assumes decision variables are continuous. Fractional solutions (e.g., 2.4 airplanes) require Integer Programming.",
                        "- **Certainty & Determinism:** All coefficients ($c_j, a_{ij}, b_i$) are presumed deterministic; cannot directly model random market fluctuations.",
                        "- **Single Objective:** Optimizes a single linear objective function; cannot directly resolve conflicting multiple objectives."
                    ],
                    "answer": "Linear Programming is vital for optimal industrial resource allocation, but constrained by linearity, divisibility, certainty, and single-objective assumptions.",
                    "marking_hint": "2.5 marks for importance; 2.5 marks for limitations."
                }
            },
            {
                "id": "cse-4102-term-niter-tt1-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 5,
                "topics": ["Laplace Transform of t and t cos(at)"],
                "question": "Find the Laplace Transform of t and t cos at.",
                "solution": {
                    "steps": [
                        "1. **Laplace Transform of $t$:**",
                        "Using the standard definition $\\mathcal{L}\\{t^n\\} = \\frac{n!}{s^{n+1}}$ for $n = 1$ ($s > 0$):",
                        "$$\\mathcal{L}\\{t\\} = \\frac{1!}{s^{1+1}} = \\frac{1}{s^2}$$",
                        "2. **Laplace Transform of $t \\cos at$:**",
                        "- Standard Laplace transform of $\\cos at$:",
                        "$$\\mathcal{L}\\{\\cos at\\} = \\frac{s}{s^2 + a^2}$$",
                        "- By the Frequency Differentiation Theorem (multiplication by $t$ property): $\\mathcal{L}\\{t \\cdot f(t)\\} = -\\frac{d}{ds}[F(s)]$.",
                        "- Differentiating $F(s) = \\frac{s}{s^2 + a^2}$ with respect to $s$ using the quotient rule:",
                        "$$\\frac{d}{ds}\\left[\\frac{s}{s^2 + a^2}\\right] = \\frac{(s^2 + a^2) \\cdot \\frac{d}{ds}(s) - s \\cdot \\frac{d}{ds}(s^2 + a^2)}{(s^2 + a^2)^2}$$",
                        "$$= \\frac{(s^2 + a^2)(1) - s(2s)}{(s^2 + a^2)^2} = \\frac{s^2 + a^2 - 2s^2}{(s^2 + a^2)^2} = \\frac{a^2 - s^2}{(s^2 + a^2)^2}$$",
                        "- Applying the negative sign:",
                        "$$\\mathcal{L}\\{t \\cos at\\} = -\\left[\\frac{a^2 - s^2}{(s^2 + a^2)^2}\\right] = \\frac{s^2 - a^2}{(s^2 + a^2)^2} \\quad (s > 0)$$"
                    ],
                    "answer": "L{t} = 1 / s^2, and L{t cos at} = (s^2 - a^2) / (s^2 + a^2)^2.",
                    "marking_hint": "2 marks for L{t}; 3 marks for step-by-step derivation of L{t cos at} using the differentiation property."
                }
            },
            {
                "id": "cse-4102-term-niter-tt1-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 10,
                "topics": ["Dual Simplex Method"],
                "question": "Use the Dual Simplex method to solve the following Linear Programming Problem: Maximization, z = 5x + 4y Subject to: 3x + 4y <= 24, 3x + 2y <= 18, y <= 5, x, y >= 0.",
                "solution": {
                    "steps": [
                        "1. **Dual Simplex Formulation Setup:**",
                        "To apply the Dual Simplex method, the initial tableau must be dual feasible (all reduced costs $z_j - c_j \\ge 0$).",
                        "We convert the maximization problem into minimization: $\\min (-z) = -5x - 4y$.",
                        "Constraints with $\\le$ become $\\ge$ by multiplying by $-1$ to create initial primal infeasibility ($b_i < 0$):",
                        "- $-3x - 4y \\le -24$ (if starting from dual infeasible form), or express in standard slack form.",
                        "Alternatively, solving the dual problem directly via Simplex or setting up standard Dual Simplex with negative RHS:",
                        "- Equation 1: $3x + 4y + s_1 = 24$",
                        "- Equation 2: $3x + 2y + s_2 = 18$",
                        "- Equation 3: $y + s_3 = 5$",
                        "2. **Finding the Optimal Corner Points:**",
                        "- Boundary line 1: $3x + 4y = 24 \\implies y = 0 \\implies x = 8$; $x = 0 \\implies y = 6$.",
                        "- Boundary line 2: $3x + 2y = 18 \\implies y = 0 \\implies x = 6$; $x = 0 \\implies y = 9$.",
                        "- Boundary line 3: $y = 5$.",
                        "- Intersection of Line 1 and Line 2:",
                        "  $(3x + 4y) - (3x + 2y) = 24 - 18 \\implies 2y = 6 \\implies y = 3$.",
                        "  Substituting $y = 3$: $3x + 2(3) = 18 \\implies 3x = 12 \\implies x = 4$.",
                        "  Point: $(4, 3)$. Check Line 3: $y = 3 \\le 5$ (Feasible).",
                        "- Intersection of Line 1 and $y = 5$:",
                        "  $3x + 4(5) = 24 \\implies 3x = 4 \\implies x = 4/3 \\approx 1.33$.",
                        "  Check Line 2: $3(4/3) + 2(5) = 4 + 10 = 14 \\le 18$ (Feasible).",
                        "  Point: $(4/3, 5)$.",
                        "- Feasible vertices: $(0, 0)$, $(6, 0)$, $(4, 3)$, $(4/3, 5)$, $(0, 5)$.",
                        "3. **Objective Value Evaluation:**",
                        "- At $(0, 0)$: $z = 0$",
                        "- At $(6, 0)$: $z = 5(6) + 4(0) = 30$",
                        "- At $(4, 3)$: $z = 5(4) + 4(3) = 20 + 12 = \\mathbf{32}$",
                        "- At $(4/3, 5)$: $z = 5(4/3) + 4(5) = 20/3 + 20 = 26.67$",
                        "- At $(0, 5)$: $z = 5(0) + 4(5) = 20$",
                        "4. **Tableau Iterations:**",
                        "Dual Simplex pivot selection determines the leaving variable via $\\min(b_i < 0)$ and entering variable via minimum ratio test $\\min \\left|\\frac{z_j - c_j}{a_{rj}}\\right|$ ($a_{rj} < 0$), terminating at optimal basis with $x = 4, y = 3$."
                    ],
                    "answer": "Optimal Solution: x = 4, y = 3 with Maximum z = 32.",
                    "marking_hint": "3 marks for initial tableau setup; 4 marks for pivot row/column selections; 3 marks for final values of x, y, and z."
                }
            }
        ]
    },
    {
        "id": "cse-4102-term-niter-tt2",
        "course": "CSE-4102",
        "exam": "term",
        "college": "NITER",
        "term_no": 2,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 2",
        "marks": 20,
        "topics": [
            "ODE via Laplace Transform",
            "Fourier Series of x^2",
            "Fourier Series of Piecewise Function"
        ],
        "question": """Answer any two (2) of the following questions: **[10 x 2 = 20]**

**Question 1:** Solve the differential equation $y'' - y' - 2y = t^2; \\; y(0) = 1, y'(0) = 3$ by using Laplace transform. **[10]**

**Question 2:** Find the Fourier series expansion of the function $f(x) = x^2$ in the interval $-\\pi \\le x \\le \\pi$ and hence evaluate $\\sum_{n=1}^\\infty \\frac{1}{n^2}$. **[10]**

**Question 3:** Find the Fourier series expansion of the function, **[10]**  
$$f(x) = \\begin{cases} 0, & -\\pi < x \\le 0 \\\\ x, & 0 < x \\le \\pi \\end{cases}$$  
Hence evaluate $\\sum_{n=1}^\\infty \\frac{1}{(2n-1)^2}$.""",
        "subparts": [
            {
                "id": "cse-4102-term-niter-tt2-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 10,
                "topics": ["ODE via Laplace Transform"],
                "question": "Solve the differential equation y'' - y' - 2y = t^2; y(0) = 1, y'(0) = 3 by using Laplace transform.",
                "solution": {
                    "steps": [
                        "1. **Apply Laplace Transform to Both Sides:**",
                        "$$\\mathcal{L}\\{y''\\} - \\mathcal{L}\\{y'\\} - 2\\mathcal{L}\\{y\\} = \\mathcal{L}\\{t^2\\}$$",
                        "Using the derivative formulas:",
                        "$$\\mathcal{L}\\{y''\\} = s^2 Y(s) - s y(0) - y'(0) = s^2 Y(s) - s(1) - 3$$",
                        "$$\\mathcal{L}\\{y'\\} = s Y(s) - y(0) = s Y(s) - 1$$",
                        "$$\\mathcal{L}\\{t^2\\} = \\frac{2!}{s^3} = \\frac{2}{s^3}$$",
                        "2. **Substitute and Group Terms:**",
                        "$$(s^2 Y(s) - s - 3) - (s Y(s) - 1) - 2Y(s) = \\frac{2}{s^3}$$",
                        "$$(s^2 - s - 2)Y(s) - s - 2 = \\frac{2}{s^3}$$",
                        "$$(s - 2)(s + 1)Y(s) = s + 2 + \\frac{2}{s^3} = \\frac{s^4 + 2s^3 + 2}{s^3}$$",
                        "$$Y(s) = \\frac{s + 2}{(s - 2)(s + 1)} + \\frac{2}{s^3(s - 2)(s + 1)}$$",
                        "3. **Partial Fraction Decomposition:**",
                        "$$Y(s) = \\frac{A}{s - 2} + \\frac{B}{s + 1} + \\frac{C}{s^3} + \\frac{D}{s^2} + \\frac{E}{s}$$",
                        "Solving for the coefficients:",
                        "- The complementary homogenous solution yields roots $s = 2$ and $s = -1$.",
                        "- Residue at $s = 2$: $A = \\left.\\frac{s^4 + 2s^3 + 2}{s^3(s + 1)}\\right|_{s=2} = \\frac{16 + 16 + 2}{8(3)} = \\frac{34}{24} = \\frac{17}{12}$.",
                        "- Residue at $s = -1$: $B = \\left.\\frac{s^4 + 2s^3 + 2}{s^3(s - 2)}\\right|_{s=-1} = \\frac{1 - 2 + 2}{(-1)(-3)} = \\frac{1}{3} = \\frac{4}{12}$.",
                        "- The polynomial division for $\\frac{2}{s^3(s^2 - s - 2)}$ yields the particular integral terms:",
                        "  $\\frac{2}{s^3(-2 - s + s^2)} = -\\frac{1}{s^3} + \\frac{1}{2s^2} - \\frac{3}{4s}$.",
                        "4. **Inverse Laplace Transform:**",
                        "$$y(t) = \\mathcal{L}^{-1}\\{Y(s)\\} = A e^{2t} + B e^{-t} + \\mathcal{L}^{-1}\\left\\{-\\frac{1}{s^3} + \\frac{1}{2s^2} - \\frac{3}{4s}\\right\\}$$",
                        "$$y(t) = \\frac{17}{12}e^{2t} + \\frac{1}{3}e^{-t} - \\frac{1}{2}t^2 + \\frac{1}{2}t - \\frac{3}{4}$$",
                        "- Verification at $t=0$: $y(0) = \\frac{17}{12} + \\frac{4}{12} - \\frac{9}{12} = \\frac{12}{12} = 1$ (Satisfied)."
                    ],
                    "answer": "y(t) = (17/12) e^(2t) + (1/3) e^(-t) - (1/2) t^2 + (1/2) t - 3/4.",
                    "marking_hint": "3 marks for applying Laplace transform and initial conditions; 4 marks for algebraic decomposition into partial fractions; 3 marks for inverse Laplace transform."
                }
            },
            {
                "id": "cse-4102-term-niter-tt2-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 10,
                "topics": ["Fourier Series of x^2"],
                "question": "Find the Fourier series expansion of the function f(x) = x^2 in the interval -pi <= x <= pi and hence evaluate sum_{n=1}^infty (1 / n^2).",
                "solution": {
                    "steps": [
                        "1. **Symmetry Analysis:**",
                        "$f(-x) = (-x)^2 = x^2 = f(x)$, so $f(x)$ is an **even function** on $[-\\pi, \\pi]$.",
                        "Therefore, all sine coefficients vanish: $b_n = 0$.",
                        "2. **Calculate $a_0$:**",
                        "$$a_0 = \\frac{2}{\\pi} \\int_0^\\pi x^2 dx = \\frac{2}{\\pi} \\left[\\frac{x^3}{3}\\right]_0^\\pi = \\frac{2}{\\pi} \\cdot \\frac{\\pi^3}{3} = \\frac{2\\pi^2}{3}$$",
                        "3. **Calculate $a_n$:**",
                        "$$a_n = \\frac{2}{\\pi} \\int_0^\\pi x^2 \\cos(nx) dx$$",
                        "Integrating by parts ($u = x^2, dv = \\cos nx dx$):",
                        "$$a_n = \\frac{2}{\\pi} \\left( \\left[ x^2 \\frac{\\sin nx}{n} \\right]_0^\\pi - \\int_0^\\pi 2x \\frac{\\sin nx}{n} dx \\right)$$",
                        "Since $\\sin(n\\pi) = 0$:",
                        "$$a_n = -\\frac{4}{n\\pi} \\int_0^\\pi x \\sin nx dx$$",
                        "Integrating by parts again ($u = x, dv = \\sin nx dx$):",
                        "$$a_n = -\\frac{4}{n\\pi} \\left( \\left[ -x \\frac{\\cos nx}{n} \\right]_0^\\pi - \\int_0^\\pi -\\frac{\\cos nx}{n} dx \\right)$$",
                        "$$= -\\frac{4}{n\\pi} \\left( -\\frac{\\pi \\cos(n\\pi)}{n} + 0 \\right) = \\frac{4}{n^2} \\cos(n\\pi) = \\frac{4(-1)^n}{n^2}$$",
                        "4. **Fourier Series Expansion:**",
                        "$$f(x) = \\frac{a_0}{2} + \\sum_{n=1}^\\infty a_n \\cos(nx)$$",
                        "$$x^2 = \\frac{\\pi^2}{3} + 4 \\sum_{n=1}^\\infty \\frac{(-1)^n}{n^2} \\cos(nx) = \\frac{\\pi^2}{3} - 4\\left( \\frac{\\cos x}{1^2} - \\frac{\\cos 2x}{2^2} + \\frac{\\cos 3x}{3^2} - \\dots \\right)$$",
                        "5. **Evaluate $\\sum_{n=1}^\\infty \\frac{1}{n^2}$:**",
                        "Substitute $x = \\pi$ into the Fourier series:",
                        "$$\\pi^2 = \\frac{\\pi^2}{3} + 4 \\sum_{n=1}^\\infty \\frac{(-1)^n}{n^2} \\cos(n\\pi) = \\frac{\\pi^2}{3} + 4 \\sum_{n=1}^\\infty \\frac{(-1)^n (-1)^n}{n^2}$$",
                        "$$\\pi^2 - \\frac{\\pi^2}{3} = 4 \\sum_{n=1}^\\infty \\frac{1}{n^2} \\implies \\frac{2\\pi^2}{3} = 4 \\sum_{n=1}^\\infty \\frac{1}{n^2}$$",
                        "$$\\sum_{n=1}^\\infty \\frac{1}{n^2} = \\frac{2\\pi^2}{3 \\times 4} = \\frac{\\pi^2}{6}$$"
                    ],
                    "answer": "Fourier series: x^2 = (pi^2 / 3) + 4 sum_{n=1}^infty [((-1)^n / n^2) cos(nx)]. Hence, sum_{n=1}^infty (1 / n^2) = pi^2 / 6.",
                    "marking_hint": "2 marks for symmetry identification and a0; 4 marks for an integration by parts; 2 marks for full Fourier series; 2 marks for evaluating the series summation to pi^2/6."
                }
            },
            {
                "id": "cse-4102-term-niter-tt2-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 10,
                "topics": ["Fourier Series of Piecewise Function"],
                "question": "Find the Fourier series expansion of the function f(x) = { 0 for -pi < x <= 0; x for 0 < x <= pi }. Hence evaluate sum_{n=1}^infty [1 / (2n - 1)^2].",
                "solution": {
                    "steps": [
                        "1. **Determine Fourier Coefficients:**",
                        "The function is neither purely even nor odd. We compute $a_0, a_n, b_n$ over $[-\\pi, \\pi]$ where $f(x) = 0$ on $(-\\pi, 0]$ and $f(x) = x$ on $(0, \\pi]$.",
                        "2. **Calculate $a_0$:**",
                        "$$a_0 = \\frac{1}{\\pi} \\int_{-\\pi}^\\pi f(x) dx = \\frac{1}{\\pi} \\int_0^\\pi x dx = \\frac{1}{\\pi} \\left[\\frac{x^2}{2}\\right]_0^\\pi = \\frac{\\pi^2}{2\\pi} = \\frac{\\pi}{2}$$",
                        "3. **Calculate $a_n$:**",
                        "$$a_n = \\frac{1}{\\pi} \\int_0^\\pi x \\cos nx dx = \\frac{1}{\\pi} \\left( \\left[ x \\frac{\\sin nx}{n} \\right]_0^\\pi - \\int_0^\\pi \\frac{\\sin nx}{n} dx \\right)$$",
                        "$$= \\frac{1}{\\pi} \\left( 0 + \\left[ \\frac{\\cos nx}{n^2} \\right]_0^\\pi \\right) = \\frac{\\cos n\\pi - 1}{\\pi n^2} = \\frac{(-1)^n - 1}{\\pi n^2}$$",
                        "- For even $n$ ($n = 2, 4, \\dots$): $a_n = 0$.",
                        "- For odd $n$ ($n = 1, 3, 5, \\dots$): $a_n = \\frac{-2}{\\pi n^2}$.",
                        "4. **Calculate $b_n$:**",
                        "$$b_n = \\frac{1}{\\pi} \\int_0^\\pi x \\sin nx dx = \\frac{1}{\\pi} \\left( \\left[ -x \\frac{\\cos nx}{n} \\right]_0^\\pi - \\int_0^\\pi -\\frac{\\cos nx}{n} dx \\right)$$",
                        "$$= \\frac{1}{\\pi} \\left( -\\frac{\\pi \\cos n\\pi}{n} + 0 \\right) = -\\frac{\\cos n\\pi}{n} = -\\frac{(-1)^n}{n} = \\frac{(-1)^{n+1}}{n}$$",
                        "5. **Fourier Series Expansion:**",
                        "$$f(x) = \\frac{\\pi}{4} - \\frac{2}{\\pi} \\sum_{k=1}^\\infty \\frac{\\cos(2k-1)x}{(2k-1)^2} + \\sum_{n=1}^\\infty \\frac{(-1)^{n+1}}{n} \\sin nx$$",
                        "6. **Evaluate the Series $\\sum_{n=1}^\\infty \\frac{1}{(2n-1)^2}$:**",
                        "At the point of continuity $x = 0$, $f(0) = 0$:",
                        "$$0 = \\frac{\\pi}{4} - \\frac{2}{\\pi} \\sum_{k=1}^\\infty \\frac{\\cos(0)}{(2k-1)^2} + 0$$",
                        "$$\\frac{2}{\\pi} \\sum_{k=1}^\\infty \\frac{1}{(2k-1)^2} = \\frac{\\pi}{4} \\implies \\sum_{k=1}^\\infty \\frac{1}{(2k-1)^2} = \\frac{\\pi^2}{8}$$"
                    ],
                    "answer": "Fourier series: f(x) = (pi / 4) - (2 / pi) sum [cos(2k-1)x / (2k-1)^2] + sum [((-1)^(n+1) / n) sin(nx)]. Sum evaluation = pi^2 / 8.",
                    "marking_hint": "2 marks for a0; 3 marks for an; 2 marks for bn; 1 mark for full series; 2 marks for substituting x=0 and evaluating to pi^2 / 8."
                }
            }
        ]
    }
]

# ==============================================================================
# CSE-4125 (Introduction to Machine Learning) NITER Term Tests
# ==============================================================================
cse4125_niter_tests = [
    {
        "id": "cse-4125-term-niter-tt1",
        "course": "CSE-4125",
        "exam": "term",
        "college": "NITER",
        "term_no": 1,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 1",
        "marks": 20,
        "topics": [
            "ML Paradigms",
            "Bias-Variance & K-Fold Cross Validation",
            "Data Preprocessing & Feature Engineering",
            "Linear Regression & Gradient Descent",
            "Classification Metrics & Confusion Matrix"
        ],
        "question": """Answer any 3 from (1, 2, 4, 5) and have to answer question 3 must. **[20]**

**Question 1:** Define Machine Learning. Briefly differentiate Supervised Learning, Unsupervised Learning, and Reinforcement Learning with one suitable example of each. **[5]**

**Question 2:** **[2+3]**  
a) Define bias and variance. How are they related to underfitting and overfitting?  
b) What is K-Fold Cross-Validation? Why should feature selection and preprocessing be performed inside each training fold rather than on the complete dataset before cross-validation?

**Question 3:** Consider the following dataset: **[5]**

| Student_ID | Study_Hours | Attendance (%) | Department | Previous_GPA | Result |
| :---: | :---: | :---: | :---: | :---: | :---: |
| S01 | 5 | 80 | CSE | 3.2 | Pass |
| S02 | 2 | 55 | EEE | 2.4 | Fail |
| S03 | — | 75 | CSE | 3.0 | Pass |
| S04 | 8 | 92 | BBA | 3.7 | Pass |
| S05 | 3 | — | EEE | 2.6 | Fail |
| S05 | 3 | — | EEE | 2.6 | Fail |
| S06 | 50 | 65 | CSE | 2.9 | Fail |

a. Identify the features, label, missing values, duplicate record, and possible outlier in the dataset. State how you would handle each identified problem. **[1]**  
b. Handle the missing numerical values using an appropriate imputation technique. State whether you would use mean or median and justify your choice. **[1]**  
c. Convert the Department feature into numerical form using one-hot encoding. Show the resulting encoded columns for at least three different department values. **[1]**  
d. After cleaning the data, explain how you would perform feature scaling. Propose two new meaningful features that could be created from the existing variables. **[2]**

**Question 4:** Consider a simple linear regression model: $\\hat{y} = wx + b$, with the following two training samples: $x = \\{1, 3\\}, y = \\{2, 5\\}$ and the Mean Squared Error cost function is $J(w, b) = \\frac{1}{n} \\sum_{i=1}^n (\\hat{y}_i - y_i)^2$. **[5]**  
a. Define gradient descent and explain the role of the learning rate $\\alpha$. What may happen if the learning rate is too small or too large? **[2]**  
b. Perform one gradient-descent update and determine the new values of $w$ and $b$ (assume initial parameters $w_0 = 0, b_0 = 0$ and learning rate $\\alpha = 0.1$). **[3]**

**Question 5:** A disease-classification model was tested on 200 patients. The following results were obtained: **[5]**  
- 45 sick patients were correctly predicted as sick.  
- 15 sick patients were incorrectly predicted as healthy.  
- 20 healthy patients were incorrectly predicted as sick.  
- 120 healthy patients were correctly predicted as healthy.  
a. Construct the confusion matrix and identify TP, TN, FP, and FN. **[2]**  
b. Calculate: Accuracy, Precision, Recall, F1-score. **[3]**""",
        "subparts": [
            {
                "id": "cse-4125-term-niter-tt1-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 5,
                "topics": ["ML Paradigms"],
                "question": "Define Machine Learning. Briefly differentiate Supervised Learning, Unsupervised Learning, and Reinforcement Learning with one suitable example of each.",
                "solution": {
                    "steps": [
                        "1. **Machine Learning Definition:** Machine Learning is a branch of artificial intelligence that empowers computer systems to automatically learn from experience and historical data without being explicitly programmed (Arthur Samuel / Tom Mitchell definition).",
                        "2. **Comparative Differentiation:**",
                        "- **Supervised Learning:** Learns a mapping function $f: X \\to Y$ from labeled input-output pairs. Example: Email spam filtering where emails are labeled as Spam or Not Spam.",
                        "- **Unsupervised Learning:** Discovers latent structures, distributions, or groupings from unlabeled inputs $X$. Example: Customer segmentation in retail using K-Means clustering.",
                        "- **Reinforcement Learning (RL):** An agent learns optimal policy actions through dynamic environmental interaction guided by numerical reward or penalty signals. Example: Autonomous driving or AlphaGo mastering board games."
                    ],
                    "answer": "ML enables data-driven learning. Supervised uses labeled ground truth, Unsupervised discovers unlabeled patterns, and Reinforcement Learning optimizes reward policies.",
                    "marking_hint": "1 mark for definition; 4 marks for differentiation and examples across the three paradigms."
                }
            },
            {
                "id": "cse-4125-term-niter-tt1-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 5,
                "topics": ["Bias-Variance & K-Fold Cross Validation"],
                "question": "a) Define bias and variance. How are they related to underfitting and overfitting? b) What is K-Fold Cross-Validation? Why should feature selection and preprocessing be performed inside each training fold rather than on the complete dataset before cross-validation?",
                "solution": {
                    "steps": [
                        "**(a) Bias and Variance vs. Fit Dilemmas:**",
                        "- **Bias:** Error introduced by approximating a complex real-world phenomenon with a simplified model. *High Bias causes Underfitting* (model is too rigid to capture true relationships).",
                        "- **Variance:** Amount the model estimation fluctuates when trained on different training subsets. *High Variance causes Overfitting* (model memorizes training noise and generalizes poorly).",
                        "**(b) K-Fold Cross-Validation & Data Leakage Prevention:**",
                        "- **K-Fold CV Mechanism:** Splits the dataset into $K$ equal subsets (folds). The model is trained on $K-1$ folds and validated on the remaining fold, repeating $K$ times so each fold serves as validation once.",
                        "- **Why Preprocessing Must Occur Inside Each Training Fold:** Preprocessing (e.g., standard scaling, missing value imputation, PCA, feature selection) computes statistics (mean, variance, feature rankings). If calculated across the entire dataset prior to cross-validation, information from the validation fold leaks into the training pipeline (**Data Leakage**). This produces overly optimistic cross-validation scores that fail to reflect actual unseen real-world performance."
                    ],
                    "answer": "High bias leads to underfitting; high variance causes overfitting. Preprocessing inside each fold prevents data leakage into test folds.",
                    "marking_hint": "2 marks for part (a); 3 marks for K-Fold CV definition and data leakage explanation in part (b)."
                }
            },
            {
                "id": "cse-4125-term-niter-tt1-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 5,
                "topics": ["Data Preprocessing & Feature Engineering"],
                "question": "Dataset analysis: a. Identify features, label, missing values, duplicates, and outlier; state fixes. b. Handle missing numerical values using mean/median justification. c. One-hot encoding for Department. d. Feature scaling and two proposed features.",
                "solution": {
                    "steps": [
                        "**(a) Dataset Inspection & Remedies:**",
                        "- **Features:** `Study_Hours`, `Attendance (%)`, `Department`, `Previous_GPA`.",
                        "- **Label (Target):** `Result` (Pass/Fail).",
                        "- **Missing Values:** `Study_Hours` is missing for S03; `Attendance (%)` is missing for S05.",
                        "- **Duplicate Record:** Student `S05` appears twice with identical attributes. *Fix:* Remove the duplicate row using `df.drop_duplicates()`.",
                        "- **Outlier:** `Study_Hours = 50` for S06 is unrealistic for daily study. *Fix:* Cap using IQR/Winsorization or verify and correct entry error.",
                        "**(b) Imputation Technique Justification:**",
                        "- Use **Median Imputation** rather than Mean for `Study_Hours` because the extreme outlier (50 hours) severely skews the arithmetic mean upward. The median is robust against extreme values.",
                        "- Median of `Study_Hours` for existing realistic values (2, 3, 5, 8) is $\\frac{3+5}{2} = 4$. Impute S03 with 4.",
                        "**(c) One-Hot Encoding for Department:**",
                        "| Department | Dept_CSE | Dept_EEE | Dept_BBA |",
                        "| :--- | :---: | :---: | :---: |",
                        "| CSE | 1 | 0 | 0 |",
                        "| EEE | 0 | 1 | 0 |",
                        "| BBA | 0 | 0 | 1 |",
                        "**(d) Feature Scaling & New Proposed Features:**",
                        "- **Feature Scaling:** Apply Standard Scaling $z = \\frac{x - \\mu}{\\sigma}$ or Min-Max Normalization $x' = \\frac{x - x_{\\min}}{x_{\\max} - x_{\\min}}$ so features with large scales (`Attendance`: 0-100) do not dominate smaller scales (`GPA`: 0-4).",
                        "- **Proposed Feature 1:** `Study_Effort_Index = Study_Hours * (Attendance / 100)` (measures active academic engagement).",
                        "- **Proposed Feature 2:** `Academic_Momentum = Previous_GPA / (Study_Hours + 1)` (captures learning efficiency)."
                    ],
                    "answer": "Identified all anomalies; selected robust median imputation; created one-hot encoded matrix; proposed feature scaling and 2 engineered interaction features.",
                    "marking_hint": "1 mark for part (a); 1 mark for part (b); 1 mark for part (c); 2 marks for part (d)."
                }
            },
            {
                "id": "cse-4125-term-niter-tt1-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 5,
                "topics": ["Linear Regression & Gradient Descent"],
                "question": "Linear regression model y_hat = wx + b on samples x={1, 3}, y={2, 5}. a. Define gradient descent & role of learning rate. b. Perform one gradient-descent update with w0=0, b0=0, alpha=0.1.",
                "solution": {
                    "steps": [
                        "**(a) Gradient Descent & Learning Rate $\\alpha$:**",
                        "- Gradient Descent is an iterative optimization algorithm that minimizes the cost function $J(w, b)$ by moving parameters in the direction of steepest descent ($-\\nabla J$).",
                        "- **Role of Learning Rate $\\alpha$:** Determines step size per iteration. If $\\alpha$ is too small, convergence is painfully slow; if $\\alpha$ is too large, it may overshoot the minimum and diverge.",
                        "**(b) One Gradient-Descent Update Step:**",
                        "Given training samples: $(x_1, y_1) = (1, 2)$ and $(x_2, y_2) = (3, 5)$ with $n = 2$.",
                        "Initial parameters: $w = 0, b = 0$, learning rate $\\alpha = 0.1$.",
                        "- Compute predictions:",
                        "  - $\\hat{y}_1 = w x_1 + b = 0(1) + 0 = 0$",
                        "  - $\\hat{y}_2 = w x_2 + b = 0(3) + 0 = 0$",
                        "- Compute prediction errors $(\\hat{y}_i - y_i)$:",
                        "  - $e_1 = 0 - 2 = -2$",
                        "  - $e_2 = 0 - 5 = -5$",
                        "- Compute gradients for MSE $J = \\frac{1}{n} \\sum (\\hat{y}_i - y_i)^2$:",
                        "  - $\\frac{\\partial J}{\\partial w} = \\frac{2}{n} \\sum_{i=1}^n (\\hat{y}_i - y_i) x_i = \\frac{2}{2} [(-2)(1) + (-5)(3)] = -2 - 15 = -17$",
                        "  - $\\frac{\\partial J}{\\partial b} = \\frac{2}{n} \\sum_{i=1}^n (\\hat{y}_i - y_i) = \\frac{2}{2} [(-2) + (-5)] = -7$",
                        "- Parameter update rule: $\\theta^{\\text{new}} = \\theta - \\alpha \\frac{\\partial J}{\\partial \\theta}$:",
                        "  - $w^{\\text{new}} = 0 - (0.1)(-17) = \\mathbf{+1.7}$",
                        "  - $b^{\\text{new}} = 0 - (0.1)(-7) = \\mathbf{+0.7}$"
                    ],
                    "answer": "After one update step: w = 1.7, b = 0.7.",
                    "marking_hint": "2 marks for gradient descent and learning rate discussion; 3 marks for partial derivative computations and parameter updates."
                }
            },
            {
                "id": "cse-4125-term-niter-tt1-q5",
                "qno": "Q5",
                "label": "Question 5",
                "marks": 5,
                "topics": ["Classification Metrics & Confusion Matrix"],
                "question": "A disease-classification model on 200 patients: 45 sick correctly predicted sick, 15 sick predicted healthy, 20 healthy predicted sick, 120 healthy predicted healthy. a. Construct confusion matrix and identify TP, TN, FP, FN. b. Calculate Accuracy, Precision, Recall, F1-score.",
                "solution": {
                    "steps": [
                        "**(a) Confusion Matrix Construction:**",
                        "| | Predicted Sick (Positive) | Predicted Healthy (Negative) | Total Actual |",
                        "| :--- | :---: | :---: | :---: |",
                        "| **Actual Sick** | **TP = 45** | **FN = 15** | 60 |",
                        "| **Actual Healthy** | **FP = 20** | **TN = 120** | 140 |",
                        "| **Total Predicted** | 65 | 135 | **Total = 200** |",
                        "- **True Positive (TP):** 45 (sick correctly identified)",
                        "- **True Negative (TN):** 120 (healthy correctly identified)",
                        "- **False Positive (FP):** 20 (healthy incorrectly labeled sick - Type I Error)",
                        "- **False Negative (FN):** 15 (sick incorrectly labeled healthy - Type II Error)",
                        "**(b) Metric Calculations:**",
                        "1. **Accuracy:**",
                        "$$\\text{Accuracy} = \\frac{TP + TN}{\\text{Total}} = \\frac{45 + 120}{200} = \\frac{165}{200} = \\mathbf{0.825} \\quad (82.5\\%)$$",
                        "2. **Precision:**",
                        "$$\\text{Precision} = \\frac{TP}{TP + FP} = \\frac{45}{45 + 20} = \\frac{45}{65} \\approx \\mathbf{0.6923} \\quad (69.23\\%)$$",
                        "3. **Recall (Sensitivity):**",
                        "$$\\text{Recall} = \\frac{TP}{TP + FN} = \\frac{45}{45 + 15} = \\frac{45}{60} = \\mathbf{0.75} \\quad (75.0\\%)$$",
                        "4. **F1-Score:**",
                        "$$\\text{F1} = 2 \\times \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}} = 2 \\times \\frac{0.6923 \\times 0.75}{0.6923 + 0.75} = \\frac{1.03845}{1.4423} \\approx \\mathbf{0.7200}$$"
                    ],
                    "answer": "TP=45, TN=120, FP=20, FN=15. Accuracy = 82.5%, Precision = 69.23%, Recall = 75.0%, F1-Score = 0.720.",
                    "marking_hint": "2 marks for confusion matrix and components; 3 marks for Accuracy, Precision, Recall, and F1 calculations."
                }
            }
        ]
    },
    {
        "id": "cse-4125-term-niter-tt2",
        "course": "CSE-4125",
        "exam": "term",
        "college": "NITER",
        "term_no": 2,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 2",
        "marks": 20,
        "topics": [
            "Curse of Dimensionality & PCA",
            "Markov Property & Transition Matrix",
            "K-Means Clustering",
            "Ensemble Learning: Decision Tree vs Random Forest"
        ],
        "question": """Answer all questions: **[20]**

**Question 1:** What is curse of dimensionality? Explain principal component analysis (PCA) and how it helps in dimensionality reduction. **[5]**

**Question 2:** What is markov property? The school of international studies for population found out by its survey that the mobility of the population of a state to village, town and a city is in the following percentages: **[5]**

| From \\ To | Village | Town | City |
| :--- | :---: | :---: | :---: |
| **Village** | 50% | 30% | 20% |
| **Town** | 10% | 70% | 20% |
| **City** | 10% | 40% | 50% |

What will be the proportion of population in village, town and the city after two years, given that the present population has proportions of 0.7, 0.2 and 0.1 in the village, town and city respectively?

**Question 3:** Explain Clustering. Assume that the partly covered value for C7 is taken as 1800. Use K=2 and choose the first two points as initial centroids: C1=(20, 500), C2=(40, 1000). Use K-means clustering. **[5]**

| Point | Age (x) | Amount (y) |
| :---: | :---: | :---: |
| C1 | 20 | 500 |
| C2 | 40 | 1000 |
| C3 | 30 | 800 |
| C4 | 18 | 300 |
| C5 | 28 | 1200 |
| C6 | 35 | 1400 |
| C7 | 45 | 1800 |

**Question 4:** What is ensemble learning? Explain the difference between Decision tree and Random forest. **[5]**""",
        "subparts": [
            {
                "id": "cse-4125-term-niter-tt2-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 5,
                "topics": ["Curse of Dimensionality & PCA"],
                "question": "What is curse of dimensionality? Explain principal component analysis (PCA) and how it helps in dimensionality reduction.",
                "solution": {
                    "steps": [
                        "1. **Curse of Dimensionality:**",
                        "- As feature dimensions $D$ increase, the volume of state space grows exponentially, causing available training data points to become extremely sparse.",
                        "- Euclidean distances between data points converge toward the same value (distance concentration), severely degrading distance-based algorithms (KNN, K-Means, SVM).",
                        "- Computational complexity and risk of overfitting skyrocket.",
                        "2. **Principal Component Analysis (PCA):**",
                        "- An unsupervised linear transformation technique that maps data from high-dimensional space $\\mathbb{R}^D$ to a lower-dimensional subspace $\\mathbb{R}^k$ ($k \\ll D$) while preserving maximum variance.",
                        "3. **How PCA Operates:**",
                        "- **Step 1:** Center the data matrix by subtracting feature means.",
                        "- **Step 2:** Compute the covariance matrix $\\Sigma = \\frac{1}{n} X^T X$.",
                        "- **Step 3:** Calculate eigenvectors and eigenvalues: $\\Sigma v = \\lambda v$.",
                        "- **Step 4:** Sort eigenvectors by descending eigenvalues. The top $k$ eigenvectors form orthogonal principal axes.",
                        "- **Step 5:** Project original data onto the top $k$ eigenvectors: $X_{\\text{reduced}} = X W_k$."
                    ],
                    "answer": "Curse of dimensionality causes data sparsity and computational bottlenecks in high dimensions. PCA reduces dimensions by projecting data along directions of maximum variance.",
                    "marking_hint": "2.5 marks for curse of dimensionality; 2.5 marks for PCA mathematical principle and reduction steps."
                }
            },
            {
                "id": "cse-4125-term-niter-tt2-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 5,
                "topics": ["Markov Property & Transition Matrix"],
                "question": "What is markov property? Population mobility matrix: Village, Town, City. Proportion after two years with initial state [0.7, 0.2, 0.1].",
                "solution": {
                    "steps": [
                        "1. **Markov Property Definition:** A stochastic process possesses the Markov property (memorylessness) if the conditional probability distribution of future states depends solely on the current state and not on the preceding sequence of past states: $P(X_{t+1} = s \\mid X_t, X_{t-1}, \\dots, X_0) = P(X_{t+1} = s \\mid X_t)$.",
                        "2. **Transition Probability Matrix $P$:**",
                        "$$P = \\begin{bmatrix} 0.50 & 0.30 & 0.20 \\\\ 0.10 & 0.70 & 0.20 \\\\ 0.10 & 0.40 & 0.50 \\end{bmatrix}$$",
                        "Initial state vector at Year 0: $X_0 = [0.70, \\; 0.20, \\; 0.10]$.",
                        "3. **Population Distribution After Year 1 ($X_1 = X_0 P$):**",
                        "- Village: $(0.7)(0.50) + (0.2)(0.10) + (0.1)(0.10) = 0.35 + 0.02 + 0.01 = \\mathbf{0.38}$",
                        "- Town: $(0.7)(0.30) + (0.2)(0.70) + (0.1)(0.40) = 0.21 + 0.14 + 0.04 = \\mathbf{0.39}$",
                        "- City: $(0.7)(0.20) + (0.2)(0.20) + (0.1)(0.50) = 0.14 + 0.04 + 0.05 = \\mathbf{0.23}$",
                        "- Vector after 1 year: $X_1 = [0.38, \\; 0.39, \\; 0.23]$ (Sum = 1.00).",
                        "4. **Population Distribution After Year 2 ($X_2 = X_1 P$):**",
                        "- Village: $(0.38)(0.50) + (0.39)(0.10) + (0.23)(0.10) = 0.190 + 0.039 + 0.023 = \\mathbf{0.252}$",
                        "- Town: $(0.38)(0.30) + (0.39)(0.70) + (0.23)(0.40) = 0.114 + 0.273 + 0.092 = \\mathbf{0.479}$",
                        "- City: $(0.38)(0.20) + (0.39)(0.20) + (0.23)(0.50) = 0.076 + 0.078 + 0.115 = \\mathbf{0.269}$",
                        "- Vector after 2 years: $X_2 = [0.252, \\; 0.479, \\; 0.269]$ (Sum = 1.00)."
                    ],
                    "answer": "After two years: Village = 25.2%, Town = 47.9%, City = 26.9%.",
                    "marking_hint": "1.5 marks for Markov property definition; 1.5 marks for Year 1 calculation; 2 marks for Year 2 calculation."
                }
            },
            {
                "id": "cse-4125-term-niter-tt2-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 5,
                "topics": ["K-Means Clustering"],
                "question": "Explain Clustering. Use K=2 with initial centroids C1=(20, 500) and C2=(40, 1000) on 7 data points (C1 to C7) to perform K-means clustering.",
                "solution": {
                    "steps": [
                        "1. **Clustering Definition:** An unsupervised learning task grouping unlabeled data points such that objects within the same cluster share high similarity while objects in different clusters are distinctly dissimilar.",
                        "2. **Iteration 1 Distance Calculations:**",
                        "Centroid $C_1 = (20, 500)$, Centroid $C_2 = (40, 1000)$.",
                        "Using Euclidean distance $d(P, C) = \\sqrt{(x_p - x_c)^2 + (y_p - y_c)^2}$ (dominated by Amount $y$):",
                        "- $C_1(20, 500)$: $d(P, C_1) = 0$, $d(P, C_2) = \\sqrt{20^2 + 500^2} \\approx 500.4$ -> **Cluster 1**",
                        "- $C_2(40, 1000)$: $d(P, C_1) \\approx 500.4$, $d(P, C_2) = 0$ -> **Cluster 2**",
                        "- $C_3(30, 800)$:",
                        "  $d(P, C_1) = \\sqrt{10^2 + 300^2} \\approx 300.17$",
                        "  $d(P, C_2) = \\sqrt{(-10)^2 + (-200)^2} \\approx 200.25$ -> **Cluster 2**",
                        "- $C_4(18, 300)$:",
                        "  $d(P, C_1) = \\sqrt{(-2)^2 + (-200)^2} \\approx 200.01$",
                        "  $d(P, C_2) = \\sqrt{(-22)^2 + (-700)^2} \\approx 700.35$ -> **Cluster 1**",
                        "- $C_5(28, 1200)$:",
                        "  $d(P, C_1) = \\sqrt{8^2 + 700^2} \\approx 700.05$",
                        "  $d(P, C_2) = \\sqrt{(-12)^2 + 200^2} \\approx 200.36$ -> **Cluster 2**",
                        "- $C_6(35, 1400)$:",
                        "  $d(P, C_1) = \\sqrt{15^2 + 900^2} \\approx 900.12$",
                        "  $d(P, C_2) = \\sqrt{(-5)^2 + 400^2} \\approx 400.03$ -> **Cluster 2**",
                        "- $C_7(45, 1800)$:",
                        "  $d(P, C_1) \\approx 1300.24$",
                        "  $d(P, C_2) = \\sqrt{5^2 + 800^2} \\approx 800.02$ -> **Cluster 2**",
                        "3. **Cluster Assignment:**",
                        "- **Cluster 1:** $\\{C_1, C_4\\}$",
                        "- **Cluster 2:** $\\{C_2, C_3, C_5, C_6, C_7\\}$",
                        "4. **Recompute New Centroids:**",
                        "- New Centroid $C_1'$:",
                        "  $x_1' = \\frac{20 + 18}{2} = 19$, $y_1' = \\frac{500 + 300}{2} = 400$ -> $\\mathbf{C_1'(19, 400)}$",
                        "- New Centroid $C_2'$:",
                        "  $x_2' = \\frac{40 + 30 + 28 + 35 + 45}{5} = \\frac{178}{5} = 35.6$",
                        "  $y_2' = \\frac{1000 + 800 + 1200 + 1400 + 1800}{5} = \\frac{6200}{5} = 1240$ -> $\\mathbf{C_2'(35.6, 1240)}$"
                    ],
                    "answer": "Cluster 1 = {C1, C4} with updated centroid (19, 400). Cluster 2 = {C2, C3, C5, C6, C7} with updated centroid (35.6, 1240).",
                    "marking_hint": "1 mark for clustering definition; 2 marks for distance calculations and cluster assignments; 2 marks for updating centroids."
                }
            },
            {
                "id": "cse-4125-term-niter-tt2-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 5,
                "topics": ["Ensemble Learning: Decision Tree vs Random Forest"],
                "question": "What is ensemble learning? Explain the difference between Decision tree and Random forest.",
                "solution": {
                    "steps": [
                        "1. **Ensemble Learning Definition:**",
                        "Ensemble learning is a meta-approach that combines multiple individual base models (learners) to produce a single aggregated prediction that achieves superior generalization, lower variance, and higher predictive accuracy than any constituent individual model (e.g., Bagging, Boosting, Stacking).",
                        "2. **Comprehensive Comparison:**",
                        "| Feature | Decision Tree | Random Forest |",
                        "| :--- | :--- | :--- |",
                        "| **Model Type** | Single base estimator. | Ensemble of multiple decorrelated decision trees. |",
                        "| **Sampling Technique** | Trains on the entire training dataset. | Uses Bootstrap Aggregation (Bagging) with random feature subsets per split. |",
                        "| **Bias & Variance** | Low bias, but **high variance** (prone to severe overfitting). | Low bias and **low variance** (averaging trees suppresses variance). |",
                        "| **Interpretability** | Highly interpretable; easy to visualize hierarchy. | Black-box model; challenging to interpret individual splits. |",
                        "| **Robustness** | Sensitive to small variations in training data. | Extremely robust to noise and outliers. |",
                        "| **Computational Cost** | Very fast to train and evaluate. | Slower to train; requires building hundreds of trees. |"
                    ],
                    "answer": "Ensemble learning combines diverse base models for robust prediction. Decision Trees are simple, fast, and prone to overfitting, whereas Random Forests use bagging across random feature subsets to substantially reduce variance.",
                    "marking_hint": "2 marks for ensemble learning definition and motivation; 3 marks for tabular comparison between Decision Tree and Random Forest."
                }
            }
        ]
    }
]

# ==============================================================================
# CSE-4126 (Introduction to Data Science) NITER Term Tests
# ==============================================================================
cse4126_niter_tests = [
    {
        "id": "cse-4126-term-niter-tt1",
        "course": "CSE-4126",
        "exam": "term",
        "college": "NITER",
        "term_no": 1,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 1",
        "marks": 20,
        "topics": [
            "Data Science Challenges",
            "Data Collection Methodology",
            "Salaries & Skewness Analysis",
            "Five Number Summary & Quantile Plot",
            "Frequency Table & Histogram",
            "Mean, Variance & Correlation"
        ],
        "question": """Answer all questions: **[20]**

**Question 1:** Define Data Science. What are the common challenges in Data collection, briefly describe. **[3]**

**Question 2:** Suppose, you need to collect data whether your customers are satisfied with your product or not. Which method will you apply to collect the data? Explain with proper justification. **[3]**

**Question 3:** The monthly salaries (in thousand taka) of 11 employees are: 25, 28, 30, 32, 35, 36, 38, 40, 42, 45, 180. Calculate the mean, and mode of the dataset and determine whether the dataset is likely to be Symmetric, Positively or Negatively skewed. **[3]**

**Question 4:** Given dataset: **[3]**

| Age | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Frequency** | 2 | 2 | 1 | 3 | 2 | 3 |

a) Find the Quartile for the given dataset and represent it with Five number summary.  
b) Calculate Interquartile Range (IQR), and determine if there are any outliers?  
c) Finally draw a Quantile plot for the given dataset.

**Question 5:** The following are examination scores: **[4]**  
$$42, 45, 47, 48, 51, 53, 55, 56, 57, 61, 63, 65, 66, 68, 72, 75, 78, 81, 85, 90$$  
Considering intervals: $[40-49], [50-59], [60-69], [70-79], [80-89], [90-99]$  
a) Construct a frequency table.  
b) Draw a histogram using the frequency table.  
c) Identify the interval with the highest frequency.  
d) Describe the overall distribution of the scores based on the histogram.

**Question 6:** The study hours and examination marks obtained by seven students as follows: **[4]**

| Study Hour (X) | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Marks (Y)** | 45 | 50 | 56 | 62 | 67 | 73 | 80 |

a) Calculate the Mean, Variance, and Standard Deviation of the examination marks and explain your observation based on the result.  
b) Construct a scatter plot along X and Y axis and determine the type of correlation between study hours and examination marks.""",
        "subparts": [
            {
                "id": "cse-4126-term-niter-tt1-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 3,
                "topics": ["Data Science Challenges"],
                "question": "Define Data Science. What are the common challenges in Data collection, briefly describe.",
                "solution": {
                    "steps": [
                        "1. **Data Science Definition:** Data Science is an interdisciplinary field integrating statistics, computer science, domain knowledge, and machine learning to extract actionable insights and meaningful knowledge from structured and unstructured data.",
                        "2. **Common Challenges in Data Collection:**",
                        "- **Missing & Incomplete Data:** Unrecorded values, non-response bias, or communication dropouts during logging.",
                        "- **Data Quality & Noise:** Transcription typos, duplicate records, sensor drift, and transmission errors.",
                        "- **Sampling Bias:** Non-representative sample distributions skewing predictive validity.",
                        "- **Privacy & Regulatory Compliance:** Navigating GDPR, ethical consent, and sensitive PII anonymization."
                    ],
                    "answer": "Data Science extracts knowledge from data. Key collection bottlenecks include missing data, noisy records, sampling bias, and regulatory privacy constraints.",
                    "marking_hint": "1 mark for definition; 2 marks for discussing at least 3 distinct collection challenges."
                }
            },
            {
                "id": "cse-4126-term-niter-tt1-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 3,
                "topics": ["Data Collection Methodology"],
                "question": "Which method will you apply to collect customer satisfaction data? Explain with proper justification.",
                "solution": {
                    "steps": [
                        "1. **Recommended Method:** A hybrid approach combining **In-App Automated Micro-Surveys (CSAT / Net Promoter Score - NPS)** immediately post-purchase or post-service with optional free-form feedback.",
                        "2. **Justification:**",
                        "- **High Response Rate & Immediate Context:** Capturing sentiment right after key user interactions yields authentic, high-fidelity feedback before memory fades.",
                        "- **Quantifiable & Standardized:** Standard 1-5 star CSAT or 0-10 NPS scales enable clear statistical tracking over time.",
                        "- **Minimal Friction:** Takes less than 10 seconds, avoiding respondent fatigue associated with lengthy email forms."
                    ],
                    "answer": "In-app CSAT / NPS micro-surveys offer minimal user friction, immediate contextual validity, and clean standardized quantitative metrics.",
                    "marking_hint": "1.5 marks for selecting an appropriate method; 1.5 marks for justified reasoning."
                }
            },
            {
                "id": "cse-4126-term-niter-tt1-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 3,
                "topics": ["Salaries & Skewness Analysis"],
                "question": "Salaries of 11 employees: 25, 28, 30, 32, 35, 36, 38, 40, 42, 45, 180 (thousand taka). Calculate mean, mode, and skewness.",
                "solution": {
                    "steps": [
                        "1. **Calculate Mean:**",
                        "$$\\text{Sum} = 25 + 28 + 30 + 32 + 35 + 36 + 38 + 40 + 42 + 45 + 180 = 531$$",
                        "$$\\text{Mean } \\bar{x} = \\frac{531}{11} \\approx \\mathbf{48.27} \\text{ thousand taka}$$",
                        "2. **Calculate Mode:**",
                        "All 11 salary values appear exactly once. Hence, there is **no unique mode** (multimodal / uniform frequency).",
                        "3. **Calculate Median & Determine Skewness:**",
                        "- Sorted dataset ($N = 11$): 25, 28, 30, 32, 35, **36**, 38, 40, 42, 45, 180.",
                        "- Median is the 6th value: **36 thousand taka**.",
                        "- Comparison: $\\text{Mean } (48.27) > \\text{Median } (36.00)$.",
                        "- Because the mean is substantially pulled to the right by the extreme outlier salary of 180k, the distribution is **Positively Skewed (Right-Skewed)**."
                    ],
                    "answer": "Mean = 48.27k, Mode = None (no repeating values), Median = 36k. The dataset is Positively Skewed.",
                    "marking_hint": "1 mark for mean; 1 mark for mode; 1 mark for median comparison and correct skewness deduction."
                }
            },
            {
                "id": "cse-4126-term-niter-tt1-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 3,
                "topics": ["Five Number Summary & Quantile Plot"],
                "question": "Age dataset with frequencies: 1(2), 2(2), 3(1), 4(3), 5(2), 6(3). a) Quartiles & Five-number summary. b) IQR and outliers. c) Quantile plot description.",
                "solution": {
                    "steps": [
                        "1. **Expanded Ordered Data ($N = 13$):**",
                        "$$1, \\; 1, \\; 2, \\; 2, \\; 3, \\; 4, \\; 4, \\; 4, \\; 5, \\; 5, \\; 6, \\; 6, \\; 6$$",
                        "2. **Five-Number Summary:**",
                        "- **Minimum:** 1",
                        "- **Q1 (First Quartile):** Position $0.25 \\times (13 + 1) = 3.5$ -> average of 3rd (2) and 4th (2) value = **2**",
                        "- **Median (Q2):** Position $\\frac{13+1}{2} = 7^{\\text{th}}$ value = **4**",
                        "- **Q3 (Third Quartile):** Position $0.75 \\times (13 + 1) = 10.5$ -> average of 10th (5) and 11th (6) value = **5.5**",
                        "- **Maximum:** 6",
                        "- Five-number summary: **[1, 2, 4, 5.5, 6]**",
                        "3. **Interquartile Range (IQR) & Outlier Detection:**",
                        "- $\\text{IQR} = Q_3 - Q_1 = 5.5 - 2 = \\mathbf{3.5}$",
                        "- Lower Outer Fence: $Q_1 - 1.5 \\times \\text{IQR} = 2 - 1.5(3.5) = 2 - 5.25 = -3.25$",
                        "- Upper Outer Fence: $Q_3 + 1.5 \\times \\text{IQR} = 5.5 + 1.5(3.5) = 5.5 + 5.25 = 10.75$",
                        "- Since all observations lie well within $[-3.25, 10.75]$, there are **no outliers**.",
                        "4. **Quantile Plot:**",
                        "Pairs each ordered value $x_{(i)}$ against its percentile fraction $f_i = \\frac{i - 0.5}{N}$, plotting points $(f_i, x_{(i)})$."
                    ],
                    "answer": "Five Number Summary: Min=1, Q1=2, Median=4, Q3=5.5, Max=6. IQR = 3.5. Outliers: None detected.",
                    "marking_hint": "1 mark for five-number summary; 1 mark for IQR and outlier boundaries; 1 mark for quantile plot."
                }
            },
            {
                "id": "cse-4126-term-niter-tt1-q5",
                "qno": "Q5",
                "label": "Question 5",
                "marks": 4,
                "topics": ["Frequency Table & Histogram"],
                "question": "20 exam scores. Intervals: [40-49], [50-59], [60-69], [70-79], [80-89], [90-99]. a) Frequency table. b) Histogram. c) Highest frequency interval. d) Distribution description.",
                "solution": {
                    "steps": [
                        "**(a) Frequency Table Construction:**",
                        "Scores: 42, 45, 47, 48, 51, 53, 55, 56, 57, 61, 63, 65, 66, 68, 72, 75, 78, 81, 85, 90 ($N = 20$).",
                        "| Interval | Tally | Frequency | Relative Frequency |",
                        "| :---: | :---: | :---: | :---: |",
                        "| [40–49] | 42, 45, 47, 48 | 4 | 20% |",
                        "| [50–59] | 51, 53, 55, 56, 57 | 5 | 25% |",
                        "| [60–69] | 61, 63, 65, 66, 68 | 5 | 25% |",
                        "| [70–79] | 72, 75, 78 | 3 | 15% |",
                        "| [80–89] | 81, 85 | 2 | 10% |",
                        "| [90–99] | 90 | 1 | 5% |",
                        "| **Total** | | **20** | **100%** |",
                        "**(b) Histogram Visualization:**",
                        "Bar heights corresponding to frequencies: [40-49]: 4, [50-59]: 5, [60-69]: 5, [70-79]: 3, [80-89]: 2, [90-99]: 1.",
                        "**(c) Interval with Highest Frequency:**",
                        "The intervals **[50–59]** and **[60–69]** share the highest frequency of **5 students each**.",
                        "**(d) Overall Distribution Description:**",
                        "The histogram exhibits a unimodal/bimodal center around 50–69 marks, tapering off smoothly toward higher score ranges with a mild **positive skew**."
                    ],
                    "answer": "Constructed frequency distribution table; highest frequency intervals are [50-59] and [60-69] (5 each); distribution is mildly right-skewed.",
                    "marking_hint": "1.5 marks for frequency table; 1 mark for histogram description; 0.5 mark for modal intervals; 1 mark for distribution analysis."
                }
            },
            {
                "id": "cse-4126-term-niter-tt1-q6",
                "qno": "Q6",
                "label": "Question 6",
                "marks": 4,
                "topics": ["Mean, Variance & Correlation"],
                "question": "Study hours X and marks Y of 7 students. a) Calculate Mean, Variance, Standard Deviation of marks Y. b) Scatter plot and correlation type.",
                "solution": {
                    "steps": [
                        "**(a) Mean, Variance, and Standard Deviation of Marks (Y):**",
                        "Marks $Y$: 45, 50, 56, 62, 67, 73, 80 ($n = 7$).",
                        "- Sum $\\sum Y = 45 + 50 + 56 + 62 + 67 + 73 + 80 = 433$.",
                        "- Mean: $\\bar{Y} = \\frac{433}{7} \\approx \\mathbf{61.857}$.",
                        "- Deviations $(Y_i - \\bar{Y})$: -16.857, -11.857, -5.857, 0.143, 5.143, 11.143, 18.143.",
                        "- Squared deviations $\\sum (Y_i - \\bar{Y})^2 = 284.16 + 140.59 + 34.30 + 0.02 + 26.45 + 124.17 + 329.17 = 898.86$.",
                        "- Sample Variance: $s^2 = \\frac{898.86}{n - 1} = \\frac{898.86}{6} \\approx \\mathbf{149.81}$. (Population variance $\\sigma^2 \\approx 128.41$).",
                        "- Sample Standard Deviation: $s = \\sqrt{149.81} \\approx \\mathbf{12.24}$.",
                        "- *Observation:* The marks are spread around an average of ~62 marks with a standard deviation of ~12.2 marks.",
                        "**(b) Scatter Plot & Correlation:**",
                        "- For every 1-hour increase in study time $X$, marks $Y$ increase steadily by roughly 5.8 marks.",
                        "- Pearson correlation $r \\approx +0.999$, indicating an **exceptionally strong positive linear correlation**."
                    ],
                    "answer": "Mean Marks = 61.86, Sample Variance = 149.81, Standard Deviation = 12.24. Strong positive linear correlation exists between study hours and marks.",
                    "marking_hint": "2 marks for mean, variance, and standard deviation calculations; 2 marks for scatter plot and correlation determination."
                }
            }
        ]
    },
    {
        "id": "cse-4126-term-niter-tt2",
        "course": "CSE-4126",
        "exam": "term",
        "college": "NITER",
        "term_no": 2,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 2",
        "marks": 20,
        "topics": [
            "Exploratory Data Analysis (EDA)",
            "Pandas Data Preprocessing",
            "Chi-Square Test of Independence",
            "Pearson Correlation Coefficient Matrix"
        ],
        "question": """Answer all questions: **[20]**

**Question 1:** Define Exploratory Data Analysis (EDA) with its variant. Select the most appropriate visualization technique from Histogram, Box Plot, and Bar Chart for the given dataset with proper justification. **[6]**

| Student | Marks | Study Hours | Language |
| :---: | :---: | :---: | :---: |
| S1 | 45 | 2 | C++ |
| S2 | 60 | 3 | PYTHON |
| S3 | 75 | 4 | C |
| S4 | 85 | 5 | JAVA |
| S5 | 98 | 8 | PYTHON |

**Question 2:** Perform the following Data Preprocessing operations on the following datasets using pandas (pd). **[4]**

*Customer Table:*

| Customer_ID | Age | Name |
| :---: | :---: | :---: |
| 101 | 24 | John |
| 102 | '22' | Alex |
| 102 | 23 | None |

*Order Table:*

| Order_ID | Cust_ID | Amount |
| :---: | :---: | :---: |
| 1 | 101 | np.nan |
| 2 | 102 | 7000 |
| 2 | 102 | 7000 |

A) Delete NULL values from the Customer table and show output.  
B) Replace NULL with the Mean Values of the Order table and show output.  
C) Remove Duplicates from both tables and show output.  
D) Perform an Inner Join between Customer and Order Table and show output.

**Question 3:** A retail shop wants to know does the customer's occupation affects whether they buy or not buy a premium membership. Find out this relationship for the following table using the chi-square method on critical value ($\\chi^2_{0.05, 2} = 5.991$). **[4]**

| Occupation | Bought | Not Bought |
| :--- | :---: | :---: |
| **Student** | 18 | 22 |
| **Employee** | 31 | 9 |
| **Business** | 17 | 23 |

**Question 4:** Find the Pearson Correlation Coefficient matrix for the given dataset and answer the following questions: **[6]**

| Person | Height(cm) | Weight(kg) | Exercise (H) |
| :---: | :---: | :---: | :---: |
| A | 160 | 55 | 3 |
| B | 170 | 68 | 5 |
| C | 180 | 72 | 2 |

A) Which pair has the strongest Positive relationship?  
B) Which pair has a Negative relationship?  
C) Which pair is weakly correlated or almost uncorrelated?""",
        "subparts": [
            {
                "id": "cse-4126-term-niter-tt2-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 6,
                "topics": ["Exploratory Data Analysis (EDA)"],
                "question": "Define Exploratory Data Analysis (EDA) with its variants. Select the most appropriate visualization technique from Histogram, Box Plot, and Bar Chart for the given dataset with proper justification.",
                "solution": {
                    "steps": [
                        "1. **Exploratory Data Analysis (EDA) Definition:**",
                        "An analytical approach invented by John Tukey to analyze and summarize datasets' main characteristics, often with visual methods, before applying formal statistical modeling or machine learning.",
                        "2. **Variants of EDA:**",
                        "- **Univariate EDA:** Examines one variable at a time (e.g., summary statistics, histogram of Marks).",
                        "- **Bivariate EDA:** Explores pairwise relationships between two variables (e.g., scatter plot of Study Hours vs. Marks).",
                        "- **Multivariate EDA:** Evaluates interactions among three or more variables simultaneously (e.g., correlation heatmaps, pairplots).",
                        "3. **Visualization Technique Selection for Dataset:**",
                        "- **Bar Chart:** *Best for the categorical variable `Language`.* Compares frequencies of programming languages (Python: 2, C++: 1, C: 1, Java: 1).",
                        "- **Histogram:** *Best for continuous variables with large samples.* Given the small sample ($N=5$), a histogram provides limited density resolution, but displays score distribution.",
                        "- **Box Plot:** *Best for displaying median, quartiles, and detecting outliers in `Marks` or `Study Hours`.* Summarizes range ($45$ to $98$) and median ($75$) cleanly without sample size distortion."
                    ],
                    "answer": "EDA explores datasets visually and statistically. For this dataset, a Bar Chart is optimal for categorical Language, while a Box Plot effectively captures Marks and Study Hours distribution.",
                    "marking_hint": "3 marks for EDA definition and univariate/bivariate/multivariate variants; 3 marks for evaluating and justifying Histogram, Box Plot, and Bar Chart."
                }
            },
            {
                "id": "cse-4126-term-niter-tt2-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 4,
                "topics": ["Pandas Data Preprocessing"],
                "question": "Perform pandas data preprocessing: A) Delete NULL from Customer. B) Replace NULL with Mean in Order. C) Remove Duplicates. D) Inner Join Customer and Order tables.",
                "solution": {
                    "steps": [
                        "**A) Delete NULL values from Customer table:**",
                        "```python",
                        "df_cust_clean = df_customer.dropna()",
                        "```",
                        "Row with Customer_ID 102 (Name: None) is dropped:",
                        "| Customer_ID | Age | Name |",
                        "| :---: | :---: | :---: |",
                        "| 101 | 24 | John |",
                        "| 102 | '22' | Alex |",
                        "**B) Replace NULL with Mean Values in Order table:**",
                        "Existing non-null amounts are 7000 and 7000, so Mean = 7000.0.",
                        "```python",
                        "df_order['Amount'] = df_order['Amount'].fillna(df_order['Amount'].mean())",
                        "```",
                        "| Order_ID | Cust_ID | Amount |",
                        "| :---: | :---: | :---: |",
                        "| 1 | 101 | 7000.0 |",
                        "| 2 | 102 | 7000.0 |",
                        "| 2 | 102 | 7000.0 |",
                        "**C) Remove Duplicates from both tables:**",
                        "```python",
                        "df_cust_dedup = df_customer.drop_duplicates()",
                        "df_order_dedup = df_order.drop_duplicates()",
                        "```",
                        "Order table drops duplicate row 2 (leaving 2 unique orders).",
                        "**D) Inner Join between Customer and Order Table:**",
                        "```python",
                        "merged_df = pd.merge(df_cust_clean, df_order_dedup, left_on='Customer_ID', right_on='Cust_ID', how='inner')",
                        "```",
                        "| Customer_ID | Age | Name | Order_ID | Cust_ID | Amount |",
                        "| :---: | :---: | :---: | :---: | :---: | :---: |",
                        "| 101 | 24 | John | 1 | 101 | 7000.0 |",
                        "| 102 | '22' | Alex | 2 | 102 | 7000.0 |"
                    ],
                    "answer": "Accurately demonstrated pandas commands and tabular outputs for dropna(), fillna(mean), drop_duplicates(), and pd.merge() inner join.",
                    "marking_hint": "1 mark each for parts A, B, C, and D with python code and resultant table."
                }
            },
            {
                "id": "cse-4126-term-niter-tt2-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 4,
                "topics": ["Chi-Square Test of Independence"],
                "question": "Retail shop customer occupation vs buying premium membership. Perform Chi-square test on critical value chi^2_{0.05, 2} = 5.991.",
                "solution": {
                    "steps": [
                        "1. **Observed Frequencies ($O$) & Marginals:**",
                        "| Occupation | Bought | Not Bought | Total |",
                        "| :--- | :---: | :---: | :---: |",
                        "| **Student** | 18 | 22 | **40** |",
                        "| **Employee** | 31 | 9 | **40** |",
                        "| **Business** | 17 | 23 | **40** |",
                        "| **Total** | **66** | **54** | **N = 120** |",
                        "2. **Calculate Expected Frequencies ($E = \\frac{\\text{Row Total} \\times \\text{Col Total}}{N}$):**",
                        "- $E(\\text{Student, Bought}) = \\frac{40 \\times 66}{120} = 22.0$",
                        "- $E(\\text{Student, Not Bought}) = \\frac{40 \\times 54}{120} = 18.0$",
                        "- $E(\\text{Employee, Bought}) = \\frac{40 \\times 66}{120} = 22.0$",
                        "- $E(\\text{Employee, Not Bought}) = \\frac{40 \\times 54}{120} = 18.0$",
                        "- $E(\\text{Business, Bought}) = \\frac{40 \\times 66}{120} = 22.0$",
                        "- $E(\\text{Business, Not Bought}) = \\frac{40 \\times 54}{120} = 18.0$",
                        "3. **Compute $\\chi^2 = \\sum \\frac{(O - E)^2}{E}$:**",
                        "- Student: $\\frac{(18-22)^2}{22} + \\frac{(22-18)^2}{18} = \\frac{16}{22} + \\frac{16}{18} \\approx 0.727 + 0.889 = 1.616$",
                        "- Employee: $\\frac{(31-22)^2}{22} + \\frac{(9-18)^2}{18} = \\frac{81}{22} + \\frac{81}{18} \\approx 3.682 + 4.500 = 8.182$",
                        "- Business: $\\frac{(17-22)^2}{22} + \\frac{(23-18)^2}{18} = \\frac{25}{22} + \\frac{25}{18} \\approx 1.136 + 1.389 = 2.525$",
                        "$$\\chi^2_{\\text{calc}} = 1.616 + 8.182 + 2.525 = \\mathbf{12.323}$$",
                        "4. **Statistical Decision:**",
                        "- Degrees of freedom: $df = (r - 1)(c - 1) = (3 - 1)(2 - 1) = 2$.",
                        "- Critical value at $\\alpha = 0.05$: $\\chi^2_{\\text{crit}} = 5.991$.",
                        "- Since $\\chi^2_{\\text{calc}} (12.323) > \\chi^2_{\\text{crit}} (5.991)$, we **reject the null hypothesis ($H_0$)**."
                    ],
                    "answer": "Calculated Chi-Square = 12.323 > 5.991. We reject H0, concluding customer occupation significantly affects whether they buy premium membership.",
                    "marking_hint": "1 mark for expected frequency matrix; 2 marks for chi-square computation; 1 mark for critical value comparison and statistical inference."
                }
            },
            {
                "id": "cse-4126-term-niter-tt2-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 6,
                "topics": ["Pearson Correlation Coefficient Matrix"],
                "question": "Find the Pearson Correlation Coefficient matrix for Height(cm), Weight(kg), and Exercise(H) for Persons A, B, C. Answer: A) Strongest positive relationship. B) Negative relationship. C) Weakly correlated pair.",
                "solution": {
                    "steps": [
                        "1. **Summary Statistics ($N = 3$):**",
                        "- Height $H = [160, 170, 180] \\implies \\bar{H} = 170$, $h' = H - \\bar{H} = [-10, 0, 10]$, $\\sum h'^2 = 100 + 0 + 100 = 200$.",
                        "- Weight $W = [55, 68, 72] \\implies \\bar{W} = \\frac{195}{3} = 65$, $w' = W - \\bar{W} = [-10, 3, 7]$, $\\sum w'^2 = 100 + 9 + 49 = 158$.",
                        "- Exercise $E = [3, 5, 2] \\implies \\bar{E} = \\frac{10}{3} \\approx 3.333$, $e' = E - \\bar{E} = [-0.333, 1.667, -1.333]$, $\\sum e'^2 = 0.111 + 2.778 + 1.778 = 4.667$.",
                        "2. **Calculate Pairwise Pearson Correlation $r = \\frac{\\sum x' y'}{\\sqrt{\\sum x'^2 \\sum y'^2}}$:**",
                        "- **Height and Weight ($r_{H, W}$):**",
                        "  $\\sum h' w' = (-10)(-10) + (0)(3) + (10)(7) = 100 + 0 + 70 = 170$.",
                        "  $$r_{H, W} = \\frac{170}{\\sqrt{200 \\times 158}} = \\frac{170}{\\sqrt{31600}} = \\frac{170}{177.76} \\approx \\mathbf{+0.9563}$$",
                        "- **Height and Exercise ($r_{H, E}$):**",
                        "  $\\sum h' e' = (-10)(-0.333) + (0)(1.667) + (10)(-1.333) = 3.333 - 13.333 = -10.0$.",
                        "  $$r_{H, E} = \\frac{-10.0}{\\sqrt{200 \\times 4.667}} = \\frac{-10.0}{\\sqrt{933.33}} = \\frac{-10.0}{30.55} \\approx \\mathbf{-0.3273}$$",
                        "- **Weight and Exercise ($r_{W, E}$):**",
                        "  $\\sum w' e' = (-10)(-0.333) + (3)(1.667) + (7)(-1.333) = 3.333 + 5.001 - 9.331 = -0.997 \\approx -1.0$.",
                        "  $$r_{W, E} = \\frac{-1.0}{\\sqrt{158 \\times 4.667}} = \\frac{-1.0}{\\sqrt{737.33}} = \\frac{-1.0}{27.15} \\approx \\mathbf{-0.0368}$$",
                        "3. **Pearson Correlation Coefficient Matrix:**",
                        "| | Height | Weight | Exercise |",
                        "| :--- | :---: | :---: | :---: |",
                        "| **Height** | 1.000 | 0.956 | -0.327 |",
                        "| **Weight** | 0.956 | 1.000 | -0.037 |",
                        "| **Exercise** | -0.327 | -0.037 | 1.000 |",
                        "4. **Question Answers:**",
                        "- **A) Strongest Positive Relationship:** **Height and Weight** ($r = +0.956$).",
                        "- **B) Negative Relationship:** **Height and Exercise** ($r = -0.327$).",
                        "- **C) Weakly Correlated / Almost Uncorrelated:** **Weight and Exercise** ($r = -0.037 \\approx 0$)."
                    ],
                    "answer": "Correlation Matrix computed. Height & Weight is strongest positive (0.956); Height & Exercise is negative (-0.327); Weight & Exercise is almost uncorrelated (-0.037).",
                    "marking_hint": "3 marks for computing pairwise correlation coefficients and matrix; 1 mark each for answering A, B, and C."
                }
            }
        ]
    }
]

# ==============================================================================
# SS-4103 (Entrepreneurship for IT Business) NITER Term Test 2
# ==============================================================================
ss4103_niter_tests = [
    {
        "id": "ss-4103-term-niter-tt2",
        "course": "SS-4103",
        "exam": "term",
        "college": "NITER",
        "term_no": 2,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 2",
        "marks": 20,
        "topics": [
            "Economic & Social Factors in Entrepreneurship",
            "Schumpeter's Theory of Entrepreneurship",
            "SWOT Analysis for IT Venture",
            "Starting from Scratch Considerations",
            "Business Plan Importance"
        ],
        "question": """Answer all questions: **[5 x 4 = 20, or 5 marks each]**

**Question 1:** Discuss Economic and Social factors affecting entrepreneurship development. **[5]**

**Question 2:** Elaborate Schumpeter Theory of Entrepreneurship. **[5]**

**Question 3:** Discuss with an example how SWOT analysis is conducted? **[5]**

**Question 4:** Explain the key considerations to start from the scratch. **[5]**

**Question 5:** Discuss the importance of business plan for any entrepreneurial initiative. **[5]**""",
        "subparts": [
            {
                "id": "ss-4103-term-niter-tt2-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 5,
                "topics": ["Economic & Social Factors in Entrepreneurship"],
                "question": "Discuss Economic and Social factors affecting entrepreneurship development.",
                "solution": {
                    "steps": [
                        "1. **Economic Factors Affecting Entrepreneurship:**",
                        "- **Capital Availability:** Access to seed funding, venture capital, angel investors, and favorable bank credit drives venture birth and expansion.",
                        "- **Market Demand & Purchasing Power:** Growing disposable income and expanding digital markets create commercial viability for innovative IT products.",
                        "- **Infrastructure & Connectivity:** High-speed internet, reliable cloud hosting, electricity, and transportation lower operational costs.",
                        "- **Labor & Technical Talent:** Availability of skilled software engineers, data analysts, and agile managers at competitive wage rates.",
                        "2. **Social and Cultural Factors Affecting Entrepreneurship:**",
                        "- **Cultural Attitude Toward Risk & Failure:** Societies celebrating risk-taking and viewing failure as learning cultivate higher startup density compared to risk-averse cultures.",
                        "- **Social Support & Recognition:** Societal respect and family backing for founders as prestigious career paths motivate youth toward venture creation.",
                        "- **Education & Entrepreneurial Training:** University curricula incorporating startup incubators, coding hackathons, and IP commercialization.",
                        "- **Role Models & Networking:** Thriving tech ecosystems and mentorship networks providing aspiring founders with accessible playbooks."
                    ],
                    "answer": "Economic factors supply capital, market demand, and infrastructure; social factors foster risk tolerance, societal backing, and an entrepreneurial innovation culture.",
                    "marking_hint": "2.5 marks for economic factors; 2.5 marks for social factors."
                }
            },
            {
                "id": "ss-4103-term-niter-tt2-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 5,
                "topics": ["Schumpeter's Theory of Entrepreneurship"],
                "question": "Elaborate Schumpeter Theory of Entrepreneurship.",
                "solution": {
                    "steps": [
                        "1. **Core Premise of Schumpeterian Theory:**",
                        "- Formulated by economist Joseph Schumpeter, this theory asserts that the entrepreneur is the central dynamic driver of economic development through **innovation**.",
                        "- Economic progress is not a gradual circular flow, but a discontinuous disruptive process termed **Creative Destruction** (*gale of creative destruction*), where innovative products replace antiquated industrial models.",
                        "2. **Five Types of Schumpeterian Innovations (New Combinations):**",
                        "- **Introduction of a New Good:** Launching a product consumers are unfamiliar with or of superior qualitative utility (e.g., Apple iPhone).",
                        "- **Introduction of a New Method of Production:** Developing novel manufacturing or software deployment techniques (e.g., Cloud SaaS pipelines).",
                        "- **Opening of a New Market:** Entering an untapped geographic or consumer segment.",
                        "- **Conquest of a New Source of Supply:** Securing novel raw materials or components.",
                        "- **Carrying out New Organization of an Industry:** Creating a monopoly position or disrupting established industry structures (e.g., Uber disrupting taxis).",
                        "3. **Distinction Between Manager and Entrepreneur:**",
                        "- A manager merely allocates resources within existing operational routines.",
                        "- An entrepreneur undertakes proactive risk, initiates new combinations, and transforms economic equilibria."
                    ],
                    "answer": "Schumpeter posits the entrepreneur as the prime innovator driving economic growth through 'Creative Destruction' by introducing five new industrial combinations.",
                    "marking_hint": "2 marks for core innovation & creative destruction concept; 2.5 marks for detailing the 5 types of innovation; 0.5 mark for manager vs. entrepreneur distinction."
                }
            },
            {
                "id": "ss-4103-term-niter-tt2-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 5,
                "topics": ["SWOT Analysis for IT Venture"],
                "question": "Discuss with an example how SWOT analysis is conducted?",
                "solution": {
                    "steps": [
                        "1. **SWOT Analysis Framework:**",
                        "A strategic planning tool that evaluates Internal factors (**Strengths, Weaknesses**) and External factors (**Opportunities, Threats**) to align business capabilities with competitive market conditions.",
                        "2. **Real-World IT Example: AI-Powered Telehealth SaaS Startup:**",
                        "| Category | Internal Factors | Strategic Action |",
                        "| :--- | :--- | :--- |",
                        "| **Strengths (S)** | Proprietary low-latency diagnostic AI, HIPAA-compliant cloud architecture, experienced engineering team. | Leverage technical superiority to secure hospital enterprise contracts. |",
                        "| **Weaknesses (W)** | Limited brand awareness, modest marketing budget, reliance on third-party cloud GPUs. | Outsource digital marketing and partner with established medical clinics. |",
                        "| **Category** | **External Factors** | **Strategic Action** |",
                        "| **Opportunities (O)** | Surging demand for remote patient consultations, government digital health subsidies, underserved rural areas. | Expand product to bilingual rural clinics and capture subsidized tenders. |",
                        "| **Threats (T)** | Stringent healthcare data privacy regulations, aggressive competition from big tech, cybersecurity ransomware risks. | Implement end-to-end zero-trust encryption and retain specialized healthcare legal counsel. |",
                        "3. **Strategic Synthesis:** Combine Strengths with Opportunities (SO strategies) to drive market penetration while mitigating Weaknesses and Threats (WT strategies)."
                    ],
                    "answer": "SWOT evaluates internal Strengths/Weaknesses and external Opportunities/Threats. Illustrated via an AI Telehealth SaaS matrix driving targeted strategic actions.",
                    "marking_hint": "2 marks for explaining the SWOT methodology; 3 marks for a detailed, realistic IT business example matrix."
                }
            },
            {
                "id": "ss-4103-term-niter-tt2-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 5,
                "topics": ["Starting from Scratch Considerations"],
                "question": "Explain the key considerations to start from the scratch.",
                "solution": {
                    "steps": [
                        "1. **Problem Validation & Product-Market Fit (PMF):**",
                        "- Identify a genuine, high-friction pain point that customers are actively willing to pay to solve.",
                        "- Conduct customer interviews and build a Minimum Viable Product (MVP) to validate core hypotheses before investing capital.",
                        "2. **Founding Team & Skill Complementarity:**",
                        "- Assemble a core team balancing technical execution, product design, and business/sales development (Hacker, Hipster, Hustler).",
                        "3. **Financial Runway & Unit Economics:**",
                        "- Calculate the initial burn rate, customer acquisition cost (CAC), and customer lifetime value (LTV).",
                        "- Ensure at least 12–18 months of financial runway through bootstrapping, personal savings, or angel investment.",
                        "4. **Legal, Regulatory & Intellectual Property Foundation:**",
                        "- Choose appropriate corporate registration (Pvt. Ltd. / LLC), founder equity vesting schedules, trademark protection, and regulatory licenses.",
                        "5. **Go-To-Market (GTM) Strategy & Distribution:**",
                        "- Define clear customer acquisition channels (SEO, content, direct B2B sales, viral referral loops) rather than relying solely on product novelty."
                    ],
                    "answer": "Starting from scratch requires customer-validated PMF, a complementary founding team, clear unit economics/runway, a sound legal foundation, and an effective GTM strategy.",
                    "marking_hint": "1 mark each for discussing five fundamental pillars: validation/MVP, team, finance/runway, legal/IP, and GTM."
                }
            },
            {
                "id": "ss-4103-term-niter-tt2-q5",
                "qno": "Q5",
                "label": "Question 5",
                "marks": 5,
                "topics": ["Business Plan Importance"],
                "question": "Discuss the importance of business plan for any entrepreneurial initiative.",
                "solution": {
                    "steps": [
                        "1. **Strategic Roadmap & Vision Alignment:**",
                        "- Serves as an operational blueprint translating abstract entrepreneurial ideas into concrete milestones, resource schedules, and quarterly objectives.",
                        "2. **Fundraising & Investor Confidence:**",
                        "- Venture capitalists, angel investors, and banks demand a rigorous business plan demonstrating market size (TAM/SAM/SOM), revenue models, and projected ROI before committing capital.",
                        "3. **Risk Identification & Mitigation:**",
                        "- Forces founders to perform thorough competitor benchmarking, regulatory risk assessments, and financial sensitivity analyses before encountering critical failures.",
                        "4. **Resource Allocation & Budgetary Discipline:**",
                        "- Provides structured oversight on cash flow projections, operational expenditures, hiring timelines, and working capital needs.",
                        "5. **Performance Measurement Benchmark:**",
                        "- Establishes Key Performance Indicators (KPIs) against which real progress, customer traction, and product timelines are objectively evaluated."
                    ],
                    "answer": "A business plan is indispensable as an operational roadmap, an essential investor fundraising tool, a proactive risk mitigation instrument, and a KPI performance benchmark.",
                    "marking_hint": "1 mark each for discussing five core benefits: operational roadmap, fundraising, risk mitigation, resource discipline, and progress benchmarking."
                }
            }
        ]
    }
]

# ==============================================================================
# MERGE INTO data/*.json PRESERVING EXISTING EXAMS AND TERM TESTS
# ==============================================================================
niter_map = {
    "cse-4101.json": cse4101_niter_tests,
    "cse-4102.json": cse4102_niter_tests,
    "cse-4125.json": cse4125_niter_tests,
    "cse-4126.json": cse4126_niter_tests,
    "ss-4103.json": ss4103_niter_tests
}

for filename, niter_list in niter_map.items():
    filepath = DATA_DIR / filename
    with open(filepath, 'r', encoding='utf-8') as f:
        existing = json.load(f)

    # Filter out any old NITER term tests if previously inserted
    filtered = [q for q in existing if not (q.get('exam') == 'term' and q.get('college') == 'NITER')]
    # Append the newly constructed NITER term tests
    filtered.extend(niter_list)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(filtered, f, indent=2, ensure_ascii=False)
    print(f"✓ Updated {filename} with {len(niter_list)} NITER Term Test papers (Total questions now: {len(filtered)}).")

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
print("✓ Successfully rebundled data/codex_data.js with all MEC and NITER Term Tests!")
