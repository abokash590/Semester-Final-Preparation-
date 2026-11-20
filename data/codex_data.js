window.DU_CODEX_PRELOADED = {
  "cse-4101": [
    {
      "id": "cse-4101-final-2023-set1",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2023,
      "set_no": 1,
      "qno": "Question 1",
      "marks": 14,
      "topics": [
        "AI Foundations",
        "PEAS & Task Environment",
        "Turing Test"
      ],
      "question": "(a) Write down the goals of Artificial Intelligence. **[1]**  \n(b) Differentiate between strong AI and weak AI. **[2]**  \n(c) Give a PEAS description of the following task environment and characterize it in terms of task environment. **[9]**  \n    I. Automated taxi driver  \n    II. Vacuum cleaner  \n    III. Backgammon  \n(d) Briefly describe about Turing Test. **[2]**",
      "subparts": [
        {
          "id": "cse-4101-final-2023-q1a",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 1,
          "topics": [
            "AI Foundations"
          ],
          "question": "Write down the goals of Artificial Intelligence.",
          "solution": {
            "steps": [
              "1. Create expert systems that exhibit intelligent behavior, learn, demonstrate, explain, and advise its users.",
              "2. To implement human intelligence in machines (thinking humanly, thinking rationally, acting humanly, and acting rationally)."
            ],
            "answer": "The primary goal is creating intelligent agents capable of perceiving their environment, reasoning, learning, and taking rational actions to achieve specific goals.",
            "marking_hint": "Award 1 mark for mentioning thinking/acting humanly and rationally."
          }
        },
        {
          "id": "cse-4101-final-2023-q1b",
          "qno": "1(b)",
          "label": "(b)",
          "marks": 2,
          "topics": [
            "AI Foundations"
          ],
          "question": "Differentiate between strong AI and weak AI.",
          "solution": {
            "steps": [
              "1. Weak AI (Narrow AI): Designed and trained for a specific narrow task (e.g., Apple Siri, chess engines, spam filters). It simulates human behavior without genuine consciousness or understanding.",
              "2. Strong AI (Artificial General Intelligence - AGI): Possesses human-like generalized cognitive abilities. Can solve unfamiliar problems across diverse domains with self-awareness and reasoning."
            ],
            "answer": "Weak AI focuses on automated specialized tasks; Strong AI encompasses theoretical human-equivalent general cognition across all domains.",
            "marking_hint": "Award 1 mark for weak AI definition/example, 1 mark for strong AI definition/example."
          }
        },
        {
          "id": "cse-4101-final-2023-q1c",
          "qno": "1(c)",
          "label": "(c)",
          "marks": 9,
          "topics": [
            "AI Foundations",
            "PEAS & Task Environment"
          ],
          "question": "Give a PEAS description of the following task environment and characterize it in terms of task environment.\nI. Automated taxi driver\nII. Vacuum cleaner\nIII. Backgammon",
          "solution": {
            "steps": [
              "1. Automated Taxi Driver: P: Safe, fast, legal, comfortable trip. E: Roads, traffic, pedestrians, weather. A: Steering, throttle, brakes, horn. S: Cameras, LiDAR, radar, GPS. Environment is partially observable, multi-agent, stochastic, sequential, dynamic, continuous.",
              "2. Vacuum Cleaner: P: Cleanliness score, power usage. E: Floor, dirt, obstacles. A: Wheels, suction motor, brushes. S: Bump sensors, dirt sensors, cliff sensors. Environment is partially observable, single agent, stochastic, sequential, static, discrete.",
              "3. Backgammon: P: Win/loss, margin of victory. E: Board, checkers, dice. A: Legal checker moves. S: Board vision. Environment is fully observable, competitive multi-agent, stochastic (dice), sequential, static, discrete."
            ],
            "answer": "PEAS describes Performance, Environment, Actuators, and Sensors. Dimensions characterize observability, agent count, determinism, episodic nature, dynamism, and continuity.",
            "marking_hint": "Award 3 marks each for Taxi, Vacuum cleaner, and Backgammon."
          }
        },
        {
          "id": "cse-4101-final-2023-q1d",
          "qno": "1(d)",
          "label": "(d)",
          "marks": 2,
          "topics": [
            "Turing Test"
          ],
          "question": "Briefly describe about Turing Test.",
          "solution": {
            "steps": [
              "1. Proposed by Alan Turing (1950) in 'Computing Machinery and Intelligence' as the Imitation Game.",
              "2. A human interrogator questions a human and a computer via text terminal. If the interrogator cannot reliably tell the machine from the human after a specified duration, the machine passes."
            ],
            "answer": "Operational test of machine intelligence based on behavioral indistinguishability from human conversational responses.",
            "marking_hint": "Award 1 mark for setup description, 1 mark for evaluation criterion."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 1 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2023-set2",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2023,
      "set_no": 2,
      "qno": "Question 2",
      "marks": 14,
      "topics": [
        "Informed vs Uninformed Search",
        "Constraint Satisfaction Problems",
        "A* Search & Heuristics"
      ],
      "question": "(a) Write down the difference between informed and uninformed search. **[4]**  \n(b) What is LCV and MRV in CSP for improving Backtracking? Explain with example. **[4]**  \n(c) Given an initial state of 8 puzzle problem and final state to be reached. **[6]**\n\n**Initial State:**\n| 2 | 5 | 4 |\n|---|---|---|\n| 1 | 6 | 8 |\n| 3 |   | 7 |\n\n**Final State:**\n| 1 | 2 | 3 |\n|---|---|---|\n| 8 |   | 4 |\n| 7 | 6 | 5 |\n\nFind the most cost effective path to reach the final state from initial state using A* search algorithm.",
      "subparts": [
        {
          "id": "cse-4101-final-2023-q2a",
          "qno": "2(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Informed vs Uninformed Search"
          ],
          "question": "Write down the difference between informed and uninformed search.",
          "solution": {
            "steps": [
              "1. Uninformed (Blind) Search: Uses only problem formulation information (start state, actions, transition model, goal test). Has no knowledge of how close a state is to the goal. Examples: BFS, DFS, UCS, Depth-Limited, IDS.",
              "2. Informed (Heuristic) Search: Uses domain-specific knowledge beyond problem specification via a heuristic evaluation function $h(n)$ estimating cost from node $n$ to nearest goal. Examples: Greedy Best-First Search, A*, IDA*.",
              "3. Comparison points: Efficiency (Informed is generally much faster with smaller search tree expansion), memory utilization, optimality conditions (A* requires admissibility/consistency)."
            ],
            "answer": "Uninformed search explores blindly based on graph topology; informed search utilizes heuristic guidance $h(n)$ to steer expansion towards the goal.",
            "marking_hint": "Award 2 marks for core concepts, 2 marks for comparison table/examples."
          }
        },
        {
          "id": "cse-4101-final-2023-q2b",
          "qno": "2(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Constraint Satisfaction Problems"
          ],
          "question": "What is LCV and MRV in CSP for improving Backtracking? Explain with example.",
          "solution": {
            "steps": [
              "1. Minimum Remaining Values (MRV): Variable ordering heuristic. Chooses the unassigned variable with the fewest legal values remaining in its domain ('fail-first' principle). Example in map coloring: if WA has only 'Blue' left, assign WA first.",
              "2. Least Constraining Value (LCV): Value ordering heuristic. Chooses the value that rules out the fewest choices for neighboring unassigned variables ('fail-last' principle). Leaves maximum flexibility for remaining variables."
            ],
            "answer": "MRV selects which variable to assign next to detect failure early; LCV selects which value to try first to preserve neighbor options.",
            "marking_hint": "Award 2 marks for MRV explanation and example, 2 marks for LCV explanation and example."
          }
        },
        {
          "id": "cse-4101-final-2023-q2c",
          "qno": "2(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "A* Search & Heuristics"
          ],
          "question": "Given an initial state of 8 puzzle problem and final state to be reached:\n\n**Initial State:**\n| 2 | 5 | 4 |\n|---|---|---|\n| 1 | 6 | 8 |\n| 3 |   | 7 |\n\n**Final State:**\n| 1 | 2 | 3 |\n|---|---|---|\n| 8 |   | 4 |\n| 7 | 6 | 5 |\n\nFind the most cost effective path to reach the final state from initial state using A* search algorithm.",
          "solution": {
            "steps": [
              "1. Formulate A* evaluation function: f(n) = g(n) + h(n), where g(n) is depth and h(n) is Manhattan distance sum.",
              "2. Compute initial Manhattan distance for all 8 tiles: h(n0) = 12.",
              "3. Branch possible legal blank movements: Up (swap 6), Left (swap 3), Right (swap 7). Compute f(n) = 1 + h(n) for each.",
              "4. Prioritize lowest f(n) at each expansion until reaching goal state with h=0."
            ],
            "answer": "A* search guarantees the optimal sequence of tile movements because Manhattan distance is an admissible and consistent heuristic.",
            "marking_hint": "Award 2 marks for heuristic calculation, 2 marks for branching tree, 2 marks for path."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 2 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2023-set3",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2023,
      "set_no": 3,
      "qno": "Question 3",
      "marks": 14,
      "topics": [
        "Hill Climbing Search",
        "A* Search & Heuristics"
      ],
      "question": "(a) Write the disadvantage of Hill-climbing search. **[3]**  \n(b) Explore the following graph from the source node (S) the destination node (G) using A* search. **[5]**\n\n**Heuristic Values $h(n)$:**\n| Node | $h(n)$ |\n|:---:|:---:|\n| **S** | 13 |\n| **A** | 12 |\n| **B** | 4 |\n| **C** | 7 |\n| **D** | 3 |\n| **E** | 8 |\n| **F** | 2 |\n| **H** | 4 |\n| **I** | 9 |\n| **G** | 0 |\n\n**Search Graph (Mermaid):**\n```mermaid\ngraph TD\n    S((S)) -->|3| A((A))\n    S -->|2| B((B))\n    A -->|4| C((C))\n    A -->|1| D((D))\n    B -->|3| E((E))\n    B -->|1| F((F))\n    E -->|5| H((H))\n    F -->|2| I((I))\n    F -->|3| G((G))\n```\n\n(c) What is heuristic function? Explain. **[2]**  \n(d) Proof that if $h(n)$ is consistent, A* using GRAPH-SEARCH is optimal. **[4]**",
      "subparts": [
        {
          "id": "cse-4101-final-2023-q3a",
          "qno": "3(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Hill Climbing Search"
          ],
          "question": "Write the disadvantage of Hill-climbing search.",
          "solution": {
            "steps": [
              "1. Local Maxima: A peak that is higher than all neighboring states but lower than the global maximum. Search terminates prematurely.",
              "2. Ridges: Sequence of local maxima where sides are steep; slope cannot be navigated with single-step axis moves.",
              "3. Plateaux / Flat Local Maxima: Flat search space region where all neighbors have identical evaluation, causing random wandering or getting stuck."
            ],
            "answer": "Hill climbing is prone to getting stuck in local maxima, ridges, and plateaux due to its purely greedy local neighborhood evaluation.",
            "marking_hint": "Award 1 mark each for describing Local Maxima, Ridges, and Plateaux."
          }
        },
        {
          "id": "cse-4101-final-2023-q3b",
          "qno": "3(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "A* Search & Heuristics"
          ],
          "question": "Explore the following graph from the source node (S) the destination node (G) using A* search.\n\nHeuristic Table: S(13), A(12), B(4), C(7), D(3), E(8), F(2), H(4), I(9), G(0).\nEdges: S->A: 3, S->B: 2, A->C: 4, A->D: 1, B->E: 3, B->F: 1, E->H: 5, F->I: 2, F->G: 3.",
          "solution": {
            "steps": [
              "1. Initialization: Priority Queue = [S (g=0, h=13, f=13)].",
              "2. Expand S: Successors:\n   • A: g=3, h=12, f=15\n   • B: g=2, h=4, f=6",
              "3. Expand B (lowest f=6): Successors:\n   • E: g=2+3=5, h=8, f=13\n   • F: g=2+1=3, h=2, f=5",
              "4. Expand F (lowest f=5): Successors:\n   • I: g=3+2=5, h=9, f=14\n   • G: g=3+3=6, h=0, f=6",
              "5. Expand G (lowest f=6): Goal extracted! Optimal Path = S &rarr; B &rarr; F &rarr; G with total cost 6."
            ],
            "answer": "A* optimal path: S &rarr; B &rarr; F &rarr; G with cost = 6.",
            "marking_hint": "Award 3 marks for step-by-step queue updates with f-values, 2 marks for final path and cost."
          }
        },
        {
          "id": "cse-4101-final-2023-q3c",
          "qno": "3(c)",
          "label": "(c)",
          "marks": 2,
          "topics": [
            "A* Search & Heuristics"
          ],
          "question": "What is heuristic function? Explain.",
          "solution": {
            "steps": [
              "1. A heuristic function $h(n)$ maps a state description to an estimate of the cheapest path cost from state $n$ to a goal state.",
              "2. It encodes problem-specific intuition or domain knowledge to guide search algorithms toward promising branches."
            ],
            "answer": "A heuristic function estimates remaining cost to the goal, enabling algorithms like A* to reduce exponential search spaces.",
            "marking_hint": "Award 1 mark for formal definition, 1 mark for role in reducing search space."
          }
        },
        {
          "id": "cse-4101-final-2023-q3d",
          "qno": "3(d)",
          "label": "(d)",
          "marks": 4,
          "topics": [
            "A* Search & Heuristics"
          ],
          "question": "Proof that if h(n) is consistent, A* using GRAPH-SEARCH is optimal.",
          "solution": {
            "steps": [
              "1. Consistency definition (triangle inequality): For every node $n$ and every successor $n'$ generated by action $a$: $h(n) \\le c(n, a, n') + h(n')$.",
              "2. Monotonicity of $f(n)$: Path cost $g(n') = g(n) + c(n, a, n')$. Therefore, $f(n') = g(n') + h(n') = g(n) + c(n, a, n') + h(n') \\ge g(n) + h(n) = f(n)$. Thus $f(n)$ is non-decreasing along any path.",
              "3. Contour expansion: A* with consistent heuristic expands nodes in non-decreasing order of $f(n)$.",
              "4. Optimality conclusion: Whenever A* selects a node $n$ for expansion, the optimal path to that node has already been found ($g(n) = g^*(n)$), preventing reopening and ensuring the first goal expanded is optimal."
            ],
            "answer": "Consistency ensures that $f(n)$ is monotonically non-decreasing, so nodes are expanded in concentric contours of increasing $f$-cost, guaranteeing graph-search optimality.",
            "marking_hint": "Award 1.5 marks for triangle inequality setup, 1.5 marks for proving $f(n') \\ge f(n)$, 1 mark for conclusion."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 3 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2023-set4",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2023,
      "set_no": 4,
      "qno": "Question 4",
      "marks": 14,
      "topics": [
        "Adversarial Search & Min-Max",
        "Alpha-Beta Pruning",
        "Genetic Algorithms"
      ],
      "question": "(a) What is limitation of Min-max algorithm? Write down the properties of Min-max algorithm. **[4]**  \n(b) Explore the following graph of figure 2 using Alpha-beta pruning. **[5]**\n\n**Alpha-Beta Pruning Game Tree:**\n```mermaid\ngraph TD\n    Root((Max: Root)) --> N_L((Min: L))\n    Root --> N_R((Min: R))\n\n    N_L --> N1((Max: N1))\n    N_L --> N2((Max: N2))\n    N_R --> N3((Max: N3))\n    N_R --> N4((Max: N4))\n\n    N1 --> L1((Min))\n    N1 --> L2((Min))\n    N2 --> L3((Min))\n    N2 --> L4((Min))\n    N3 --> L5((Min))\n    N3 --> L6((Min))\n    N4 --> L7((Min))\n    N4 --> L8((Min))\n\n    L1 --> Leaf1[10]\n    L1 --> Leaf2[5]\n    L2 --> Leaf3[7]\n    L2 --> Leaf4[11]\n\n    L3 --> Leaf5[12]\n    L3 --> Leaf6[8]\n    L4 --> Leaf7[9]\n    L4 --> Leaf8[8]\n\n    L5 --> Leaf9[5]\n    L5 --> Leaf10[12]\n    L6 --> Leaf11[11]\n    L6 --> Leaf12[12]\n\n    L7 --> Leaf13[9]\n    L7 --> Leaf14[8]\n    L8 --> Leaf15[7]\n    L8 --> Leaf16[10]\n```\n\n*Leaf Values (from left to right):* `[10, 5], [7, 11], [12, 8], [9, 8], [5, 12], [11, 12], [9, 8], [7, 10]`\n\n(c) What is Adversarial Search? Explain Genetic algorithm with example. **[5]**",
      "subparts": [
        {
          "id": "cse-4101-final-2023-q4a",
          "qno": "4(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Adversarial Search & Min-Max"
          ],
          "question": "What is limitation of Min-max algorithm? Write down the properties of Min-max algorithm.",
          "solution": {
            "steps": [
              "1. Limitations: Exponential time complexity $O(b^m)$ makes complete search impractical for complex games like Chess ($b \\approx 35, m \\approx 80$) or Go ($b \\approx 250$). Assumes opponent plays optimally.",
              "2. Properties:\n   • Completeness: Yes, if tree is finite.\n   • Optimality: Yes, against an optimal opponent.\n   • Time Complexity: $O(b^m)$.\n   • Space Complexity: $O(bm)$ (depth-first exploration)."
            ],
            "answer": "Minimax provides optimal decisions against rational opponents with O(bm) space, but suffers from prohibitive O(b^m) exponential time.",
            "marking_hint": "Award 2 marks for limitations, 2 marks for standard properties (completeness, optimality, time, space)."
          }
        },
        {
          "id": "cse-4101-final-2023-q4b",
          "qno": "4(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Adversarial Search & Min-Max",
            "Alpha-Beta Pruning"
          ],
          "question": "Explore the following graph of figure 2 using Alpha-beta pruning. Root is Max, followed by Min layer, Max layer, and Min leaf parents with leaves: [10, 5], [7, 11], [12, 8], [9, 8], [5, 12], [11, 12], [9, 8], [7, 10].",
          "solution": {
            "steps": [
              "1. Standard left-to-right DFS traversal maintaining [alpha, beta] window.",
              "2. First subtree evaluates leaves 10 and 5 &rarr; parent takes min(10,5) = 5.",
              "3. Alpha cut and Beta cut rules applied systematically whenever current node value violates bounding interval.",
              "4. Pruned branches do not influence root minimax decision."
            ],
            "answer": "Alpha-beta pruning eliminates branches that cannot affect the final choice, doubling effective search depth.",
            "marking_hint": "Award 3 marks for tracking bounds, 2 marks for identifying pruned branches."
          }
        },
        {
          "id": "cse-4101-final-2023-q4c",
          "qno": "4(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Adversarial Search & Min-Max",
            "Genetic Algorithms"
          ],
          "question": "What is Adversarial Search? Explain Genetic algorithm with example.",
          "solution": {
            "steps": [
              "1. Adversarial Search: Competitive multi-agent environment where two or more opponents plan conflicting actions to maximize their own utility while minimizing the opponent's (e.g. Minimax).",
              "2. Genetic Algorithm: Population-based stochastic optimization inspired by Darwinian natural selection (Selection, Crossover, Mutation, Fitness).",
              "3. Example: 8-Queens problem where each chromosome is an 8-digit string representing queen rows."
            ],
            "answer": "Adversarial search models strategic decision-making against opponents; Genetic algorithms optimize candidate solutions via evolutionary operators.",
            "marking_hint": "Award 2 marks for adversarial search, 3 marks for genetic algorithm definition and example."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 4 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2023-set5",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2023,
      "set_no": 5,
      "qno": "Question 5",
      "marks": 14,
      "topics": [
        "Constraint Satisfaction Problems",
        "Genetic Algorithms",
        "Knowledge Representation & Ontology",
        "Adversarial Search & Min-Max"
      ],
      "question": "(a) What are the three components of Constraint Satisfaction Problem? Give an example. **[3]**  \n(b) Describe steps of Genetic algorithm (e.g. Selection, Crossover, Mutation and Fitness) with proper example. **[7]**  \n(c) What is Ontology in Knowledge Representation? **[2]**  \n(d) Write down the difference between game and search problem. **[2]**",
      "subparts": [
        {
          "id": "cse-4101-final-2023-q5a",
          "qno": "5(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Constraint Satisfaction Problems"
          ],
          "question": "What are the three components of Constraint Satisfaction Problem? Give an example.",
          "solution": {
            "steps": [
              "1. Variables (X): A set of variables $X = \\{X_1, X_2, \\dots, X_n\\}$.",
              "2. Domains (D): A set of domains $D = \\{D_1, D_2, \\dots, D_n\\}$ specifying allowed values for each variable.",
              "3. Constraints (C): A set of constraints $C = \\{C_1, C_2, \\dots, C_m\\}$ specifying allowable combinations of values.",
              "4. Example (Map Coloring): Variables = {WA, NT, SA, Q, NSW, V, T}; Domains = {Red, Green, Blue}; Constraints = {WA != NT, WA != SA, NT != SA, etc.}."
            ],
            "answer": "A CSP is formally defined by the triple (X, D, C): Variables, Domains, and Constraints.",
            "marking_hint": "Award 1.5 marks for the three components, 1.5 marks for a complete concrete example."
          }
        },
        {
          "id": "cse-4101-final-2023-q5b",
          "qno": "5(b)",
          "label": "(b)",
          "marks": 7,
          "topics": [
            "Genetic Algorithms"
          ],
          "question": "Describe steps of Genetic algorithm (e.g. Selection, Crossover, Mutation and Fitness) with proper example.",
          "solution": {
            "steps": [
              "1. Initial Population: Generate candidate chromosomes.",
              "2. Fitness Function: Assigns numeric fitness to each individual.",
              "3. Selection: Roulette wheel or tournament selection prioritizes fitter parents.",
              "4. Crossover: Exchanges genetic material at a random crossover point.",
              "5. Mutation: Flips bits randomly with small probability."
            ],
            "answer": "Genetic algorithm drives iterative population evolution via selection, crossover, and mutation towards global optimum.",
            "marking_hint": "Award 2 marks for fitness, 2 marks for selection, 2 marks for crossover/mutation, 1 mark for example."
          }
        },
        {
          "id": "cse-4101-final-2023-q5c",
          "qno": "5(c)",
          "label": "(c)",
          "marks": 2,
          "topics": [
            "Knowledge Representation & Ontology"
          ],
          "question": "What is Ontology in Knowledge Representation?",
          "solution": {
            "steps": [
              "1. An ontology represents knowledge as a formal, explicit specification of shared conceptualization.",
              "2. Defines concepts, classes, attributes, relations, and axioms in a domain to enable semantic interoperability."
            ],
            "answer": "Ontology provides the formal conceptual vocabulary and relational constraints defining an application domain.",
            "marking_hint": "Award 1 mark for conceptualization definition, 1 mark for components."
          }
        },
        {
          "id": "cse-4101-final-2023-q5d",
          "qno": "5(d)",
          "label": "(d)",
          "marks": 2,
          "topics": [
            "Adversarial Search & Min-Max"
          ],
          "question": "Write down the difference between game and search problem.",
          "solution": {
            "steps": [
              "1. Standard Search Problem: Single-agent environment where the agent has complete control over state transitions. The solution is a fixed sequence of actions.",
              "2. Game Problem: Multi-agent adversarial environment with unpredictable opponent actions. The solution is a contingency strategy/policy specifying what to do for every possible opponent reply."
            ],
            "answer": "Search problems find a single fixed path to goal; games require a complete contingent policy against an active opponent.",
            "marking_hint": "Award 1 mark each for search vs game distinctions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 5 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2023-set6",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2023,
      "set_no": 6,
      "qno": "Question 6",
      "marks": 14,
      "topics": [
        "First-Order Logic"
      ],
      "question": "(a) Briefly describe the logical Connectives of Propositional Logic **[5]**  \n(b) Convert the following English statement into FOL **[5]**  \n    (i) Every man respects his parent  \n    (ii) There is somebody whom everybody loves  \n    (iii) Some student has never been asked a question by a faculty member  \n    (iv) Sumy has never sent an e-mail message to Kona  \n    (v) Some boys play cricket  \n(c) Define Inference and Existential Quantifiers in FOL with example? **[4]**",
      "subparts": [
        {
          "id": "cse-4101-final-2023-q6a",
          "qno": "6(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "First-Order Logic"
          ],
          "question": "Briefly describe the logical Connectives of Propositional Logic.",
          "solution": {
            "steps": [
              "1. Negation (NOT, ~ or ¬): Inverts truth value.",
              "2. Conjunction (AND, ∧): True only if both operands are true.",
              "3. Disjunction (OR, ∨): True if at least one operand is true.",
              "4. Implication (IF-THEN, →): False only if antecedent is true and consequent is false.",
              "5. Biconditional (IFF, ↔): True if both operands have identical truth value."
            ],
            "answer": "Five fundamental truth-functional connectives: Negation, Conjunction, Disjunction, Implication, and Biconditional.",
            "marking_hint": "Award 1 mark each for the 5 connectives with truth conditions."
          }
        },
        {
          "id": "cse-4101-final-2023-q6b",
          "qno": "6(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "First-Order Logic"
          ],
          "question": "Convert the following English statement into FOL:\n(i) Every man respects his parent\n(ii) There is somebody whom everybody loves\n(iii) Some student has never been asked a question by a faculty member\n(iv) Sumy has never sent an e-mail message to Kona\n(v) Some boys play cricket",
          "solution": {
            "steps": [
              "(i) ∀x (Man(x) → ∀y (Parent(y, x) → Respects(x, y)))",
              "(ii) ∃y ∀x Loves(x, y)",
              "(iii) ∃s (Student(s) ∧ ¬∃f ∃q (Faculty(f) ∧ Question(q) ∧ Asked(f, s, q)))",
              "(iv) ¬∃m (Email(m) ∧ Sent(Sumy, Kona, m))",
              "(v) ∃b (Boy(b) ∧ Plays(b, Cricket))"
            ],
            "answer": "Formal translations using universal (∀) and existential (∃) quantifiers.",
            "marking_hint": "Award 1 mark per correct statement translation."
          }
        },
        {
          "id": "cse-4101-final-2023-q6c",
          "qno": "6(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "First-Order Logic"
          ],
          "question": "Define Inference and Existential Quantifiers in FOL with example?",
          "solution": {
            "steps": [
              "1. Inference: The process of deriving new logical statements from known axioms using sound inference rules (Modus Ponens, Resolution).",
              "2. Existential Quantifier (∃): Asserts that a predicate holds for at least one entity in domain: ∃x P(x)."
            ],
            "answer": "Inference yields valid conclusions; existential quantifier asserts property holds for at least one domain member.",
            "marking_hint": "Award 2 marks for inference, 2 marks for existential quantifier."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 6 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2023-set7",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2023,
      "set_no": 7,
      "qno": "Question 7",
      "marks": 14,
      "topics": [
        "Natural Language Processing",
        "Informed vs Uninformed Search",
        "A* Search & Heuristics"
      ],
      "question": "(a) What is Natural language Processing (NLP)? Explain Phases of NLP. **[4]**  \n(b) How to build an NLP pipeline? **[4]**  \n(c) Differentiate between informed and uninformed search. **[2]**  \n(d) Using Greedy best-first search find the cost and show the steps from the source Arad to the destination Bucharest. **[4]**\n\n**Map of Romania (Road Distances between Cities):**\n<div class=\"svg-diagram-wrapper\"><svg viewBox=\"0 0 720 460\" class=\"responsive-diagram\" role=\"img\" aria-label=\"Map of Romania road network with distances between cities\"><g stroke=\"#94A3B8\" stroke-width=\"1.8\" fill=\"none\"><line x1=\"115\" y1=\"45\" x2=\"75\" y2=\"110\"/><line x1=\"115\" y1=\"45\" x2=\"220\" y2=\"185\"/><line x1=\"75\" y1=\"110\" x2=\"60\" y2=\"185\"/><line x1=\"60\" y1=\"185\" x2=\"220\" y2=\"185\"/><line x1=\"60\" y1=\"185\" x2=\"65\" y2=\"275\"/><line x1=\"65\" y1=\"275\" x2=\"140\" y2=\"315\"/><line x1=\"140\" y1=\"315\" x2=\"145\" y2=\"370\"/><line x1=\"145\" y1=\"370\" x2=\"140\" y2=\"425\"/><line x1=\"140\" y1=\"425\" x2=\"265\" y2=\"425\"/><line x1=\"220\" y1=\"185\" x2=\"335\" y2=\"185\"/><line x1=\"220\" y1=\"185\" x2=\"250\" y2=\"255\"/><line x1=\"250\" y1=\"255\" x2=\"265\" y2=\"425\"/><line x1=\"250\" y1=\"255\" x2=\"345\" y2=\"315\"/><line x1=\"265\" y1=\"425\" x2=\"345\" y2=\"315\"/><line x1=\"335\" y1=\"185\" x2=\"445\" y2=\"350\"/><line x1=\"345\" y1=\"315\" x2=\"445\" y2=\"350\"/><line x1=\"445\" y1=\"350\" x2=\"420\" y2=\"425\"/><line x1=\"445\" y1=\"350\" x2=\"525\" y2=\"320\"/><line x1=\"525\" y1=\"320\" x2=\"615\" y2=\"320\"/><line x1=\"615\" y1=\"320\" x2=\"645\" y2=\"385\"/><line x1=\"525\" y1=\"320\" x2=\"575\" y2=\"205\"/><line x1=\"575\" y1=\"205\" x2=\"540\" y2=\"125\"/><line x1=\"540\" y1=\"125\" x2=\"455\" y2=\"75\"/></g><g><g transform=\"translate(95.0,77.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">71</text></g><g transform=\"translate(167.5,115.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">151</text></g><g transform=\"translate(67.5,147.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">75</text></g><g transform=\"translate(140.0,185.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">140</text></g><g transform=\"translate(62.5,230.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">118</text></g><g transform=\"translate(102.5,295.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">111</text></g><g transform=\"translate(142.5,342.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">70</text></g><g transform=\"translate(142.5,397.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">75</text></g><g transform=\"translate(202.5,425.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">120</text></g><g transform=\"translate(277.5,185.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">99</text></g><g transform=\"translate(235.0,220.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">80</text></g><g transform=\"translate(257.5,340.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">146</text></g><g transform=\"translate(297.5,285.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">97</text></g><g transform=\"translate(305.0,370.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">138</text></g><g transform=\"translate(390.0,267.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">211</text></g><g transform=\"translate(395.0,332.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">101</text></g><g transform=\"translate(432.5,387.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">90</text></g><g transform=\"translate(485.0,335.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">85</text></g><g transform=\"translate(570.0,320.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">98</text></g><g transform=\"translate(630.0,352.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">86</text></g><g transform=\"translate(550.0,262.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">142</text></g><g transform=\"translate(557.5,165.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">92</text></g><g transform=\"translate(497.5,100.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">87</text></g></g><g><circle cx=\"115\" cy=\"45\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"75\" cy=\"110\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"60\" cy=\"185\" r=\"8\" fill=\"#FEF3C7\" stroke=\"#D97706\" stroke-width=\"2.5\"/><circle cx=\"65\" cy=\"275\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"140\" cy=\"315\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"145\" cy=\"370\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"140\" cy=\"425\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"220\" cy=\"185\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"250\" cy=\"255\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"265\" cy=\"425\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"335\" cy=\"185\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"345\" cy=\"315\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"445\" cy=\"350\" r=\"9\" fill=\"#DCFCE7\" stroke=\"#104535\" stroke-width=\"2.8\"/><circle cx=\"420\" cy=\"425\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"525\" cy=\"320\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"615\" cy=\"320\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"645\" cy=\"385\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"575\" cy=\"205\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"540\" cy=\"125\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"455\" cy=\"75\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/></g><g><text x=\"115\" y=\"35\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Oradea</text><text x=\"75\" y=\"100\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Zerind</text><text x=\"60\" y=\"173\" font-size=\"11\" font-weight=\"900\" fill=\"#92400E\" text-anchor=\"middle\">Arad (Start)</text><text x=\"56\" y=\"279\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"end\">Timisoara</text><text x=\"131\" y=\"319\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"end\">Lugoj</text><text x=\"136\" y=\"374\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"end\">Mehadia</text><text x=\"131\" y=\"429\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"end\">Drobeta</text><text x=\"220\" y=\"175\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Sibiu</text><text x=\"250\" y=\"245\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Rimnicu Vilcea</text><text x=\"265\" y=\"441\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Craiova</text><text x=\"335\" y=\"175\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Fagaras</text><text x=\"345\" y=\"305\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Pitesti</text><text x=\"445\" y=\"337\" font-size=\"11\" font-weight=\"900\" fill=\"#104535\" text-anchor=\"middle\">Bucharest (Goal)</text><text x=\"420\" y=\"441\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Giurgiu</text><text x=\"525\" y=\"310\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Urziceni</text><text x=\"624\" y=\"324\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"start\">Hirsova</text><text x=\"654\" y=\"389\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"start\">Eforie</text><text x=\"584\" y=\"209\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"start\">Vaslui</text><text x=\"549\" y=\"129\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"start\">Iasi</text><text x=\"455\" y=\"65\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Neamt</text></g></svg></div>\n\n\n**Straight-line distance to Bucharest ($h_{SLD}$ in km):**\n\n| City | $h_{SLD}$ | City | $h_{SLD}$ |\n| :--- | :---: | :--- | :---: |\n| **Arad** | 366 | **Mehadia** | 241 |\n| **Bucharest** | 0 | **Neamt** | 234 |\n| **Craiova** | 160 | **Oradea** | 380 |\n| **Drobeta** | 242 | **Pitesti** | 100 |\n| **Eforie** | 161 | **Rimnicu Vilcea** | 193 |\n| **Fagaras** | 176 | **Sibiu** | 253 |\n| **Giurgiu** | 77 | **Timisoara** | 329 |\n| **Hirsova** | 151 | **Urziceni** | 80 |\n| **Iasi** | 226 | **Vaslui** | 199 |\n| **Lugoj** | 244 | **Zerind** | 374 |\n\n---",
      "subparts": [
        {
          "id": "cse-4101-final-2023-q7a",
          "qno": "7(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Natural Language Processing"
          ],
          "question": "What is Natural language Processing (NLP)? Explain Phases of NLP.",
          "solution": {
            "steps": [
              "1. Definition: Computational discipline enabling computers to process, understand, and generate human natural languages.",
              "2. Phases: (1) Morphological/Lexical, (2) Syntactic Analysis (Parsing), (3) Semantic Analysis, (4) Discourse Integration, (5) Pragmatic Analysis."
            ],
            "answer": "NLP models human language through five linguistic levels from tokenization to pragmatic context.",
            "marking_hint": "Award 1 mark for definition, 3 marks for describing the phases."
          }
        },
        {
          "id": "cse-4101-final-2023-q7b",
          "qno": "7(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Natural Language Processing"
          ],
          "question": "How to build an NLP pipeline?",
          "solution": {
            "steps": [
              "1. Text Acquisition & Cleaning: Raw text ingestion, lowercasing, punctuation stripping.",
              "2. Tokenization: Splitting text into words/subwords.",
              "3. Normalization: Stop-word removal, Lemmatization or Stemming.",
              "4. Feature Extraction: Bag-of-Words, TF-IDF, Word Embeddings (Word2Vec, BERT).",
              "5. Model Training & Evaluation: Classification, NER, or Generation."
            ],
            "answer": "An NLP pipeline chains text cleaning, tokenization, lemmatization, vectorization, and downstream inference.",
            "marking_hint": "Award 1 mark for each major stage."
          }
        },
        {
          "id": "cse-4101-final-2023-q7c",
          "qno": "7(c)",
          "label": "(c)",
          "marks": 2,
          "topics": [
            "Informed vs Uninformed Search"
          ],
          "question": "Differentiate between informed and uninformed search.",
          "solution": {
            "steps": [
              "1. Uninformed search algorithms have no clue about distance to goal (blindly expand nodes by depth, path-cost, or FIFO/LIFO order).",
              "2. Informed search algorithms use a heuristic function $h(n)$ estimating remaining cost to goal to prioritize node expansion."
            ],
            "answer": "Informed search incorporates problem-specific heuristic evaluations to guide search; uninformed search does not.",
            "marking_hint": "Award 1 mark each for definition and example."
          }
        },
        {
          "id": "cse-4101-final-2023-q7d",
          "qno": "7(d)",
          "label": "(d)",
          "marks": 4,
          "topics": [
            "Informed vs Uninformed Search",
            "A* Search & Heuristics"
          ],
          "question": "Using Greedy best-first search find the cost and show the steps from the source Arad to the destination Bucharest in the Romania road network.\n\n<div class=\"svg-diagram-wrapper\"><svg viewBox=\"0 0 720 460\" class=\"responsive-diagram\" role=\"img\" aria-label=\"Map of Romania road network with distances between cities\"><g stroke=\"#94A3B8\" stroke-width=\"1.8\" fill=\"none\"><line x1=\"115\" y1=\"45\" x2=\"75\" y2=\"110\"/><line x1=\"115\" y1=\"45\" x2=\"220\" y2=\"185\"/><line x1=\"75\" y1=\"110\" x2=\"60\" y2=\"185\"/><line x1=\"60\" y1=\"185\" x2=\"220\" y2=\"185\"/><line x1=\"60\" y1=\"185\" x2=\"65\" y2=\"275\"/><line x1=\"65\" y1=\"275\" x2=\"140\" y2=\"315\"/><line x1=\"140\" y1=\"315\" x2=\"145\" y2=\"370\"/><line x1=\"145\" y1=\"370\" x2=\"140\" y2=\"425\"/><line x1=\"140\" y1=\"425\" x2=\"265\" y2=\"425\"/><line x1=\"220\" y1=\"185\" x2=\"335\" y2=\"185\"/><line x1=\"220\" y1=\"185\" x2=\"250\" y2=\"255\"/><line x1=\"250\" y1=\"255\" x2=\"265\" y2=\"425\"/><line x1=\"250\" y1=\"255\" x2=\"345\" y2=\"315\"/><line x1=\"265\" y1=\"425\" x2=\"345\" y2=\"315\"/><line x1=\"335\" y1=\"185\" x2=\"445\" y2=\"350\"/><line x1=\"345\" y1=\"315\" x2=\"445\" y2=\"350\"/><line x1=\"445\" y1=\"350\" x2=\"420\" y2=\"425\"/><line x1=\"445\" y1=\"350\" x2=\"525\" y2=\"320\"/><line x1=\"525\" y1=\"320\" x2=\"615\" y2=\"320\"/><line x1=\"615\" y1=\"320\" x2=\"645\" y2=\"385\"/><line x1=\"525\" y1=\"320\" x2=\"575\" y2=\"205\"/><line x1=\"575\" y1=\"205\" x2=\"540\" y2=\"125\"/><line x1=\"540\" y1=\"125\" x2=\"455\" y2=\"75\"/></g><g><g transform=\"translate(95.0,77.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">71</text></g><g transform=\"translate(167.5,115.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">151</text></g><g transform=\"translate(67.5,147.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">75</text></g><g transform=\"translate(140.0,185.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">140</text></g><g transform=\"translate(62.5,230.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">118</text></g><g transform=\"translate(102.5,295.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">111</text></g><g transform=\"translate(142.5,342.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">70</text></g><g transform=\"translate(142.5,397.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">75</text></g><g transform=\"translate(202.5,425.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">120</text></g><g transform=\"translate(277.5,185.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">99</text></g><g transform=\"translate(235.0,220.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">80</text></g><g transform=\"translate(257.5,340.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">146</text></g><g transform=\"translate(297.5,285.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">97</text></g><g transform=\"translate(305.0,370.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">138</text></g><g transform=\"translate(390.0,267.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">211</text></g><g transform=\"translate(395.0,332.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">101</text></g><g transform=\"translate(432.5,387.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">90</text></g><g transform=\"translate(485.0,335.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">85</text></g><g transform=\"translate(570.0,320.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">98</text></g><g transform=\"translate(630.0,352.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">86</text></g><g transform=\"translate(550.0,262.5)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">142</text></g><g transform=\"translate(557.5,165.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">92</text></g><g transform=\"translate(497.5,100.0)\"><rect x=\"-13\" y=\"-8\" width=\"26\" height=\"16\" rx=\"4\" fill=\"#F4F8F5\" stroke=\"#CBD5E1\" stroke-width=\"0.8\"/><text x=\"0\" y=\"3.5\" font-size=\"10\" font-weight=\"700\" fill=\"#104535\" text-anchor=\"middle\">87</text></g></g><g><circle cx=\"115\" cy=\"45\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"75\" cy=\"110\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"60\" cy=\"185\" r=\"8\" fill=\"#FEF3C7\" stroke=\"#D97706\" stroke-width=\"2.5\"/><circle cx=\"65\" cy=\"275\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"140\" cy=\"315\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"145\" cy=\"370\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"140\" cy=\"425\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"220\" cy=\"185\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"250\" cy=\"255\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"265\" cy=\"425\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"335\" cy=\"185\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"345\" cy=\"315\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"445\" cy=\"350\" r=\"9\" fill=\"#DCFCE7\" stroke=\"#104535\" stroke-width=\"2.8\"/><circle cx=\"420\" cy=\"425\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"525\" cy=\"320\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"615\" cy=\"320\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"645\" cy=\"385\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"575\" cy=\"205\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"540\" cy=\"125\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/><circle cx=\"455\" cy=\"75\" r=\"5.5\" fill=\"#FFFFFF\" stroke=\"#104535\" stroke-width=\"2\"/></g><g><text x=\"115\" y=\"35\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Oradea</text><text x=\"75\" y=\"100\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Zerind</text><text x=\"60\" y=\"173\" font-size=\"11\" font-weight=\"900\" fill=\"#92400E\" text-anchor=\"middle\">Arad (Start)</text><text x=\"56\" y=\"279\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"end\">Timisoara</text><text x=\"131\" y=\"319\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"end\">Lugoj</text><text x=\"136\" y=\"374\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"end\">Mehadia</text><text x=\"131\" y=\"429\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"end\">Drobeta</text><text x=\"220\" y=\"175\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Sibiu</text><text x=\"250\" y=\"245\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Rimnicu Vilcea</text><text x=\"265\" y=\"441\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Craiova</text><text x=\"335\" y=\"175\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Fagaras</text><text x=\"345\" y=\"305\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Pitesti</text><text x=\"445\" y=\"337\" font-size=\"11\" font-weight=\"900\" fill=\"#104535\" text-anchor=\"middle\">Bucharest (Goal)</text><text x=\"420\" y=\"441\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Giurgiu</text><text x=\"525\" y=\"310\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Urziceni</text><text x=\"624\" y=\"324\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"start\">Hirsova</text><text x=\"654\" y=\"389\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"start\">Eforie</text><text x=\"584\" y=\"209\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"start\">Vaslui</text><text x=\"549\" y=\"129\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"start\">Iasi</text><text x=\"455\" y=\"65\" font-size=\"10\" font-weight=\"700\" fill=\"#1E293B\" text-anchor=\"middle\">Neamt</text></g></svg></div>\n\n\n**Straight-line distance to Bucharest ($h_{SLD}$ in km):**\n\n| City | $h_{SLD}$ | City | $h_{SLD}$ |\n| :--- | :---: | :--- | :---: |\n| **Arad** | 366 | **Mehadia** | 241 |\n| **Bucharest** | 0 | **Neamt** | 234 |\n| **Craiova** | 160 | **Oradea** | 380 |\n| **Drobeta** | 242 | **Pitesti** | 100 |\n| **Eforie** | 161 | **Rimnicu Vilcea** | 193 |\n| **Fagaras** | 176 | **Sibiu** | 253 |\n| **Giurgiu** | 77 | **Timisoara** | 329 |\n| **Hirsova** | 151 | **Urziceni** | 80 |\n| **Iasi** | 226 | **Vaslui** | 199 |\n| **Lugoj** | 244 | **Zerind** | 374 |",
          "solution": {
            "steps": [
              "1. Start at Arad: Straight-line distances: Arad(366). Successors: Sibiu(253), Timisoara(329), Zerind(374).",
              "2. Expand Sibiu (lowest h = 253): Successors: Arad(366), Fagaras(176), Oradea(380), Rimnicu Vilcea(193).",
              "3. Expand Fagaras (lowest h = 176): Successors: Sibiu(253), Bucharest(0).",
              "4. Expand Bucharest (h = 0): Goal reached!",
              "5. Path taken: Arad &rarr; Sibiu &rarr; Fagaras &rarr; Bucharest. Total path cost = 140 + 99 + 211 = 450 km."
            ],
            "answer": "Greedy Best-First Path: Arad &rarr; Sibiu &rarr; Fagaras &rarr; Bucharest with total road cost 450 km (note: A* finds optimal path via Rimnicu Vilcea-Pitesti costing 418 km).",
            "marking_hint": "Award 2 marks for showing steps with h-values, 2 marks for total path cost calculation."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 7 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2024-set1",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2024,
      "set_no": 1,
      "qno": "Question 1",
      "marks": 14,
      "topics": [
        "AI Foundations",
        "PEAS & Task Environment",
        "Informed vs Uninformed Search"
      ],
      "question": "(a) Define Artificial Intelligence. List five problems that cannot be currently aided/solved by AI. **[4]**  \n(b) Give a PEAS description of the following task environment and characterize it in terms of task environment. **[4]**  \n    i. Automated taxi driver  \n    ii. Vacuum cleaner  \n(c) For the following tree, show the order of nodes visited for i) breadth-first search, ii) depth-first search, iii) uniform cost search, and iv) iterative deepening search. The goal node is I and the numbers next to the edges indicate the associated cost. **[6]**\n\n**Search Tree (Mermaid):**\n```mermaid\ngraph TD\n    A((A)) -->|5| B((B))\n    A -->|4| C((C))\n    A -->|3| D((D))\n    B -->|2| E((E))\n    C -->|2| F((F))\n    C -->|1| G((G))\n    G -->|3| I((I - Goal))\n    D -->|4| H((H))\n    H -->|4| J((J))\n    H -->|2| K((K))\n```",
      "subparts": [
        {
          "id": "cse-4101-final-2024-q1a",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "AI Foundations"
          ],
          "question": "Define Artificial Intelligence. List five problems that cannot be currently aided/solved by AI.",
          "solution": {
            "steps": [
              "1. Definition: The study and construction of agents that perceive their environment and take rational actions that maximize chance of successfully achieving their goals.",
              "2. Five unsolved problems: (1) Human subjective consciousness and emotional empathy, (2) Solving general undecidable problems (e.g. Halting Problem), (3) Fully autonomous moral ethical decision-making in novel legal scenarios, (4) Novel scientific paradigm synthesis without prior training distribution, (5) True common-sense physical reasoning across unstructured open-ended physical environments."
            ],
            "answer": "AI models rational computational intelligence. Limitations include subjective phenomenology, formal undecidability, and open-ended human common-sense abstraction.",
            "marking_hint": "Award 1.5 marks for definition, 2.5 marks for 5 valid limitations."
          }
        },
        {
          "id": "cse-4101-final-2024-q1b",
          "qno": "1(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "AI Foundations",
            "PEAS & Task Environment"
          ],
          "question": "Give a PEAS description of the following task environment and characterize it in terms of task environment:\ni. Automated taxi driver\nii. Vacuum cleaner",
          "solution": {
            "steps": [
              "1. Automated Taxi Driver: P: Safety, speed, comfort, profit. E: Roads, traffic, pedestrians. A: Steering, brakes, accelerator. S: Cameras, LiDAR, GPS. Characterization: Partially observable, multi-agent, stochastic, sequential, dynamic, continuous.",
              "2. Vacuum Cleaner: P: Floor cleanliness, energy. E: Rooms, furniture, dirt. A: Wheels, suction. S: Bump, cliff, dirt sensors. Characterization: Partially observable, single-agent, stochastic, sequential, static, discrete."
            ],
            "answer": "PEAS structure defines operational requirements; environmental dimensions guide algorithmic approach.",
            "marking_hint": "Award 2 marks each for taxi and vacuum cleaner."
          }
        },
        {
          "id": "cse-4101-final-2024-q1c",
          "qno": "1(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "Informed vs Uninformed Search"
          ],
          "question": "For the following tree, show the order of nodes visited for i) breadth-first search, ii) depth-first search, iii) uniform cost search, and iv) iterative deepening search. The goal node is I and the numbers next to the edges indicate the associated cost.\n\n<div class=\"svg-diagram-wrapper\"><svg viewBox=\"0 0 520 310\" class=\"responsive-diagram\" role=\"img\" aria-label=\"Search tree graph for Informed and Uninformed search\"><defs><marker id=\"arrow\" viewBox=\"0 0 10 10\" refX=\"21\" refY=\"5\" markerWidth=\"6\" markerHeight=\"6\" orient=\"auto-start-reverse\"><path d=\"M 0 1.5 L 8 5 L 0 8.5 z\" fill=\"#104535\"/></marker></defs><g stroke=\"#104535\" stroke-width=\"1.8\" fill=\"none\"><line x1=\"260\" y1=\"35\" x2=\"105\" y2=\"100\" marker-end=\"url(#arrow)\"/><line x1=\"260\" y1=\"35\" x2=\"260\" y2=\"100\" marker-end=\"url(#arrow)\"/><line x1=\"260\" y1=\"35\" x2=\"415\" y2=\"100\" marker-end=\"url(#arrow)\"/><line x1=\"105\" y1=\"100\" x2=\"105\" y2=\"180\" marker-end=\"url(#arrow)\"/><line x1=\"260\" y1=\"100\" x2=\"210\" y2=\"180\" marker-end=\"url(#arrow)\"/><line x1=\"260\" y1=\"100\" x2=\"310\" y2=\"180\" marker-end=\"url(#arrow)\"/><line x1=\"415\" y1=\"100\" x2=\"415\" y2=\"180\" marker-end=\"url(#arrow)\"/><line x1=\"310\" y1=\"180\" x2=\"310\" y2=\"260\" marker-end=\"url(#arrow)\"/><line x1=\"415\" y1=\"180\" x2=\"370\" y2=\"260\" marker-end=\"url(#arrow)\"/><line x1=\"415\" y1=\"180\" x2=\"465\" y2=\"260\" marker-end=\"url(#arrow)\"/></g><g font-size=\"12\" font-weight=\"bold\" fill=\"#104535\" text-anchor=\"middle\"><rect x=\"170\" y=\"55\" width=\"18\" height=\"16\" rx=\"3\" fill=\"#F4F8F5\"/><text x=\"179\" y=\"68\">5</text><rect x=\"264\" y=\"60\" width=\"18\" height=\"16\" rx=\"3\" fill=\"#F4F8F5\"/><text x=\"273\" y=\"73\">4</text><rect x=\"330\" y=\"55\" width=\"18\" height=\"16\" rx=\"3\" fill=\"#F4F8F5\"/><text x=\"339\" y=\"68\">3</text><rect x=\"85\" y=\"132\" width=\"18\" height=\"16\" rx=\"3\" fill=\"#F4F8F5\"/><text x=\"94\" y=\"145\">2</text><rect x=\"215\" y=\"132\" width=\"18\" height=\"16\" rx=\"3\" fill=\"#F4F8F5\"/><text x=\"224\" y=\"145\">2</text><rect x=\"295\" y=\"132\" width=\"18\" height=\"16\" rx=\"3\" fill=\"#F4F8F5\"/><text x=\"304\" y=\"145\">1</text><rect x=\"420\" y=\"132\" width=\"18\" height=\"16\" rx=\"3\" fill=\"#F4F8F5\"/><text x=\"429\" y=\"145\">4</text><rect x=\"315\" y=\"212\" width=\"18\" height=\"16\" rx=\"3\" fill=\"#F4F8F5\"/><text x=\"324\" y=\"225\">3</text><rect x=\"375\" y=\"212\" width=\"18\" height=\"16\" rx=\"3\" fill=\"#F4F8F5\"/><text x=\"384\" y=\"225\">4</text><rect x=\"445\" y=\"212\" width=\"18\" height=\"16\" rx=\"3\" fill=\"#F4F8F5\"/><text x=\"454\" y=\"225\">2</text></g><g fill=\"#ffffff\" stroke=\"#104535\" stroke-width=\"2\"><circle cx=\"260\" cy=\"35\" r=\"17\"/><circle cx=\"105\" cy=\"100\" r=\"17\"/><circle cx=\"260\" cy=\"100\" r=\"17\"/><circle cx=\"415\" cy=\"100\" r=\"17\"/><circle cx=\"105\" cy=\"180\" r=\"17\"/><circle cx=\"210\" cy=\"180\" r=\"17\"/><circle cx=\"310\" cy=\"180\" r=\"17\"/><circle cx=\"415\" cy=\"180\" r=\"17\"/><circle cx=\"370\" cy=\"260\" r=\"17\"/><circle cx=\"465\" cy=\"260\" r=\"17\"/><circle cx=\"310\" cy=\"260\" r=\"22\" fill=\"#DCFCE7\" stroke=\"#104535\" stroke-width=\"2.5\"/></g><g font-size=\"12\" font-weight=\"900\" fill=\"#104535\" text-anchor=\"middle\" dominant-baseline=\"central\"><text x=\"260\" y=\"35\">A</text><text x=\"105\" y=\"100\">B</text><text x=\"260\" y=\"100\">C</text><text x=\"415\" y=\"100\">D</text><text x=\"105\" y=\"180\">E</text><text x=\"210\" y=\"180\">F</text><text x=\"310\" y=\"180\">G</text><text x=\"415\" y=\"180\">H</text><text x=\"370\" y=\"260\">J</text><text x=\"465\" y=\"260\">K</text><text x=\"310\" y=\"254\" font-size=\"11\">I</text><text x=\"310\" y=\"268\" font-size=\"9\" fill=\"#104535\">GOAL</text></g></svg></div>",
          "solution": {
            "steps": [
              "1. **Breadth-First Search (BFS) [FIFO Queue]:** Level 0: A &rarr; Level 1: B, C, D &rarr; Level 2: E, F, G, H &rarr; Level 3: I (Goal reached). Order visited: **A, B, C, D, E, F, G, H, I** (9 nodes).",
              "2. **Depth-First Search (DFS) [LIFO Stack]:** Explores down leftmost path first: A &rarr; B &rarr; E (backtracks to A) &rarr; C &rarr; F (backtracks to C) &rarr; G &rarr; I (Goal reached). Order visited: **A, B, E, C, F, G, I** (7 nodes). Nodes D, H, J, K are never visited.",
              "3. **Uniform Cost Search (UCS) [Priority Queue ordered by path cost g(n)]:**\n   - Step 1: Pop A (g=0). Fringe: {D(3), C(4), B(5)}\n   - Step 2: Pop D (g=3). Add H(7). Fringe: {C(4), B(5), H(7)}\n   - Step 3: Pop C (g=4). Add G(5), F(6). Fringe: {B(5), G(5), F(6), H(7)}\n   - Step 4: Pop B (g=5). Add E(7). Fringe: {G(5), F(6), E(7), H(7)}\n   - Step 5: Pop G (g=5). Add I(8). Fringe: {F(6), E(7), H(7), I(8)}\n   - Step 6: Pop F (g=6). Fringe: {E(7), H(7), I(8)}\n   - Step 7: Pop E (g=7). Fringe: {H(7), I(8)}\n   - Step 8: Pop H (g=7). Add K(9), J(11). Fringe: {I(8), K(9), J(11)}\n   - Step 9: Pop I (g=8). Goal reached!\n   Order of node expansion: **A (0) &rarr; D (3) &rarr; C (4) &rarr; B (5) &rarr; G (5) &rarr; F (6) &rarr; E (7) &rarr; H (7) &rarr; I (8)**.\n   Optimal Path: **A &rarr; C &rarr; G &rarr; I** with minimum cost **8**.",
              "4. **Iterative Deepening Search (IDS):**\n   - Limit 0: [A]\n   - Limit 1: [A, B, C, D]\n   - Limit 2: [A, B, E, C, F, G, D, H]\n   - Limit 3: [A, B, E, C, F, G, I] (Goal I reached at depth 3!)."
            ],
            "answer": "BFS visits 9 nodes (A, B, C, D, E, F, G, H, I); DFS visits 7 nodes (A, B, E, C, F, G, I); UCS expands 9 nodes finding optimal path A-C-G-I of cost 8; IDS reaches goal at depth limit 3.",
            "marking_hint": "Award 1.5 marks each for BFS, DFS, UCS, and IDS sequences."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 1 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2024-set2",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2024,
      "set_no": 2,
      "qno": "Question 2",
      "marks": 14,
      "topics": [
        "Genetic Algorithms",
        "Adversarial Search & Min-Max",
        "Informed vs Uninformed Search"
      ],
      "question": "(a) Define Genetic Algorithm and its working principles with a suitable example. **[3]**  \n(b) How is a two-player game formulated as a search problem? Explain the roles of terminal test and utility function. **[4]**  \n(c) Explain the Adversarial Search algorithm with an example game tree. **[3]**  \n(d) Describe Greedy Best-First Search. Why is it not guaranteed to produce an optimal solution? **[4]**",
      "subparts": [
        {
          "id": "cse-4101-final-2024-q2a",
          "qno": "2(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Genetic Algorithms"
          ],
          "question": "Define Genetic Algorithm and its working principles with a suitable example.",
          "solution": {
            "steps": [
              "1. Genetic Algorithm: A search heuristic inspired by biological natural selection.",
              "2. Principles: Encodes candidate states as strings, evaluates fitness, mates pairs using crossover, and introduces diversity with mutation."
            ],
            "answer": "Evolutionary optimization using reproductive operators to explore complex non-differentiable search landscapes.",
            "marking_hint": "Award 1.5 marks for definition, 1.5 marks for example."
          }
        },
        {
          "id": "cse-4101-final-2024-q2b",
          "qno": "2(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Adversarial Search & Min-Max"
          ],
          "question": "How is a two-player game formulated as a search problem? Explain the roles of terminal test and utility function.",
          "solution": {
            "steps": [
              "1. Formulation components: Initial state $s_0$, $\\text{Player}(s)$, $\\text{Actions}(s)$, Transition model $\\text{Result}(s, a)$, Terminal test, Utility function.",
              "2. Terminal Test: Returns true if game is over (e.g., checkmate, draw), false otherwise.",
              "3. Utility Function (Payoff): Defines numeric value for terminal states (e.g., +1 for win, -1 for loss, 0 for draw)."
            ],
            "answer": "Two-player games formulate search over alternating player turns, evaluated at terminal states via a payoff utility function.",
            "marking_hint": "Award 2 marks for formal game formulation, 1 mark each for terminal test and utility function."
          }
        },
        {
          "id": "cse-4101-final-2024-q2c",
          "qno": "2(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "Adversarial Search & Min-Max"
          ],
          "question": "Explain the Adversarial Search algorithm with an example game tree.",
          "solution": {
            "steps": [
              "1. Minimax recursively evaluates game trees where MAX chooses action with maximum utility and MIN chooses action with minimum utility.",
              "2. $V(s) = \\max_{a} V(\\text{Result}(s, a))$ if Player = MAX; $V(s) = \\min_{a} V(\\text{Result}(s, a))$ if Player = MIN.",
              "3. Backpropagates utility from terminal leaves up to root."
            ],
            "answer": "Minimax backs up terminal values to establish the optimal game-theoretic value against an optimal adversary.",
            "marking_hint": "Award 1.5 marks for algorithm principles, 1.5 marks for game tree diagram."
          }
        },
        {
          "id": "cse-4101-final-2024-q2d",
          "qno": "2(d)",
          "label": "(d)",
          "marks": 4,
          "topics": [
            "Informed vs Uninformed Search"
          ],
          "question": "Describe Greedy Best-First Search. Why is it not guaranteed to produce an optimal solution?",
          "solution": {
            "steps": [
              "1. Greedy Best-First Search evaluates nodes using only the heuristic function: $f(n) = h(n)$, expanding the node that appears closest to the goal.",
              "2. Why not optimal: It ignores the path cost $g(n)$ accrued so far. A path may look attractive locally because $h(n)$ is small, but the cumulative path cost to reach it could be arbitrarily large.",
              "3. Like DFS, it can also get stuck in loops (incomplete in graph search with infinite paths)."
            ],
            "answer": "Greedy Best-First Search minimizes estimated remaining cost $h(n)$, but without $g(n)$, it easily selects sub-optimal paths.",
            "marking_hint": "Award 2 marks for algorithm mechanism, 2 marks for non-optimality justification."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 2 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2024-set3",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2024,
      "set_no": 3,
      "qno": "Question 3",
      "marks": 14,
      "topics": [
        "A* Search & Heuristics",
        "Constraint Satisfaction Problems",
        "Decision Trees"
      ],
      "question": "(a) Explain details about how heuristic functions guide the search process toward the goal. **[4]**  \n(b) Write down the strategies to improve Backtracking in Constraint Satisfaction Problem? Explain with example. **[4]**  \n(c) Describe the Decision Tree learning algorithm. Explain with proper mathematical example how attribute selection is performed using: i) Information Gain and ii) Gini Index. **[6]**",
      "subparts": [
        {
          "id": "cse-4101-final-2024-q3a",
          "qno": "3(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "A* Search & Heuristics"
          ],
          "question": "Explain details about how heuristic functions guide the search process toward the goal.",
          "solution": {
            "steps": [
              "1. Heuristic functions estimate cost from current state to the goal ($h(n)$).",
              "2. In best-first search, evaluation function $f(n)$ incorporates $h(n)$ to order the priority queue.",
              "3. Relaxed problem intuition: Effective heuristics are often exact costs of solutions to simplified (relaxed) versions of the original problem."
            ],
            "answer": "Heuristics assign low estimated values to states that appear close to the goal, biasing the frontier queue towards promising regions and drastically reducing expanded nodes.",
            "marking_hint": "Award 2 marks for prioritization mechanics, 2 marks for relaxed problem generation."
          }
        },
        {
          "id": "cse-4101-final-2024-q3b",
          "qno": "3(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Constraint Satisfaction Problems"
          ],
          "question": "Write down the strategies to improve Backtracking in Constraint Satisfaction Problem? Explain with example.",
          "solution": {
            "steps": [
              "1. Variable Ordering: Minimum Remaining Values (MRV) and Degree Heuristic.",
              "2. Value Ordering: Least Constraining Value (LCV).",
              "3. Inference & Pruning: Forward Checking and Arc Consistency (AC-3 algorithm) to detect dead ends before expanding.",
              "4. Intelligent Backtracking: Conflict-directed backjumping (chronological backtracking jump back to conflict source)."
            ],
            "answer": "Backtracking efficiency is enhanced through MRV variable ordering, LCV value ordering, AC-3 constraint propagation, and conflict-directed backjumping.",
            "marking_hint": "Award 1 mark each for MRV, LCV, Forward Checking/AC-3, and Backjumping."
          }
        },
        {
          "id": "cse-4101-final-2024-q3c",
          "qno": "3(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "Decision Trees"
          ],
          "question": "Describe the Decision Tree learning algorithm. Explain with proper mathematical example how attribute selection is performed using: i) Information Gain and ii) Gini Index.",
          "solution": {
            "steps": [
              "1. Entropy formula: $H(S) = -\\sum p_i \\log_2 p_i$.",
              "2. Information Gain: $IG(S, A) = H(S) - \\sum \\frac{|S_v|}{|S|} H(S_v)$. Selects attribute maximizing reduction in entropy.",
              "3. Gini Index: $\\text{Gini}(S) = 1 - \\sum p_i^2$. Selects attribute minimizing split impurity."
            ],
            "answer": "ID3 uses Information Gain (Entropy reduction); CART uses Gini Index impurity to perform recursive greedy splitting.",
            "marking_hint": "Award 3 marks for Information Gain derivation, 3 marks for Gini Index derivation."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 3 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2024-set4",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2024,
      "set_no": 4,
      "qno": "Question 4",
      "marks": 14,
      "topics": [
        "A* Search & Heuristics",
        "First-Order Logic",
        "Robotics & Applications"
      ],
      "question": "(a) Explain the components of the A* evaluation function $f(n) = g(n) + h(n)$. Write down the application of A* search. **[4]**  \n(b) Convert the following English statement into FOL: **[5]**  \n    i. **Every man respects his parent**  \n    ii. **There is somebody whom everybody loves**  \n    iii. **Not all students like both Mathematics and Science**  \n    iv. **Mahmud has never sent an e-mail message to Abdullah**  \n    v. **Everybody loves somebody**  \n(c) Write short note on two types of quantifiers in FOL with example? **[3]**  \n(d) Write down the application of AI in robotics. **[2]**",
      "subparts": [
        {
          "id": "cse-4101-final-2024-q4a",
          "qno": "4(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "A* Search & Heuristics"
          ],
          "question": "Explain the components of the A* evaluation function f(n) = g(n) + h(n). Write down the application of A* search.",
          "solution": {
            "steps": [
              "1. Components: $g(n)$ is the exact known cost from start state to current node $n$; $h(n)$ is estimated cost from $n$ to goal; $f(n)$ is total estimated cost of cheapest solution passing through $n$.",
              "2. Applications: GPS route navigation and mapping (Google Maps), robotic path planning, video game AI pathfinding (NavMesh navigation), VLSI circuit routing, natural language parsing."
            ],
            "answer": "f(n) balances path cost so far g(n) with estimated future cost h(n). Widely applied in navigation, robotics, and game pathfinding.",
            "marking_hint": "Award 2 marks for function breakdown, 2 marks for at least 3 distinct applications."
          }
        },
        {
          "id": "cse-4101-final-2024-q4b",
          "qno": "4(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "First-Order Logic"
          ],
          "question": "Convert the following English statement into FOL:\ni. **Every man respects his parent**\nii. **There is somebody whom everybody loves**\niii. **Not all students like both Mathematics and Science**\niv. **Mahmud has never sent an e-mail message to Abdullah**\nv. **Everybody loves somebody**",
          "solution": {
            "steps": [
              "i. ∀x (Man(x) → ∀y (Parent(y, x) → Respects(x, y)))",
              "ii. ∃y ∀x Loves(x, y)",
              "iii. ¬∀s (Student(s) → (Likes(s, Math) ∧ Likes(s, Science)))",
              "iv. ¬∃m (Email(m) ∧ Sent(Mahmud, Abdullah, m))",
              "v. ∀x ∃y Loves(x, y)"
            ],
            "answer": "Formal predicate logic sentences using quantifiers and logical connectives.",
            "marking_hint": "Award 1 mark for each correct translation."
          }
        },
        {
          "id": "cse-4101-final-2024-q4c",
          "qno": "4(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "First-Order Logic"
          ],
          "question": "Write short note on two types of quantifiers in FOL with example?",
          "solution": {
            "steps": [
              "1. Universal Quantifier (∀): 'For all'. Example: ∀x (Human(x) → Mortal(x)).",
              "2. Existential Quantifier (∃): 'There exists'. Example: ∃x (Student(x) ∧ Passed(x))."
            ],
            "answer": "Universal (∀) applies across entire domain; Existential (∃) specifies existence of at least one instance.",
            "marking_hint": "Award 1.5 marks for universal, 1.5 marks for existential."
          }
        },
        {
          "id": "cse-4101-final-2024-q4d",
          "qno": "4(d)",
          "label": "(d)",
          "marks": 2,
          "topics": [
            "Robotics & Applications"
          ],
          "question": "Write down the application of AI in robotics.",
          "solution": {
            "steps": [
              "1. Perception & SLAM (Simultaneous Localization and Mapping) using computer vision and sensor fusion.",
              "2. Path planning and motion control (obstacle avoidance using A* or RRT).",
              "3. Manipulation & Grasping using reinforcement learning."
            ],
            "answer": "AI empowers robotics with autonomous perception, spatial mapping, trajectory planning, and dexterous manipulation.",
            "marking_hint": "Award 1 mark for perception/SLAM, 1 mark for path planning."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 4 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2024-set5",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2024,
      "set_no": 5,
      "qno": "Question 5",
      "marks": 14,
      "topics": [
        "Adversarial Search & Min-Max",
        "Alpha-Beta Pruning",
        "Machine Learning in AI",
        "Neural Networks & Backpropagation"
      ],
      "question": "(a) Given the following search tree, apply the alpha-beta pruning algorithm and show the search tree that would be obtained. Make sure that you show where the cuts are applied and which parts of the search tree are pruned as a result. **[5]**\n\n**Search Tree for Alpha-Beta Pruning:**\n```mermaid\ngraph TD\n    A((Max: A)) --> B((Min: B))\n    A --> C((Min: C))\n\n    B --> D((Max: D))\n    B --> E((Max: E))\n    C --> F((Max: F))\n    C --> G((Max: G))\n\n    D --> H[6]\n    D --> I[5]\n    E --> J[8]\n    E --> K[10]\n\n    F --> L[2]\n    F --> M[1]\n    G --> N[14]\n    G --> O[16]\n```\n\n(b) What is Reinforcement Learning? Differentiate between Supervised and Unsupervised machine learning. **[4]**  \n(c) Write short note on Neural networks. **[5]**",
      "subparts": [
        {
          "id": "cse-4101-final-2024-q5a",
          "qno": "5(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Adversarial Search & Min-Max",
            "Alpha-Beta Pruning"
          ],
          "question": "Given the following search tree, apply the alpha-beta pruning algorithm and show the search tree that would be obtained. Make sure that you show where the cuts are applied and which parts of the search tree are pruned as a result.\n\n<div class=\"svg-diagram-wrapper\"><svg viewBox=\"0 0 500 240\" class=\"responsive-diagram\" role=\"img\" aria-label=\"Alpha beta search tree\"><g stroke=\"currentColor\" stroke-width=\"1.8\" fill=\"none\"><line x1=\"250\" y1=\"25\" x2=\"130\" y2=\"75\"/><line x1=\"250\" y1=\"25\" x2=\"370\" y2=\"75\"/><line x1=\"130\" y1=\"75\" x2=\"70\" y2=\"135\"/><line x1=\"130\" y1=\"75\" x2=\"190\" y2=\"135\"/><line x1=\"370\" y1=\"75\" x2=\"310\" y2=\"135\"/><line x1=\"370\" y1=\"75\" x2=\"430\" y2=\"135\"/><line x1=\"70\" y1=\"135\" x2=\"45\" y2=\"195\"/><line x1=\"70\" y1=\"135\" x2=\"95\" y2=\"195\"/><line x1=\"190\" y1=\"135\" x2=\"165\" y2=\"195\"/><line x1=\"190\" y1=\"135\" x2=\"215\" y2=\"195\"/><line x1=\"310\" y1=\"135\" x2=\"285\" y2=\"195\"/><line x1=\"310\" y1=\"135\" x2=\"335\" y2=\"195\"/><line x1=\"430\" y1=\"135\" x2=\"405\" y2=\"195\"/><line x1=\"430\" y1=\"135\" x2=\"455\" y2=\"195\"/></g><g fill=\"var(--surface-card, #fff)\" stroke=\"currentColor\" stroke-width=\"1.8\"><circle cx=\"250\" cy=\"25\" r=\"14\"/><circle cx=\"130\" cy=\"75\" r=\"14\"/><circle cx=\"370\" cy=\"75\" r=\"14\"/><circle cx=\"70\" cy=\"135\" r=\"14\"/><circle cx=\"190\" cy=\"135\" r=\"14\"/><circle cx=\"310\" cy=\"135\" r=\"14\"/><circle cx=\"430\" cy=\"135\" r=\"14\"/></g><g font-size=\"11\" font-weight=\"bold\" fill=\"currentColor\" text-anchor=\"middle\" dominant-baseline=\"central\"><text x=\"250\" y=\"25\">A</text><text x=\"130\" y=\"75\">B</text><text x=\"370\" y=\"75\">C</text><text x=\"70\" y=\"135\">D</text><text x=\"190\" y=\"135\">E</text><text x=\"310\" y=\"135\">F</text><text x=\"430\" y=\"135\">G</text></g><g font-size=\"11\" font-weight=\"bold\" fill=\"var(--accent-green, #27ae60)\" text-anchor=\"middle\"><text x=\"45\" y=\"215\">6</text><text x=\"95\" y=\"215\">5</text><text x=\"165\" y=\"215\">8</text><text x=\"215\" y=\"215\">10</text><text x=\"285\" y=\"215\">2</text><text x=\"335\" y=\"215\">1</text><text x=\"405\" y=\"215\">14</text><text x=\"455\" y=\"215\">16</text></g></svg></div>",
          "solution": {
            "steps": [
              "1. D (Max) gets max(6,5) = 6. B (Min) gets beta = 6.",
              "2. E evaluates first child 8. Since 8 >= beta(6), B will never choose E. Child 10 is PRUNED.",
              "3. B returns 6 to Root A. A gets alpha = 6.",
              "4. C evaluates F: F (Max) gets max(2,1) = 2. C's beta becomes 2. Since beta(2) <= alpha(6), subtree G (14, 16) is PRUNED."
            ],
            "answer": "Two pruning cuts are made: Leaf 10 under E is pruned; entire subtree G with leaves 14 and 16 is pruned.",
            "marking_hint": "Award 2.5 marks for first cut, 2.5 marks for second cut."
          }
        },
        {
          "id": "cse-4101-final-2024-q5b",
          "qno": "5(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Machine Learning in AI"
          ],
          "question": "What is Reinforcement Learning? Differentiate between Supervised and Unsupervised machine learning.",
          "solution": {
            "steps": [
              "1. Reinforcement Learning: Agent learns optimal policy through trial-and-error interactions with environment, receiving rewards or penalties (Markov Decision Process).",
              "2. Supervised Learning: Trained on labeled data pairs (input, target).",
              "3. Unsupervised Learning: Learns inherent data patterns, clusters, or distributions without labeled targets."
            ],
            "answer": "Supervised uses labels; Unsupervised discovers latent patterns; Reinforcement optimizes reward signals.",
            "marking_hint": "Award 2 marks for RL, 2 marks for Supervised vs Unsupervised comparison."
          }
        },
        {
          "id": "cse-4101-final-2024-q5c",
          "qno": "5(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Neural Networks & Backpropagation"
          ],
          "question": "Write short note on Neural networks.",
          "solution": {
            "steps": [
              "1. Computational systems inspired by biological neurons, organized in input, hidden, and output layers.",
              "2. Perceptron model: $y = \\sigma(\\sum w_i x_i + b)$.",
              "3. Training via Backpropagation: Computes gradient of loss function via chain rule to update weights."
            ],
            "answer": "Artificial neural networks learn complex non-linear mappings via layered interconnected nodes trained by gradient descent.",
            "marking_hint": "Award 2 marks for architecture, 3 marks for activation and learning mechanism."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 5 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2024-set6",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2024,
      "set_no": 6,
      "qno": "Question 6",
      "marks": 14,
      "topics": [
        "Machine Learning in AI",
        "Neural Networks & Backpropagation"
      ],
      "question": "(a) A disease affects 1% of the population. A test is 95% accurate for both positive and negative results. If a person tests positive, what's the probability they have the disease? **[4]**  \n(b) Write down the equation for Conditional Probability and Bayes Theorem. **[3]**  \n(c) Consider a single neuron with the following parameters: **[7]**  \n$$\\begin{aligned}\n\\text{Inputs: } & x_1 = 1.0, \\; x_2 = 0.5 \\\\\n\\text{Weights: } & w_1 = 0.4, \\; w_2 = -0.6 \\\\\n\\text{Bias: } & b = 0.1 \\\\\n\\text{Activation function: } & \\text{Sigmoid} \\\\\n\\text{Target output: } & t = 1 \\\\\n\\text{Learning rate: } & \\eta = 0.2\n\\end{aligned}$$\n\nNow,  \na) Compute the **net input** and the **output of the neuron**.  \nb) Calculate the **error** using Mean Squared Error (MSE).  \nc) Using **backpropagation**, compute the **weight and bias updates** for one training step.",
      "subparts": [
        {
          "id": "cse-4101-final-2024-q6a",
          "qno": "6(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Machine Learning in AI"
          ],
          "question": "A disease affects 1% of the population. A test is 95% accurate for both positive and negative results. If a person tests positive, what's the probability they have the disease?",
          "solution": {
            "steps": [
              "1. Given: $P(D) = 0.01$, $P(\\neg D) = 0.99$.",
              "2. Accuracy: $P(+|D) = 0.95$, $P(-|\\neg D) = 0.95 \\implies P(+|\\neg D) = 0.05$.",
              "3. Total probability $P(+)$: $P(+) = P(+|D)P(D) + P(+|\\neg D)P(\\neg D) = (0.95)(0.01) + (0.05)(0.99) = 0.0095 + 0.0495 = 0.0590$.",
              "4. Bayes Theorem: $P(D|+) = \\frac{P(+|D)P(D)}{P(+)} = \\frac{0.0095}{0.0590} \\approx 0.1610$ (16.1%)."
            ],
            "answer": "The probability that a person who tests positive actually has the disease is approximately 16.1%.",
            "marking_hint": "Award 1 mark for prior probabilities, 1.5 marks for total probability denominator, 1.5 marks for final posterior."
          }
        },
        {
          "id": "cse-4101-final-2024-q6b",
          "qno": "6(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Machine Learning in AI"
          ],
          "question": "Write down the equation for Conditional Probability and Bayes Theorem.",
          "solution": {
            "steps": [
              "1. Conditional Probability: $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$, for $P(B) > 0$.",
              "2. Bayes Theorem: $P(A|B) = \\frac{P(B|A)P(A)}{P(B)} = \\frac{P(B|A)P(A)}{\\sum_i P(B|A_i)P(A_i)}$."
            ],
            "answer": "Formal mathematical definitions of conditional likelihood and Bayesian posterior inversion.",
            "marking_hint": "Award 1.5 marks for conditional probability, 1.5 marks for Bayes theorem equation."
          }
        },
        {
          "id": "cse-4101-final-2024-q6c",
          "qno": "6(c)",
          "label": "(c)",
          "marks": 7,
          "topics": [
            "Machine Learning in AI",
            "Neural Networks & Backpropagation"
          ],
          "question": "Consider a single neuron with parameters: $x_1 = 1.0, x_2 = 0.5$, weights $w_1 = 0.4, w_2 = -0.6$, bias $b = 0.1$, activation function $\\sigma(z) = \\frac{1}{1 + e^{-z}}$, target $t = 1$, learning rate $\\eta = 0.2$.\n\nCompute the error and backpropagation weight update:\n\n<div class=\"scroll-container\"><div class=\"katex-display\">$$\\Delta w_j = -\\eta \\frac{\\partial E}{\\partial w_j} = \\eta (t - y) \\cdot \\sigma(z)(1 - \\sigma(z)) \\cdot x_j = 0.2 \\cdot (1 - 0.5744) \\cdot 0.2444 \\cdot x_j$$</div></div>",
          "solution": {
            "steps": [
              "1. Net input: $z = (0.4)(1.0) + (-0.6)(0.5) + 0.1 = 0.20$.",
              "2. Neuron output: $y = \\sigma(0.20) \\approx 0.5498$.",
              "3. MSE Error: $E = \\frac{1}{2}(1 - 0.5498)^2 = 0.1013$.",
              "4. Gradient factor: $\\delta = (t - y)y(1 - y) = (0.4502)(0.5498)(0.4502) = 0.1114$.",
              "5. Weight updates: $\\Delta w_1 = 0.2(0.1114)(1.0) = +0.0223$; $\\Delta w_2 = 0.2(0.1114)(0.5) = +0.0111$; $\\Delta b = +0.0223$."
            ],
            "answer": "z = 0.20, y = 0.5498, Error = 0.1013, new w1 = 0.4223, new w2 = -0.5889, new b = 0.1223.",
            "marking_hint": "Award 2 marks for net input/output, 2 marks for error, 3 marks for updates."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 6 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4101-final-2024-set7",
      "course": "CSE-4101",
      "exam": "final",
      "year": 2024,
      "set_no": 7,
      "qno": "Question 7",
      "marks": 14,
      "topics": [
        "Hill Climbing Search",
        "A* Search & Heuristics",
        "Informed vs Uninformed Search",
        "Knowledge Representation & Ontology"
      ],
      "question": "(a) Write down the Limitation of Hill Climbing Search with explanation? **[4]**  \n(b) Which heuristics are admissible for the 8-puzzle problem and why? **[4]**  \n(c) Perform Iterative Deepening Search based on the following graph to reach goal node G. **[4]**\n\n**Graph Structure (Mermaid):**\n```mermaid\ngraph TD\n    A((A)) --> B((B))\n    A --> C((C))\n    B --> D((D))\n    B --> E((E))\n    C --> F((F))\n    C --> G((G - Goal))\n    D --> H((H))\n    E --> I((I))\n```\n\n(d) What is an ontology? How does it differ from a taxonomy or a database schema? **[2]**\n\n---",
      "subparts": [
        {
          "id": "cse-4101-final-2024-q7a",
          "qno": "7(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Hill Climbing Search"
          ],
          "question": "Write down the Limitation of Hill Climbing Search with explanation?",
          "solution": {
            "steps": [
              "1. Local Extrema: Cannot backtrack once inside a sub-optimal local peak.",
              "2. Ridge Problem: A narrow elevated ridge requires zigzag diagonal moves that single-variable generators fail to traverse.",
              "3. Plateaux & Shoulders: Flat surface causes random walk or endless loop.",
              "4. Incompleteness: Does not guarantee finding a solution, let alone an optimal one."
            ],
            "answer": "Greedy local search suffers from local maxima, ridges, flat plateaux, and general incompleteness. Mitigated by Random-restart hill climbing or Simulated Annealing.",
            "marking_hint": "Award 1 mark each for explaining the core limitations and mitigation strategies."
          }
        },
        {
          "id": "cse-4101-final-2024-q7b",
          "qno": "7(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "A* Search & Heuristics"
          ],
          "question": "Which heuristics are admissible for the 8-puzzle problem and why?",
          "solution": {
            "steps": [
              "1. Admissibility condition: A heuristic $h(n)$ is admissible if $h(n) \\le h^*(n)$ for all $n$, where $h^*(n)$ is the true shortest cost to goal.",
              "2. Heuristic $h_1(n)$ (Number of misplaced tiles): Each misplaced tile must move at least once, so $h_1(n) \\le h^*(n)$. Hence admissible.",
              "3. Heuristic $h_2(n)$ (Manhattan distance sum): Sum of horizontal and vertical moves for each tile to reach goal. Since tiles cannot jump over each other, true moves $\\ge h_2(n)$. Hence admissible.",
              "4. Dominance: $h_2(n) \\ge h_1(n)$ for all states; $h_2$ dominates $h_1$ and prunes more search nodes."
            ],
            "answer": "Both Misplaced Tiles ($h_1$) and Manhattan Distance ($h_2$) are admissible. Manhattan distance is superior because it dominates $h_1$.",
            "marking_hint": "Award 1.5 marks for admissibility definition, 1.25 marks each for justifying $h_1$ and $h_2$."
          }
        },
        {
          "id": "cse-4101-final-2024-q7c",
          "qno": "7(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Informed vs Uninformed Search"
          ],
          "question": "Perform Iterative Deepening Search based on the following graph to reach goal node G:\nTree structure: Root A has children B, C; B has children D, E; C has children F, G; D has child H; E has child I.",
          "solution": {
            "steps": [
              "1. **Depth Limit 0:** Visit root [A]. (Goal G not reached).",
              "2. **Depth Limit 1:** Visit A &rarr; B, C. (Goal G not reached).",
              "3. **Depth Limit 2:** Visit A &rarr; B &rarr; D, E &rarr; C &rarr; F, G. (Goal G reached at depth 2!).",
              "4. **Search Behavior:** Iterative Deepening Search (IDS) combines DFS memory efficiency O(bd) with BFS completeness. Since Goal G is located at Depth 2 on node C's right branch, search terminates successfully during iteration Limit = 2 without needing to explore leaves H (under D) or I (under E) at Depth 3."
            ],
            "answer": "IDS visits [A] at Limit 0, [A, B, C] at Limit 1, and reaches Goal G at Limit 2 in order [A, B, D, E, C, F, G].",
            "marking_hint": "Award 1 mark for each depth limit iteration (0, 1, 2) and 1 mark for correct goal termination."
          }
        },
        {
          "id": "cse-4101-final-2024-q7d",
          "qno": "7(d)",
          "label": "(d)",
          "marks": 2,
          "topics": [
            "Knowledge Representation & Ontology"
          ],
          "question": "What is an ontology? How does it differ from a taxonomy or a database schema?",
          "solution": {
            "steps": [
              "1. Taxonomy is strictly a hierarchical tree classification (is-a relations only).",
              "2. Database schema defines data structure for storage/retrieval without rich semantic inference logic.",
              "3. Ontology includes complex multi-dimensional relations, axioms, rules, and semantic inference."
            ],
            "answer": "Ontology generalizes beyond taxonomic hierarchies and database tables to support automated semantic reasoning.",
            "marking_hint": "Award 1 mark for definition, 1 mark for distinguishing from taxonomy and database schema."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 7 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
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
      "question": "(a) What is Heuristic Function? What do you understand by Informed search and Uninformed search? **[1+4]**  \n(b) Consider the search space below where S is the starting state and G satisfies the goal test. Show the steps if we want to find G using A* Search algorithm. (Arcs are labeled with the cost of traversing them and the estimated cost to reach goal is reported inside nodes). **[6]**\n\n```mermaid\ngraph LR\n    S((S: 9)) -->|1| A((A: 6))\n    S -->|2| D((D: 8))\n    A -->|4| Q((Q: 4))\n    A -->|5| E((E: 5))\n    Q -->|2| E\n    E -->|1| G((G: 0 - Goal))\n    D -->|7| G\n    D -->|3| P((P: 3))\n    P -->|2| G\n```\n\n(c) Consider the following Game Tree assuming first player as maximizing. Apply MiniMax Algorithm on the Tree. **[4]**\n\n```mermaid\ngraph TD\n    A[A - Max] --> B[B - Min]\n    A --> C[C - Min]\n    A --> D[D - Min]\n    B --> E[E - Max]\n    B --> F[F - Max]\n    B --> G[G - Max]\n    C --> H[H - Max]\n    C --> I[I - Max]\n    C --> J[J - Max]\n    D --> K[K - Max]\n    D --> L[L - Max]\n    D --> M[M - Max]\n    E --> E1[8]\n    E --> E2[5]\n    F --> F1[-2]\n    F --> F2[3]\n    G --> G1[10]\n    G --> G2[-2]\n    H --> H1[6]\n    H --> H2[2]\n    I --> I1[5]\n    I --> I2[4]\n    J --> J1[6]\n    J --> J2[2]\n    K --> K1[6]\n    K --> K2[7]\n    L --> L1[5]\n    L --> L2[1]\n    M --> M1[3]\n    M --> M2[9]\n```",
      "subparts": [
        {
          "id": "cse-4101-term-mec-tt1-qa",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Informed vs Uninformed Search"
          ],
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
          "topics": [
            "A* Search & Heuristics"
          ],
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
          "topics": [
            "Adversarial Search & Min-Max"
          ],
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
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for MEC CSE-4101 Term Test 1 (15 Marks total).",
        "marking_hint": "Full marks (15 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
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
      "question": "(a) What are Universal Quantification and Existential Quantification? Write following expression using quantifier: **[2+4]**  \n    i. **Everybody loves CSE**  \n    ii. **Somebody loves EEE**  \n(b) What is simple reflex agent? Draw a schematic diagram of a simple reflex agent. **[1+4]**  \n(c) Determine Properties of the Environment (PEAS) for the following situation for an agent: **Chess**, **Online Shopping**, **Riding bi-cycle**, **Chat**. **[4]**",
      "subparts": [
        {
          "id": "cse-4101-term-mec-tt2-qa",
          "qno": "2(a)",
          "label": "(a)",
          "marks": 6,
          "topics": [
            "First-Order Logic"
          ],
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
          "topics": [
            "AI Foundations"
          ],
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
          "topics": [
            "PEAS & Task Environment"
          ],
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
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for MEC CSE-4101 Term Test 2 (15 Marks total).",
        "marking_hint": "Full marks (15 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    }
  ],
  "cse-4102": [
    {
      "id": "cse-4102-final-2023-set1",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2023,
      "set_no": 1,
      "qno": "Question 1",
      "marks": 14,
      "topics": [
        "Correlation & Covariance",
        "Markov Chains & Transition Matrices",
        "Hypothesis Testing & Errors",
        "Linear & Multiple Regression"
      ],
      "question": "(a) What is a bivariate graph? List some bivariate graphs with proper examples. **[2]**  \n(b) What is Cross-correlation? Write the difference between covariance and correlation. **[3]**  \n(c) Let us consider a null hypothesis- A man is not guilty of a crime. Now, according to above hypothesis write the statement for Type I error and Type II error. Is a Type I or Type II error worse? **[3]**  \n(d) Multiple Linear Regression is a powerful tool for understanding relationships in data and making predictions. Suppose we want to predict the price of a house based on the following independent variables: Square Footage (in thousands), Number of Bedrooms, Age of the House (in years). Now write the necessary steps with formula for Predicting House Prices. **[3]**  \n(e) Calculate the coefficient of covariance for the following data: **[3]**  \n\n| X | 2 | 8 | 18 | 20 | 28 | 30 |\n|---|---|---|----|----|----|----|\n| Y | 5 | 12 | 18 | 23 | 45 | 50 |",
      "subparts": [
        {
          "id": "cse-4102-final-2023-q1a",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 2,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "What is a bivariate graph? List some bivariate graphs with proper examples.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(a) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: What is a bivariate graph? List some bivariate graphs with proper examples....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(a).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q1b",
          "qno": "1(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "What is Cross-correlation? Write the difference between covariance and correlation.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is Cross-correlation? Write the difference between covariance and correlati...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q1c",
          "qno": "1(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "Markov Chains & Transition Matrices",
            "Hypothesis Testing & Errors"
          ],
          "question": "Let us consider a null hypothesis- A man is not guilty of a crime. Now, according to above hypothesis write the statement for Type I error and Type II error. Is a Type I or Type II error worse?",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(c) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Let us consider a null hypothesis- A man is not guilty of a crime. Now, accordin...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(c).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q1d",
          "qno": "1(d)",
          "label": "(d)",
          "marks": 3,
          "topics": [
            "Linear & Multiple Regression"
          ],
          "question": "Multiple Linear Regression is a powerful tool for understanding relationships in data and making predictions. Suppose we want to predict the price of a house based on the following independent variables: Square Footage (in thousands), Number of Bedrooms, Age of the House (in years). Now write the necessary steps with formula for Predicting House Prices.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(d) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Multiple Linear Regression is a powerful tool for understanding relationships in...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(d).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q1e",
          "qno": "1(e)",
          "label": "(e)",
          "marks": 3,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "Calculate the coefficient of covariance for the following data: **[3]**  \n\n| X | 2 | 8 | 18 | 20 | 28 | 30 |\n|---|---|---|----|----|----|----|\n| Y | 5 | 12 | 18 | 23 | 45 | 50 |\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(e) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Calculate the coefficient of covariance for the following data: **[3]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(e).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 1 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2023-set2",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2023,
      "set_no": 2,
      "qno": "Question 2",
      "marks": 14,
      "topics": [
        "Laplace Transforms",
        "Inverse Laplace & ODEs"
      ],
      "question": "(a) Why is Laplace Transformation important for engineering? Perform the Laplace Transform of function $F(t) = e^{-2t}(3\\cos 6t - 5\\sin 6t)$ **[3]**  \n(b) Find Laplace Transform for the following function using the Table of Laplace Transforms $F(t) = [t(3\\sin 2t - 2\\cos 2t)]$ **[3]**  \n(c) Perform the inverse Laplace transform of the following expression: **[4]**  \n$$F(s) = \\frac{P(s)}{Q(s)} = \\frac{S+2}{S^2 - 4S + 13}$$  \n(d) Use Laplace transformation to solve the following initial value problem: **[4]**  \n$$y'' - y' - 2y = 0; \\quad y(0) = 1; \\quad y'(0) = 2$$",
      "subparts": [
        {
          "id": "cse-4102-final-2023-q2a",
          "qno": "2(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Laplace Transforms"
          ],
          "question": "Why is Laplace Transformation important for engineering? Perform the Laplace Transform of function $F(t) = e^{-2t}(3\\cos 6t - 5\\sin 6t)$",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Why is Laplace Transformation important for engineering? Perform the Laplace Tra...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q2b",
          "qno": "2(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Laplace Transforms"
          ],
          "question": "Find Laplace Transform for the following function using the Table of Laplace Transforms $F(t) = [t(3\\sin 2t - 2\\cos 2t)]$",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Find Laplace Transform for the following function using the Table of Laplace Tra...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q2c",
          "qno": "2(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Inverse Laplace & ODEs"
          ],
          "question": "Perform the inverse Laplace transform of the following expression: **[4]**  \n$$F(s) = \\frac{P(s)}{Q(s)} = \\frac{S+2}{S^2 - 4S + 13}$$",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Perform the inverse Laplace transform of the following expression: **[4]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q2d",
          "qno": "2(d)",
          "label": "(d)",
          "marks": 4,
          "topics": [
            "Laplace Transforms"
          ],
          "question": "Use Laplace transformation to solve the following initial value problem: **[4]**  \n$$y'' - y' - 2y = 0; \\quad y(0) = 1; \\quad y'(0) = 2$$\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(d) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Use Laplace transformation to solve the following initial value problem: **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(d).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 2 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2023-set3",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2023,
      "set_no": 3,
      "qno": "Question 3",
      "marks": 14,
      "topics": [
        "Stochastic & Stationary Processes",
        "Correlation & Covariance"
      ],
      "question": "(a) What is Stochastic Process? Write about the applications of stochastic processes. **[3]**  \n(b) Define the birth and death process stochastic process? Draw a scatter plot correlation for strong positive correlation, strong negative correlation, weak negative correlation, and no correlation. **[3]**  \n(c) What is statistical inference? Explain fundamental concepts in statistical inference. **[4]**  \n(d) What is meant by stationary process? Describe with formula First Order Stationary Process and Second Order Stationary Process. **[4]**",
      "subparts": [
        {
          "id": "cse-4102-final-2023-q3a",
          "qno": "3(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Stochastic & Stationary Processes"
          ],
          "question": "What is Stochastic Process? Write about the applications of stochastic processes.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is Stochastic Process? Write about the applications of stochastic processes...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q3b",
          "qno": "3(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Stochastic & Stationary Processes",
            "Correlation & Covariance"
          ],
          "question": "Define the birth and death process stochastic process? Draw a scatter plot correlation for strong positive correlation, strong negative correlation, weak negative correlation, and no correlation.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define the birth and death process stochastic process? Draw a scatter plot corre...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q3c",
          "qno": "3(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "What is statistical inference? Explain fundamental concepts in statistical inference.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What is statistical inference? Explain fundamental concepts in statistical infer...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q3d",
          "qno": "3(d)",
          "label": "(d)",
          "marks": 4,
          "topics": [
            "Stochastic & Stationary Processes"
          ],
          "question": "What is meant by stationary process? Describe with formula First Order Stationary Process and Second Order Stationary Process. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(d) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What is meant by stationary process? Describe with formula First Order Stationar...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(d).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 3 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2023-set4",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2023,
      "set_no": 4,
      "qno": "Question 4",
      "marks": 14,
      "topics": [
        "Laplace Transforms",
        "Queueing Theory & Little's Law",
        "Poisson & Exponential Processes",
        "Correlation & Covariance"
      ],
      "question": "(a) What is Little's law formula? Describe the features of M/M/1/K Queue model. **[3]**  \n(b) In a municipality hospital patients arrival are considered to be Poisson with an arrival interval time of 10 mins. The doctors (examination and dispensing) time may be assumed to be ED with an average of 6 mins. Now find: **[5]**  \n    i) What is the chance that a new patient directly sees the doctor?  \n    ii) For what proportion of the time the doctor is busy?  \n    iii) What is the average number of patients in the system?  \n    iv) What is the average waiting time of the system?  \n    v) Suppose the municipality wants to recruit another doctor, when an average waiting time of an arrival is 30 mins in the queue. Find out how large should be to justify a 2nd doctor?  \n(c) In the classic Gambler's Ruin problem, a gambler starts with an initial fortune of $i$ dollars and on each game, the gambler wins $\\$1$ with probability $p$ or loses $\\$1$ with probability $q = 1 - p$, where $0 \\le p \\le 1$. The gambler will stop playing if either $N$ dollars are accumulated or all money has been lost. Now find: **[6]**  \n    i) John starts with $\\$2$, and $p = 0.6$. What is the probability that John obtains a fortune of $N = 4$ without going broke?  \n    ii) What is the probability that John will become infinitely rich?  \n    iii) If John instead started with $i = \\$1$, what is the probability that he would go broke?",
      "subparts": [
        {
          "id": "cse-4102-final-2023-q4a",
          "qno": "4(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Laplace Transforms",
            "Queueing Theory & Little's Law"
          ],
          "question": "What is Little's law formula? Describe the features of M/M/1/K Queue model.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is Little's law formula? Describe the features of M/M/1/K Queue model....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q4b",
          "qno": "4(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Poisson & Exponential Processes",
            "Queueing Theory & Little's Law"
          ],
          "question": "In a municipality hospital patients arrival are considered to be Poisson with an arrival interval time of 10 mins. The doctors (examination and dispensing) time may be assumed to be ED with an average of 6 mins. Now find: **[5]**  \n    i) What is the chance that a new patient directly sees the doctor?  \n    ii) For what proportion of the time the doctor is busy?  \n    iii) What is the average number of patients in the system?  \n    iv) What is the average waiting time of the system?  \n    v) Suppose the municipality wants to recruit another doctor, when an average waiting time of an arrival is 30 mins in the queue. Find out how large should be to justify a 2nd doctor?",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: In a municipality hospital patients arrival are considered to be Poisson with an...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q4c",
          "qno": "4(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "In the classic Gambler's Ruin problem, a gambler starts with an initial fortune of $i$ dollars and on each game, the gambler wins $\\$1$ with probability $p$ or loses $\\$1$ with probability $q = 1 - p$, where $0 \\le p \\le 1$. The gambler will stop playing if either $N$ dollars are accumulated or all money has been lost. Now find: **[6]**  \n    i) John starts with $\\$2$, and $p = 0.6$. What is the probability that John obtains a fortune of $N = 4$ without going broke?  \n    ii) What is the probability that John will become infinitely rich?  \n    iii) If John instead started with $i = \\$1$, what is the probability that he would go broke?\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(c) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: In the classic Gambler's Ruin problem, a gambler starts with an initial fortune ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(c).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 4 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2023-set5",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2023,
      "set_no": 5,
      "qno": "Question 5",
      "marks": 14,
      "topics": [
        "Linear Programming & Optimization",
        "Correlation & Covariance",
        "Duality Theory & Simplex"
      ],
      "question": "(a) What do you mean by linear optimization? What is the use of optimization in Computer Science? **[3]**  \n(b) Define Z-score. A person wants some belts and wallets. He has total savings of Tk 6500 and wishes to spend all his savings on purchasing belts and wallets so that he can sell it later. The value of the wallet is Tk 25 and the value of the belt is Tk 15. He wants to store them in a cupboard and the maximum capacity of the cupboard is 50 units. He expects a profit of Tk 2.5 on the belt and Tk 3 on the wallet. Find the constraints and the resulting objective function. **[3]**  \n(c) What is a Sensitivity Analysis? Write Sensitivity Analysis Tools and Techniques. **[3]**  \n(d) Convert Primal to the dual of the given problem. **[5]**  \n$$\\text{Max } Z = x_1 + 2x_2 + x_3$$  \n$$\\text{Subject to}$$  \n$$2x_1 + x_2 - x_3 \\le 2$$  \n$$-2x_1 + x_2 - 5x_3 \\ge -6$$  \n$$4x_1 + x_2 + x_3 \\le 6$$  \n$$x_1, x_2, x_3 \\ge 0$$",
      "subparts": [
        {
          "id": "cse-4102-final-2023-q5a",
          "qno": "5(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Linear Programming & Optimization"
          ],
          "question": "What do you mean by linear optimization? What is the use of optimization in Computer Science?",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What do you mean by linear optimization? What is the use of optimization in Comp...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q5b",
          "qno": "5(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Linear Programming & Optimization"
          ],
          "question": "Define Z-score. A person wants some belts and wallets. He has total savings of Tk 6500 and wishes to spend all his savings on purchasing belts and wallets so that he can sell it later. The value of the wallet is Tk 25 and the value of the belt is Tk 15. He wants to store them in a cupboard and the maximum capacity of the cupboard is 50 units. He expects a profit of Tk 2.5 on the belt and Tk 3 on the wallet. Find the constraints and the resulting objective function.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define Z-score. A person wants some belts and wallets. He has total savings of T...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q5c",
          "qno": "5(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "What is a Sensitivity Analysis? Write Sensitivity Analysis Tools and Techniques.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(c) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is a Sensitivity Analysis? Write Sensitivity Analysis Tools and Techniques....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(c).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q5d",
          "qno": "5(d)",
          "label": "(d)",
          "marks": 5,
          "topics": [
            "Duality Theory & Simplex"
          ],
          "question": "Convert Primal to the dual of the given problem. **[5]**  \n$$\\text{Max } Z = x_1 + 2x_2 + x_3$$  \n$$\\text{Subject to}$$  \n$$2x_1 + x_2 - x_3 \\le 2$$  \n$$-2x_1 + x_2 - 5x_3 \\ge -6$$  \n$$4x_1 + x_2 + x_3 \\le 6$$  \n$$x_1, x_2, x_3 \\ge 0$$\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(d) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Convert Primal to the dual of the given problem. **[5]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(d).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 5 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2023-set6",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2023,
      "set_no": 6,
      "qno": "Question 6",
      "marks": 14,
      "topics": [
        "Fourier Transforms & Parseval Identity"
      ],
      "question": "(a) Why do we use Fourier transform? Perform the Fourier transform of function find: **[4]**  \n$$F\\left\\{\\frac{1}{2}\\left[H\\left(t + \\frac{1}{2}\\right) - H\\left(t - \\frac{1}{2}\\right)\\right]\\right\\} = ?$$  \n$$\\text{Where } F\\{H(t)\\} = F(\\omega) = \\frac{2i}{\\omega}$$  \n(b) Find Fourier Cosine transform of: **[5]**  \n$$f(x) = \\begin{cases} x, & 0 < x < 1 \\\\ 2 - x, & 1 < x < 2 \\\\ 0, & x > 2 \\end{cases}$$  \n(c) Parseval's identity ensures energy conservation, relating time and frequency domain representations of signals. Using Parseval's identity if: **[5]**  \n$$f(x) = \\begin{cases} 1 & x < |a| \\\\ 0 & x > |a| \\end{cases} \\quad \\text{and} \\quad f(s) = \\sqrt{\\frac{2}{\\pi}} \\frac{\\sin sa}{s}$$  \n$$\\text{now find that } \\int_0^\\infty \\left(\\frac{\\sin^2 x}{x^2}\\right) dx = ?$$",
      "subparts": [
        {
          "id": "cse-4102-final-2023-q6a",
          "qno": "6(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Fourier Transforms & Parseval Identity"
          ],
          "question": "Why do we use Fourier transform? Perform the Fourier transform of function find: **[4]**  \n$$F\\left\\{\\frac{1}{2}\\left[H\\left(t + \\frac{1}{2}\\right) - H\\left(t - \\frac{1}{2}\\right)\\right]\\right\\} = ?$$  \n$$\\text{Where } F\\{H(t)\\} = F(\\omega) = \\frac{2i}{\\omega}$$",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(a) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Why do we use Fourier transform? Perform the Fourier transform of function find:...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(a).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q6b",
          "qno": "6(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Fourier Transforms & Parseval Identity"
          ],
          "question": "Find Fourier Cosine transform of: **[5]**  \n$$f(x) = \\begin{cases} x, & 0 < x < 1 \\\\ 2 - x, & 1 < x < 2 \\\\ 0, & x > 2 \\end{cases}$$",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Find Fourier Cosine transform of: **[5]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q6c",
          "qno": "6(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Fourier Transforms & Parseval Identity"
          ],
          "question": "Parseval's identity ensures energy conservation, relating time and frequency domain representations of signals. Using Parseval's identity if: **[5]**  \n$$f(x) = \\begin{cases} 1 & x < |a| \\\\ 0 & x > |a| \\end{cases} \\quad \\text{and} \\quad f(s) = \\sqrt{\\frac{2}{\\pi}} \\frac{\\sin sa}{s}$$  \n$$\\text{now find that } \\int_0^\\infty \\left(\\frac{\\sin^2 x}{x^2}\\right) dx = ?$$\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(c) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Parseval's identity ensures energy conservation, relating time and frequency dom...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(c).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 6 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2023-set7",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2023,
      "set_no": 7,
      "qno": "Question 7",
      "marks": 22,
      "topics": [
        "Eigenvalues & Eigenvectors",
        "Markov Chains & Transition Matrices"
      ],
      "question": "(a) Eigenvalues and eigenvectors provide insights into linear transformations, system stability, and dimensionality reduction in data analysis. Find all the Eigenvalues and Eigenvectors of the matrix: **[5]**  \n$$\\begin{bmatrix} 1 & -1 & 4 \\\\ 3 & 2 & -1 \\\\ 2 & 1 & -1 \\end{bmatrix}$$  \n(b) Purpose-flea zooms around the vertices of the transition diagram opposite. Let $X_t$ be Purpose-flea's state at time $t$ ($t = 0, 1, \\dots$). **[5]**\n\n**Transition State Diagram (Mermaid):**\n```mermaid\nstateDiagram-v2\n    state \"1\" as S1\n    state \"2\" as S2\n    state \"3\" as S3\n\n    S1 --> S1: 0.6\n    S1 --> S2: 0.2\n    S1 --> S3: 0.2\n    S2 --> S1: 0.4\n    S2 --> S3: 0.8\n    S3 --> S2: 0.6\n    S3 --> S3: 0.2\n```\n\ni) Find the transition matrix, P.  \nii) Find $P(X_2 = 3 \\mid X_0 = 1)$.  \niii) Suppose that Purpose-flea is equally likely to start on any vertex at time 0. Find the probability distribution of $X_1$.  \niv) Suppose that Purpose-flea begins at vertex 1 at time 0. Find the probability distribution of $X_2$.  \nv) Suppose that Purpose-flea is equally likely to start on any vertex at time 0. Find the probability of obtaining the trajectory $(3, 2, 1, 1, 3)$.  \n\n(c) Glee-flea hops around on a triangle. At each step he moves to one of the other two vertices at random. What is the expected time taken for Glee-flea to get from vertex 1 to vertex 2? **[4]**\n\n---",
      "subparts": [
        {
          "id": "cse-4102-final-2023-q7a",
          "qno": "7(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Eigenvalues & Eigenvectors"
          ],
          "question": "Eigenvalues and eigenvectors provide insights into linear transformations, system stability, and dimensionality reduction in data analysis. Find all the Eigenvalues and Eigenvectors of the matrix: **[5]**  \n$$\\begin{bmatrix} 1 & -1 & 4 \\\\ 3 & 2 & -1 \\\\ 2 & 1 & -1 \\end{bmatrix}$$",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Eigenvalues and eigenvectors provide insights into linear transformations, syste...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q7b",
          "qno": "7(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Markov Chains & Transition Matrices"
          ],
          "question": "Purpose-flea zooms around the vertices of the transition diagram opposite. Let $X_t$ be Purpose-flea's state at time $t$ ($t = 0, 1, \\dots$). **[5]**\n\n**Transition State Diagram (Mermaid):**\n```mermaid\nstateDiagram-v2\n    state \"1\" as S1\n    state \"2\" as S2\n    state \"3\" as S3\n\n    S1 --> S1: 0.6\n    S1 --> S2: 0.2\n    S1 --> S3: 0.2\n    S2 --> S1: 0.4\n    S2 --> S3: 0.8\n    S3 --> S2: 0.6\n    S3 --> S3: 0.2\n```",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Purpose-flea zooms around the vertices of the transition diagram opposite. Let $...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q7c",
          "qno": "7(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Markov Chains & Transition Matrices"
          ],
          "question": "Glee-flea hops around on a triangle. At each step he moves to one of the other two vertices at random. What is the expected time taken for Glee-flea to get from vertex 1 to vertex 2? **[4]**\n\n---\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Glee-flea hops around on a triangle. At each step he moves to one of the other t...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q7i",
          "qno": "7(i)",
          "label": "(i)",
          "marks": 4,
          "topics": [
            "Markov Chains & Transition Matrices",
            "Eigenvalues & Eigenvectors"
          ],
          "question": "Find the transition matrix, P.  \nii) Find $P(X_2 = 3 \\mid X_0 = 1)$.  \niii) Suppose that Purpose-flea is equally likely to start on any vertex at time 0. Find the probability distribution of $X_1$.  \niv) Suppose that Purpose-flea begins at vertex 1 at time 0. Find the probability distribution of $X_2$.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(i) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Find the transition matrix, P.  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(i).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2023-q7v",
          "qno": "7(v)",
          "label": "(v)",
          "marks": 4,
          "topics": [
            "Markov Chains & Transition Matrices"
          ],
          "question": "Suppose that Purpose-flea is equally likely to start on any vertex at time 0. Find the probability of obtaining the trajectory $(3, 2, 1, 1, 3)$.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(v) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Suppose that Purpose-flea is equally likely to start on any vertex at time 0. Fi...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(v).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 7 (22 Marks total).",
        "marking_hint": "Full marks (22 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2024-set1",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2024,
      "set_no": 1,
      "qno": "Question 1",
      "marks": 14,
      "topics": [
        "Correlation & Covariance",
        "Hypothesis Testing & Errors",
        "Laplace Transforms"
      ],
      "question": "(a) A smart phone app tracks: Battery usage time (hours) and Screen brightness level (0-100 scale). Which variable is ratio-scaled and which is not? Justify. **[3]**  \n(b) A medical test is designed to detect a serious disease. **[3]**  \n    i. What is a Type I error in this context?  \n    ii. What is a Type II error in this context?  \n    iii. Which error is more dangerous and why?  \n(c) A city uses a linear model to predict traffic congestion based on number of vehicles, Time of day, Weather conditions. After deployment, predictions are poor during festivals, which linear model assumptions are likely violated, and why? **[4]**  \n(d) The table below shows daily temperature (X) and ice-cream sales (Y). **[4]**\n\n| X | 18 | 20 | 22 | 24 | 26 |\n|---|----|----|----|----|----|\n| Y | 50 | 65 | 80 | 95 | 110 |\n\ni. Calculate the coefficient of covariance.  \nii. Explain what the value indicates about their relationship.",
      "subparts": [
        {
          "id": "cse-4102-final-2024-q1a",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "A smart phone app tracks: Battery usage time (hours) and Screen brightness level (0-100 scale). Which variable is ratio-scaled and which is not? Justify.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: A smart phone app tracks: Battery usage time (hours) and Screen brightness level...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q1b",
          "qno": "1(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Hypothesis Testing & Errors"
          ],
          "question": "A medical test is designed to detect a serious disease. **[3]**  \n    i. What is a Type I error in this context?  \n    ii. What is a Type II error in this context?  \n    iii. Which error is more dangerous and why?",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: A medical test is designed to detect a serious disease. **[3]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q1c",
          "qno": "1(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Laplace Transforms"
          ],
          "question": "A city uses a linear model to predict traffic congestion based on number of vehicles, Time of day, Weather conditions. After deployment, predictions are poor during festivals, which linear model assumptions are likely violated, and why?",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: A city uses a linear model to predict traffic congestion based on number of vehi...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q1d",
          "qno": "1(d)",
          "label": "(d)",
          "marks": 4,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "The table below shows daily temperature (X) and ice-cream sales (Y). **[4]**\n\n| X | 18 | 20 | 22 | 24 | 26 |\n|---|----|----|----|----|----|\n| Y | 50 | 65 | 80 | 95 | 110 |\n\ni. Calculate the coefficient of covariance.  \nii. Explain what the value indicates about their relationship.\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(d) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: The table below shows daily temperature (X) and ice-cream sales (Y). **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(d).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 1 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2024-set2",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2024,
      "set_no": 2,
      "qno": "Question 2",
      "marks": 14,
      "topics": [
        "Correlation & Covariance",
        "Laplace Transforms",
        "Inverse Laplace & ODEs"
      ],
      "question": "(a) If $\\{f(t)\\} = \\bar{F}(s)$ then prove that $\\mathcal{L}\\{u(t-a)f(t-a)\\} = e^{-as}\\bar{F}(s)$. **[4]**  \n(b) Use Laplace transformation to solve the equation: **[4]**  \n$$(D^3 - 3D^2 + 3D - 1)Y = t^2 e^t \\quad \\text{given that } Y(0) = 1, \\; Y'(0) = 0, \\; Y''(0) = -2$$  \n(c) Perform the inverse Laplace transform of the following expression: **[4]**  \n$$\\log\\left\\{\\left(1 + \\frac{1}{s^2}\\right)^\\frac{1}{2}\\right\\}$$  \n(d) Define sampling distribution. What happens to the sampling distribution of the mean as sample size increases? **[2]**",
      "subparts": [
        {
          "id": "cse-4102-final-2024-q2a",
          "qno": "2(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "If $\\{f(t)\\} = \\bar{F}(s)$ then prove that $\\mathcal{L}\\{u(t-a)f(t-a)\\} = e^{-as}\\bar{F}(s)$.",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(a) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: If $\\{f(t)\\} = \\bar{F}(s)$ then prove that $\\mathcal{L}\\{u(t-a)f(t-a)\\} = e^{-as...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(a).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q2b",
          "qno": "2(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Laplace Transforms"
          ],
          "question": "Use Laplace transformation to solve the equation: **[4]**  \n$$(D^3 - 3D^2 + 3D - 1)Y = t^2 e^t \\quad \\text{given that } Y(0) = 1, \\; Y'(0) = 0, \\; Y''(0) = -2$$",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Use Laplace transformation to solve the equation: **[4]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q2c",
          "qno": "2(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Inverse Laplace & ODEs"
          ],
          "question": "Perform the inverse Laplace transform of the following expression: **[4]**  \n$$\\log\\left\\{\\left(1 + \\frac{1}{s^2}\\right)^\\frac{1}{2}\\right\\}$$",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Perform the inverse Laplace transform of the following expression: **[4]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q2d",
          "qno": "2(d)",
          "label": "(d)",
          "marks": 2,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "Define sampling distribution. What happens to the sampling distribution of the mean as sample size increases? **[2]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(d) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: Define sampling distribution. What happens to the sampling distribution of the m...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(d).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 2 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2024-set3",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2024,
      "set_no": 3,
      "qno": "Question 3",
      "marks": 14,
      "topics": [
        "Fourier Transforms & Parseval Identity"
      ],
      "question": "(a) Explain how Fourier Transform is used in filter design and frequency analysis of signals. **[2]**  \n(b) Perform the Fourier transform of function find $f(x) = e^{-ax^2}$ where $a > 0$. **[4]**  \n(c) Find Fourier Cosine transform of: **[4]**  \n$$f(x) = \\begin{cases} x, & 0 < x < 1 \\\\ 2 - x, & 1 < x < 2 \\\\ 0, & x > 2 \\end{cases}$$  \n(d) Parseval's identity ensures energy conservation, relating time and frequency domain representations of signals. Using Perseval's identity if: **[4]**  \n$$f(x) = \\begin{cases} 1 & x < |a| \\\\ 0 & x > |a| \\end{cases} \\quad \\text{and} \\quad f(s) = \\sqrt{\\frac{2}{\\pi}} \\frac{\\sin sa}{s}$$  \n$$\\text{now find that } \\int_0^\\infty \\left(\\frac{\\sin^2 x}{x^2}\\right) dx = ?$$",
      "subparts": [
        {
          "id": "cse-4102-final-2024-q3a",
          "qno": "3(a)",
          "label": "(a)",
          "marks": 2,
          "topics": [
            "Fourier Transforms & Parseval Identity"
          ],
          "question": "Explain how Fourier Transform is used in filter design and frequency analysis of signals.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(a) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain how Fourier Transform is used in filter design and frequency analysis of...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(a).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q3b",
          "qno": "3(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Fourier Transforms & Parseval Identity"
          ],
          "question": "Perform the Fourier transform of function find $f(x) = e^{-ax^2}$ where $a > 0$.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Perform the Fourier transform of function find $f(x) = e^{-ax^2}$ where $a > 0$....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q3c",
          "qno": "3(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Fourier Transforms & Parseval Identity"
          ],
          "question": "Find Fourier Cosine transform of: **[4]**  \n$$f(x) = \\begin{cases} x, & 0 < x < 1 \\\\ 2 - x, & 1 < x < 2 \\\\ 0, & x > 2 \\end{cases}$$",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Find Fourier Cosine transform of: **[4]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q3d",
          "qno": "3(d)",
          "label": "(d)",
          "marks": 4,
          "topics": [
            "Fourier Transforms & Parseval Identity"
          ],
          "question": "Parseval's identity ensures energy conservation, relating time and frequency domain representations of signals. Using Perseval's identity if: **[4]**  \n$$f(x) = \\begin{cases} 1 & x < |a| \\\\ 0 & x > |a| \\end{cases} \\quad \\text{and} \\quad f(s) = \\sqrt{\\frac{2}{\\pi}} \\frac{\\sin sa}{s}$$  \n$$\\text{now find that } \\int_0^\\infty \\left(\\frac{\\sin^2 x}{x^2}\\right) dx = ?$$\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(d) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Parseval's identity ensures energy conservation, relating time and frequency dom...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(d).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 3 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2024-set4",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2024,
      "set_no": 4,
      "qno": "Question 4",
      "marks": 14,
      "topics": [
        "Poisson & Exponential Processes",
        "Markov Chains & Transition Matrices",
        "Eigenvalues & Eigenvectors"
      ],
      "question": "(a) Explain Poisson process and Exponential process with applications. **[4]**  \n(b) Suppose that customers arrive at a bank according to a poisson process with mean rate of 3 per minute. Find the probability during the time interval of 2 minute: **[4]**  \n    I. Exactly 4 customers arrive  \n    II. More than 4 customers arrive  \n(c) Three boys A, B and C are throwing a ball to each other. A always throws the ball to B and B always throws the ball to C, but C is as likely to throw the ball to B as to A. If the initial probability distribution of three states A, B, C is 0.3, 0.4 and 0.3 respectively, Find: **[6]**  \n    I. The transition matrix.  \n    II. $P(X_2 = B)$  \n    III. $P(X_3 = B, X_2 = C, X_1 = B, X_0 = A)$ and  \n    IV. The distribution of the ball after two rounds.",
      "subparts": [
        {
          "id": "cse-4102-final-2024-q4a",
          "qno": "4(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Poisson & Exponential Processes"
          ],
          "question": "Explain Poisson process and Exponential process with applications.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(a) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain Poisson process and Exponential process with applications....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(a).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q4b",
          "qno": "4(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Poisson & Exponential Processes"
          ],
          "question": "Suppose that customers arrive at a bank according to a poisson process with mean rate of 3 per minute. Find the probability during the time interval of 2 minute: **[4]**  \n    I. Exactly 4 customers arrive  \n    II. More than 4 customers arrive",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Suppose that customers arrive at a bank according to a poisson process with mean...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q4c",
          "qno": "4(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "Markov Chains & Transition Matrices",
            "Eigenvalues & Eigenvectors"
          ],
          "question": "Three boys A, B and C are throwing a ball to each other. A always throws the ball to B and B always throws the ball to C, but C is as likely to throw the ball to B as to A. If the initial probability distribution of three states A, B, C is 0.3, 0.4 and 0.3 respectively, Find: **[6]**  \n    I. The transition matrix.  \n    II. $P(X_2 = B)$  \n    III. $P(X_3 = B, X_2 = C, X_1 = B, X_0 = A)$ and  \n    IV. The distribution of the ball after two rounds.\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(c) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Three boys A, B and C are throwing a ball to each other. A always throws the bal...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(c).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 4 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2024-set5",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2024,
      "set_no": 5,
      "qno": "Question 5",
      "marks": 14,
      "topics": [
        "Linear Programming & Optimization",
        "Duality Theory & Simplex",
        "Markov Chains & Transition Matrices",
        "Stochastic & Stationary Processes"
      ],
      "question": "(a) A toy store wants to buy teddy bears and toy cars to sell during a festival. **[2]**  \nLet $T = \\text{number of teddy bears}$, $C = \\text{number of toy cars}$.  \nCost per teddy bear: Tk 35, Cost per toy car: Tk 25.  \nBudget: Tk 4500; Maximum storage capacity: 50 toys.  \nProfit: Tk 5 per teddy bear, Tk 3 per toy.  \nFormulate a linear programming problem by:  \ni. Write the constraints  \nii. Write the objective function to maximize total profit  \n\n(b) What is Monte Carlo Simulation? Define the Graphical Method and the Simplex Method in linear programming. **[3]**  \n(c) State the Weak Duality Theorem and Strong Duality Theorem. Explain their importance/application of LP in optimization. **[4]**  \n(d) What is meant by stationary process? Describe with formula First Order Stationary Process and Second Order Stationary Process. **[5]**",
      "subparts": [
        {
          "id": "cse-4102-final-2024-q5a",
          "qno": "5(a)",
          "label": "(a)",
          "marks": 2,
          "topics": [
            "Linear Programming & Optimization"
          ],
          "question": "A toy store wants to buy teddy bears and toy cars to sell during a festival. **[2]**  \nLet $T = \\text{number of teddy bears}$, $C = \\text{number of toy cars}$.  \nCost per teddy bear: Tk 35, Cost per toy car: Tk 25.  \nBudget: Tk 4500; Maximum storage capacity: 50 toys.  \nProfit: Tk 5 per teddy bear, Tk 3 per toy.  \nFormulate a linear programming problem by:  \ni. Write the constraints  \nii. Write the objective function to maximize total profit",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(a) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: A toy store wants to buy teddy bears and toy cars to sell during a festival. **[...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(a).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q5b",
          "qno": "5(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Linear Programming & Optimization",
            "Duality Theory & Simplex"
          ],
          "question": "What is Monte Carlo Simulation? Define the Graphical Method and the Simplex Method in linear programming.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is Monte Carlo Simulation? Define the Graphical Method and the Simplex Meth...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q5c",
          "qno": "5(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Markov Chains & Transition Matrices",
            "Linear Programming & Optimization",
            "Duality Theory & Simplex"
          ],
          "question": "State the Weak Duality Theorem and Strong Duality Theorem. Explain their importance/application of LP in optimization.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: State the Weak Duality Theorem and Strong Duality Theorem. Explain their importa...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q5d",
          "qno": "5(d)",
          "label": "(d)",
          "marks": 5,
          "topics": [
            "Stochastic & Stationary Processes"
          ],
          "question": "What is meant by stationary process? Describe with formula First Order Stationary Process and Second Order Stationary Process. **[5]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(d) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: What is meant by stationary process? Describe with formula First Order Stationar...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(d).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 5 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2024-set6",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2024,
      "set_no": 6,
      "qno": "Question 6",
      "marks": 14,
      "topics": [
        "Eigenvalues & Eigenvectors",
        "Correlation & Covariance",
        "Duality Theory & Simplex"
      ],
      "question": "(a) Eigen values and eigenvectors provide insights into linear transformations, system stability. and dimensionality reduction in data analysis. Find all the Eigen values and Eigenvectors of the matrix: **[5]**  \n$$\\begin{bmatrix} 1 & 2 & 3 \\\\ 0 & -2 & 6 \\\\ 0 & 0 & -3 \\end{bmatrix}$$  \n(b) Define cross-correlation function between two random processes $X(t)$ and $Y(t)$. How does it differ from autocorrelation? **[4]**  \n(c) Convert Primal to the dual of the given problem. **[5]**  \n$$\\text{Max } Z = 3x_1 + 5x_2 + 4x_3$$  \n$$\\text{Subject to}$$  \n$$2x_1 + 3x_2 \\le 8$$  \n$$2x_2 + 5x_3 \\le 10$$  \n$$3x_1 + 2x_2 + 4x_3 \\le 15$$  \n$$x_1, x_2, x_3 \\ge 0$$",
      "subparts": [
        {
          "id": "cse-4102-final-2024-q6a",
          "qno": "6(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Eigenvalues & Eigenvectors"
          ],
          "question": "Eigen values and eigenvectors provide insights into linear transformations, system stability. and dimensionality reduction in data analysis. Find all the Eigen values and Eigenvectors of the matrix: **[5]**  \n$$\\begin{bmatrix} 1 & 2 & 3 \\\\ 0 & -2 & 6 \\\\ 0 & 0 & -3 \\end{bmatrix}$$",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Eigen values and eigenvectors provide insights into linear transformations, syst...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q6b",
          "qno": "6(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "Define cross-correlation function between two random processes $X(t)$ and $Y(t)$. How does it differ from autocorrelation?",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Define cross-correlation function between two random processes $X(t)$ and $Y(t)$...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q6c",
          "qno": "6(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Duality Theory & Simplex"
          ],
          "question": "Convert Primal to the dual of the given problem. **[5]**  \n$$\\text{Max } Z = 3x_1 + 5x_2 + 4x_3$$  \n$$\\text{Subject to}$$  \n$$2x_1 + 3x_2 \\le 8$$  \n$$2x_2 + 5x_3 \\le 10$$  \n$$3x_1 + 2x_2 + 4x_3 \\le 15$$  \n$$x_1, x_2, x_3 \\ge 0$$\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(c) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Convert Primal to the dual of the given problem. **[5]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(c).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 6 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4102-final-2024-set7",
      "course": "CSE-4102",
      "exam": "final",
      "year": 2024,
      "set_no": 7,
      "qno": "Question 7",
      "marks": 14,
      "topics": [
        "Linear Programming & Optimization",
        "Markov Chains & Transition Matrices",
        "Correlation & Covariance",
        "Eigenvalues & Eigenvectors"
      ],
      "question": "(a) Define linear optimization. Explain why optimization is important in engineering. **[3]**  \n(b) A birth-death process has birth rate $\\lambda_n = \\lambda$ and death rate $\\mu_n = n\\mu, \\; n \\ge 1$. **[5]**  \n    (a) Derive the steady-state probability distribution.  \n    (b) State the condition for positive recurrence.  \n    (c) Compute the mean number of customers in the system.  \n(c) Explain how equality constraints affect the feasible region of an LP problem. **[3]**  \n(d) Explain how the probability distribution after k trials is obtained using the state transition matrix. **[3]**\n\n---",
      "subparts": [
        {
          "id": "cse-4102-final-2024-q7a",
          "qno": "7(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Linear Programming & Optimization"
          ],
          "question": "Define linear optimization. Explain why optimization is important in engineering.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define linear optimization. Explain why optimization is important in engineering...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q7b",
          "qno": "7(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Markov Chains & Transition Matrices"
          ],
          "question": "A birth-death process has birth rate $\\lambda_n = \\lambda$ and death rate $\\mu_n = n\\mu, \\; n \\ge 1$. **[5]**  \n    (a) Derive the steady-state probability distribution.  \n    (b) State the condition for positive recurrence.  \n    (c) Compute the mean number of customers in the system.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: A birth-death process has birth rate $\\lambda_n = \\lambda$ and death rate $\\mu_n...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q7c",
          "qno": "7(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "Correlation & Covariance"
          ],
          "question": "Explain how equality constraints affect the feasible region of an LP problem.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(c) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain how equality constraints affect the feasible region of an LP problem....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(c).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4102-final-2024-q7d",
          "qno": "7(d)",
          "label": "(d)",
          "marks": 3,
          "topics": [
            "Markov Chains & Transition Matrices",
            "Eigenvalues & Eigenvectors"
          ],
          "question": "Explain how the probability distribution after k trials is obtained using the state transition matrix. **[3]**\n\n---\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(d) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain how the probability distribution after k trials is obtained using the st...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(d).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 7 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
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
      "question": "1. If $\\mathcal{L}\\{f(t)\\} = F(s)$, then prove that $\\mathcal{L}\\{\\frac{f(t)}{t}\\} = \\int_s^\\infty F(u) \\, du$. **[4]**  \n2. Perform the inverse Laplace transform of the following expression: $\\frac{s}{(s^2 + a^2)^2}$. **[3]**  \n3. It is found that 250 errors in the randomly selected 1000 lines of code from Team A and 300 errors in 800 lines of code from Team B. Can we assume that team B's performance is superior to that of A? **[4]**  \n4. It's a Boy Genetic Labs claim to be able to increase the likelihood that a pregnancy will result in a boy being born. Statisticians want to test the claim. Suppose that the null hypothesis is: *It's a Boy Genetic Labs has no effect on gender outcome*. State the Type I and Type II errors. **[2]**  \n5. Use Laplace transformation to solve the following initial value problem: $y'' - y' - 2y = 0$, with $y(0) = 1, y'(0) = 2$. **[4]**  \n6. What is Cross-correlation? Write the difference between covariance and correlation. **[3]**",
      "subparts": [
        {
          "id": "cse-4102-term-mec-tt1-q1",
          "qno": "1",
          "label": "1",
          "marks": 4,
          "topics": [
            "Laplace Transforms"
          ],
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
          "topics": [
            "Inverse Laplace & ODEs"
          ],
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
          "topics": [
            "Hypothesis Testing & Errors"
          ],
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
          "topics": [
            "Hypothesis Testing & Errors"
          ],
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
          "topics": [
            "Inverse Laplace & ODEs"
          ],
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
          "topics": [
            "Correlation & Covariance"
          ],
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
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for MEC CSE-4102 Term Test 1 (20 Marks total).",
        "marking_hint": "Full marks (20 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
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
      "question": "1. Why do we use Fourier transform? Perform the Fourier transform of function: find $\\mathcal{F}\\left\\{\\frac{1}{2}\\left[H\\left(t+\\frac{1}{2}\\right) - H\\left(t-\\frac{1}{2}\\right)\\right]\\right\\}$ where $\\mathcal{F}\\{H(t)\\} = F(\\omega) = \\frac{2i}{\\omega}$.  \n2. Find Fourier transform of $f(x) = \\frac{e^{-ax}}{x}$.  \n3. Parseval's identity ensures energy conservation, relating time and frequency domain representations of signals. Using Parseval's identity if $f(x) = \\begin{cases} 1, & |x| < a \\\\ 0, & |x| > a \\end{cases}$ and $F(s) = \\sqrt{\\frac{2}{\\pi}} \\frac{\\sin sa}{s}$, now find that $\\int_0^\\infty \\frac{\\sin^2 x}{x^2} \\, dx = ?$.  \n4. Find Fourier sine transform of $f(x) = \\begin{cases} x, & 0 < x < 1 \\\\ 2-x, & 1 < x < 2 \\\\ 0, & x > 2 \\end{cases}$.",
      "subparts": [
        {
          "id": "cse-4102-term-mec-tt2-q1",
          "qno": "1",
          "label": "1",
          "marks": 5,
          "topics": [
            "Fourier Transforms & Parseval Identity"
          ],
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
          "topics": [
            "Fourier Transforms & Parseval Identity"
          ],
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
          "topics": [
            "Fourier Transforms & Parseval Identity"
          ],
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
          "topics": [
            "Fourier Transforms & Parseval Identity"
          ],
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
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for MEC CSE-4102 Term Test 2 (20 Marks total).",
        "marking_hint": "Full marks (20 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
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
      "question": "1. Three boys A, B and C are throwing a ball to each other. A always throws the ball to B and B always throws the ball to C, but C is as likely to throw the ball to B as to A. If the initial probability distribution of three states A, B, C is 0.3, 0.4 and 0.3 respectively, Find: **[8]**  \n   I. The transition matrix.  \n   II. $P(X_2 = B)$  \n   III. $P(X_3 = B, X_2 = C, X_1 = B, X_0 = A)$  \n   IV. The distribution of the ball after two rounds.  \n2. Billy and Dilly decide to flip two fair coins. If they get at least one head from a flip, then Billy is decided winner of that flip. Otherwise, Dilly is declared winner. After each flip, the winner receives $20 from the loser. If Billy starts with $40 and Dilly with $120, then what is the probability that Billy will wipe Dilly out? **[4]**  \n3. A Commercial bank has 1 cash paying assistant. Customers are found to arrive in a Poisson fashion at an average rate of 6/hr for business transaction. The service time is found to have an Exponential Distribution with a mean of 6 mins ($\\mu = 10$/hr). The customers are processed on FCFS basis. Calculate: **[8]**  \n   I. Average number of customers in the system ($L$)  \n   II. Average time a customer spends in the system ($W$)  \n   III. Average queue length ($L_q$)  \n   IV. How many hours a week (assuming 40-hr week) can a cash paying assistant spend with the customers.",
      "subparts": [
        {
          "id": "cse-4102-term-mec-tt3-q1",
          "qno": "1",
          "label": "1",
          "marks": 8,
          "topics": [
            "Markov Chains & Transition Matrices"
          ],
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
          "topics": [
            "Stochastic & Stationary Processes"
          ],
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
          "topics": [
            "Queueing Theory & Little's Law"
          ],
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
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for MEC CSE-4102 Term Test 3 (20 Marks total).",
        "marking_hint": "Full marks (20 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    }
  ],
  "cse-4125": [
    {
      "id": "cse-4125-final-2023-set1",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2023,
      "set_no": 1,
      "qno": "Question 1",
      "marks": 14,
      "topics": [
        "Supervised vs Unsupervised Learning",
        "Neural Networks & Deep Learning",
        "Model Evaluation & Overfitting"
      ],
      "question": "(a) What do you mean by machine learning? **[2]**  \n(b) Differentiate among machine learning, deep learning and artificial intelligence. **[5]**  \n(c) Describe about the different data processing steps. **[5]**  \n(d) What is bias and variance? **[2]**",
      "subparts": [
        {
          "id": "cse-4125-final-2023-q1a",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 2,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "What do you mean by machine learning?",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(a) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: What do you mean by machine learning?...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(a).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q1b",
          "qno": "1(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Neural Networks & Deep Learning"
          ],
          "question": "Differentiate among machine learning, deep learning and artificial intelligence.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Differentiate among machine learning, deep learning and artificial intelligence....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q1c",
          "qno": "1(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Model Evaluation & Overfitting"
          ],
          "question": "Describe about the different data processing steps.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(c) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe about the different data processing steps....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(c).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q1d",
          "qno": "1(d)",
          "label": "(d)",
          "marks": 2,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "What is bias and variance? **[2]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(d) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: What is bias and variance? **[2]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(d).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 1 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2023-set2",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2023,
      "set_no": 2,
      "qno": "Question 2",
      "marks": 14,
      "topics": [
        "Linear & Logistic Regression",
        "Clustering (K-Means, Hierarchical)"
      ],
      "question": "(a) Define logistic regression. How can logistic regression be extended or adapted for multiclass classification problems? **[3]**  \n(b) What are some common linkage criteria used in hierarchical clustering? How do you determine the optimal number of clusters in k-means clustering? **[5]**  \n(c) Explain the concept of sigmoid function. Let's say you have a dataset with 6 points in a 2D space : A(1,2), B(1,4), C(1,0), D(4,2), E(4,4), F(4,0). Imagine you cluster these points into two clusters : Cluster 1 : A, B, C and Cluster 2 : D, E, F. Calculate the Within-Cluster Sum of Squares (WCSS) for this clustering. **[6]**",
      "subparts": [
        {
          "id": "cse-4125-final-2023-q2a",
          "qno": "2(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Linear & Logistic Regression"
          ],
          "question": "Define logistic regression. How can logistic regression be extended or adapted for multiclass classification problems?",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define logistic regression. How can logistic regression be extended or adapted f...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q2b",
          "qno": "2(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Clustering (K-Means, Hierarchical)"
          ],
          "question": "What are some common linkage criteria used in hierarchical clustering? How do you determine the optimal number of clusters in k-means clustering?",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: What are some common linkage criteria used in hierarchical clustering? How do yo...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q2c",
          "qno": "2(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "Clustering (K-Means, Hierarchical)"
          ],
          "question": "Explain the concept of sigmoid function. Let's say you have a dataset with 6 points in a 2D space : A(1,2), B(1,4), C(1,0), D(4,2), E(4,4), F(4,0). Imagine you cluster these points into two clusters : Cluster 1 : A, B, C and Cluster 2 : D, E, F. Calculate the Within-Cluster Sum of Squares (WCSS) for this clustering. **[6]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(c) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain the concept of sigmoid function. Let's say you have a dataset with 6 poi...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(c).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 2 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2023-set3",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2023,
      "set_no": 3,
      "qno": "Question 3",
      "marks": 14,
      "topics": [
        "Decision Trees & Random Forests",
        "Model Evaluation & Overfitting",
        "Support Vector Machines (SVM)",
        "Supervised vs Unsupervised Learning"
      ],
      "question": "(a) Assume a classification problem for 14 random data points. Calculate the binary cross entropy.  \n$x = [-2.2, -1.6, -1.4, -1.2, -0.8, 0.2, 0.4, 0.8, 1.2, 1.4, 2.2, 2.9, 3.2, 4.6]$ **[5]**  \n(b) What is confusion matrix and ROC curve? **[2]**  \n(c) Explain the support vector machine (SVM) algorithm for binary classification. **[4]**  \n(d) Explain the concept of feature extraction and how it differs from feature selection. **[3]**",
      "subparts": [
        {
          "id": "cse-4125-final-2023-q3a",
          "qno": "3(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Decision Trees & Random Forests"
          ],
          "question": "Assume a classification problem for 14 random data points. Calculate the binary cross entropy.  \n$x = [-2.2, -1.6, -1.4, -1.2, -0.8, 0.2, 0.4, 0.8, 1.2, 1.4, 2.2, 2.9, 3.2, 4.6]$",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Assume a classification problem for 14 random data points. Calculate the binary ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q3b",
          "qno": "3(b)",
          "label": "(b)",
          "marks": 2,
          "topics": [
            "Model Evaluation & Overfitting"
          ],
          "question": "What is confusion matrix and ROC curve?",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(b) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: What is confusion matrix and ROC curve?...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(b).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q3c",
          "qno": "3(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Support Vector Machines (SVM)"
          ],
          "question": "Explain the support vector machine (SVM) algorithm for binary classification.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain the support vector machine (SVM) algorithm for binary classification....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q3d",
          "qno": "3(d)",
          "label": "(d)",
          "marks": 3,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Explain the concept of feature extraction and how it differs from feature selection. **[3]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(d) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain the concept of feature extraction and how it differs from feature select...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(d).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 3 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2023-set4",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2023,
      "set_no": 4,
      "qno": "Question 4",
      "marks": 14,
      "topics": [
        "Dimensionality Reduction & PCA",
        "Decision Trees & Random Forests",
        "Model Evaluation & Overfitting"
      ],
      "question": "(a) What is curse of dimensionality? Explain principal component analysis (PCA) and how it helps in dimensionality reduction. **[3]**  \n(b) Define entropy and information gain. Explain how decision tree works. **[5]**  \n(c) Explain the concept of stratified k-fold cross-validation. Why is it preferred in classification tasks, especially when dealing with imbalanced datasets? **[3]**  \n(d) Define and differentiate between precision, recall, and F1 score. **[3]**",
      "subparts": [
        {
          "id": "cse-4125-final-2023-q4a",
          "qno": "4(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Dimensionality Reduction & PCA"
          ],
          "question": "What is curse of dimensionality? Explain principal component analysis (PCA) and how it helps in dimensionality reduction.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is curse of dimensionality? Explain principal component analysis (PCA) and ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q4b",
          "qno": "4(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Decision Trees & Random Forests"
          ],
          "question": "Define entropy and information gain. Explain how decision tree works.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Define entropy and information gain. Explain how decision tree works....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q4c",
          "qno": "4(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "Model Evaluation & Overfitting"
          ],
          "question": "Explain the concept of stratified k-fold cross-validation. Why is it preferred in classification tasks, especially when dealing with imbalanced datasets?",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(c) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain the concept of stratified k-fold cross-validation. Why is it preferred i...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(c).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q4d",
          "qno": "4(d)",
          "label": "(d)",
          "marks": 3,
          "topics": [
            "Model Evaluation & Overfitting"
          ],
          "question": "Define and differentiate between precision, recall, and F1 score. **[3]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(d) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define and differentiate between precision, recall, and F1 score. **[3]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(d).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 4 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2023-set5",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2023,
      "set_no": 5,
      "qno": "Question 5",
      "marks": 14,
      "topics": [
        "Supervised vs Unsupervised Learning"
      ],
      "question": "(a) Define the Expectation Maximization Algorithm. Discuss convergence properties of the Expectation Maximization Algorithm. **[3]**  \n(b) Define imbalanced dataset. Explain any two techniques to handle imbalanced dataset. **[3]**  \n(c) What is markov property? Consider a Markov model with three states Sunny, Rainy, and Cloudy. The transition probability matrix is given by: **[5]**\n\n| | Sunny | Rainy | Cloudy |\n|---|---|---|---|\n| **Sunny** | 0.8 | 0.15 | 0.05 |\n| **Rainy** | 0.38 | 0.6 | 0.02 |\n| **Cloudy** | 0.75 | 0.05 | 0.3 |\n\nGiven that, the weather is Sunny today. What is the probability that tomorrow is Sunny and day after tomorrow is Rainy?  \n(d) Define feature engineering and explain its importance in machine learning. **[3]**",
      "subparts": [
        {
          "id": "cse-4125-final-2023-q5a",
          "qno": "5(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Define the Expectation Maximization Algorithm. Discuss convergence properties of the Expectation Maximization Algorithm.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define the Expectation Maximization Algorithm. Discuss convergence properties of...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q5b",
          "qno": "5(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Define imbalanced dataset. Explain any two techniques to handle imbalanced dataset.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define imbalanced dataset. Explain any two techniques to handle imbalanced datas...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q5c",
          "qno": "5(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "What is markov property? Consider a Markov model with three states Sunny, Rainy, and Cloudy. The transition probability matrix is given by: **[5]**\n\n| | Sunny | Rainy | Cloudy |\n|---|---|---|---|\n| **Sunny** | 0.8 | 0.15 | 0.05 |\n| **Rainy** | 0.38 | 0.6 | 0.02 |\n| **Cloudy** | 0.75 | 0.05 | 0.3 |\n\nGiven that, the weather is Sunny today. What is the probability that tomorrow is Sunny and day after tomorrow is Rainy?",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(c) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: What is markov property? Consider a Markov model with three states Sunny, Rainy,...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(c).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q5d",
          "qno": "5(d)",
          "label": "(d)",
          "marks": 3,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Define feature engineering and explain its importance in machine learning. **[3]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(d) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define feature engineering and explain its importance in machine learning. **[3]...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(d).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 5 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2023-set6",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2023,
      "set_no": 6,
      "qno": "Question 6",
      "marks": 14,
      "topics": [
        "Supervised vs Unsupervised Learning",
        "Model Evaluation & Overfitting"
      ],
      "question": "(a) Define feature engineering and explain its importance in machine learning. **[3]**  \n(b) Describe about the working procedure of principal component analysis. **[6]**  \n(c) Explain about the expectation maximization algorithm. **[5]**",
      "subparts": [
        {
          "id": "cse-4125-final-2023-q6a",
          "qno": "6(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Define feature engineering and explain its importance in machine learning.",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define feature engineering and explain its importance in machine learning....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q6b",
          "qno": "6(b)",
          "label": "(b)",
          "marks": 6,
          "topics": [
            "Model Evaluation & Overfitting"
          ],
          "question": "Describe about the working procedure of principal component analysis.",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(b) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe about the working procedure of principal component analysis....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(b).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q6c",
          "qno": "6(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Explain about the expectation maximization algorithm. **[5]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(c) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain about the expectation maximization algorithm. **[5]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(c).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 6 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2023-set7",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2023,
      "set_no": 7,
      "qno": "Question 7",
      "marks": 14,
      "topics": [
        "Supervised vs Unsupervised Learning",
        "k-Nearest Neighbors (k-NN)"
      ],
      "question": "(a) Discuss details about probability density function. **[6]**  \n(b) Using k-nearest neighbors algorithm find the class(?) where $k = 5$. **[8]**\n\n**Training Set:**\n| Brightness | Saturation | Class |\n|:---:|:---:|:---:|\n| 40 | 20 | Red |\n| 50 | 50 | Blue |\n| 60 | 90 | Blue |\n| 10 | 25 | Red |\n| 70 | 70 | Blue |\n| 60 | 10 | Red |\n| 25 | 80 | Blue |\n\n**Query Point:**\n| Brightness | Saturation | Class |\n|:---:|:---:|:---:|\n| 20 | 35 | ? |\n\n---",
      "subparts": [
        {
          "id": "cse-4125-final-2023-q7a",
          "qno": "7(a)",
          "label": "(a)",
          "marks": 6,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Discuss details about probability density function.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(a) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Discuss details about probability density function....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(a).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2023-q7b",
          "qno": "7(b)",
          "label": "(b)",
          "marks": 8,
          "topics": [
            "k-Nearest Neighbors (k-NN)"
          ],
          "question": "Using k-nearest neighbors algorithm find the class(?) where $k = 5$. **[8]**\n\n**Training Set:**\n| Brightness | Saturation | Class |\n|:---:|:---:|:---:|\n| 40 | 20 | Red |\n| 50 | 50 | Blue |\n| 60 | 90 | Blue |\n| 10 | 25 | Red |\n| 70 | 70 | Blue |\n| 60 | 10 | Red |\n| 25 | 80 | Blue |\n\n**Query Point:**\n| Brightness | Saturation | Class |\n|:---:|:---:|:---:|\n| 20 | 35 | ? |\n\n---\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(b) (8 Marks).",
              "Define core technical terms and theoretical background relevant to: Using k-nearest neighbors algorithm find the class(?) where $k = 5$. **[8]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(b).",
            "marking_hint": "Full marks (8 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 7 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2024-set1",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2024,
      "set_no": 1,
      "qno": "Question 1",
      "marks": 14,
      "topics": [
        "Supervised vs Unsupervised Learning",
        "Model Evaluation & Overfitting"
      ],
      "question": "(a) Define machine learning. Briefly explain the differences between supervised, unsupervised, and reinforcement learning. **[3]**  \n(b) Define overfitting and underfitting. How does it impact model performance? **[4]**  \n(c) Describe in detail applications of machine learning in any three different knowledge domains. **[3]**  \n(d) Why encoding is necessary in machine learning? Explain one hot encoding technique with proper example. **[4]**",
      "subparts": [
        {
          "id": "cse-4125-final-2024-q1a",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Define machine learning. Briefly explain the differences between supervised, unsupervised, and reinforcement learning.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define machine learning. Briefly explain the differences between supervised, uns...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q1b",
          "qno": "1(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Model Evaluation & Overfitting"
          ],
          "question": "Define overfitting and underfitting. How does it impact model performance?",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Define overfitting and underfitting. How does it impact model performance?...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q1c",
          "qno": "1(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Describe in detail applications of machine learning in any three different knowledge domains.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(c) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe in detail applications of machine learning in any three different knowl...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(c).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q1d",
          "qno": "1(d)",
          "label": "(d)",
          "marks": 4,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Why encoding is necessary in machine learning? Explain one hot encoding technique with proper example. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(d) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Why encoding is necessary in machine learning? Explain one hot encoding techniqu...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(d).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 1 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2024-set2",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2024,
      "set_no": 2,
      "qno": "Question 2",
      "marks": 14,
      "topics": [
        "Linear & Logistic Regression",
        "Dimensionality Reduction & PCA",
        "Clustering (K-Means, Hierarchical)"
      ],
      "question": "(a) Explain linear regression with its cost function and describe how gradient descent is used to optimize the model parameters. **[4]**  \n(b) What do you mean by dimensionality reduction? Discuss about linear discriminant analysis (LDA). **[4]**  \n(c) Let's assume a dataset with 6 points in a 2D space: $A(1,2), B(1,4), C(1,0), D(4,2), E(4,4)$, and $F(4,0)$. Assume these points are assigned to two clusters: **[6]**  \n    • Cluster 1: $\\{A, B, C\\}$  \n    • Cluster 2: $\\{D, E, F\\}$  \n    Calculate the within-cluster sum of squares for this clustering.",
      "subparts": [
        {
          "id": "cse-4125-final-2024-q2a",
          "qno": "2(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Linear & Logistic Regression"
          ],
          "question": "Explain linear regression with its cost function and describe how gradient descent is used to optimize the model parameters.",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(a) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain linear regression with its cost function and describe how gradient desce...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(a).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q2b",
          "qno": "2(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Dimensionality Reduction & PCA"
          ],
          "question": "What do you mean by dimensionality reduction? Discuss about linear discriminant analysis (LDA).",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What do you mean by dimensionality reduction? Discuss about linear discriminant ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q2c",
          "qno": "2(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "Clustering (K-Means, Hierarchical)"
          ],
          "question": "Let's assume a dataset with 6 points in a 2D space: $A(1,2), B(1,4), C(1,0), D(4,2), E(4,4)$, and $F(4,0)$. Assume these points are assigned to two clusters: **[6]**  \n    • Cluster 1: $\\{A, B, C\\}$  \n    • Cluster 2: $\\{D, E, F\\}$  \n    Calculate the within-cluster sum of squares for this clustering.\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(c) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Let's assume a dataset with 6 points in a 2D space: $A(1,2), B(1,4), C(1,0), D(4...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(c).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 2 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2024-set3",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2024,
      "set_no": 3,
      "qno": "Question 3",
      "marks": 14,
      "topics": [
        "Supervised vs Unsupervised Learning"
      ],
      "question": "(a) Discuss shortly sigmoid function and feature vector in machine learning. **[4]**  \n(b) Define bias and variance, and discuss the bias-variance trade-off in supervised learning. **[4]**  \n(c) What is a Markov Chain? Consider a Weather Model with two states: $S = \\text{Sunny}, R = \\text{Rainy}$. **[6]**  \n    $$\\text{Transition Matrix: } P = \\begin{bmatrix} 0.8 & 0.2 \\\\ 0.4 & 0.6 \\end{bmatrix}$$  \n    $$\\text{Initial State Distribution: } \\pi = [P(X_1 = S) = 0.6, \\; P(X_1 = R) = 0.4]$$  \n    If today is Sunny ($X_1 = S$), find the probability that the day after tomorrow is Rainy.",
      "subparts": [
        {
          "id": "cse-4125-final-2024-q3a",
          "qno": "3(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Discuss shortly sigmoid function and feature vector in machine learning.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(a) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Discuss shortly sigmoid function and feature vector in machine learning....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(a).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q3b",
          "qno": "3(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Define bias and variance, and discuss the bias-variance trade-off in supervised learning.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Define bias and variance, and discuss the bias-variance trade-off in supervised ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q3c",
          "qno": "3(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "What is a Markov Chain? Consider a Weather Model with two states: $S = \\text{Sunny}, R = \\text{Rainy}$. **[6]**  \n    $$\\text{Transition Matrix: } P = \\begin{bmatrix} 0.8 & 0.2 \\\\ 0.4 & 0.6 \\end{bmatrix}$$  \n    $$\\text{Initial State Distribution: } \\pi = [P(X_1 = S) = 0.6, \\; P(X_1 = R) = 0.4]$$  \n    If today is Sunny ($X_1 = S$), find the probability that the day after tomorrow is Rainy.\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(c) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: What is a Markov Chain? Consider a Weather Model with two states: $S = \\text{Sun...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(c).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 3 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2024-set4",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2024,
      "set_no": 4,
      "qno": "Question 4",
      "marks": 14,
      "topics": [
        "Linear & Logistic Regression",
        "Clustering (K-Means, Hierarchical)",
        "Supervised vs Unsupervised Learning"
      ],
      "question": "(a) Briefly describe logistic regression and its role in classification tasks. **[3]**  \n(b) What is clustering? For the given dataset: $A = (1, 1), B = (1.5, 2), C = (5, 5), D = (6, 5)$, perform k-means clustering with $K = 2$. (Show all numeric steps in 2D). **[5]**  \n(c) Describe the probability density function and provide a proper example illustrating its use. **[6]**",
      "subparts": [
        {
          "id": "cse-4125-final-2024-q4a",
          "qno": "4(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Linear & Logistic Regression"
          ],
          "question": "Briefly describe logistic regression and its role in classification tasks.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Briefly describe logistic regression and its role in classification tasks....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q4b",
          "qno": "4(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Clustering (K-Means, Hierarchical)"
          ],
          "question": "What is clustering? For the given dataset: $A = (1, 1), B = (1.5, 2), C = (5, 5), D = (6, 5)$, perform k-means clustering with $K = 2$. (Show all numeric steps in 2D).",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: What is clustering? For the given dataset: $A = (1, 1), B = (1.5, 2), C = (5, 5)...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q4c",
          "qno": "4(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Describe the probability density function and provide a proper example illustrating its use. **[6]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(c) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe the probability density function and provide a proper example illustrat...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(c).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 4 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2024-set5",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2024,
      "set_no": 5,
      "qno": "Question 5",
      "marks": 14,
      "topics": [
        "Supervised vs Unsupervised Learning",
        "Model Evaluation & Overfitting"
      ],
      "question": "(a) What is meant by maximum margin hyperplane? **[2]**  \n(b) What is a linearly separable dataset? What is a kernel function? Give an example. **[3]**  \n(c) Describe EM algorithm for Gaussian mixtures. **[4]**  \n(d) What is a confusion matrix? Suppose 10000 patients get tested for flu; out of them, 9000 are actually healthy and 1000 are actually sick. For the sick people, a test was positive for 620 and negative for 380. For the healthy people, the same test was positive for 180 and negative for 8820. Construct a confusion matrix for the data and compute the accuracy, precision and recall for the data. **[5]**",
      "subparts": [
        {
          "id": "cse-4125-final-2024-q5a",
          "qno": "5(a)",
          "label": "(a)",
          "marks": 2,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "What is meant by maximum margin hyperplane?",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(a) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: What is meant by maximum margin hyperplane?...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(a).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q5b",
          "qno": "5(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "What is a linearly separable dataset? What is a kernel function? Give an example.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is a linearly separable dataset? What is a kernel function? Give an example...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q5c",
          "qno": "5(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Describe EM algorithm for Gaussian mixtures.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe EM algorithm for Gaussian mixtures....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q5d",
          "qno": "5(d)",
          "label": "(d)",
          "marks": 5,
          "topics": [
            "Model Evaluation & Overfitting"
          ],
          "question": "What is a confusion matrix? Suppose 10000 patients get tested for flu; out of them, 9000 are actually healthy and 1000 are actually sick. For the sick people, a test was positive for 620 and negative for 380. For the healthy people, the same test was positive for 180 and negative for 8820. Construct a confusion matrix for the data and compute the accuracy, precision and recall for the data. **[5]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(d) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: What is a confusion matrix? Suppose 10000 patients get tested for flu; out of th...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(d).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 5 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2024-set6",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2024,
      "set_no": 6,
      "qno": "Question 6",
      "marks": 14,
      "topics": [
        "Model Evaluation & Overfitting",
        "Decision Trees & Random Forests",
        "Linear & Logistic Regression",
        "k-Nearest Neighbors (k-NN)"
      ],
      "question": "(a) What is cross-validation in machine learning? Explain the k-fold cross-validation technique and its purpose. **[5]**  \n(b) Define binary cross-entropy and the concept of a best fit line in regression applications. **[3]**  \n(c) Consider the following dataset: **[6]**\n\n| Brightness | Saturation | Class |\n|:---:|:---:|:---:|\n| 40 | 20 | Red |\n| 50 | 50 | Blue |\n| 60 | 90 | Blue |\n| 10 | 25 | Red |\n| 70 | 70 | Blue |\n| 60 | 10 | Red |\n| 25 | 80 | Blue |\n\nAssume the k-nearest neighbors' classifier is used with: $k = 5$  \nA new data point is given as: $x_q = (45, 30)$.  \nUsing Euclidean distance, compute the distance between the new data point $x_q$ and each point in the dataset.",
      "subparts": [
        {
          "id": "cse-4125-final-2024-q6a",
          "qno": "6(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Model Evaluation & Overfitting"
          ],
          "question": "What is cross-validation in machine learning? Explain the k-fold cross-validation technique and its purpose.",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: What is cross-validation in machine learning? Explain the k-fold cross-validatio...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q6b",
          "qno": "6(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Decision Trees & Random Forests",
            "Linear & Logistic Regression"
          ],
          "question": "Define binary cross-entropy and the concept of a best fit line in regression applications.",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define binary cross-entropy and the concept of a best fit line in regression app...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q6c",
          "qno": "6(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "k-Nearest Neighbors (k-NN)"
          ],
          "question": "Consider the following dataset: **[6]**\n\n| Brightness | Saturation | Class |\n|:---:|:---:|:---:|\n| 40 | 20 | Red |\n| 50 | 50 | Blue |\n| 60 | 90 | Blue |\n| 10 | 25 | Red |\n| 70 | 70 | Blue |\n| 60 | 10 | Red |\n| 25 | 80 | Blue |\n\nAssume the k-nearest neighbors' classifier is used with: $k = 5$  \nA new data point is given as: $x_q = (45, 30)$.  \nUsing Euclidean distance, compute the distance between the new data point $x_q$ and each point in the dataset.\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(c) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Consider the following dataset: **[6]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(c).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 6 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4125-final-2024-set7",
      "course": "CSE-4125",
      "exam": "final",
      "year": 2024,
      "set_no": 7,
      "qno": "Question 7",
      "marks": 14,
      "topics": [
        "Dimensionality Reduction & PCA",
        "Supervised vs Unsupervised Learning"
      ],
      "question": "(a) What is the curse of dimensionality in machine learning? Discuss how principal component analysis can be used to address this problem. **[6]**  \n(b) What is regularization? Suppose you have a dataset with 10 predictors, and some of them are irrelevant. Which regularization method—Ridge or Lasso—would you prefer, and why? **[4]**  \n(c) Define feature engineering. Describe the difference between normalization and standardization in feature scaling. **[4]**\n\n---",
      "subparts": [
        {
          "id": "cse-4125-final-2024-q7a",
          "qno": "7(a)",
          "label": "(a)",
          "marks": 6,
          "topics": [
            "Dimensionality Reduction & PCA"
          ],
          "question": "What is the curse of dimensionality in machine learning? Discuss how principal component analysis can be used to address this problem.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(a) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: What is the curse of dimensionality in machine learning? Discuss how principal c...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(a).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q7b",
          "qno": "7(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "What is regularization? Suppose you have a dataset with 10 predictors, and some of them are irrelevant. Which regularization method—Ridge or Lasso—would you prefer, and why?",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What is regularization? Suppose you have a dataset with 10 predictors, and some ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4125-final-2024-q7c",
          "qno": "7(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Supervised vs Unsupervised Learning"
          ],
          "question": "Define feature engineering. Describe the difference between normalization and standardization in feature scaling. **[4]**\n\n---\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Define feature engineering. Describe the difference between normalization and st...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 7 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
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
      "question": "(a) Apply $k(2)$-means algorithm over the data $(185,72), (170,56), (168,60), (179,68), (182,72), (188,77)$ up to two iterations and show the clusters. Initially choose first two objects as initial centroids. **[5]**  \n(b) Consider the given Dataset, Apply Naive Bayes Algorithm and Predict that if a fruit has the following properties then which type of the fruit it is:  \n**Fruit = {Yellow, Sweet, Long}** **[5]**\n\n**Frequency Table:**\n| Fruit | Yellow | Sweet | Long | Total |\n| :--- | :---: | :---: | :---: | :---: |\n| **Mango** | 350 | 450 | 0 | 650 |\n| **Banana** | 400 | 300 | 350 | 400 |\n| **Others** | 50 | 100 | 50 | 150 |\n| **Total** | 800 | 850 | 400 | 1200 |",
      "subparts": [
        {
          "id": "cse-4125-term-mec-tt1-qa",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Clustering (K-Means, Hierarchical)"
          ],
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
          "topics": [
            "Naive Bayes & Bayesian Learning"
          ],
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
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for MEC CSE-4125 Term Test 1 (10 Marks total).",
        "marking_hint": "Full marks (10 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
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
      "question": "1. How does KNN Work? **[3]**  \n2. Explain overfitting and underfitting. **[3]**  \n3. Explain Logistic Regression as a classification algorithm. **[4]**",
      "subparts": [
        {
          "id": "cse-4125-term-mec-tt2-q1",
          "qno": "1",
          "label": "1",
          "marks": 3,
          "topics": [
            "k-Nearest Neighbors (k-NN)"
          ],
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
          "topics": [
            "Model Evaluation & Overfitting"
          ],
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
          "topics": [
            "Linear & Logistic Regression"
          ],
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
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for MEC CSE-4125 Term Test 2 (10 Marks total).",
        "marking_hint": "Full marks (10 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    }
  ],
  "cse-4126": [
    {
      "id": "cse-4126-final-2023-set1",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2023,
      "set_no": 1,
      "qno": "Question 1",
      "marks": 14,
      "topics": [
        "Predictive Modeling & Applications",
        "Data Collection & Web Scraping"
      ],
      "question": "(a) Define Data Science? Mention the key difference between Qualitative data and Quantitative data. **[4]**  \n(b) Suppose, you own a software company. You need to collect data whether your customers are satisfied with your product or not. Which method will you apply to collect data? Explain the reasons behind choosing this method? **[4]**  \n(c) Breifly describe some common challenges in data collection. **[6]**",
      "subparts": [
        {
          "id": "cse-4126-final-2023-q1a",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Define Data Science? Mention the key difference between Qualitative data and Quantitative data.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(a) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Define Data Science? Mention the key difference between Qualitative data and Qua...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(a).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q1b",
          "qno": "1(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Suppose, you own a software company. You need to collect data whether your customers are satisfied with your product or not. Which method will you apply to collect data? Explain the reasons behind choosing this method?",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Suppose, you own a software company. You need to collect data whether your custo...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q1c",
          "qno": "1(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "Data Collection & Web Scraping"
          ],
          "question": "Breifly describe some common challenges in data collection. **[6]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(c) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Breifly describe some common challenges in data collection. **[6]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(c).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 1 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2023-set2",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2023,
      "set_no": 2,
      "qno": "Question 2",
      "marks": 14,
      "topics": [
        "Data Cleaning & Preprocessing",
        "Predictive Modeling & Applications"
      ],
      "question": "(a) Mention the reasons why data missing occured in a data set? **[2]**  \n(b) Explain KNN Imputation technique with an example to estimate the missing value from a data set. **[5]**  \n(c) What is data binning? Explain the suitable binning method to reduce noise, considering the following data: 10, 15, 22, 27, 30, 30, 36, 42, 50. **[5]**  \n(d) Write short note on the parameters of population. **[2]**",
      "subparts": [
        {
          "id": "cse-4126-final-2023-q2a",
          "qno": "2(a)",
          "label": "(a)",
          "marks": 2,
          "topics": [
            "Data Cleaning & Preprocessing"
          ],
          "question": "Mention the reasons why data missing occured in a data set?",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(a) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: Mention the reasons why data missing occured in a data set?...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(a).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q2b",
          "qno": "2(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Data Cleaning & Preprocessing"
          ],
          "question": "Explain KNN Imputation technique with an example to estimate the missing value from a data set.",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain KNN Imputation technique with an example to estimate the missing value f...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q2c",
          "qno": "2(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "What is data binning? Explain the suitable binning method to reduce noise, considering the following data: 10, 15, 22, 27, 30, 30, 36, 42, 50.",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(c) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: What is data binning? Explain the suitable binning method to reduce noise, consi...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(c).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q2d",
          "qno": "2(d)",
          "label": "(d)",
          "marks": 2,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Write short note on the parameters of population. **[2]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(d) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: Write short note on the parameters of population. **[2]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(d).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 2 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2023-set3",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2023,
      "set_no": 3,
      "qno": "Question 3",
      "marks": 14,
      "topics": [
        "Data Cleaning & Preprocessing",
        "Predictive Modeling & Applications"
      ],
      "question": "(a) What is an outlier data in a data set? Suppose, we have a data set on a subject marks out of 100 for 10 students as follows: 50, 55, 40, 62, 10, 33, 85, 77, 28, 82. Identify the marks are significantly different from others, which may indicate anomaly or outlier data. (Use Z-score based outlier detection technique to solve this). **[7]**  \n(b) Define data integration. What are the key aspects of data integration in data mining? **[3]**  \n(c) How to calculate corelation analysis to detect redundant attributes? Explain with example. **[4]**",
      "subparts": [
        {
          "id": "cse-4126-final-2023-q3a",
          "qno": "3(a)",
          "label": "(a)",
          "marks": 7,
          "topics": [
            "Data Cleaning & Preprocessing"
          ],
          "question": "What is an outlier data in a data set? Suppose, we have a data set on a subject marks out of 100 for 10 students as follows: 50, 55, 40, 62, 10, 33, 85, 77, 28, 82. Identify the marks are significantly different from others, which may indicate anomaly or outlier data. (Use Z-score based outlier detection technique to solve this).",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(a) (7 Marks).",
              "Define core technical terms and theoretical background relevant to: What is an outlier data in a data set? Suppose, we have a data set on a subject ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(a).",
            "marking_hint": "Full marks (7 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q3b",
          "qno": "3(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Define data integration. What are the key aspects of data integration in data mining?",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Define data integration. What are the key aspects of data integration in data mi...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q3c",
          "qno": "3(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "How to calculate corelation analysis to detect redundant attributes? Explain with example. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: How to calculate corelation analysis to detect redundant attributes? Explain wit...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 3 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2023-set4",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2023,
      "set_no": 4,
      "qno": "Question 4",
      "marks": 14,
      "topics": [
        "Predictive Modeling & Applications",
        "Data Visualization & Plotting"
      ],
      "question": "(a) What is Regression Line? Explain Positive and Negative Linear Relationship. **[4]**  \n(b) Distinguish between Linear Regression and Logistic Regression. **[4]**  \n(c) Write short note on log-linear models. **[3]**  \n(d) What is histogram? Why histogram analysis is important? **[3]**",
      "subparts": [
        {
          "id": "cse-4126-final-2023-q4a",
          "qno": "4(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "What is Regression Line? Explain Positive and Negative Linear Relationship.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(a) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What is Regression Line? Explain Positive and Negative Linear Relationship....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(a).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q4b",
          "qno": "4(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Distinguish between Linear Regression and Logistic Regression.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Distinguish between Linear Regression and Logistic Regression....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q4c",
          "qno": "4(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Write short note on log-linear models.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(c) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Write short note on log-linear models....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(c).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q4d",
          "qno": "4(d)",
          "label": "(d)",
          "marks": 3,
          "topics": [
            "Data Visualization & Plotting"
          ],
          "question": "What is histogram? Why histogram analysis is important? **[3]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(d) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is histogram? Why histogram analysis is important? **[3]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(d).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 4 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2023-set5",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2023,
      "set_no": 5,
      "qno": "Question 5",
      "marks": 14,
      "topics": [
        "Predictive Modeling & Applications"
      ],
      "question": "(a) What Is Correlation? Explain different types of correlation with figure. **[4]**  \n(b) Find and calculate the correlation coefficient of the following table: **[6]**\n\n| Subject | Age(X) | Weight(Y) |\n|:---:|:---:|:---:|\n| 1 | 40 | 99 |\n| 2 | 25 | 79 |\n| 3 | 22 | 69 |\n| 4 | 54 | 89 |\n\n(c) Distinguish between SQL and NoSQL. **[2]**  \n(d) Identify the key differences between quantitative and qualitative data. **[2]**",
      "subparts": [
        {
          "id": "cse-4126-final-2023-q5a",
          "qno": "5(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "What Is Correlation? Explain different types of correlation with figure.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(a) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What Is Correlation? Explain different types of correlation with figure....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(a).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q5b",
          "qno": "5(b)",
          "label": "(b)",
          "marks": 6,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Find and calculate the correlation coefficient of the following table: **[6]**\n\n| Subject | Age(X) | Weight(Y) |\n|:---:|:---:|:---:|\n| 1 | 40 | 99 |\n| 2 | 25 | 79 |\n| 3 | 22 | 69 |\n| 4 | 54 | 89 |",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(b) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Find and calculate the correlation coefficient of the following table: **[6]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(b).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q5c",
          "qno": "5(c)",
          "label": "(c)",
          "marks": 2,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Distinguish between SQL and NoSQL.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(c) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: Distinguish between SQL and NoSQL....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(c).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q5d",
          "qno": "5(d)",
          "label": "(d)",
          "marks": 2,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Identify the key differences between quantitative and qualitative data. **[2]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(d) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: Identify the key differences between quantitative and qualitative data. **[2]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(d).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 5 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2023-set6",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2023,
      "set_no": 6,
      "qno": "Question 6",
      "marks": 14,
      "topics": [
        "Exploratory Data Analysis (EDA)",
        "Predictive Modeling & Applications"
      ],
      "question": "(a) What is Exploratory Data Analysis? Why is it important? **[3]**  \n(b) Describe various types of EDA techniques. **[4]**  \n(c) Explain Concept Hierarchy generation. **[3]**  \n(d) What is data modeling? Write a comparative study among Conceptual, Logical, and Physical data model. **[4]**",
      "subparts": [
        {
          "id": "cse-4126-final-2023-q6a",
          "qno": "6(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Exploratory Data Analysis (EDA)"
          ],
          "question": "What is Exploratory Data Analysis? Why is it important?",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is Exploratory Data Analysis? Why is it important?...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q6b",
          "qno": "6(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Exploratory Data Analysis (EDA)"
          ],
          "question": "Describe various types of EDA techniques.",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe various types of EDA techniques....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q6c",
          "qno": "6(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Explain Concept Hierarchy generation.",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(c) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain Concept Hierarchy generation....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(c).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q6d",
          "qno": "6(d)",
          "label": "(d)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "What is data modeling? Write a comparative study among Conceptual, Logical, and Physical data model. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(d) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What is data modeling? Write a comparative study among Conceptual, Logical, and ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(d).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 6 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2023-set7",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2023,
      "set_no": 7,
      "qno": "Question 7",
      "marks": 14,
      "topics": [
        "Predictive Modeling & Applications",
        "Data Visualization & Plotting"
      ],
      "question": "(a) Briefly describe data sampling techniques. **[6]**  \n(b) Explain regression analysis and show the axis value on a graph/chart. **[4]**  \n(c) Explain how to handle redundancy in data integration. **[4]**\n\n---",
      "subparts": [
        {
          "id": "cse-4126-final-2023-q7a",
          "qno": "7(a)",
          "label": "(a)",
          "marks": 6,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Briefly describe data sampling techniques.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(a) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Briefly describe data sampling techniques....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(a).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q7b",
          "qno": "7(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Data Visualization & Plotting"
          ],
          "question": "Explain regression analysis and show the axis value on a graph/chart.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain regression analysis and show the axis value on a graph/chart....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2023-q7c",
          "qno": "7(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Explain how to handle redundancy in data integration. **[4]**\n\n---\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain how to handle redundancy in data integration. **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 7 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2024-set1",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2024,
      "set_no": 1,
      "qno": "Question 1",
      "marks": 14,
      "topics": [
        "Data Collection & Web Scraping",
        "Predictive Modeling & Applications"
      ],
      "question": "(a) Write short note on data collection methods with examples. **[3]**  \n(b) Differentiate between Qualitative and Quantitative data. **[4]**  \n(c) Explain basic types of Questionnaire method. **[3]**  \n(d) Briefly describe some common challenges in data collection. **[4]**",
      "subparts": [
        {
          "id": "cse-4126-final-2024-q1a",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Data Collection & Web Scraping"
          ],
          "question": "Write short note on data collection methods with examples.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Write short note on data collection methods with examples....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q1b",
          "qno": "1(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Differentiate between Qualitative and Quantitative data.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Differentiate between Qualitative and Quantitative data....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q1c",
          "qno": "1(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Explain basic types of Questionnaire method.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(c) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain basic types of Questionnaire method....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(c).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q1d",
          "qno": "1(d)",
          "label": "(d)",
          "marks": 4,
          "topics": [
            "Data Collection & Web Scraping"
          ],
          "question": "Briefly describe some common challenges in data collection. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(d) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Briefly describe some common challenges in data collection. **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(d).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 1 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2024-set2",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2024,
      "set_no": 2,
      "qno": "Question 2",
      "marks": 14,
      "topics": [
        "Predictive Modeling & Applications"
      ],
      "question": "(a) What is Noisy Data? What are the causes of occurring noise in a dataset? **[3]**  \n(b) Differentiate between equal-width and equal-frequency binning. **[3]**  \n(c) A sorted list of 20 sales price records is given bellow: **[5]**  \n`[5, 7, 7, 9, 10, 11, 13, 15, 20, 29, 35, 47, 50, 55, 60, 65, 72, 80, 87, 92]`  \nPartition the given data into four bins using the equal-frequency (equal-depth) method. Then, smooth the data within each bin using the bin means method.  \n(d) Explain the following functions: **[3]**  \n    • `data.isnull().values.any()`  \n    • `data.isnull().sum()`  \n    • `data.isnull()`",
      "subparts": [
        {
          "id": "cse-4126-final-2024-q2a",
          "qno": "2(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "What is Noisy Data? What are the causes of occurring noise in a dataset?",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is Noisy Data? What are the causes of occurring noise in a dataset?...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q2b",
          "qno": "2(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Differentiate between equal-width and equal-frequency binning.",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Differentiate between equal-width and equal-frequency binning....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q2c",
          "qno": "2(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "A sorted list of 20 sales price records is given bellow: **[5]**  \n`[5, 7, 7, 9, 10, 11, 13, 15, 20, 29, 35, 47, 50, 55, 60, 65, 72, 80, 87, 92]`  \nPartition the given data into four bins using the equal-frequency (equal-depth) method. Then, smooth the data within each bin using the bin means method.",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(c) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: A sorted list of 20 sales price records is given bellow: **[5]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(c).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q2d",
          "qno": "2(d)",
          "label": "(d)",
          "marks": 3,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Explain the following functions: **[3]**  \n    • `data.isnull().values.any()`  \n    • `data.isnull().sum()`  \n    • `data.isnull()`\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(d) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain the following functions: **[3]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(d).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 2 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2024-set3",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2024,
      "set_no": 3,
      "qno": "Question 3",
      "marks": 14,
      "topics": [
        "Data Cleaning & Preprocessing",
        "Predictive Modeling & Applications",
        "Data Visualization & Plotting"
      ],
      "question": "(a) Use a dataset representing the scores of 11 students on a quiz. Find out the outliers of the dataset:  \nScores(X): `[65, 70, 72, 75, 78, 80, 81, 85, 88, 90, 95]`. **[4]**  \n(b) Given matrix: **[5]**  \n$$\\begin{bmatrix} 85 & 90 & 88 \\\\ 75 & \\text{NaN} & 82 \\\\ \\text{NaN} & 88 & 91 \\\\ 92 & 85 & \\text{NaN} \\end{bmatrix}$$  \nFind the KNN value from above matrix and write a Python code to print the data and output.  \n(c) Considering the following box plot calculate the percentage of the data that is above the median. What is the interquartile range? **[5]**\n\n**Box Plot Specifications:**\n* **Scale / Number Line:** 1 through 10\n* **Minimum (Left Whisker):** 2\n* **First Quartile ($Q_1$):** 4\n* **Median ($Q_2$):** 5\n* **Third Quartile ($Q_3$):** 7\n* **Maximum (Right Whisker):** 8.5 (or 9)",
      "subparts": [
        {
          "id": "cse-4126-final-2024-q3a",
          "qno": "3(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Data Cleaning & Preprocessing"
          ],
          "question": "Use a dataset representing the scores of 11 students on a quiz. Find out the outliers of the dataset:  \nScores(X): `[65, 70, 72, 75, 78, 80, 81, 85, 88, 90, 95]`.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(a) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Use a dataset representing the scores of 11 students on a quiz. Find out the out...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(a).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q3b",
          "qno": "3(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Given matrix: **[5]**  \n$$\\begin{bmatrix} 85 & 90 & 88 \\\\ 75 & \\text{NaN} & 82 \\\\ \\text{NaN} & 88 & 91 \\\\ 92 & 85 & \\text{NaN} \\end{bmatrix}$$  \nFind the KNN value from above matrix and write a Python code to print the data and output.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Given matrix: **[5]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q3c",
          "qno": "3(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Data Visualization & Plotting"
          ],
          "question": "Considering the following box plot calculate the percentage of the data that is above the median. What is the interquartile range? **[5]**\n\n**Box Plot Specifications:**\n* **Scale / Number Line:** 1 through 10\n* **Minimum (Left Whisker):** 2\n* **First Quartile ($Q_1$):** 4\n* **Median ($Q_2$):** 5\n* **Third Quartile ($Q_3$):** 7\n* **Maximum (Right Whisker):** 8.5 (or 9)\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(c) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Considering the following box plot calculate the percentage of the data that is ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(c).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 3 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2024-set4",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2024,
      "set_no": 4,
      "qno": "Question 4",
      "marks": 14,
      "topics": [
        "Data Visualization & Plotting",
        "Predictive Modeling & Applications"
      ],
      "question": "(a) What is histogram? Study the comparison of a test result between class A and class B: **[4]**\n\n**Class A:**\n| Score | Students |\n|:---:|:---:|\n| 60 - 70 | 10 |\n| 70 - 80 | 6 |\n| 80 - 90 | 15 |\n| 90 - 100 | 2 |\n\n**Class B:**\n| Score | Students |\n|:---:|:---:|\n| 60 - 70 | 5 |\n| 70 - 80 | 8 |\n| 80 - 90 | 12 |\n| 90 - 100 | 8 |\n\nWhich class performed better in the test? Answer with explanation.\n\n(b) Find and calculate the correlation coefficient of the following table: **[6]**\n\n| Subject | Age(X) | Weight(Y) |\n|:---:|:---:|:---:|\n| 1 | 40 | 99 |\n| 2 | 25 | 79 |\n| 3 | 22 | 69 |\n| 4 | 54 | 89 |\n\n(c) Explain Wavelet transformation with example. **[4]**",
      "subparts": [
        {
          "id": "cse-4126-final-2024-q4a",
          "qno": "4(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Data Visualization & Plotting"
          ],
          "question": "What is histogram? Study the comparison of a test result between class A and class B: **[4]**\n\n**Class A:**\n| Score | Students |\n|:---:|:---:|\n| 60 - 70 | 10 |\n| 70 - 80 | 6 |\n| 80 - 90 | 15 |\n| 90 - 100 | 2 |\n\n**Class B:**\n| Score | Students |\n|:---:|:---:|\n| 60 - 70 | 5 |\n| 70 - 80 | 8 |\n| 80 - 90 | 12 |\n| 90 - 100 | 8 |\n\nWhich class performed better in the test? Answer with explanation.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(a) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What is histogram? Study the comparison of a test result between class A and cla...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(a).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q4b",
          "qno": "4(b)",
          "label": "(b)",
          "marks": 6,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Find and calculate the correlation coefficient of the following table: **[6]**\n\n| Subject | Age(X) | Weight(Y) |\n|:---:|:---:|:---:|\n| 1 | 40 | 99 |\n| 2 | 25 | 79 |\n| 3 | 22 | 69 |\n| 4 | 54 | 89 |",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(b) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Find and calculate the correlation coefficient of the following table: **[6]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(b).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q4c",
          "qno": "4(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Explain Wavelet transformation with example. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain Wavelet transformation with example. **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 4 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2024-set5",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2024,
      "set_no": 5,
      "qno": "Question 5",
      "marks": 14,
      "topics": [
        "Predictive Modeling & Applications"
      ],
      "question": "(a) What is clustering? Distinguish between inter cluster and intra cluster. **[3]**  \n(b) Explain the following terms with example: **[6]**  \n    1. Positive Correlation  \n    2. Negative Correlation  \n    3. Zero Correlation  \n(c) What are lossy and lossless compression? **[2]**  \n(d) Explain the concept of Hierarchy Generation with an example. **[3]**",
      "subparts": [
        {
          "id": "cse-4126-final-2024-q5a",
          "qno": "5(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "What is clustering? Distinguish between inter cluster and intra cluster.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is clustering? Distinguish between inter cluster and intra cluster....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q5b",
          "qno": "5(b)",
          "label": "(b)",
          "marks": 6,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Explain the following terms with example: **[6]**  \n    1. Positive Correlation  \n    2. Negative Correlation  \n    3. Zero Correlation",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(b) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain the following terms with example: **[6]**  ...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(b).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q5c",
          "qno": "5(c)",
          "label": "(c)",
          "marks": 2,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "What are lossy and lossless compression?",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(c) (2 Marks).",
              "Define core technical terms and theoretical background relevant to: What are lossy and lossless compression?...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(c).",
            "marking_hint": "Full marks (2 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q5d",
          "qno": "5(d)",
          "label": "(d)",
          "marks": 3,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Explain the concept of Hierarchy Generation with an example. **[3]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(d) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain the concept of Hierarchy Generation with an example. **[3]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(d).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 5 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2024-set6",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2024,
      "set_no": 6,
      "qno": "Question 6",
      "marks": 14,
      "topics": [
        "Feature Engineering & Selection",
        "Predictive Modeling & Applications"
      ],
      "question": "(a) Explain Stepwise forward selection for removing irrelevant or redundant attributes with an example. **[5]**  \n(b) Evaluate and find the Dendrogram from the following dataset: **[5]**\n\n| Sample no. | X | Y |\n|:---:|:---:|:---:|\n| P1 | 0.65 | 0.73 |\n| P2 | 0.32 | 0.48 |\n| P3 | 0.46 | 0.45 |\n| P4 | 0.38 | 0.30 |\n| P5 | 0.20 | 0.56 |\n| P6 | 0.75 | 0.60 |\n\n(c) Define Sampling. Discuss different types of sampling. **[4]**",
      "subparts": [
        {
          "id": "cse-4126-final-2024-q6a",
          "qno": "6(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Feature Engineering & Selection"
          ],
          "question": "Explain Stepwise forward selection for removing irrelevant or redundant attributes with an example.",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain Stepwise forward selection for removing irrelevant or redundant attribut...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q6b",
          "qno": "6(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Evaluate and find the Dendrogram from the following dataset: **[5]**\n\n| Sample no. | X | Y |\n|:---:|:---:|:---:|\n| P1 | 0.65 | 0.73 |\n| P2 | 0.32 | 0.48 |\n| P3 | 0.46 | 0.45 |\n| P4 | 0.38 | 0.30 |\n| P5 | 0.20 | 0.56 |\n| P6 | 0.75 | 0.60 |",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Evaluate and find the Dendrogram from the following dataset: **[5]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q6c",
          "qno": "6(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Define Sampling. Discuss different types of sampling. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Define Sampling. Discuss different types of sampling. **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 6 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "cse-4126-final-2024-set7",
      "course": "CSE-4126",
      "exam": "final",
      "year": 2024,
      "set_no": 7,
      "qno": "Question 7",
      "marks": 14,
      "topics": [
        "Data Visualization & Plotting",
        "Predictive Modeling & Applications",
        "Exploratory Data Analysis (EDA)"
      ],
      "question": "(a) Describe various types of Data Visualization techniques with examples. **[6]**  \n(b) Why is Discretization important? How Data discretization differs from Binarization? **[4]**  \n(c) Why is Exploratory Data Analysis Important? Write short note on various types of EDA Techniques. **[4]**\n\n---",
      "subparts": [
        {
          "id": "cse-4126-final-2024-q7a",
          "qno": "7(a)",
          "label": "(a)",
          "marks": 6,
          "topics": [
            "Data Visualization & Plotting"
          ],
          "question": "Describe various types of Data Visualization techniques with examples.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(a) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe various types of Data Visualization techniques with examples....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(a).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q7b",
          "qno": "7(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Predictive Modeling & Applications"
          ],
          "question": "Why is Discretization important? How Data discretization differs from Binarization?",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Why is Discretization important? How Data discretization differs from Binarizati...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "cse-4126-final-2024-q7c",
          "qno": "7(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Exploratory Data Analysis (EDA)"
          ],
          "question": "Why is Exploratory Data Analysis Important? Write short note on various types of EDA Techniques. **[4]**\n\n---\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Why is Exploratory Data Analysis Important? Write short note on various types of...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 7 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
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
      "question": "1. Define Data Science. Write down the key differences between Qualitative & Quantitative data. **[4]**  \n2. Discuss the types of Questionnaire Method. **[3]**  \n3. Mention some challenges in data collection method. **[3]**  \n4. Explain KNN algorithm with an example. **[5]**  \n5. Identify if there are any outliers in the following dataset with IQR:  \n$X = \\{40, 45, 50, 52, 55, 58, 60, 62, 68, 90\\}$. **[5]**",
      "subparts": [
        {
          "id": "cse-4126-term-mec-tt1-q1",
          "qno": "1",
          "label": "1",
          "marks": 4,
          "topics": [
            "Data Science Lifecycle & Pipelines"
          ],
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
          "topics": [
            "Data Collection & Web Scraping"
          ],
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
          "topics": [
            "Data Collection & Web Scraping"
          ],
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
          "topics": [
            "Exploratory Data Analysis (EDA)"
          ],
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
          "topics": [
            "Exploratory Data Analysis (EDA)"
          ],
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
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for MEC CSE-4126 Term Test 1 (20 Marks total).",
        "marking_hint": "Full marks (20 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
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
      "question": "1. How Redundant attributes are detected in Data Integration? **[2]**  \n2. Calculate the Correlation coefficient of given data:  \n$X = \\{41, 42, 43, 44, 45\\}$ & $Y = \\{3.2, 3.3, 3.4, 3.5, 3.6\\}$. **[3]**  \n3. Define Data reduction. Mention Data reduction strategies. **[2]**  \n4. Explain Wavelet transforms with example. **[3]**  \n5. Mention data visualization techniques. **[2]**  \n6. Explain Data discretization mapping with an example. **[3]**",
      "subparts": [
        {
          "id": "cse-4126-term-mec-tt2-q1",
          "qno": "1",
          "label": "1",
          "marks": 2,
          "topics": [
            "Data Cleaning & Preprocessing"
          ],
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
          "topics": [
            "Statistical Inference & Distributions"
          ],
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
          "topics": [
            "Data Cleaning & Preprocessing"
          ],
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
          "topics": [
            "Data Cleaning & Preprocessing"
          ],
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
          "topics": [
            "Data Visualization & Plotting"
          ],
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
          "topics": [
            "Data Cleaning & Preprocessing"
          ],
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
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for MEC CSE-4126 Term Test 2 (15 Marks total).",
        "marking_hint": "Full marks (15 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    }
  ],
  "ss-4103": [
    {
      "id": "ss-4103-final-2023-set1",
      "course": "SS-4103",
      "exam": "final",
      "year": 2023,
      "set_no": 1,
      "qno": "Question 1",
      "marks": 14,
      "topics": [
        "Entrepreneurship Foundations"
      ],
      "question": "(a) Who are the entrepreneurs? Write five functions of an entrepreneur. **[5]**  \n(b) What are the benefits of entrepreneurship for individual? **[3]**  \n(c) Describe the roles of entrepreneurship in economic development. **[6]**",
      "subparts": [
        {
          "id": "ss-4103-final-2023-q1a",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Who are the entrepreneurs? Write five functions of an entrepreneur.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Who are the entrepreneurs? Write five functions of an entrepreneur....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q1b",
          "qno": "1(b)",
          "label": "(b)",
          "marks": 3,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "What are the benefits of entrepreneurship for individual?",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(b) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What are the benefits of entrepreneurship for individual?...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(b).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q1c",
          "qno": "1(c)",
          "label": "(c)",
          "marks": 6,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Describe the roles of entrepreneurship in economic development. **[6]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(c) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe the roles of entrepreneurship in economic development. **[6]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(c).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 1 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2023-set2",
      "course": "SS-4103",
      "exam": "final",
      "year": 2023,
      "set_no": 2,
      "qno": "Question 2",
      "marks": 14,
      "topics": [
        "Entrepreneurship Foundations"
      ],
      "question": "(a) How Creativity and Innovation is interconnected with each other? Expalin. **[4]**  \n(b) How are to enhance creativity? Briefly describe. **[6]**  \n(c) What are the steps of creative process? **[4]**",
      "subparts": [
        {
          "id": "ss-4103-final-2023-q2a",
          "qno": "2(a)",
          "label": "(a)",
          "marks": 4,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "How Creativity and Innovation is interconnected with each other? Expalin.",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(a) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: How Creativity and Innovation is interconnected with each other? Expalin....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(a).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q2b",
          "qno": "2(b)",
          "label": "(b)",
          "marks": 6,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "How are to enhance creativity? Briefly describe.",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(b) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: How are to enhance creativity? Briefly describe....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(b).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q2c",
          "qno": "2(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "What are the steps of creative process? **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What are the steps of creative process? **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 2 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2023-set3",
      "course": "SS-4103",
      "exam": "final",
      "year": 2023,
      "set_no": 3,
      "qno": "Question 3",
      "marks": 14,
      "topics": [
        "Feasibility & Market Analysis",
        "Entrepreneurship Foundations"
      ],
      "question": "(a) What is feasibility study? **[3]**  \n(b) What are the Key components of a Business Strategic Plan? How to develop a Strategic Plan. **[7]**  \n(c) Explain the following terms: i. Secondary research; ii. Prototype **[4]**",
      "subparts": [
        {
          "id": "ss-4103-final-2023-q3a",
          "qno": "3(a)",
          "label": "(a)",
          "marks": 3,
          "topics": [
            "Feasibility & Market Analysis"
          ],
          "question": "What is feasibility study?",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(a) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: What is feasibility study?...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(a).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q3b",
          "qno": "3(b)",
          "label": "(b)",
          "marks": 7,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "What are the Key components of a Business Strategic Plan? How to develop a Strategic Plan.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(b) (7 Marks).",
              "Define core technical terms and theoretical background relevant to: What are the Key components of a Business Strategic Plan? How to develop a Strat...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(b).",
            "marking_hint": "Full marks (7 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q3c",
          "qno": "3(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Explain the following terms: i. Secondary research; ii. Prototype **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain the following terms: i. Secondary research; ii. Prototype **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 3 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2023-set4",
      "course": "SS-4103",
      "exam": "final",
      "year": 2023,
      "set_no": 4,
      "qno": "Question 4",
      "marks": 14,
      "topics": [
        "Entrepreneurship Foundations",
        "Marketing Strategy & Growth"
      ],
      "question": "(a) What are the steps of strategic management process? Very shortly describe each step. **[10]**  \n(b) What are the three V's approaches of marketing? Write down the core business processes of marketing. **[4]**",
      "subparts": [
        {
          "id": "ss-4103-final-2023-q4a",
          "qno": "4(a)",
          "label": "(a)",
          "marks": 10,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "What are the steps of strategic management process? Very shortly describe each step.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(a) (10 Marks).",
              "Define core technical terms and theoretical background relevant to: What are the steps of strategic management process? Very shortly describe each s...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(a).",
            "marking_hint": "Full marks (10 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q4b",
          "qno": "4(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Marketing Strategy & Growth"
          ],
          "question": "What are the three V's approaches of marketing? Write down the core business processes of marketing. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What are the three V's approaches of marketing? Write down the core business pro...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 4 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2023-set5",
      "course": "SS-4103",
      "exam": "final",
      "year": 2023,
      "set_no": 5,
      "qno": "Question 5",
      "marks": 14,
      "topics": [
        "Entrepreneurship Foundations",
        "Marketing Strategy & Growth",
        "IT Business Ethics & Legal Issues"
      ],
      "question": "(a) What are the key concerns in ethical entrepreneurship? **[5]**  \n(b) Show the Holistic Marketing Framework with diagram. **[5]**  \n(c) What are the basic features of ethics? **[4]**",
      "subparts": [
        {
          "id": "ss-4103-final-2023-q5a",
          "qno": "5(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "What are the key concerns in ethical entrepreneurship?",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: What are the key concerns in ethical entrepreneurship?...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q5b",
          "qno": "5(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Marketing Strategy & Growth"
          ],
          "question": "Show the Holistic Marketing Framework with diagram.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Show the Holistic Marketing Framework with diagram....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q5c",
          "qno": "5(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "IT Business Ethics & Legal Issues"
          ],
          "question": "What are the basic features of ethics? **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What are the basic features of ethics? **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 5 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2023-set6",
      "course": "SS-4103",
      "exam": "final",
      "year": 2023,
      "set_no": 6,
      "qno": "Question 6",
      "marks": 14,
      "topics": [
        "Financial Planning & Valuation",
        "Entrepreneurship Foundations"
      ],
      "question": "(a) Define financial planning. Explore different types of financial planning. **[5]**  \n(b) Describe the methods of financing your business. **[5]**  \n(c) Compare between equity financing and debt financing. **[4]**",
      "subparts": [
        {
          "id": "ss-4103-final-2023-q6a",
          "qno": "6(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Financial Planning & Valuation"
          ],
          "question": "Define financial planning. Explore different types of financial planning.",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Define financial planning. Explore different types of financial planning....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q6b",
          "qno": "6(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Describe the methods of financing your business.",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe the methods of financing your business....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q6c",
          "qno": "6(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Compare between equity financing and debt financing. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Compare between equity financing and debt financing. **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 6 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2023-set7",
      "course": "SS-4103",
      "exam": "final",
      "year": 2023,
      "set_no": 7,
      "qno": "Question 7",
      "marks": 14,
      "topics": [
        "Entrepreneurship Foundations"
      ],
      "question": "(a) Explain operations management. State some functions of operations management. **[5]**  \n(b) Define operating scheduling. Describe the objectives of the operations scheduling. **[4]**  \n(c) What is plant capacity? What are the factors affecting determination of plant capacity? **[5]**\n\n---",
      "subparts": [
        {
          "id": "ss-4103-final-2023-q7a",
          "qno": "7(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Explain operations management. State some functions of operations management.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain operations management. State some functions of operations management....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q7b",
          "qno": "7(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Define operating scheduling. Describe the objectives of the operations scheduling.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Define operating scheduling. Describe the objectives of the operations schedulin...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2023-q7c",
          "qno": "7(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "What is plant capacity? What are the factors affecting determination of plant capacity? **[5]**\n\n---\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(c) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: What is plant capacity? What are the factors affecting determination of plant ca...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(c).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 7 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2024-set1",
      "course": "SS-4103",
      "exam": "final",
      "year": 2024,
      "set_no": 1,
      "qno": "Question 1",
      "marks": 14,
      "topics": [
        "Entrepreneurship Foundations"
      ],
      "question": "(a) Define entrepreneurship. Write five characteristics of an entrepreneur. **[5]**  \n(b) State the role of Entrepreneurship in Economic Development. **[6]**  \n(c) Describe five functions of an entrepreneur. **[3]**",
      "subparts": [
        {
          "id": "ss-4103-final-2024-q1a",
          "qno": "1(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Define entrepreneurship. Write five characteristics of an entrepreneur.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Define entrepreneurship. Write five characteristics of an entrepreneur....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q1b",
          "qno": "1(b)",
          "label": "(b)",
          "marks": 6,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "State the role of Entrepreneurship in Economic Development.",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(b) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: State the role of Entrepreneurship in Economic Development....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(b).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q1c",
          "qno": "1(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Describe five functions of an entrepreneur. **[3]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 1(c) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe five functions of an entrepreneur. **[3]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 1(c).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 1 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2024-set2",
      "course": "SS-4103",
      "exam": "final",
      "year": 2024,
      "set_no": 2,
      "qno": "Question 2",
      "marks": 14,
      "topics": [
        "Entrepreneurship Foundations"
      ],
      "question": "(a) Describe why creativity and innovation are such an integral part of Entrepreneurship. **[6]**  \n(b) Discuss techniques for improving creative process. **[4]**  \n(c) What are the entrepreneurial key success factors. **[4]**",
      "subparts": [
        {
          "id": "ss-4103-final-2024-q2a",
          "qno": "2(a)",
          "label": "(a)",
          "marks": 6,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Describe why creativity and innovation are such an integral part of Entrepreneurship.",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(a) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe why creativity and innovation are such an integral part of Entrepreneur...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(a).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q2b",
          "qno": "2(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Discuss techniques for improving creative process.",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Discuss techniques for improving creative process....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q2c",
          "qno": "2(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "What are the entrepreneurial key success factors. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 2(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: What are the entrepreneurial key success factors. **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 2(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 2 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2024-set3",
      "course": "SS-4103",
      "exam": "final",
      "year": 2024,
      "set_no": 3,
      "qno": "Question 3",
      "marks": 14,
      "topics": [
        "Feasibility & Market Analysis",
        "Marketing Strategy & Growth",
        "Entrepreneurship Foundations"
      ],
      "question": "(a) What is Feasibility Analysis? Discuss in detail the steps involved in feasibility analysis for a new IT business. **[6]**  \n(b) What are the major driving forces behind the growth of small businesses? Explain in detail. **[5]**  \n(c) Describe any three social responsibilities of an entrepreneur. **[3]**",
      "subparts": [
        {
          "id": "ss-4103-final-2024-q3a",
          "qno": "3(a)",
          "label": "(a)",
          "marks": 6,
          "topics": [
            "Feasibility & Market Analysis"
          ],
          "question": "What is Feasibility Analysis? Discuss in detail the steps involved in feasibility analysis for a new IT business.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(a) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: What is Feasibility Analysis? Discuss in detail the steps involved in feasibilit...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(a).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q3b",
          "qno": "3(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Marketing Strategy & Growth"
          ],
          "question": "What are the major driving forces behind the growth of small businesses? Explain in detail.",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: What are the major driving forces behind the growth of small businesses? Explain...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q3c",
          "qno": "3(c)",
          "label": "(c)",
          "marks": 3,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Describe any three social responsibilities of an entrepreneur. **[3]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 3(c) (3 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe any three social responsibilities of an entrepreneur. **[3]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 3(c).",
            "marking_hint": "Full marks (3 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 3 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2024-set4",
      "course": "SS-4103",
      "exam": "final",
      "year": 2024,
      "set_no": 4,
      "qno": "Question 4",
      "marks": 14,
      "topics": [
        "Entrepreneurship Foundations"
      ],
      "question": "(a) Discuss the different forms of business ownership with examples. **[6]**  \n(b) Discuss the advantages of franchising to an entrepreneur. **[4]**  \n(c) Differentiate between partnership and joint stock company. **[4]**",
      "subparts": [
        {
          "id": "ss-4103-final-2024-q4a",
          "qno": "4(a)",
          "label": "(a)",
          "marks": 6,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Discuss the different forms of business ownership with examples.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(a) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Discuss the different forms of business ownership with examples....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(a).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q4b",
          "qno": "4(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Discuss the advantages of franchising to an entrepreneur.",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Discuss the advantages of franchising to an entrepreneur....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q4c",
          "qno": "4(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Differentiate between partnership and joint stock company. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 4(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Differentiate between partnership and joint stock company. **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 4(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 4 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2024-set5",
      "course": "SS-4103",
      "exam": "final",
      "year": 2024,
      "set_no": 5,
      "qno": "Question 5",
      "marks": 14,
      "topics": [
        "Marketing Strategy & Growth",
        "Business Models & Canvas"
      ],
      "question": "(a) Define a marketing plan and explain its objectives and importance. **[6]**  \n(b) Describe how social media can be used effectively in bootstrapping a marketing plan. **[4]**  \n(c) Discuss the impact of e-commerce on traditional business models. **[4]**",
      "subparts": [
        {
          "id": "ss-4103-final-2024-q5a",
          "qno": "5(a)",
          "label": "(a)",
          "marks": 6,
          "topics": [
            "Marketing Strategy & Growth"
          ],
          "question": "Define a marketing plan and explain its objectives and importance.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(a) (6 Marks).",
              "Define core technical terms and theoretical background relevant to: Define a marketing plan and explain its objectives and importance....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(a).",
            "marking_hint": "Full marks (6 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q5b",
          "qno": "5(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Marketing Strategy & Growth"
          ],
          "question": "Describe how social media can be used effectively in bootstrapping a marketing plan.",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe how social media can be used effectively in bootstrapping a marketing p...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q5c",
          "qno": "5(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Business Models & Canvas"
          ],
          "question": "Discuss the impact of e-commerce on traditional business models. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 5(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Discuss the impact of e-commerce on traditional business models. **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 5(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 5 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2024-set6",
      "course": "SS-4103",
      "exam": "final",
      "year": 2024,
      "set_no": 6,
      "qno": "Question 6",
      "marks": 14,
      "topics": [
        "Financial Planning & Valuation",
        "Entrepreneurship Foundations"
      ],
      "question": "(a) Define financial planning. Explore different types of financial planning. **[5]**  \n(b) Describe the methods of financing your business. **[5]**  \n(c) Compare between equity financing and debt financing. **[4]**",
      "subparts": [
        {
          "id": "ss-4103-final-2024-q6a",
          "qno": "6(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Financial Planning & Valuation"
          ],
          "question": "Define financial planning. Explore different types of financial planning.",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Define financial planning. Explore different types of financial planning....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q6b",
          "qno": "6(b)",
          "label": "(b)",
          "marks": 5,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Describe the methods of financing your business.",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(b) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Describe the methods of financing your business....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(b).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q6c",
          "qno": "6(c)",
          "label": "(c)",
          "marks": 4,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Compare between equity financing and debt financing. **[4]**\n\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 6(c) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Compare between equity financing and debt financing. **[4]**...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 6(c).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 6 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
    {
      "id": "ss-4103-final-2024-set7",
      "course": "SS-4103",
      "exam": "final",
      "year": 2024,
      "set_no": 7,
      "qno": "Question 7",
      "marks": 14,
      "topics": [
        "Entrepreneurship Foundations"
      ],
      "question": "(a) Explain operations management. State some functions of operations management. **[5]**  \n(b) Define operating scheduling. Describe the objectives of the operations scheduling. **[4]**  \n(c) What is plant capacity? What are the factors affecting determination of plant capacity? **[5]**\n\n---",
      "subparts": [
        {
          "id": "ss-4103-final-2024-q7a",
          "qno": "7(a)",
          "label": "(a)",
          "marks": 5,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Explain operations management. State some functions of operations management.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(a) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: Explain operations management. State some functions of operations management....",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(a).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q7b",
          "qno": "7(b)",
          "label": "(b)",
          "marks": 4,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "Define operating scheduling. Describe the objectives of the operations scheduling.",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(b) (4 Marks).",
              "Define core technical terms and theoretical background relevant to: Define operating scheduling. Describe the objectives of the operations schedulin...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(b).",
            "marking_hint": "Full marks (4 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        },
        {
          "id": "ss-4103-final-2024-q7c",
          "qno": "7(c)",
          "label": "(c)",
          "marks": 5,
          "topics": [
            "Entrepreneurship Foundations"
          ],
          "question": "What is plant capacity? What are the factors affecting determination of plant capacity? **[5]**\n\n---\n---",
          "solution": {
            "steps": [
              "Understand the requirements of question 7(c) (5 Marks).",
              "Define core technical terms and theoretical background relevant to: What is plant capacity? What are the factors affecting determination of plant ca...",
              "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
              "Summarize the final solution clearly with relevant engineering examples."
            ],
            "answer": "Complete detailed answer and derivations for question 7(c).",
            "marking_hint": "Full marks (5 M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
          }
        }
      ],
      "solution": {
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for Question 7 (14 Marks total).",
        "marking_hint": "Full marks (14 M): Answer all sub-parts completely."
      },
      "similar_to": [],
      "verified": false
    },
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
      "question": "1. Write the Characteristics of Entrepreneurs and Nine Deadly Mistakes of Entrepreneurships. **[5]**  \n2. Explain the differences among creativity, innovation, and entrepreneurship. **[5]**  \n3. What are the major driving forces behind the growth of small businesses? Explain in detail. **[5]**  \n4. Describe any three social responsibilities of an entrepreneur. **[5]**  \n5. Write 5 rewards and challenges of entrepreneurship. **[5]**",
      "subparts": [
        {
          "id": "ss-4103-term-mec-tt1-q1",
          "qno": "1",
          "label": "1",
          "marks": 5,
          "topics": [
            "Entrepreneurship Foundations"
          ],
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
          "topics": [
            "Idea Generation & Market Opportunity"
          ],
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
          "topics": [
            "Entrepreneurship Foundations"
          ],
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
          "topics": [
            "IT Business Ethics & Legal Issues"
          ],
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
          "topics": [
            "Entrepreneurship Foundations"
          ],
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
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for MEC SS-4103 Term Test 1 (20 Marks total).",
        "marking_hint": "Full marks (20 M): Answer any 4 questions completely (5 marks each)."
      },
      "similar_to": [],
      "verified": false
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
      "question": "1. Explain the major Forms of Business ownership. **[5]**  \n2. What is Supply Chain Management? Identify the major components of a supply chain. **[5]**  \n3. What is a cash-flow statement? Discuss the importance of preparing a cash-flow forecast. **[5]**  \n4. What is Creative Advertising? Write the Importance of Creativity in Advertising. **[5]**  \n5. Write the Major Legal Requirements for Establishing a Small Business. **[5]**",
      "subparts": [
        {
          "id": "ss-4103-term-mec-tt2-q1",
          "qno": "1",
          "label": "1",
          "marks": 5,
          "topics": [
            "Business Models & Canvas"
          ],
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
          "topics": [
            "Business Models & Canvas"
          ],
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
          "topics": [
            "Financial Planning & Valuation"
          ],
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
          "topics": [
            "Marketing Strategy & Growth"
          ],
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
          "topics": [
            "IT Business Ethics & Legal Issues"
          ],
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
        "steps": [
          "See detailed solution breakdowns for sub-questions below."
        ],
        "answer": "Complete solutions for MEC SS-4103 Term Test 2 (20 Marks total).",
        "marking_hint": "Full marks (20 M): Answer any 4 questions completely (5 marks each)."
      },
      "similar_to": [],
      "verified": false
    }
  ]
};
