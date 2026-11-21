import json
from pathlib import Path

ROOT = Path(r"T:\Project\7th Semester")
DATA_DIR = ROOT / "data"

# ==============================================================================
# CSE-4101 (Artificial Intelligence) FEC Term Tests
# ==============================================================================
cse4101_fec_tests = [
    {
        "id": "cse-4101-term-fec-tt1",
        "course": "CSE-4101",
        "exam": "term",
        "college": "FEC",
        "term_no": 1,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 1",
        "marks": 20,
        "topics": [
            "A* Evaluation Function & Inference Rules",
            "Heuristic Admissibility & Consistency",
            "Greedy Best-First Search on Romania Map",
            "Hill Climbing Variants & First-Order Logic",
            "Turing Test & Learning Agents"
        ],
        "question": """4Y1S 2021-22 • CSE 4101 Incourse 01 (Answer all questions)

**Question 1:** **[2+3 = 5]**  
a) Explain the components of the evaluation function $f(n) = g(n) + h(n)$. **[2]**  
b) Write short notes on: i) Modus Ponens ii) Modus Tollens with example. **[3]**

**Question 2:** Explain "For a heuristic function to search safely and optimally, it must satisfy Admissibility and Consistency". **[3]**

**Question 3:** Using Greedy best-first search find the cost and show the steps from the source Arad to the destination Bucharest. **[4]**

```mermaid
graph LR
    Arad((Arad: 366)) ---|140| Sibiu((Sibiu: 253))
    Arad ---|118| Timisoara((Timisoara: 329))
    Arad ---|75| Zerind((Zerind: 374))
    Zerind ---|71| Oradea((Oradea: 380))
    Oradea ---|151| Sibiu
    Sibiu ---|99| Fagaras((Fagaras: 176))
    Sibiu ---|80| RimnicuVilcea((Rimnicu Vilcea: 193))
    Fagaras ---|211| Bucharest((Bucharest: 0))
    RimnicuVilcea ---|97| Pitesti((Pitesti: 100))
    RimnicuVilcea ---|146| Craiova((Craiova: 160))
    Pitesti ---|101| Bucharest
    Pitesti ---|138| Craiova
    Craiova ---|120| Dobreta((Dobreta: 242))
    Dobreta ---|75| Mehadia((Mehadia: 241))
    Mehadia ---|70| Lugoj((Lugoj: 244))
    Lugoj ---|111| Timisoara
    Bucharest ---|90| Giurgiu((Giurgiu: 77))
    Bucharest ---|85| Urziceni((Urziceni: 80))
```

**Question 4:** **[2+2 = 4]**  
a) Briefly define the variants of hill climbing search. **[2]**  
b) Convert the following statements into First-Order Logic (FOL): **[2]**  
i. All birds can fly  
ii. Some humans are honest  
iii. Everyone is loyal to someone  
iv. Marcus tried to assassinate Caesar

**Question 5:** Shortly define "The Turing Test approach". How do you evaluate learning agent from other AI agents? **[4]**""",
        "subparts": [
            {
                "id": "cse-4101-term-fec-tt1-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 5,
                "topics": ["A* Evaluation Function & Inference Rules"],
                "question": "a) Explain the components of the evaluation function f(n) = g(n) + h(n). b) Write short notes on i) Modus Ponens ii) Modus Tollens with example.",
                "solution": {
                    "steps": [
                        "**(a) Components of the A* Evaluation Function $f(n) = g(n) + h(n)$:**",
                        "- **$g(n)$ (Past Path Cost):** The exact, cumulative edge cost accumulated along the best-known path from the initial start node $s$ to the current node $n$.",
                        "- **$h(n)$ (Heuristic Future Estimate):** An estimated cost from node $n$ to the closest goal state based on domain-specific heuristic knowledge.",
                        "- **$f(n)$ (Estimated Total Cost):** Represents the estimated total cost of the cheapest complete solution path that travels through node $n$. A* search prioritizes expanding nodes with the lowest $f(n)$.",
                        "**(b) Logical Inference Rules:**",
                        "- **i. Modus Ponens (Affirming the Antecedent):**",
                        "  $$\\frac{P, \\quad P \\implies Q}{Q}$$",
                        "  *Principle:* If proposition $P$ is true, and the implication 'If $P$ then $Q$' is true, then $Q$ is logically inferred as true.",
                        "  *Example:* $P$ = 'It is raining.' $P \\implies Q$ = 'If it is raining, the street is wet.' Inference: $Q$ = 'The street is wet.'",
                        "- **ii. Modus Tollens (Denying the Consequent):**",
                        "  $$\\frac{\\neg Q, \\quad P \\implies Q}{\\neg P}$$",
                        "  *Principle:* If $Q$ is false ($\neg Q$), and the conditional 'If $P$ then $Q$' holds, then antecedent $P$ must be false ($\neg P$).",
                        "  *Example:* $\neg Q$ = 'The street is not wet.' $P \\implies Q$ = 'If it is raining, the street is wet.' Inference: $\neg P$ = 'It is not raining.'"
                    ],
                    "answer": "f(n) combines accumulated cost g(n) with heuristic estimate h(n). Modus Ponens infers Q from P and P->Q; Modus Tollens infers ~P from ~Q and P->Q.",
                    "marking_hint": "2 marks for explaining g(n), h(n), and f(n); 1.5 marks for Modus Ponens with example; 1.5 marks for Modus Tollens with example."
                }
            },
            {
                "id": "cse-4101-term-fec-tt1-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 3,
                "topics": ["Heuristic Admissibility & Consistency"],
                "question": "Explain 'For a heuristic function to search safely and optimally, it must satisfy Admissibility and Consistency'.",
                "solution": {
                    "steps": [
                        "1. **Admissibility Condition ($h(n) \\le h^*(n)$):**",
                        "- An admissible heuristic **never overestimates** the true minimal cost $h^*(n)$ required to reach a goal from node $n$.",
                        "- *Search Safety & Optimality:* In tree search, admissibility guarantees that A* will never return a suboptimal path, because any suboptimal goal will have $f(G_2) = g(G_2) > C^*$, whereas an optimal goal's ancestor on the frontier will have $f(n) \\le C^*$ and will always be chosen first.",
                        "2. **Consistency (Monotonicity) Condition:**",
                        "- For every node $n$ and every successor $n'$ generated by action $a$: $h(n) \\le c(n, a, n') + h(n')$.",
                        "- This represents the **triangle inequality** in state space.",
                        "- *Search Safety & Efficiency:* Consistency guarantees that the values of $f(n)$ are non-decreasing along any path. Consequently, whenever A* expands a node in graph search, the path to that node is guaranteed to be optimal. This eliminates the expensive requirement to reopen nodes previously expanded in the closed set."
                    ],
                    "answer": "Admissibility prevents cost overestimation, ensuring optimal solutions in tree search. Consistency enforces the triangle inequality, guaranteeing that the first time a node is expanded in graph search, its path is optimal.",
                    "marking_hint": "1.5 marks for mathematical definition and role of Admissibility; 1.5 marks for Consistency and triangle inequality."
                }
            },
            {
                "id": "cse-4101-term-fec-tt1-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 4,
                "topics": ["Greedy Best-First Search on Romania Map"],
                "question": "Using Greedy best-first search find the cost and show the steps from the source Arad to the destination Bucharest.",
                "solution": {
                    "steps": [
                        "1. **Greedy Best-First Search Principle:**",
                        "Evaluates nodes using $f(n) = h(n)$ exclusively (where $h(n)$ is the straight-line distance heuristic to Bucharest).",
                        "Straight-line distances to Bucharest ($h$): Arad = 366, Sibiu = 253, Timisoara = 329, Zerind = 374, Fagaras = 176, Rimnicu Vilcea = 193, Bucharest = 0.",
                        "2. **Step-by-Step Search Progression:**",
                        "- **Initial State:** Start at `Arad` ($h = 366$).",
                        "- **Step 1:** Expand `Arad`. Generated frontier neighbors:",
                        "  - `Sibiu` ($h = 253$)",
                        "  - `Timisoara` ($h = 329$)",
                        "  - `Zerind` ($h = 374$)",
                        "  - Minimum heuristic is `Sibiu` ($h = 253$). Selected.",
                        "- **Step 2:** Expand `Sibiu`. Generated frontier neighbors:",
                        "  - `Fagaras` ($h = 176$)",
                        "  - `Rimnicu Vilcea` ($h = 193$)",
                        "  - `Oradea` ($h = 380$)",
                        "  - `Arad` (already visited)",
                        "  - Minimum heuristic is `Fagaras` ($h = 176$). Selected.",
                        "- **Step 3:** Expand `Fagaras`. Generated frontier neighbors:",
                        "  - `Bucharest` ($h = 0$)",
                        "  - `Sibiu` (already visited)",
                        "  - Minimum heuristic is `Bucharest` ($h = 0$). Goal reached!",
                        "3. **Path and Cost Calculation:**",
                        "- Resulting Path: **Arad -> Sibiu -> Fagaras -> Bucharest**",
                        "- Step edge costs: $\\text{Cost}(\\text{Arad}, \\text{Sibiu}) = 140$, $\\text{Cost}(\\text{Sibiu}, \\text{Fagaras}) = 99$, $\\text{Cost}(\\text{Fagaras}, \\text{Bucharest}) = 211$.",
                        "- **Total Path Cost:** $g = 140 + 99 + 211 = \\mathbf{450}$."
                    ],
                    "answer": "Greedy Best-First Path: Arad -> Sibiu -> Fagaras -> Bucharest with Total Cost = 450.",
                    "marking_hint": "1 mark for explaining Greedy Best-First Search criterion; 2 marks for step-by-step frontier heuristic evaluations; 1 mark for correct path and total cost."
                }
            },
            {
                "id": "cse-4101-term-fec-tt1-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 4,
                "topics": ["Hill Climbing Variants & First-Order Logic"],
                "question": "a) Briefly define the variants of hill climbing search. b) Convert the following statements into First-Order Logic (FOL): i. All birds can fly, ii. Some humans are honest, iii. Everyone is loyal to someone, iv. Marcus tried to assassinate Caesar.",
                "solution": {
                    "steps": [
                        "**(a) Variants of Hill Climbing Search:**",
                        "- **Simple Hill Climbing:** Evaluates neighboring states one by one and immediately transitions to the first neighbor that improves the evaluation function.",
                        "- **Steepest-Ascent Hill Climbing (Gradient Search):** Evaluates all possible successor states and chooses the single neighbor with the maximum improvement.",
                        "- **Stochastic Hill Climbing:** Randomly selects from among the uphill moves, weighting probabilities proportionally to steepness.",
                        "- **Random-Restart Hill Climbing:** Runs a series of hill climbing searches from randomly generated starting states until a goal is discovered, guaranteeing asymptotic completeness.",
                        "**(b) First-Order Logic (FOL) Translations:**",
                        "- **i. All birds can fly:**",
                        "  $$\\forall x \\, (\\text{Bird}(x) \\implies \\text{CanFly}(x))$$",
                        "- **ii. Some humans are honest:**",
                        "  $$\\exists x \\, (\\text{Human}(x) \\land \\text{Honest}(x))$$",
                        "- **iii. Everyone is loyal to someone:**",
                        "  $$\\forall x \\, (\\text{Person}(x) \\implies \\exists y \\, (\\text{Person}(y) \\land \\text{LoyalTo}(x, y)))$$  (or $\\forall x \\, \\exists y \\, \\text{LoyalTo}(x, y)$)",
                        "- **iv. Marcus tried to assassinate Caesar:**",
                        "  $$\\text{TriedToAssassinate}(\\text{Marcus}, \\text{Caesar})$$"
                    ],
                    "answer": "Defined 4 hill climbing variants. Correctly translated all 4 English statements into standard FOL predicates.",
                    "marking_hint": "2 marks for 4 hill climbing variants; 2 marks (0.5 marks each) for correct FOL statements."
                }
            },
            {
                "id": "cse-4101-term-fec-tt1-q5",
                "qno": "Q5",
                "label": "Question 5",
                "marks": 4,
                "topics": ["Turing Test & Learning Agents"],
                "question": "Shortly define 'The Turing Test approach'. How do you evaluate learning agent from other AI agents?",
                "solution": {
                    "steps": [
                        "1. **The Turing Test Approach (Alan Turing, 1950):**",
                        "- An operational benchmark for determining machine intelligence.",
                        "- A human interrogator communicates through text terminals with an unseen human and machine. If the interrogator cannot reliably tell which entity is the computer after thorough questioning, the machine passes.",
                        "- *Required Capabilities:* Natural Language Processing (NLP), Knowledge Representation, Automated Reasoning, and Machine Learning.",
                        "2. **Learning Agents vs. Other AI Agents:**",
                        "- **Traditional AI Agents (Reflex, Goal-based, Utility-based):** Rely on static, pre-programmed knowledge bases or fixed evaluation functions. They cannot adapt when deployed in unfamiliar or changing environments.",
                        "- **Learning Agent Architecture:** Separates the system into four distinct components:",
                        "  - **Learning Element:** Responsible for making improvements and discovering new knowledge.",
                        "  - **Performance Element:** Responsible for selecting external actions based on percepts (the operational agent).",
                        "  - **Critic:** Evaluates the agent's behavior against an external performance standard and provides feedback to the learning element.",
                        "  - **Problem Generator:** Suggests exploratory actions leading to novel experiences rather than merely repeating known sub-optimal behaviors.",
                        "- *Evaluation:* A learning agent is evaluated by its **learning curve** (rate of performance metric improvement over time) and its capacity to generalize in non-stationary environments."
                    ],
                    "answer": "Turing Test evaluates behavioral indistinguishability from human intelligence. Learning agents distinctly separate performance from a learning element and critic, enabling continuous self-adaptation.",
                    "marking_hint": "2 marks for Turing Test definition and required capabilities; 2 marks for learning agent architecture and comparison with traditional agents."
                }
            }
        ]
    },
    {
        "id": "cse-4101-term-fec-tt2",
        "course": "CSE-4101",
        "exam": "term",
        "college": "FEC",
        "term_no": 2,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 2",
        "marks": 20,
        "topics": [
            "Constraint Satisfaction Problems (CSP)",
            "CSP Formulation & Genetic Algorithm Steps",
            "Uncertainty in AI & Bayes' Theorem",
            "Probability & Penalty Kick Scenario",
            "Genetic Algorithm Optimization on f(x) = x^2"
        ],
        "question": """4Y1S 2021-22 • CSE 4101 Incourse 02 (Answer all questions)

**Question 1:** Define CSP with proper example. Describe varieties of CSP with example. **[4]**

**Question 2:** Elaborate standard search formulation in CSP. Describe the steps of genetic algorithm. **[4]**

**Question 3:** Briefly define the reasons for uncertainty in AI. Write down the equation for conditional probability and Bayes Theorem. **[4]**

**Question 4:** During a FIFA tournament, a team relies on two types of penalty takers: The Star Forward takes 25% of the team's penalties and scores a goal 85% of the time. Other Players take the remaining 75% of the penalties and score a goal 70% of the time. You walk beside the TV and noticed Star Forward will take the kick for a penalty. What is the probability of that penalty is a goal? **[4]**

**Question 5:** Maximize $f(x) = x^2$ over the integer interval $[0, 31]$ using a simple Genetic Algorithm. Assume an initial population size of 4 chromosomes, each encoded as a 5-bit binary string that enough for the given interval: **[4]**  
- Population 1 (P1): 01101  
- Population 2 (P2): 11000  
- Population 3 (P3): 01000  
- Population 4 (P4): 10011  
Find the total fitness and average fitness using genetic algorithm.""",
        "subparts": [
            {
                "id": "cse-4101-term-fec-tt2-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 4,
                "topics": ["Constraint Satisfaction Problems (CSP)"],
                "question": "Define CSP with proper example. Describe varieties of CSP with example.",
                "solution": {
                    "steps": [
                        "1. **Constraint Satisfaction Problem (CSP) Definition:**",
                        "A problem formulation where state is defined by a set of variables $X = \\{X_1, X_2, \\dots, X_n\\}$, each having a domain of values $D = \\{D_1, D_2, \\dots, D_n\\}$, and a set of constraints $C = \\{C_1, C_2, \\dots, C_m\\}$ specifying allowable combinations of values. A solution is a complete and consistent assignment.",
                        "- *Example:* Map Coloring of Australia: Variables = $\\{\\text{WA, NT, SA, Q, NSW, V, T}\\}$, Domains = $\\{\\text{Red, Green, Blue}\\}$, Constraints = adjacent regions must have different colors (e.g., $\\text{WA} \\ne \\text{NT}$).",
                        "2. **Varieties of CSPs:**",
                        "- **Discrete Variables:**",
                        "  - *Finite Domains:* Variables take values from finite sets (e.g., 8-Queens, Boolean SAT).",
                        "  - *Infinite Domains:* Variables take integer or string values; constraints expressed via constraint language (e.g., job scheduling).",
                        "- **Continuous Variables:** Domains are continuous real numbers $\\mathbb{R}$ (e.g., linear constraints in operations research).",
                        "- **Constraint Arity Varieties:**",
                        "  - *Unary Constraint:* Restricts a single variable (e.g., $\\text{SA} \\ne \\text{Green}$).",
                        "  - *Binary Constraint:* Relates two variables (e.g., $\\text{SA} \\ne \\text{WA}$).",
                        "  - *Higher-Order / Global Constraint:* Involves arbitrary number of variables (e.g., $\\text{Alldiff}(X_1, \\dots, X_9)$ in Sudoku)."
                    ],
                    "answer": "CSP defines states via variables, domains, and constraints. Varieties include discrete/continuous domains and unary, binary, and global constraint arities.",
                    "marking_hint": "2 marks for formal definition and map-coloring example; 2 marks for classification of CSP varieties."
                }
            },
            {
                "id": "cse-4101-term-fec-tt2-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 4,
                "topics": ["CSP Formulation & Genetic Algorithm Steps"],
                "question": "Elaborate standard search formulation in CSP. Describe the steps of genetic algorithm.",
                "solution": {
                    "steps": [
                        "1. **Standard Search Formulation in CSP:**",
                        "- **Initial State:** Empty assignment $\\{\\}$ where no variables are assigned values.",
                        "- **Successor Function:** Select an unassigned variable $X_i$ and assign a value $v \\in D_i$ that does not conflict with existing assignments.",
                        "- **Goal Test:** The current assignment is **complete** (all variables assigned) and **consistent** (satisfies all constraints $C$).",
                        "- **Path Cost:** Constant step cost (e.g., 0 or 1 per step), because the goal is the final consistent configuration rather than the path taken.",
                        "- *Standard Algorithm:* Backtracking Search (depth-first search with single-variable assignments).",
                        "2. **Steps of a Genetic Algorithm (GA):**",
                        "- **Step 1: Population Initialization:** Randomly generate an initial population of $N$ binary or real-encoded chromosomes.",
                        "- **Step 2: Fitness Evaluation:** Calculate the fitness function value $f(x)$ for each individual.",
                        "- **Step 3: Selection:** Select parent chromosomes based on fitness (e.g., Roulette Wheel, Tournament selection).",
                        "- **Step 4: Crossover (Recombination):** Pair parents and perform crossover at designated split points to create offspring.",
                        "- **Step 5: Mutation:** Randomly flip bits with small mutation probability $p_m$ to preserve genetic diversity.",
                        "- **Step 6: Termination Check:** Repeat until an optimal solution is found or generation limits are exceeded."
                    ],
                    "answer": "CSP search uses incremental variable assignments with backtracking. Genetic algorithms iteratively apply population initialization, fitness evaluation, selection, crossover, and mutation.",
                    "marking_hint": "2 marks for CSP initial state, successor, goal test, and path cost; 2 marks for the 6 steps of genetic algorithms."
                }
            },
            {
                "id": "cse-4101-term-fec-tt2-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 4,
                "topics": ["Uncertainty in AI & Bayes' Theorem"],
                "question": "Briefly define the reasons for uncertainty in AI. Write down the equation for conditional probability and Bayes Theorem.",
                "solution": {
                    "steps": [
                        "1. **Reasons for Uncertainty in AI Systems:**",
                        "- **Partial Observability:** Sensor limitations prevent the agent from observing the entire environment state (e.g., medical diagnostics, card games).",
                        "- **Stochasticity (Non-determinism):** Actions do not produce deterministic outcomes due to random physical factors or external interference.",
                        "- **Adversarial / Multi-agent Dynamics:** Competing agents introduce unpredictable behaviors and decisions.",
                        "- **Laziness & Theoretical Ignorance:** The complete domain theory is either too complex to formulate comprehensively or unknown.",
                        "2. **Conditional Probability Equation:**",
                        "$$P(A \\mid B) = \\frac{P(A \\land B)}{P(B)} \\quad \\text{where } P(B) > 0$$",
                        "3. **Bayes' Theorem Equation:**",
                        "$$P(A \\mid B) = \\frac{P(B \\mid A) \\cdot P(A)}{P(B)} = \\frac{P(B \\mid A) \\cdot P(A)}{\\sum_i P(B \\mid A_i) \\cdot P(A_i)}$$"
                    ],
                    "answer": "Uncertainty stems from partial observability, non-determinism, and domain complexity. Equations: P(A|B) = P(A,B)/P(B) and P(A|B) = [P(B|A)P(A)] / P(B).",
                    "marking_hint": "2 marks for 4 causes of uncertainty; 1 mark for conditional probability; 1 mark for Bayes' Theorem."
                }
            },
            {
                "id": "cse-4101-term-fec-tt2-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 4,
                "topics": ["Probability & Penalty Kick Scenario"],
                "question": "Star Forward takes 25% of team penalties and scores 85% of time. Other players take 75% and score 70%. You notice Star Forward takes the kick. What is the probability that penalty is a goal?",
                "solution": {
                    "steps": [
                        "1. **Define Events & Given Probabilities:**",
                        "- $S$: Star Forward takes the penalty $\\implies P(S) = 0.25$.",
                        "- $O$: Other Player takes the penalty $\\implies P(O) = 0.75$.",
                        "- $G$: The penalty results in a goal.",
                        "- Conditional goal probabilities:",
                        "  - $P(G \\mid S) = 0.85$ (85% scoring rate for Star Forward).",
                        "  - $P(G \\mid O) = 0.70$ (70% scoring rate for Other Players).",
                        "2. **Evaluation:**",
                        "- The problem states: *'You walk beside the TV and noticed Star Forward will take the kick for a penalty. What is the probability of that penalty is a goal?'*",
                        "- Since the event that Star Forward is taking the kick has **already been observed with certainty** (condition $S$ is given):",
                        "$$P(\\text{Goal} \\mid \\text{Star Forward takes kick}) = P(G \\mid S) = \\mathbf{0.85} \\quad (85\\%)$$",
                        "3. **Additional Perspective (Total Probability):**",
                        "- If instead evaluating the probability of an unknown random penalty being both taken and scored by Star Forward: $P(G \\land S) = P(G \\mid S) \\cdot P(S) = 0.85 \\times 0.25 = 0.2125$ (21.25%).",
                        "- Total probability of a goal across all players: $P(G) = P(G \\mid S)P(S) + P(G \\mid O)P(O) = (0.85)(0.25) + (0.70)(0.75) = 0.2125 + 0.5250 = 0.7375$ (73.75%)."
                    ],
                    "answer": "Given that the Star Forward is taking the kick, the conditional probability of scoring is P(Goal | Star Forward) = 0.85 (85%).",
                    "marking_hint": "4 marks for clear identification of conditional probability P(G|S) = 0.85, with optional total probability formulation."
                }
            },
            {
                "id": "cse-4101-term-fec-tt2-q5",
                "qno": "Q5",
                "label": "Question 5",
                "marks": 4,
                "topics": ["Genetic Algorithm Optimization on f(x) = x^2"],
                "question": "Maximize f(x) = x^2 over [0, 31] using GA. Population: P1=01101, P2=11000, P3=01000, P4=10011. Find total fitness and average fitness.",
                "solution": {
                    "steps": [
                        "1. **Decode 5-Bit Binary Chromosomes to Decimal $x$:**",
                        "- $P_1 = 01101_2 = 0(16) + 1(8) + 1(4) + 0(2) + 1(1) = 8 + 4 + 1 = \\mathbf{13}$",
                        "- $P_2 = 11000_2 = 1(16) + 1(8) + 0(4) + 0(2) + 0(1) = 16 + 8 = \\mathbf{24}$",
                        "- $P_3 = 01000_2 = 0(16) + 1(8) + 0(4) + 0(2) + 0(1) = \\mathbf{8}$",
                        "- $P_4 = 10011_2 = 1(16) + 0(8) + 0(4) + 1(2) + 1(1) = 16 + 2 + 1 = \\mathbf{19}$",
                        "2. **Calculate Individual Fitness $f(x) = x^2$:**",
                        "- $f(P_1) = 13^2 = \\mathbf{169}$",
                        "- $f(P_2) = 24^2 = \\mathbf{576}$",
                        "- $f(P_3) = 8^2 = \\mathbf{64}$",
                        "- $f(P_4) = 19^2 = \\mathbf{361}$",
                        "3. **Compute Total Fitness:**",
                        "$$\\text{Total Fitness} = \\sum_{i=1}^4 f(P_i) = 169 + 576 + 64 + 361 = \\mathbf{1170}$$",
                        "4. **Compute Average Fitness:**",
                        "$$\\text{Average Fitness } \\bar{f} = \\frac{\\text{Total Fitness}}{N} = \\frac{1170}{4} = \\mathbf{292.5}$$",
                        "5. **Selection Probability Distribution $p_i = \\frac{f(x_i)}{\\sum f}$:**",
                        "- $p(P_1) = \\frac{169}{1170} \\approx 14.44\\%$",
                        "- $p(P_2) = \\frac{576}{1170} \\approx 49.23\\%$",
                        "- $p(P_3) = \\frac{64}{1170} \\approx 5.47\\%$",
                        "- $p(P_4) = \\frac{361}{1170} \\approx 30.85\\%$"
                    ],
                    "answer": "Individual fitness: P1=169, P2=576, P3=64, P4=361. Total Fitness = 1170. Average Fitness = 292.5.",
                    "marking_hint": "1 mark for decoding binary strings; 1 mark for individual fitness values; 1 mark for Total Fitness = 1170; 1 mark for Average Fitness = 292.5."
                }
            }
        ]
    }
]

# ==============================================================================
# CSE-4125 (Introduction to Machine Learning) FEC Term Tests
# ==============================================================================
cse4125_fec_tests = [
    {
        "id": "cse-4125-term-fec-tt1",
        "course": "CSE-4125",
        "exam": "term",
        "college": "FEC",
        "term_no": 1,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 1",
        "marks": 20,
        "topics": [
            "ML Definition, Classification & Regression",
            "Encoding Techniques & One-Hot Encoding",
            "Linear Regression & Least Squares Method",
            "Cross Validation & K-Fold Process"
        ],
        "question": """FEC • ML-1 (Answer all questions) **[5 x 4 = 20]**

**Question 1:** Define Machine Learning (ML). Explain the difference between classification and regression. Give two practical examples of applications for each. **[5]**

**Question 2:** Why encoding is necessary in machine learning? Explain one hot encoding technique with proper example. **[5]**

**Question 3:** Explain the concept of linear regression. Given the data points $(1, 2), (2, 3), (3, 5)$, find the best-fit line using the least squares method. **[5]**

**Question 4:** What is Cross Validation? Explain K-Fold Cross Validation. Describe the step-by-step process of performing K-Fold CV. **[5]**""",
        "subparts": [
            {
                "id": "cse-4125-term-fec-tt1-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 5,
                "topics": ["ML Definition, Classification & Regression"],
                "question": "Define Machine Learning (ML). Explain the difference between classification and regression. Give two practical examples of applications for each.",
                "solution": {
                    "steps": [
                        "1. **Machine Learning Definition:** Machine Learning is a discipline of artificial intelligence enabling computer algorithms to iteratively learn from data and improve performance on specific tasks without explicit rule-based programming.",
                        "2. **Classification vs. Regression:**",
                        "| Feature | Classification | Regression |",
                        "| :--- | :--- | :--- |",
                        "| **Output Nature** | Discrete categorical class labels. | Continuous numerical quantities. |",
                        "| **Decision Boundary** | Partitioning feature space into class regions. | Fitting a continuous curve or hyperplane. |",
                        "| **Evaluation Metrics**| Accuracy, Precision, Recall, F1, ROC-AUC. | MSE, RMSE, MAE, R-squared ($R^2$). |",
                        "3. **Practical Examples:**",
                        "- **Classification Examples:**",
                        "  1. *Email Spam Detection:* Classifying incoming emails as 'Spam' or 'Not Spam'.",
                        "  2. *Medical Diagnosis:* Classifying tumor biopsy scans as 'Malignant' or 'Benign'.",
                        "- **Regression Examples:**",
                        "  1. *Real Estate Valuation:* Predicting house market prices based on square footage and location.",
                        "  2. *Weather Forecasting:* Predicting tomorrow's exact continuous temperature (°C)."
                    ],
                    "answer": "ML extracts statistical patterns from data. Classification predicts discrete class labels, whereas Regression predicts continuous numerical quantities.",
                    "marking_hint": "1 mark for ML definition; 2 marks for classification vs regression differences; 2 marks for practical examples."
                }
            },
            {
                "id": "cse-4125-term-fec-tt1-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 5,
                "topics": ["Encoding Techniques & One-Hot Encoding"],
                "question": "Why encoding is necessary in machine learning? Explain one hot encoding technique with proper example.",
                "solution": {
                    "steps": [
                        "1. **Why Encoding is Necessary:**",
                        "- Machine learning algorithms (Linear Models, Neural Networks, SVMs) perform mathematical computations (matrix dot products, gradients, Euclidean distances) that require numerical tensor inputs.",
                        "- Raw categorical strings (e.g., 'Red', 'Green', 'Blue') cannot be mathematically computed directly.",
                        "- Simple label encoding ($0, 1, 2$) unintentionally introduces an artificial ordinal ranking where none exists (e.g., implies $2 > 1 > 0$), misguiding linear algorithms.",
                        "2. **One-Hot Encoding Technique:**",
                        "- Transforms each unique categorical value into a binary vector of length equal to the number of categories.",
                        "- Each category is represented by a dedicated binary column with a $1$ indicating presence and $0$ elsewhere.",
                        "3. **Example Demonstration:**",
                        "Consider feature `Color` with categories: `Red`, `Green`, `Blue`.",
                        "| Original Color | Color_Red | Color_Green | Color_Blue |",
                        "| :--- | :---: | :---: | :---: |",
                        "| Red | 1 | 0 | 0 |",
                        "| Green | 0 | 1 | 0 |",
                        "| Blue | 0 | 0 | 1 |",
                        "| Red | 1 | 0 | 0 |"
                    ],
                    "answer": "Encoding converts non-numeric categorical data into mathematical numbers without imposing false ordinal hierarchies. One-Hot encoding assigns a binary column per category.",
                    "marking_hint": "2.5 marks for explaining the mathematical necessity of encoding; 2.5 marks for One-Hot encoding explanation and tabular example."
                }
            },
            {
                "id": "cse-4125-term-fec-tt1-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 5,
                "topics": ["Linear Regression & Least Squares Method"],
                "question": "Explain the concept of linear regression. Given data points (1, 2), (2, 3), (3, 5), find the best-fit line using the least squares method.",
                "solution": {
                    "steps": [
                        "1. **Concept of Linear Regression:**",
                        "Models the linear relationship between an independent variable $x$ and a dependent variable $y$ via $y = mx + c$, minimizing the sum of squared vertical residuals $\\sum (y_i - \\hat{y}_i)^2$.",
                        "2. **Given Data Points ($n = 3$):**",
                        "$(x_1, y_1) = (1, 2), \\quad (x_2, y_2) = (2, 3), \\quad (x_3, y_3) = (3, 5)$.",
                        "3. **Compute Sample Means:**",
                        "- $\\bar{x} = \\frac{1 + 2 + 3}{3} = \\frac{6}{3} = 2$",
                        "- $\\bar{y} = \\frac{2 + 3 + 5}{3} = \\frac{10}{3} \\approx 3.333$",
                        "4. **Compute Slope $m = \\frac{\\sum (x_i - \\bar{x})(y_i - \\bar{y})}{\\sum (x_i - \\bar{x})^2}$:**",
                        "- Deviations $(x_i - \\bar{x})$: $-1, 0, 1$",
                        "- Deviations $(y_i - \\bar{y})$: $2 - 10/3 = -4/3$, $3 - 10/3 = -1/3$, $5 - 10/3 = 5/3$",
                        "- Numerator: $\\sum (x_i - \\bar{x})(y_i - \\bar{y}) = (-1)(-4/3) + (0)(-1/3) + (1)(5/3) = \\frac{4}{3} + \\frac{5}{3} = \\frac{9}{3} = 3$",
                        "- Denominator: $\\sum (x_i - \\bar{x})^2 = (-1)^2 + 0^2 + 1^2 = 1 + 0 + 1 = 2$",
                        "- Slope: $m = \\frac{3}{2} = \\mathbf{1.5}$",
                        "5. **Compute Intercept $c = \\bar{y} - m \\bar{x}$:**",
                        "- $c = \\frac{10}{3} - (1.5)(2) = \\frac{10}{3} - 3 = \\frac{10 - 9}{3} = \\frac{1}{3} \\approx \\mathbf{0.333}$",
                        "6. **Best-Fit Regression Line:**",
                        "$$y = 1.5x + \\frac{1}{3} \\quad \\text{or} \\quad y = 1.5x + 0.333$$"
                    ],
                    "answer": "Best-fit line equation: y = 1.5x + 1/3 (or y = 1.5x + 0.333).",
                    "marking_hint": "1.5 marks for linear regression concept; 2 marks for slope m calculation; 1.5 marks for intercept c and final equation."
                }
            },
            {
                "id": "cse-4125-term-fec-tt1-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 5,
                "topics": ["Cross Validation & K-Fold Process"],
                "question": "What is Cross Validation? Explain K-Fold Cross Validation. Describe the step-by-step process of performing K-Fold CV.",
                "solution": {
                    "steps": [
                        "1. **Cross Validation (CV) Definition:**",
                        "A statistical resampling procedure used to evaluate the generalization performance of machine learning models on unseen data, preventing overfitting and eliminating train/test split bias.",
                        "2. **K-Fold Cross Validation:**",
                        "- Partitions the dataset into $K$ equal-sized mutually exclusive subsets (folds).",
                        "- In each iteration, $K-1$ folds are used for model training, and the remaining 1 fold is held out for validation.",
                        "- This process repeats $K$ times so that every single fold serves as validation data exactly once.",
                        "3. **Step-by-Step Execution Process:**",
                        "- **Step 1 (Shuffle & Partition):** Randomly shuffle the complete dataset and partition it into $K$ equal folds ($F_1, F_2, \\dots, F_K$).",
                        "- **Step 2 (Iterative Training & Validation):**",
                        "  - *Iteration 1:* Train on $F_2, \\dots, F_K$; validate on $F_1 \\implies$ Score $S_1$.",
                        "  - *Iteration 2:* Train on $F_1, F_3, \\dots, F_K$; validate on $F_2 \\implies$ Score $S_2$.",
                        "  - ...",
                        "  - *Iteration K:* Train on $F_1, \\dots, F_{K-1}$; validate on $F_K \\implies$ Score $S_K$.",
                        "- **Step 3 (Metric Aggregation):** Compute the mean cross-validation score: $S_{\\text{final}} = \\frac{1}{K} \\sum_{i=1}^K S_i$ and its standard error.",
                        "- **Step 4 (Final Model Training):** Once hyperparameters are selected, retrain the final model on the entire dataset."
                    ],
                    "answer": "Cross validation measures model generalization. K-Fold CV partitions data into K subsets, iteratively training on K-1 folds and testing on 1, then averaging the K scores.",
                    "marking_hint": "1.5 marks for CV definition; 1.5 marks for K-Fold concept; 2 marks for step-by-step procedure."
                }
            }
        ]
    },
    {
        "id": "cse-4125-term-fec-tt2",
        "course": "CSE-4125",
        "exam": "term",
        "college": "FEC",
        "term_no": 2,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 2",
        "marks": 20,
        "topics": [
            "K-Means Clustering & Optimal K",
            "Principal Component Analysis (PCA)",
            "Entropy & Information Gain Decision Tree",
            "Markov Chain Weather Transition"
        ],
        "question": """FEC • ML-2 (Answer all questions) **[5 x 4 = 20]**

**Question 1:** What is clustering in machine learning? Describe the K-Means clustering algorithm. How do you choose the optimal number of clusters (K) for K-means, and what methods can assist in this decision? **[5]**

**Question 2:** Given the following data, compute the principal component vectors and the first principal components: **[5]**

| x | 2 | 3 | 7 |
| :---: | :---: | :---: | :---: |
| **y** | 11 | 14 | 26 |

**Question 3:** State the formula of Bayes theorem. Consider the following dataset: **[5]**

| Outlook | Temperature | Humidity | Wind | Play |
| :--- | :--- | :--- | :--- | :---: |
| Sunny | Hot | High | Weak | No |
| Sunny | Hot | High | Strong | No |
| Overcast | Hot | High | Weak | Yes |
| Rainy | Mild | High | Weak | Yes |
| Rainy | Cool | Normal | Weak | Yes |
| Rainy | Cool | Normal | Strong | No |
| Overcast | Cool | Normal | Strong | Yes |
| Sunny | Mild | High | Weak | No |

Calculate entropy and information gain at each step.

**Question 4:** What is a Markov Chain? Consider the following transition matrix representing the weather conditions of a particular region. The possible weather states are Sunny (S), Rainy (R), and Cloudy (C). **[5]**

| Current State | Sunny (S) | Rainy (R) | Cloudy (C) |
| :--- | :---: | :---: | :---: |
| **Sunny (S)** | 0.80 | 0.15 | 0.05 |
| **Rainy (R)** | 0.38 | 0.60 | 0.02 |
| **Cloudy (C)** | 0.75 | 0.05 | 0.20 |

Given that today the weather is sunny (S). What is the probability that tomorrow is sunny (S) and day after tomorrow is rainy (R)?""",
        "subparts": [
            {
                "id": "cse-4125-term-fec-tt2-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 5,
                "topics": ["K-Means Clustering & Optimal K"],
                "question": "What is clustering in machine learning? Describe the K-Means clustering algorithm. How do you choose optimal K, and what methods assist in this decision?",
                "solution": {
                    "steps": [
                        "1. **Clustering Definition:**",
                        "An unsupervised learning technique that groups unlabeled data points into clusters such that points within the same cluster share high similarity while points in different clusters are distinctly dissimilar.",
                        "2. **K-Means Clustering Algorithm:**",
                        "- **Step 1:** Choose $K$ initial centroids randomly (or via K-Means++).",
                        "- **Step 2 (Assignment):** Assign each data point $x_i$ to its nearest centroid based on Euclidean distance $d(x_i, c_k) = \\|x_i - c_k\\|^2$.",
                        "- **Step 3 (Update):** Recompute each centroid as the mean of all points assigned to that cluster: $c_k = \\frac{1}{|S_k|} \\sum_{x_i \\in S_k} x_i$.",
                        "- **Step 4:** Repeat Steps 2 and 3 until centroids converge or assignments stabilize.",
                        "3. **Methods to Choose Optimal $K$:**",
                        "- **The Elbow Method:** Computes the Within-Cluster Sum of Squares (WCSS / Inertia) across candidate $K$ values. Plotting WCSS against $K$ reveals an 'elbow point' where the rate of WCSS reduction sharply diminishes; this elbow signifies optimal $K$.",
                        "- **Silhouette Analysis:** Measures how similar a point is to its own cluster compared to other clusters ($s \\in [-1, 1]$). The $K$ value yielding the highest average silhouette score is preferred."
                    ],
                    "answer": "Clustering groups unlabeled data. K-Means iterates assignment and centroid recalculation. Optimal K is determined via the Elbow Method (WCSS) and Silhouette Analysis.",
                    "marking_hint": "1.5 marks for clustering definition; 1.5 marks for K-Means steps; 2 marks for Elbow Method and Silhouette Analysis."
                }
            },
            {
                "id": "cse-4125-term-fec-tt2-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 5,
                "topics": ["Principal Component Analysis (PCA)"],
                "question": "Given data points (2, 11), (3, 14), (7, 26), compute the principal component vectors and the first principal components.",
                "solution": {
                    "steps": [
                        "1. **Compute Sample Means ($n = 3$):**",
                        "- $\\bar{x} = \\frac{2 + 3 + 7}{3} = \\frac{12}{3} = 4$",
                        "- $\\bar{y} = \\frac{11 + 14 + 26}{3} = \\frac{51}{3} = 17$",
                        "2. **Center the Data ($X_c = X - \\mu$):**",
                        "- $x' = [2-4, 3-4, 7-4] = [-2, -1, 3]$",
                        "- $y' = [11-17, 14-17, 26-17] = [-6, -3, 9]$",
                        "- *Notice $y' = 3x'$, showing exact linear collinearity!*",
                        "3. **Compute Sample Covariance Matrix $\\Sigma = \\frac{1}{n-1} X_c^T X_c$:**",
                        "- $\\text{Var}(x) = \\frac{(-2)^2 + (-1)^2 + 3^2}{2} = \\frac{4 + 1 + 9}{2} = 7$",
                        "- $\\text{Var}(y) = \\frac{(-6)^2 + (-3)^2 + 9^2}{2} = \\frac{36 + 9 + 81}{2} = \\frac{126}{2} = 63$",
                        "- $\\text{Cov}(x, y) = \\frac{(-2)(-6) + (-1)(-3) + (3)(9)}{2} = \\frac{12 + 3 + 27}{2} = \\frac{42}{2} = 21$",
                        "$$\\Sigma = \\begin{bmatrix} 7 & 21 \\\\ 21 & 63 \\end{bmatrix}$$",
                        "4. **Eigenvalues Calculation:**",
                        "$$\\det(\\Sigma - \\lambda I) = (7 - \\lambda)(63 - \\lambda) - 21^2 = \\lambda^2 - 70\\lambda = 0 \\implies \\lambda_1 = 70, \\; \\lambda_2 = 0$$",
                        "5. **Principal Component Vectors (Eigenvectors):**",
                        "- For $\\lambda_1 = 70$: $(\\Sigma - 70I)v_1 = 0 \\implies \\begin{bmatrix} -63 & 21 \\\\ 21 & -7 \\end{bmatrix} \\begin{bmatrix} v_x \\\\ v_y \\end{bmatrix} = 0 \\implies v_y = 3v_x$.",
                        "- Normalized First Principal Component Vector: $v_1 = \\frac{1}{\\sqrt{1^2 + 3^2}} \\begin{bmatrix} 1 \\\\ 3 \\end{bmatrix} = \\begin{bmatrix} \\frac{1}{\\sqrt{10}} \\\\ \\frac{3}{\\sqrt{10}} \\end{bmatrix} \\approx \\begin{bmatrix} 0.3162 \\\\ 0.9487 \\end{bmatrix}$.",
                        "- Second Principal Component Vector: $v_2 = \\begin{bmatrix} -\\frac{3}{\\sqrt{10}} \\\\ \\frac{1}{\\sqrt{10}} \\end{bmatrix}$.",
                        "6. **First Principal Component Scores ($z_{i1} = v_1^T [x_i', y_i']^T$):**",
                        "- Point 1: $z_1 = \\frac{1}{\\sqrt{10}}(-2) + \\frac{3}{\\sqrt{10}}(-6) = \\frac{-20}{\\sqrt{10}} \\approx \\mathbf{-6.325}$",
                        "- Point 2: $z_2 = \\frac{1}{\\sqrt{10}}(-1) + \\frac{3}{\\sqrt{10}}(-3) = \\frac{-10}{\\sqrt{10}} \\approx \\mathbf{-3.162}$",
                        "- Point 3: $z_3 = \\frac{1}{\\sqrt{10}}(3) + \\frac{3}{\\sqrt{10}}(9) = \\frac{30}{\\sqrt{10}} \\approx \\mathbf{+9.487}$"
                    ],
                    "answer": "First PC vector v1 = [1/sqrt(10), 3/sqrt(10)]^T. First principal component projections: z = [-6.325, -3.162, 9.487] (captures 100% of variance).",
                    "marking_hint": "1.5 marks for data centering and covariance matrix; 1.5 marks for eigenvalues; 1 mark for eigenvector v1; 1 mark for principal component scores."
                }
            },
            {
                "id": "cse-4125-term-fec-tt2-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 5,
                "topics": ["Entropy & Information Gain Decision Tree"],
                "question": "State Bayes theorem formula. Calculate entropy and information gain at each step for the given 8-sample dataset.",
                "solution": {
                    "steps": [
                        "1. **Bayes' Theorem Formula:** $P(A \\mid B) = \\frac{P(B \\mid A) \\cdot P(A)}{P(B)}$.",
                        "2. **Total Target Entropy $H(S)$:**",
                        "- Total samples $N = 8$: $\\text{Play} = \\text{Yes}$ for 4 samples, $\\text{Play} = \\text{No}$ for 4 samples.",
                        "$$H(S) = -\\left(\\frac{4}{8} \\log_2 \\frac{4}{8} + \\frac{4}{8} \\log_2 \\frac{4}{8}\\right) = -\\left(0.5(-1) + 0.5(-1)\\right) = \\mathbf{1.0 \\text{ bit}}$$",
                        "3. **Entropy & Information Gain for Features:**",
                        "- **Feature 1: Outlook**",
                        "  - *Sunny (3):* 0 Yes, 3 No $\\implies H = 0$",
                        "  - *Overcast (2):* 2 Yes, 0 No $\\implies H = 0$",
                        "  - *Rainy (3):* 2 Yes, 1 No $\\implies H = -\\left(\\frac{2}{3}\\log_2\\frac{2}{3} + \\frac{1}{3}\\log_2\\frac{1}{3}\\right) \\approx 0.918$",
                        "  - $H(S \\mid \\text{Outlook}) = \\frac{3}{8}(0) + \\frac{2}{8}(0) + \\frac{3}{8}(0.918) = 0.344$",
                        "  - $\\mathbf{\\text{Gain}(S, \\text{Outlook})} = 1.0 - 0.344 = \\mathbf{0.656}$",
                        "- **Feature 2: Humidity**",
                        "  - *High (5):* 1 Yes, 4 No $\\implies H = -\\left(\\frac{1}{5}\\log_2\\frac{1}{5} + \\frac{4}{5}\\log_2\\frac{4}{5}\\right) \\approx 0.722$",
                        "  - *Normal (3):* 3 Yes, 0 No $\\implies H = 0$",
                        "  - $H(S \\mid \\text{Humidity}) = \\frac{5}{8}(0.722) + \\frac{3}{8}(0) = 0.451$",
                        "  - $\\mathbf{\\text{Gain}(S, \\text{Humidity})} = 1.0 - 0.451 = \\mathbf{0.549}$",
                        "- **Feature 3: Wind**",
                        "  - *Weak (5):* 3 Yes, 2 No $\\implies H \\approx 0.971$",
                        "  - *Strong (3):* 1 Yes, 2 No $\\implies H \\approx 0.918$",
                        "  - $H(S \\mid \\text{Wind}) = \\frac{5}{8}(0.971) + \\frac{3}{8}(0.918) = 0.951$",
                        "  - $\\mathbf{\\text{Gain}(S, \\text{Wind})} = 1.0 - 0.951 = \\mathbf{0.049}$",
                        "- **Feature 4: Temperature**",
                        "  - *Hot (3):* 1 Yes, 2 No $\\implies H = 0.918$",
                        "  - *Mild (2):* 1 Yes, 1 No $\\implies H = 1.000$",
                        "  - *Cool (3):* 2 Yes, 1 No $\\implies H = 0.918$",
                        "  - $H(S \\mid \\text{Temp}) = \\frac{3}{8}(0.918) + \\frac{2}{8}(1.0) + \\frac{3}{8}(0.918) = 0.939$",
                        "  - $\\mathbf{\\text{Gain}(S, \\text{Temp})} = 1.0 - 0.939 = \\mathbf{0.061}$",
                        "4. **Conclusion:** **Outlook** provides the highest Information Gain ($0.656$) and is selected as root split."
                    ],
                    "answer": "Base Entropy = 1.0. Information Gains: Outlook = 0.656, Humidity = 0.549, Temp = 0.061, Wind = 0.049. Outlook is the optimal splitting attribute.",
                    "marking_hint": "1 mark for Bayes formula and base entropy; 3 marks for step-by-step entropy and gain calculations; 1 mark for selecting Outlook."
                }
            },
            {
                "id": "cse-4125-term-fec-tt2-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 5,
                "topics": ["Markov Chain Weather Transition"],
                "question": "What is a Markov Chain? Transition matrix P: Sunny, Rainy, Cloudy. Today is Sunny. What is probability tomorrow is Sunny and day after tomorrow is Rainy?",
                "solution": {
                    "steps": [
                        "1. **Markov Chain Definition:**",
                        "A discrete-time stochastic process that transitions between states in a state space according to transition probabilities satisfying the Markov property (the conditional probability of the future state depends solely on the current present state and not on the preceding past history).",
                        "2. **Transition Probability Matrix $P$:**",
                        "$$P = \\begin{bmatrix} P_{S,S} & P_{S,R} & P_{S,C} \\\\ P_{R,S} & P_{R,R} & P_{R,C} \\\\ P_{C,S} & P_{C,R} & P_{C,C} \\end{bmatrix} = \\begin{bmatrix} 0.80 & 0.15 & 0.05 \\\\ 0.38 & 0.60 & 0.02 \\\\ 0.75 & 0.05 & 0.20 \\end{bmatrix}$$",
                        "3. **Compute Probability for the Sequence:**",
                        "- Given: Today ($t = 0$) is Sunny $\\implies X_0 = S$.",
                        "- Target: Tomorrow ($t = 1$) is Sunny ($X_1 = S$) AND Day after tomorrow ($t = 2$) is Rainy ($X_2 = R$).",
                        "- By the Markov multiplication chain rule:",
                        "$$P(X_1 = S, X_2 = R \\mid X_0 = S) = P(X_1 = S \\mid X_0 = S) \\times P(X_2 = R \\mid X_1 = S)$$",
                        "- From the transition matrix (row 1 for Sunny):",
                        "  - $P(X_1 = S \\mid X_0 = S) = P_{S, S} = 0.80$",
                        "  - $P(X_2 = R \\mid X_1 = S) = P_{S, R} = 0.15$",
                        "- Joint Probability:",
                        "$$P = 0.80 \\times 0.15 = \\mathbf{0.12} \\quad (12\\%)$$",
                        "- *(Note: Weather sequence Sunny -> Sunny -> Rainy occurs with exactly 12% probability).*"
                    ],
                    "answer": "Probability that tomorrow is sunny and day after tomorrow is rainy = 0.80 * 0.15 = 0.12 (12%).",
                    "marking_hint": "2 marks for Markov chain definition; 3 marks for setting up transition probability multiplication and reaching 0.12."
                }
            }
        ]
    }
]

# ==============================================================================
# CSE-4126 (Introduction to Data Science) FEC Term Test 1
# ==============================================================================
cse4126_fec_tests = [
    {
        "id": "cse-4126-term-fec-tt1",
        "course": "CSE-4126",
        "exam": "term",
        "college": "FEC",
        "term_no": 1,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 1",
        "marks": 20,
        "topics": [
            "IQR & Outlier Detection",
            "KNN Missing Value Imputation",
            "Normalization vs Standardization",
            "Pearson Correlation Coefficient",
            "Chi-Square Test of Independence"
        ],
        "question": """Faridpur Engineering College • CSE-4126 (1st In-Course Examination) **[20]**

**Question 1:** What is IQR. How we can find out Outliers using IQR? **[3.0]**

**Question 2:** Consider the following dataset containing missing values: **[3.0]**

| X1 | X2 | X3 |
| :---: | :---: | :---: |
| 20 | 30 | 40 |
| 25 | ? | 45 |
| ? | 40 | 50 |

KNN (K = 2), use KNN Imputation techniques to handle the missing values.

**Question 3:** Describe the difference between normalization and standardization in feature scaling. **[3.0]**

**Question 4:** Calculate the correlation coefficient between Hours Studied and Test Score for 5 students: **[5.0]**

| Student | Hours Studied (X) | Test Score (Y) |
| :---: | :---: | :---: |
| 1 | 2 | 50 |
| 2 | 3 | 60 |
| 3 | 4 | 65 |
| 4 | 5 | 75 |
| 5 | 6 | 85 |

**Question 5:** A researcher wants to investigate whether there is a significant association between students' gender and their preferred learning method. The following data were collected from 100 students. Perform a Chi-Square Test of Independence at a 5% significance level ($\alpha = 0.05$) and determine whether to Reject or Fail to Reject the Null Hypothesis ($H_0$). Justify your decision based on the calculated Chi-Square value and the critical value. **[6.0]**  
*[Critical Chi-Square value = 5.991 ($df = 2, \alpha = 0.05$)]*

| Gender | Online | Offline | Hybrid | Total |
| :--- | :---: | :---: | :---: | :---: |
| **Male** | 30 | 10 | 10 | 50 |
| **Female** | 10 | 20 | 20 | 50 |
| **Total** | 40 | 30 | 30 | 100 |""",
        "subparts": [
            {
                "id": "cse-4126-term-fec-tt1-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 3,
                "topics": ["IQR & Outlier Detection"],
                "question": "What is IQR. How we can find out Outliers using IQR?",
                "solution": {
                    "steps": [
                        "1. **Interquartile Range (IQR) Definition:**",
                        "The Interquartile Range is a robust measure of statistical dispersion representing the spread of the middle 50% of an ordered dataset: $\\text{IQR} = Q_3 - Q_1$, where $Q_3$ is the 75th percentile and $Q_1$ is the 25th percentile.",
                        "2. **Outlier Detection via Tukey's Fences:**",
                        "- **Step 1:** Calculate first quartile $Q_1$ and third quartile $Q_3$.",
                        "- **Step 2:** Compute $\\text{IQR} = Q_3 - Q_1$.",
                        "- **Step 3:** Establish outlier boundaries (fences):",
                        "  - **Lower Fence:** $\\text{LF} = Q_1 - 1.5 \\times \\text{IQR}$",
                        "  - **Upper Fence:** $\\text{UF} = Q_3 + 1.5 \\times \\text{IQR}$",
                        "- **Step 4:** Any observation $x$ where $x < \\text{LF}$ or $x > \\text{UF}$ is classified as an **outlier**."
                    ],
                    "answer": "IQR = Q3 - Q1 measures middle 50% spread. Values outside [Q1 - 1.5*IQR, Q3 + 1.5*IQR] are identified as outliers.",
                    "marking_hint": "1.5 marks for IQR definition; 1.5 marks for lower/upper fence formulas and identification rule."
                }
            },
            {
                "id": "cse-4126-term-fec-tt1-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 3,
                "topics": ["KNN Missing Value Imputation"],
                "question": "Handle missing values in the 3x3 dataset using KNN Imputation with K = 2.",
                "solution": {
                    "steps": [
                        "1. **Dataset Review:**",
                        "- Row 1: $(X_1=20, X_2=30, X_3=40)$ [Complete]",
                        "- Row 2: $(X_1=25, X_2=?, X_3=45)$ [Missing $X_2$]",
                        "- Row 3: $(X_1=?, X_2=40, X_3=50)$ [Missing $X_1$]",
                        "2. **Imputing Missing $X_2$ in Row 2 ($K = 2$):**",
                        "- For Row 2, available features are $X_1 = 25$ and $X_3 = 45$.",
                        "- Distance to Row 1 (using available overlapping features $X_1, X_3$):",
                        "  $$d(\\text{R2}, \\text{R1}) = \\sqrt{(25 - 20)^2 + (45 - 40)^2} = \\sqrt{25 + 25} = \\sqrt{50} \\approx 7.07$$",
                        "- Distance to Row 3 (overlapping available feature is $X_3$):",
                        "  $$d(\\text{R2}, \\text{R3}) = |45 - 50| = 5$$",
                        "- Both Row 1 and Row 3 serve as the $K=2$ nearest neighbors.",
                        "- Impute $X_2$ as the average of $X_2$ in Row 1 ($30$) and Row 3 ($40$):",
                        "  $$X_2^{\\text{imputed}} = \\frac{30 + 40}{2} = \\mathbf{35}$$",
                        "3. **Imputing Missing $X_1$ in Row 3 ($K = 2$):**",
                        "- For Row 3, available features are $X_2 = 40$ and $X_3 = 50$.",
                        "- Distance to Row 1: $d(\\text{R3}, \\text{R1}) = \\sqrt{(40 - 30)^2 + (50 - 40)^2} = \\sqrt{100 + 100} = \\sqrt{200} \\approx 14.14$.",
                        "- Distance to Row 2 (using newly imputed $X_2 = 35$): $d(\\text{R3}, \\text{R2}) = \\sqrt{(40 - 35)^2 + (50 - 45)^2} = \\sqrt{25 + 25} = \\sqrt{50} \\approx 7.07$.",
                        "- Impute $X_1$ as the average of $X_1$ in Row 1 ($20$) and Row 2 ($25$):",
                        "  $$X_1^{\\text{imputed}} = \\frac{20 + 25}{2} = \\mathbf{22.5}$$"
                    ],
                    "answer": "Imputed values: X2 for Row 2 = 35, and X1 for Row 3 = 22.5.",
                    "marking_hint": "1.5 marks for distance calculations and imputing X2=35; 1.5 marks for distance calculations and imputing X1=22.5."
                }
            },
            {
                "id": "cse-4126-term-fec-tt1-q3",
                "qno": "Q3",
                "label": "Question 3",
                "marks": 3,
                "topics": ["Normalization vs Standardization"],
                "question": "Describe the difference between normalization and standardization in feature scaling.",
                "solution": {
                    "steps": [
                        "1. **Comparative Framework:**",
                        "| Characteristic | Normalization (Min-Max Scaling) | Standardization (Z-Score Scaling) |",
                        "| :--- | :--- | :--- |",
                        "| **Mathematical Formula** | $$x' = \\frac{x - x_{\\min}}{x_{\\max} - x_{\\min}}$$ | $$z = \\frac{x - \\mu}{\\sigma}$$ |",
                        "| **Output Range** | Strictly bounded, usually $[0, 1]$ (or $[-1, 1]$). | Unbounded; centered at mean $\\mu = 0$ with variance $\\sigma^2 = 1$. |",
                        "| **Outlier Sensitivity** | **High** (outliers compress typical values into a narrow range). | **Low / Robust** (outliers do not restrict the scaling of other points). |",
                        "| **Distribution Assumption**| Does not assume any specific probability distribution. | Assumes features roughly follow a Gaussian (normal) distribution. |",
                        "| **Typical Algorithms** | Neural Networks, Image Processing, KNN. | Linear Regression, Logistic Regression, SVM, PCA. |"
                    ],
                    "answer": "Normalization bounds data to [0, 1] and is sensitive to outliers. Standardization centers data at zero mean with unit variance and is robust against outliers.",
                    "marking_hint": "1.5 marks for formulas and value ranges; 1.5 marks for outlier sensitivity and algorithmic use cases."
                }
            },
            {
                "id": "cse-4126-term-fec-tt1-q4",
                "qno": "Q4",
                "label": "Question 4",
                "marks": 5,
                "topics": ["Pearson Correlation Coefficient"],
                "question": "Calculate the correlation coefficient between Hours Studied (X) and Test Score (Y) for 5 students.",
                "solution": {
                    "steps": [
                        "1. **Given Data Points ($n = 5$):**",
                        "$(2, 50), \\; (3, 60), \\; (4, 65), \\; (5, 75), \\; (6, 85)$.",
                        "2. **Compute Means:**",
                        "- $\\bar{X} = \\frac{2 + 3 + 4 + 5 + 6}{5} = \\frac{20}{5} = \\mathbf{4.0}$",
                        "- $\\bar{Y} = \\frac{50 + 60 + 65 + 75 + 85}{5} = \\frac{335}{5} = \\mathbf{67.0}$",
                        "3. **Compute Deviations & Products:**",
                        "| Student | $x_i$ | $y_i$ | $x' = x_i - \\bar{X}$ | $y' = y_i - \\bar{Y}$ | $x'^2$ | $y'^2$ | $x' y'$ |",
                        "| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |",
                        "| 1 | 2 | 50 | -2 | -17 | 4 | 289 | +34 |",
                        "| 2 | 3 | 60 | -1 | -7 | 1 | 49 | +7 |",
                        "| 3 | 4 | 65 | 0 | -2 | 0 | 4 | 0 |",
                        "| 4 | 5 | 75 | +1 | +8 | 1 | 64 | +8 |",
                        "| 5 | 6 | 85 | +2 | +18 | 4 | 324 | +36 |",
                        "| **Total** | | | **0** | **0** | **10** | **730** | **85** |",
                        "4. **Compute Pearson Correlation Coefficient $r$:**",
                        "$$r = \\frac{\\sum x' y'}{\\sqrt{\\sum x'^2 \\cdot \\sum y'^2}} = \\frac{85}{\\sqrt{10 \\times 730}} = \\frac{85}{\\sqrt{7300}} = \\frac{85}{85.440} \\approx \\mathbf{+0.9949}$$"
                    ],
                    "answer": "Pearson correlation coefficient r = +0.9949, indicating an almost perfect positive linear relationship between hours studied and test scores.",
                    "marking_hint": "1.5 marks for means and deviations; 2 marks for covariance and variance sums; 1.5 marks for final correlation r = 0.995."
                }
            },
            {
                "id": "cse-4126-term-fec-tt1-q5",
                "qno": "Q5",
                "label": "Question 5",
                "marks": 6,
                "topics": ["Chi-Square Test of Independence"],
                "question": "Chi-Square Test of Independence on Gender vs Learning Method at alpha = 0.05. Critical value = 5.991 (df=2). Reject or Fail to Reject H0?",
                "solution": {
                    "steps": [
                        "1. **Observed Frequencies ($O$) & Marginal Totals ($N = 100$):**",
                        "| Gender | Online | Offline | Hybrid | Row Total |",
                        "| :--- | :---: | :---: | :---: | :---: |",
                        "| **Male** | 30 | 10 | 10 | **50** |",
                        "| **Female** | 10 | 20 | 20 | **50** |",
                        "| **Col Total** | **40** | **30** | **30** | **N = 100** |",
                        "2. **Calculate Expected Frequencies ($E = \\frac{\\text{Row Total} \\times \\text{Col Total}}{N}$):**",
                        "- $E(\\text{Male, Online}) = \\frac{50 \\times 40}{100} = 20.0$",
                        "- $E(\\text{Male, Offline}) = \\frac{50 \\times 30}{100} = 15.0$",
                        "- $E(\\text{Male, Hybrid}) = \\frac{50 \\times 30}{100} = 15.0$",
                        "- $E(\\text{Female, Online}) = \\frac{50 \\times 40}{100} = 20.0$",
                        "- $E(\\text{Female, Offline}) = \\frac{50 \\times 30}{100} = 15.0$",
                        "- $E(\\text{Female, Hybrid}) = \\frac{50 \\times 30}{100} = 15.0$",
                        "3. **Compute $\\chi^2 = \\sum \\frac{(O - E)^2}{E}$:**",
                        "- Male cells:",
                        "  - Online: $\\frac{(30 - 20)^2}{20} = \\frac{100}{20} = 5.0$",
                        "  - Offline: $\\frac{(10 - 15)^2}{15} = \\frac{25}{15} \\approx 1.667$",
                        "  - Hybrid: $\\frac{(10 - 15)^2}{15} = \\frac{25}{15} \\approx 1.667$",
                        "- Female cells:",
                        "  - Online: $\\frac{(10 - 20)^2}{20} = \\frac{100}{20} = 5.0$",
                        "  - Offline: $\\frac{(20 - 15)^2}{15} = \\frac{25}{15} \\approx 1.667$",
                        "  - Hybrid: $\\frac{(20 - 15)^2}{15} = \\frac{25}{15} \\approx 1.667$",
                        "$$\\chi^2_{\\text{calc}} = 5.0 + 1.667 + 1.667 + 5.0 + 1.667 + 1.667 = \\mathbf{16.667}$$",
                        "4. **Statistical Decision:**",
                        "- Degrees of freedom: $df = (r - 1)(c - 1) = (2 - 1)(3 - 1) = 2$.",
                        "- Critical value at $\\alpha = 0.05$: $\\chi^2_{\\text{crit}} = 5.991$.",
                        "- Comparison: $\\chi^2_{\\text{calc}} (16.667) > \\chi^2_{\\text{crit}} (5.991)$.",
                        "- Decision: **Reject the Null Hypothesis ($H_0$)**.",
                        "- Conclusion: There is a statistically significant association between students' gender and their preferred learning method."
                    ],
                    "answer": "Calculated Chi-Square = 16.667 > 5.991. Reject H0; there is a significant association between gender and preferred learning method.",
                    "marking_hint": "2 marks for expected frequency matrix; 2.5 marks for chi-square computation; 1.5 marks for comparison with critical value and statistical inference."
                }
            }
        ]
    }
]

# ==============================================================================
# SS-4103 (Entrepreneurship for IT Business) FEC Term Tests
# ==============================================================================
ss4103_fec_tests = [
    {
        "id": "ss-4103-term-fec-tt1",
        "course": "SS-4103",
        "exam": "term",
        "college": "FEC",
        "term_no": 1,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 1",
        "marks": 20,
        "topics": [
            "Creativity and Innovation Interconnection",
            "Enhancing Organizational Creativity",
            "Challenges of Entrepreneurship",
            "Ethical Concerns in Entrepreneurship"
        ],
        "question": """University of Dhaka • Affiliated Engineering College • SS 4103 (Time: 50 Min, Marks: 20)

**Question 1:** **[4+6 = 10]**  
a) How Creativity and Innovation is interconnected with each other? Explain. **[4]**  
b) How are to enhance the creativity? Briefly Describe. **[6]**

**Question 2:** **[4+6 = 10]**  
a) What are the challenges of entrepreneurship? Shortly Describe. **[4]**  
b) Briefly Describe the Key concerns of ethical entrepreneurship. **[6]**""",
        "subparts": [
            {
                "id": "ss-4103-term-fec-tt1-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 10,
                "topics": ["Creativity and Innovation Interconnection", "Enhancing Organizational Creativity"],
                "question": "a) How Creativity and Innovation are interconnected? Explain. b) How to enhance creativity? Briefly describe.",
                "solution": {
                    "steps": [
                        "**(a) Interconnection Between Creativity and Innovation:**",
                        "- **Creativity:** The cognitive generation of novel, imaginative, and unconventional ideas or concepts.",
                        "- **Innovation:** The practical application, execution, and commercialization of creative ideas to create tangible business value or resolve market needs.",
                        "- *Interconnection:* Creativity is the **necessary seed and starting point**; Innovation is the **harvest and realization**. Without creativity, innovation lacks novel substance; without innovation, creativity remains mere unexploited imagination ('Creativity is thinking up new things; innovation is doing new things').",
                        "**(b) Strategies to Enhance Creativity:**",
                        "1. **Psychological Safety & Open Culture:** Establish a blameless organizational culture where failure is regarded as a natural learning vector, encouraging calculated risk-taking.",
                        "2. **Diverse & Cross-Disciplinary Teams:** Assemble multidisciplinary talent (engineers, designers, marketers) to synthesize contrasting perspectives.",
                        "3. **Structured Brainstorming & Lateral Thinking:** Utilize creative ideation frameworks (SCAMPER, mind-mapping, Edward de Bono's Six Thinking Hats) deferring premature criticism.",
                        "4. **Dedicated Incubation & Hack Time:** Allocate unstructured exploration time (e.g., Google's 20% time policy) allowing subconscious incubation.",
                        "5. **Continuous Exposure to External Stimuli:** Engage in competitor audits, customer ethnography, design sprints, and cross-industry benchmarking."
                    ],
                    "answer": "Creativity is the intellectual catalyst; Innovation is its commercial execution. Creativity is enhanced via psychological safety, diverse teams, structured brainstorming, and dedicated incubation.",
                    "marking_hint": "4 marks for creativity vs innovation synergy; 6 marks for discussing at least 5 distinct creativity enhancement strategies."
                }
            },
            {
                "id": "ss-4103-term-fec-tt1-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 10,
                "topics": ["Challenges of Entrepreneurship", "Ethical Concerns in Entrepreneurship"],
                "question": "a) What are the challenges of entrepreneurship? Shortly describe. b) Briefly describe the key concerns of ethical entrepreneurship.",
                "solution": {
                    "steps": [
                        "**(a) Core Challenges of Entrepreneurship:**",
                        "1. **Cash Flow & Capital Constraints:** Navigating the early-stage 'Valley of Death' before achieving unit economic profitability.",
                        "2. **Product-Market Fit (PMF) Uncertainty:** Validating customer demand before burning finite financial runway on unwanted features.",
                        "3. **Talent Acquisition & Retention:** Attracting top technical and operational talent to high-risk early ventures competing with high-paying tech giants.",
                        "4. **Founder Burnout & Solitary Burden:** Managing extreme stress, prolonged working hours, and sole accountability for venture survival.",
                        "**(b) Key Concerns of Ethical Entrepreneurship:**",
                        "1. **Consumer Data Privacy & AI Ethics:** Respecting user consent, ensuring robust encryption, and preventing algorithmic bias or deceptive dark patterns.",
                        "2. **Fair Labor Practices & Equity:** Providing fair living wages, safe working environments, and transparent equity sharing without worker exploitation.",
                        "3. **Honest Marketing & Transparency:** Avoiding fraudulent hype, exaggerated product capabilities, or deceptive investor pitches.",
                        "4. **Environmental Sustainability:** Mitigating corporate carbon footprint, electronic waste, and adopting green cloud architectures.",
                        "5. **Fair Competition & Anti-Corruption:** Refraining from predatory price dumping, IP theft, bribery, or monopolistic collusion."
                    ],
                    "answer": "Entrepreneurial challenges center on capital, PMF, hiring, and burnout. Ethical concerns mandate data privacy, fair labor, transparent marketing, environmental care, and fair competition.",
                    "marking_hint": "4 marks for 4 key startup challenges; 6 marks for detailing 5 foundational dimensions of ethical entrepreneurship."
                }
            }
        ]
    },
    {
        "id": "ss-4103-term-fec-tt2",
        "course": "SS-4103",
        "exam": "term",
        "college": "FEC",
        "term_no": 2,
        "set_no": 1,
        "year": 2025,
        "qno": "Term Test 2",
        "marks": 20,
        "topics": [
            "Strategic Management Process",
            "The Three V's Marketing Approach",
            "Strategic vs Tactical Planning",
            "Developing a Strategic Plan",
            "Key Components of Business Strategic Plan"
        ],
        "question": """University of Dhaka • Affiliated Engineering College • SS 4103 (Time: 50 Min, Marks: 20)

**Question 1:** **[7+3 = 10]**  
a) What are the steps of strategic management process? Very shortly describe each step. **[7]**  
b) What are the three V's approaches of marketing? Write down the core business processes of marketing. **[3]**

**Question 2:** **[3+3+4 = 10]**  
a) What is the difference of strategic Planning and Tactical Planning? **[3]**  
b) How to Develop a Strategic Plan? **[3]**  
c) What are the Key Components of a Business Strategic Plan? **[4]**""",
        "subparts": [
            {
                "id": "ss-4103-term-fec-tt2-q1",
                "qno": "Q1",
                "label": "Question 1",
                "marks": 10,
                "topics": ["Strategic Management Process", "The Three V's Marketing Approach"],
                "question": "a) What are the steps of strategic management process? Very shortly describe each step. b) What are the three V's approaches of marketing? Write down the core business processes of marketing.",
                "solution": {
                    "steps": [
                        "**(a) Steps of the Strategic Management Process:**",
                        "1. **Environmental Scanning (Analysis):** Gathering internal and external intelligence using SWOT and PESTEL frameworks to identify competitive advantages and threats.",
                        "2. **Strategy Formulation:** Defining long-term vision, mission statements, corporate objectives, and crafting competitive strategies (e.g., Porter's Cost Leadership vs. Differentiation).",
                        "3. **Strategy Implementation:** Translating strategies into actionable initiatives by allocating financial budgets, assigning organizational responsibilities, and establishing agile workflows.",
                        "4. **Strategy Evaluation & Control:** Continuously monitoring performance metrics (KPIs) against targets and initiating corrective pivots when variances emerge.",
                        "**(b) The Three V's Marketing Approach (Nirmalya Kumar):**",
                        "1. **Value Customer:** Defining which customer segments to serve and which to deliberately ignore.",
                        "2. **Value Proposition:** Articulating the distinct, differentiated bundle of benefits that compellingly solves customer pain points.",
                        "3. **Value Network:** Structuring partner networks, suppliers, digital channels, and supply chains to deliver the value proposition profitably.",
                        "- **Core Business Processes of Marketing:** Market Research & Customer Discovery, New Product Development, Lead Generation & Customer Acquisition, Customer Retention & Loyalty Management."
                    ],
                    "answer": "Strategic management spans scanning, formulation, implementation, and evaluation. Marketing's 3 V's are Value Customer, Value Proposition, and Value Network.",
                    "marking_hint": "7 marks for the 4 strategic management steps with explanations; 3 marks for the 3 V's and core marketing processes."
                }
            },
            {
                "id": "ss-4103-term-fec-tt2-q2",
                "qno": "Q2",
                "label": "Question 2",
                "marks": 10,
                "topics": ["Strategic vs Tactical Planning", "Developing a Strategic Plan", "Key Components of Business Strategic Plan"],
                "question": "a) Difference between Strategic Planning and Tactical Planning. b) How to Develop a Strategic Plan? c) Key Components of a Business Strategic Plan.",
                "solution": {
                    "steps": [
                        "**(a) Strategic Planning vs. Tactical Planning:**",
                        "| Criterion | Strategic Planning | Tactical Planning |",
                        "| :--- | :--- | :--- |",
                        "| **Time Horizon** | Long-term (3 to 5+ years). | Short to medium-term (quarterly to 1 year). |",
                        "| **Organizational Scope** | Entire enterprise / corporate level. | Departmental / functional units. |",
                        "| **Core Focus** | Defines 'What' and 'Why' (direction). | Defines 'How' and 'When' (execution). |",
                        "| **Leadership Level** | Board of Directors, C-suite executives. | Middle management, team leads. |",
                        "**(b) How to Develop a Strategic Plan:**",
                        "1. Identify current organizational baseline, core values, and founding vision.",
                        "2. Perform rigorous external competitive benchmarking and internal capability auditing.",
                        "3. Formulate Specific, Measurable, Achievable, Relevant, Time-bound (SMART) strategic goals.",
                        "4. Construct detailed functional roadmaps, budget allocation, and risk contingency plans.",
                        "5. Establish executive review rhythms and real-time dashboard scorecards (OKRs/KPIs).",
                        "**(c) Key Components of a Business Strategic Plan:**",
                        "1. **Executive Summary & Mission Statement:** Clear definition of organizational purpose and long-term ambition.",
                        "2. **Market & Competitor Analysis:** Thorough audit of target customer personas, TAM/SAM/SOM, and competitive moats.",
                        "3. **Strategic Objectives & Milestones:** Quantifiable quarterly and annual performance targets.",
                        "4. **Go-To-Market & Operational Strategy:** Sales acquisition funnel, pricing strategy, and resource deployment.",
                        "5. **Financial Projections & Risk Matrix:** Pro-forma P&L statements, burn rate, and scenario sensitivity modeling."
                    ],
                    "answer": "Strategic planning sets long-term vision; tactical planning governs short-term execution. Strategic plans integrate executive vision, market analysis, SMART goals, operational roadmaps, and financial forecasts.",
                    "marking_hint": "3 marks for strategic vs tactical comparison; 3 marks for developing a plan; 4 marks for detailing key strategic plan components."
                }
            }
        ]
    }
]

# ==============================================================================
# MERGE INTO data/*.json PRESERVING EXISTING EXAMS AND OTHER COLLEGES
# ==============================================================================
fec_map = {
    "cse-4101.json": cse4101_fec_tests,
    "cse-4125.json": cse4125_fec_tests,
    "cse-4126.json": cse4126_fec_tests,
    "ss-4103.json": ss4103_fec_tests
}

for filename, fec_list in fec_map.items():
    filepath = DATA_DIR / filename
    with open(filepath, 'r', encoding='utf-8') as f:
        existing = json.load(f)

    # Filter out any old FEC term tests if previously inserted
    filtered = [q for q in existing if not (q.get('exam') == 'term' and q.get('college') == 'FEC')]
    # Append the newly constructed FEC term tests
    filtered.extend(fec_list)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(filtered, f, indent=2, ensure_ascii=False)
    print(f"✓ Updated {filename} with {len(fec_list)} FEC Term Test papers (Total questions now: {len(filtered)}).")

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
print("✓ Successfully rebundled data/codex_data.js with all MEC, NITER, and FEC Term Tests!")
