import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / "data" / "cse-4101.json"

questions = [
  # --- AI FOUNDATIONS & PEAS ---
  {
    "id": "cse-4101-final-2023-q1a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "1(a)",
    "marks": 1,
    "topics": ["AI Foundations"],
    "question": "Write down the goals of Artificial Intelligence.",
    "solution": {
      "steps": [
        "1. Create expert systems that exhibit intelligent behavior, learn, demonstrate, explain, and advise its users.",
        "2. To implement human intelligence in machines (thinking humanly, thinking rationally, acting humanly, and acting rationally)."
      ],
      "answer": "The primary goal is creating intelligent agents capable of perceiving their environment, reasoning, learning, and taking rational actions to achieve specific goals.",
      "marking_hint": "Award 1 mark for mentioning thinking/acting humanly and rationally."
    },
    "similar_to": ["cse-4101-final-2024-q1a"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q1b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "1(b)",
    "marks": 2,
    "topics": ["AI Foundations"],
    "question": "Differentiate between strong AI and weak AI.",
    "solution": {
      "steps": [
        "1. Weak AI (Narrow AI): Designed and trained for a specific narrow task (e.g., Apple Siri, chess engines, spam filters). It simulates human behavior without genuine consciousness or understanding.",
        "2. Strong AI (Artificial General Intelligence - AGI): Possesses human-like generalized cognitive abilities. Can solve unfamiliar problems across diverse domains with self-awareness and reasoning."
      ],
      "answer": "Weak AI focuses on automated specialized tasks; Strong AI encompasses theoretical human-equivalent general cognition across all domains.",
      "marking_hint": "Award 1 mark for weak AI definition/example, 1 mark for strong AI definition/example."
    },
    "similar_to": [],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q1c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "1(c)",
    "marks": 9,
    "topics": ["AI Foundations", "PEAS & Task Environment"],
    "question": "Give a PEAS description of the following task environment and characterize it in terms of task environment.\nI. Automated taxi driver\nII. Vacuum cleaner\nIII. Backgammon",
    "solution": {
      "steps": [
        "1. Automated Taxi Driver: P: Safe, fast, legal, comfortable trip. E: Roads, traffic, pedestrians, weather. A: Steering, throttle, brakes, horn. S: Cameras, LiDAR, radar, GPS. Environment is partially observable, multi-agent, stochastic, sequential, dynamic, continuous.",
        "2. Vacuum Cleaner: P: Cleanliness score, power usage. E: Floor, dirt, obstacles. A: Wheels, suction motor, brushes. S: Bump sensors, dirt sensors, cliff sensors. Environment is partially observable, single agent, stochastic, sequential, static, discrete.",
        "3. Backgammon: P: Win/loss, margin of victory. E: Board, checkers, dice. A: Legal checker moves. S: Board vision. Environment is fully observable, competitive multi-agent, stochastic (dice), sequential, static, discrete."
      ],
      "answer": "PEAS describes Performance, Environment, Actuators, and Sensors. Dimensions characterize observability, agent count, determinism, episodic nature, dynamism, and continuity.",
      "marking_hint": "Award 3 marks each for Taxi, Vacuum cleaner, and Backgammon."
    },
    "similar_to": ["cse-4101-final-2024-q1b"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q1d",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "1(d)",
    "marks": 2,
    "topics": ["Turing Test"],
    "question": "Briefly describe about Turing Test.",
    "solution": {
      "steps": [
        "1. Proposed by Alan Turing (1950) in 'Computing Machinery and Intelligence' as the Imitation Game.",
        "2. A human interrogator questions a human and a computer via text terminal. If the interrogator cannot reliably tell the machine from the human after a specified duration, the machine passes."
      ],
      "answer": "Operational test of machine intelligence based on behavioral indistinguishability from human conversational responses.",
      "marking_hint": "Award 1 mark for setup description, 1 mark for evaluation criterion."
    },
    "similar_to": [],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q1a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "1(a)",
    "marks": 4,
    "topics": ["AI Foundations"],
    "question": "Define Artificial Intelligence. List five problems that cannot be currently aided/solved by AI.",
    "solution": {
      "steps": [
        "1. Definition: The study and construction of agents that perceive their environment and take rational actions that maximize chance of successfully achieving their goals.",
        "2. Five unsolved problems: (1) Human subjective consciousness and emotional empathy, (2) Solving general undecidable problems (e.g. Halting Problem), (3) Fully autonomous moral ethical decision-making in novel legal scenarios, (4) Novel scientific paradigm synthesis without prior training distribution, (5) True common-sense physical reasoning across unstructured open-ended physical environments."
      ],
      "answer": "AI models rational computational intelligence. Limitations include subjective phenomenology, formal undecidability, and open-ended human common-sense abstraction.",
      "marking_hint": "Award 1.5 marks for definition, 2.5 marks for 5 valid limitations."
    },
    "similar_to": ["cse-4101-final-2023-q1a"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q1b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "1(b)",
    "marks": 4,
    "topics": ["AI Foundations", "PEAS & Task Environment"],
    "question": "Give a PEAS description of the following task environment and characterize it in terms of task environment:\ni. Automated taxi driver\nii. Vacuum cleaner",
    "solution": {
      "steps": [
        "1. Automated Taxi Driver: P: Safety, speed, comfort, profit. E: Roads, traffic, pedestrians. A: Steering, brakes, accelerator. S: Cameras, LiDAR, GPS. Characterization: Partially observable, multi-agent, stochastic, sequential, dynamic, continuous.",
        "2. Vacuum Cleaner: P: Floor cleanliness, energy. E: Rooms, furniture, dirt. A: Wheels, suction. S: Bump, cliff, dirt sensors. Characterization: Partially observable, single-agent, stochastic, sequential, static, discrete."
      ],
      "answer": "PEAS structure defines operational requirements; environmental dimensions guide algorithmic approach.",
      "marking_hint": "Award 2 marks each for taxi and vacuum cleaner."
    },
    "similar_to": ["cse-4101-final-2023-q1c"],
    "verified": False
  },

  # --- UNINFORMED & INFORMED SEARCH ---
  {
    "id": "cse-4101-final-2023-q2a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "2(a)",
    "marks": 4,
    "topics": ["Informed vs Uninformed Search"],
    "question": "Write down the difference between informed and uninformed search.",
    "solution": {
      "steps": [
        "1. Uninformed (Blind) Search: Uses only problem formulation information (start state, actions, transition model, goal test). Has no knowledge of how close a state is to the goal. Examples: BFS, DFS, UCS, Depth-Limited, IDS.",
        "2. Informed (Heuristic) Search: Uses domain-specific knowledge beyond problem specification via a heuristic evaluation function $h(n)$ estimating cost from node $n$ to nearest goal. Examples: Greedy Best-First Search, A*, IDA*.",
        "3. Comparison points: Efficiency (Informed is generally much faster with smaller search tree expansion), memory utilization, optimality conditions (A* requires admissibility/consistency)."
      ],
      "answer": "Uninformed search explores blindly based on graph topology; informed search utilizes heuristic guidance $h(n)$ to steer expansion towards the goal.",
      "marking_hint": "Award 2 marks for core concepts, 2 marks for comparison table/examples."
    },
    "similar_to": ["cse-4101-final-2023-q7c"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q7c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "7(c)",
    "marks": 2,
    "topics": ["Informed vs Uninformed Search"],
    "question": "Differentiate between informed and uninformed search.",
    "solution": {
      "steps": [
        "1. Uninformed search algorithms have no clue about distance to goal (blindly expand nodes by depth, path-cost, or FIFO/LIFO order).",
        "2. Informed search algorithms use a heuristic function $h(n)$ estimating remaining cost to goal to prioritize node expansion."
      ],
      "answer": "Informed search incorporates problem-specific heuristic evaluations to guide search; uninformed search does not.",
      "marking_hint": "Award 1 mark each for definition and example."
    },
    "similar_to": ["cse-4101-final-2023-q2a"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q1c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "1(c)",
    "marks": 6,
    "topics": ["Informed vs Uninformed Search"],
    "question": "For the following tree, show the order of nodes visited for i) breadth-first search, ii) depth-first search, iii) uniform cost search, and iv) iterative deepening search. The goal node is I and the numbers next to the edges indicate the associated cost.\n\n<div class=\"svg-diagram-wrapper\"><svg viewBox=\"0 0 460 270\" class=\"responsive-diagram\" role=\"img\" aria-label=\"Search tree graph\"><g stroke=\"currentColor\" stroke-width=\"1.8\" fill=\"none\"><line x1=\"230\" y1=\"30\" x2=\"100\" y2=\"80\" /><line x1=\"230\" y1=\"30\" x2=\"230\" y2=\"80\" /><line x1=\"230\" y1=\"30\" x2=\"360\" y2=\"80\" /><line x1=\"100\" y1=\"80\" x2=\"60\" y2=\"150\" /><line x1=\"100\" y1=\"80\" x2=\"140\" y2=\"150\" /><line x1=\"230\" y1=\"80\" x2=\"230\" y2=\"150\" /><line x1=\"360\" y1=\"80\" x2=\"320\" y2=\"150\" /><line x1=\"360\" y1=\"80\" x2=\"400\" y2=\"150\" /><line x1=\"230\" y1=\"150\" x2=\"230\" y2=\"220\" /><line x1=\"320\" y1=\"150\" x2=\"320\" y2=\"220\" /></g><g font-size=\"12\" font-weight=\"bold\" fill=\"currentColor\" text-anchor=\"middle\"><text x=\"155\" y=\"50\">5</text><text x=\"240\" y=\"55\">4</text><text x=\"305\" y=\"50\">3</text><text x=\"70\" y=\"115\">2</text><text x=\"130\" y=\"115\">2</text><text x=\"240\" y=\"115\">1</text><text x=\"330\" y=\"115\">4</text><text x=\"390\" y=\"115\">2</text><text x=\"240\" y=\"185\">3</text><text x=\"330\" y=\"185\">4</text></g><g fill=\"var(--surface-card, #fff)\" stroke=\"currentColor\" stroke-width=\"1.8\"><circle cx=\"230\" cy=\"30\" r=\"16\"/><circle cx=\"100\" cy=\"80\" r=\"16\"/><circle cx=\"230\" cy=\"80\" r=\"16\"/><circle cx=\"360\" cy=\"80\" r=\"16\"/><circle cx=\"60\" cy=\"150\" r=\"16\"/><circle cx=\"140\" cy=\"150\" r=\"16\"/><circle cx=\"230\" cy=\"150\" r=\"16\"/><circle cx=\"320\" cy=\"150\" r=\"16\"/><circle cx=\"400\" cy=\"150\" r=\"16\"/><circle cx=\"230\" cy=\"220\" r=\"16\" stroke=\"var(--accent-red, #c0392b)\" stroke-width=\"2.5\"/><circle cx=\"320\" cy=\"220\" r=\"16\"/></g><g font-size=\"12\" font-weight=\"bold\" fill=\"currentColor\" text-anchor=\"middle\" dominant-baseline=\"central\"><text x=\"230\" y=\"30\">A</text><text x=\"100\" y=\"80\">B</text><text x=\"230\" y=\"80\">C</text><text x=\"360\" y=\"80\">D</text><text x=\"60\" y=\"150\">E</text><text x=\"140\" y=\"150\">F</text><text x=\"230\" y=\"150\">G</text><text x=\"320\" y=\"150\">H</text><text x=\"400\" y=\"150\">K</text><text x=\"230\" y=\"220\" fill=\"var(--accent-red, #c0392b)\">I</text><text x=\"320\" y=\"220\">J</text></g></svg></div>",
    "solution": {
      "steps": [
        "1. BFS (FIFO Queue): Visits Level 0, Level 1, Level 2, Level 3: A, B, C, D, E, F, G, H, K, I (Goal reached).",
        "2. DFS (LIFO Stack): Explores left branches first: A, B, E, F, C, G, I (Goal reached).",
        "3. UCS (Priority Queue by g(n)): Path costs: A(0), D(3), C(4), B(5), K(5), G(5), H(7), B-E(7), B-F(7), I(8). Optimal path A-C-G-I with cost 8.",
        "4. IDS (Iterative Deepening Search): L=0: [A]; L=1: [A, B, C, D]; L=2: [A, B, E, F, C, G, D, H, K]; L=3: [A, B, E, F, C, G, I]."
      ],
      "answer": "BFS visits 10 nodes; DFS visits 7 nodes; UCS finds cost-optimal path A-C-G-I of cost 8; IDS finds goal at iteration limit 3.",
      "marking_hint": "Award 1.5 marks each for BFS, DFS, UCS, and IDS sequences."
    },
    "similar_to": ["cse-4101-final-2024-q7c"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q7c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "7(c)",
    "marks": 4,
    "topics": ["Informed vs Uninformed Search"],
    "question": "Perform Iterative Deepening Search based on the following graph to reach goal node G:\nTree structure: Root A has children B, C; B has children D, E; C has children F, G; D has children H, I.",
    "solution": {
      "steps": [
        "1. Depth Limit 0: Visit A. (Goal not reached).",
        "2. Depth Limit 1: Visit A, then B, C. (Goal not reached).",
        "3. Depth Limit 2: Visit A &rarr; B &rarr; D, E &rarr; C &rarr; F, G. (Goal G reached!)."
      ],
      "answer": "IDS combines DFS space efficiency O(bd) with BFS completeness and optimality O(b^d). Node G is reached at limit 2.",
      "marking_hint": "Award 1 mark for depth level tracking, 3 marks for correct node sequences."
    },
    "similar_to": ["cse-4101-final-2024-q1c"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q2d",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "2(d)",
    "marks": 4,
    "topics": ["Informed vs Uninformed Search"],
    "question": "Describe Greedy Best-First Search. Why is it not guaranteed to produce an optimal solution?",
    "solution": {
      "steps": [
        "1. Greedy Best-First Search evaluates nodes using only the heuristic function: $f(n) = h(n)$, expanding the node that appears closest to the goal.",
        "2. Why not optimal: It ignores the path cost $g(n)$ accrued so far. A path may look attractive locally because $h(n)$ is small, but the cumulative path cost to reach it could be arbitrarily large.",
        "3. Like DFS, it can also get stuck in loops (incomplete in graph search with infinite paths)."
      ],
      "answer": "Greedy Best-First Search minimizes estimated remaining cost $h(n)$, but without $g(n)$, it easily selects sub-optimal paths.",
      "marking_hint": "Award 2 marks for algorithm mechanism, 2 marks for non-optimality justification."
    },
    "similar_to": ["cse-4101-final-2023-q7d"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q7d",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "7(d)",
    "marks": 4,
    "topics": ["Informed vs Uninformed Search", "A* Search & Heuristics"],
    "question": "Using Greedy best-first search find the cost and show the steps from the source Arad to the destination Bucharest in the Romania road network.",
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
    },
    "similar_to": ["cse-4101-final-2024-q2d"],
    "verified": False
  },

  # --- A* SEARCH & HEURISTICS ---
  {
    "id": "cse-4101-final-2023-q2c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "2(c)",
    "marks": 6,
    "topics": ["A* Search & Heuristics"],
    "question": "Given an initial state of 8 puzzle problem and final state to be reached:\n\n<div class=\"scroll-container\"><table class=\"data-table\"><thead><tr><th colspan=\"3\">Initial State</th><th></th><th colspan=\"3\">Final State</th></tr></thead><tbody><tr><td>2</td><td>5</td><td>4</td><td></td><td>1</td><td>2</td><td>3</td></tr><tr><td>1</td><td>6</td><td>8</td><td>&rarr;</td><td>8</td><td> </td><td>4</td></tr><tr><td>3</td><td> </td><td>7</td><td></td><td>7</td><td>6</td><td>5</td></tr></tbody></table></div>\n\nFind the most cost effective path to reach the final state from initial state using A* search algorithm.",
    "solution": {
      "steps": [
        "1. Formulate A* evaluation function: f(n) = g(n) + h(n), where g(n) is depth and h(n) is Manhattan distance sum.",
        "2. Compute initial Manhattan distance for all 8 tiles: h(n0) = 12.",
        "3. Branch possible legal blank movements: Up (swap 6), Left (swap 3), Right (swap 7). Compute f(n) = 1 + h(n) for each.",
        "4. Prioritize lowest f(n) at each expansion until reaching goal state with h=0."
      ],
      "answer": "A* search guarantees the optimal sequence of tile movements because Manhattan distance is an admissible and consistent heuristic.",
      "marking_hint": "Award 2 marks for heuristic calculation, 2 marks for branching tree, 2 marks for path."
    },
    "similar_to": ["cse-4101-final-2024-q7b"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q7b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "7(b)",
    "marks": 4,
    "topics": ["A* Search & Heuristics"],
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
    },
    "similar_to": ["cse-4101-final-2023-q2c"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q3b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "3(b)",
    "marks": 5,
    "topics": ["A* Search & Heuristics"],
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
    },
    "similar_to": ["cse-4101-final-2024-q4a"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q3c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "3(c)",
    "marks": 2,
    "topics": ["A* Search & Heuristics"],
    "question": "What is heuristic function? Explain.",
    "solution": {
      "steps": [
        "1. A heuristic function $h(n)$ maps a state description to an estimate of the cheapest path cost from state $n$ to a goal state.",
        "2. It encodes problem-specific intuition or domain knowledge to guide search algorithms toward promising branches."
      ],
      "answer": "A heuristic function estimates remaining cost to the goal, enabling algorithms like A* to reduce exponential search spaces.",
      "marking_hint": "Award 1 mark for formal definition, 1 mark for role in reducing search space."
    },
    "similar_to": ["cse-4101-final-2024-q3a"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q3d",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "3(d)",
    "marks": 4,
    "topics": ["A* Search & Heuristics"],
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
    },
    "similar_to": [],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q3a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "3(a)",
    "marks": 4,
    "topics": ["A* Search & Heuristics"],
    "question": "Explain details about how heuristic functions guide the search process toward the goal.",
    "solution": {
      "steps": [
        "1. Heuristic functions estimate cost from current state to the goal ($h(n)$).",
        "2. In best-first search, evaluation function $f(n)$ incorporates $h(n)$ to order the priority queue.",
        "3. Relaxed problem intuition: Effective heuristics are often exact costs of solutions to simplified (relaxed) versions of the original problem."
      ],
      "answer": "Heuristics assign low estimated values to states that appear close to the goal, biasing the frontier queue towards promising regions and drastically reducing expanded nodes.",
      "marking_hint": "Award 2 marks for prioritization mechanics, 2 marks for relaxed problem generation."
    },
    "similar_to": ["cse-4101-final-2023-q3c"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q4a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "4(a)",
    "marks": 4,
    "topics": ["A* Search & Heuristics"],
    "question": "Explain the components of the A* evaluation function f(n) = g(n) + h(n). Write down the application of A* search.",
    "solution": {
      "steps": [
        "1. Components: $g(n)$ is the exact known cost from start state to current node $n$; $h(n)$ is estimated cost from $n$ to goal; $f(n)$ is total estimated cost of cheapest solution passing through $n$.",
        "2. Applications: GPS route navigation and mapping (Google Maps), robotic path planning, video game AI pathfinding (NavMesh navigation), VLSI circuit routing, natural language parsing."
      ],
      "answer": "f(n) balances path cost so far g(n) with estimated future cost h(n). Widely applied in navigation, robotics, and game pathfinding.",
      "marking_hint": "Award 2 marks for function breakdown, 2 marks for at least 3 distinct applications."
    },
    "similar_to": ["cse-4101-final-2023-q3b"],
    "verified": False
  },

  # --- HILL CLIMBING ---
  {
    "id": "cse-4101-final-2023-q3a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "3(a)",
    "marks": 3,
    "topics": ["Hill Climbing Search"],
    "question": "Write the disadvantage of Hill-climbing search.",
    "solution": {
      "steps": [
        "1. Local Maxima: A peak that is higher than all neighboring states but lower than the global maximum. Search terminates prematurely.",
        "2. Ridges: Sequence of local maxima where sides are steep; slope cannot be navigated with single-step axis moves.",
        "3. Plateaux / Flat Local Maxima: Flat search space region where all neighbors have identical evaluation, causing random wandering or getting stuck."
      ],
      "answer": "Hill climbing is prone to getting stuck in local maxima, ridges, and plateaux due to its purely greedy local neighborhood evaluation.",
      "marking_hint": "Award 1 mark each for describing Local Maxima, Ridges, and Plateaux."
    },
    "similar_to": ["cse-4101-final-2024-q7a"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q7a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "7(a)",
    "marks": 4,
    "topics": ["Hill Climbing Search"],
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
    },
    "similar_to": ["cse-4101-final-2023-q3a"],
    "verified": False
  },

  # --- CONSTRAINT SATISFACTION PROBLEMS ---
  {
    "id": "cse-4101-final-2023-q2b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "2(b)",
    "marks": 4,
    "topics": ["Constraint Satisfaction Problems"],
    "question": "What is LCV and MRV in CSP for improving Backtracking? Explain with example.",
    "solution": {
      "steps": [
        "1. Minimum Remaining Values (MRV): Variable ordering heuristic. Chooses the unassigned variable with the fewest legal values remaining in its domain ('fail-first' principle). Example in map coloring: if WA has only 'Blue' left, assign WA first.",
        "2. Least Constraining Value (LCV): Value ordering heuristic. Chooses the value that rules out the fewest choices for neighboring unassigned variables ('fail-last' principle). Leaves maximum flexibility for remaining variables."
      ],
      "answer": "MRV selects which variable to assign next to detect failure early; LCV selects which value to try first to preserve neighbor options.",
      "marking_hint": "Award 2 marks for MRV explanation and example, 2 marks for LCV explanation and example."
    },
    "similar_to": ["cse-4101-final-2024-q3b"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q5a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "5(a)",
    "marks": 3,
    "topics": ["Constraint Satisfaction Problems"],
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
    },
    "similar_to": [],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q3b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "3(b)",
    "marks": 4,
    "topics": ["Constraint Satisfaction Problems"],
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
    },
    "similar_to": ["cse-4101-final-2023-q2b"],
    "verified": False
  },

  # --- ADVERSARIAL SEARCH & ALPHA-BETA PRUNING ---
  {
    "id": "cse-4101-final-2023-q4a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "4(a)",
    "marks": 4,
    "topics": ["Adversarial Search & Min-Max"],
    "question": "What is limitation of Min-max algorithm? Write down the properties of Min-max algorithm.",
    "solution": {
      "steps": [
        "1. Limitations: Exponential time complexity $O(b^m)$ makes complete search impractical for complex games like Chess ($b \\approx 35, m \\approx 80$) or Go ($b \\approx 250$). Assumes opponent plays optimally.",
        "2. Properties:\n   • Completeness: Yes, if tree is finite.\n   • Optimality: Yes, against an optimal opponent.\n   • Time Complexity: $O(b^m)$.\n   • Space Complexity: $O(bm)$ (depth-first exploration)."
      ],
      "answer": "Minimax provides optimal decisions against rational opponents with O(bm) space, but suffers from prohibitive O(b^m) exponential time.",
      "marking_hint": "Award 2 marks for limitations, 2 marks for standard properties (completeness, optimality, time, space)."
    },
    "similar_to": ["cse-4101-final-2024-q2b"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q4b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "4(b)",
    "marks": 5,
    "topics": ["Adversarial Search & Min-Max", "Alpha-Beta Pruning"],
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
    },
    "similar_to": ["cse-4101-final-2024-q5a"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q4c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "4(c)",
    "marks": 5,
    "topics": ["Adversarial Search & Min-Max", "Genetic Algorithms"],
    "question": "What is Adversarial Search? Explain Genetic algorithm with example.",
    "solution": {
      "steps": [
        "1. Adversarial Search: Competitive multi-agent environment where two or more opponents plan conflicting actions to maximize their own utility while minimizing the opponent's (e.g. Minimax).",
        "2. Genetic Algorithm: Population-based stochastic optimization inspired by Darwinian natural selection (Selection, Crossover, Mutation, Fitness).",
        "3. Example: 8-Queens problem where each chromosome is an 8-digit string representing queen rows."
      ],
      "answer": "Adversarial search models strategic decision-making against opponents; Genetic algorithms optimize candidate solutions via evolutionary operators.",
      "marking_hint": "Award 2 marks for adversarial search, 3 marks for genetic algorithm definition and example."
    },
    "similar_to": ["cse-4101-final-2024-q2c"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q5d",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "5(d)",
    "marks": 2,
    "topics": ["Adversarial Search & Min-Max"],
    "question": "Write down the difference between game and search problem.",
    "solution": {
      "steps": [
        "1. Standard Search Problem: Single-agent environment where the agent has complete control over state transitions. The solution is a fixed sequence of actions.",
        "2. Game Problem: Multi-agent adversarial environment with unpredictable opponent actions. The solution is a contingency strategy/policy specifying what to do for every possible opponent reply."
      ],
      "answer": "Search problems find a single fixed path to goal; games require a complete contingent policy against an active opponent.",
      "marking_hint": "Award 1 mark each for search vs game distinctions."
    },
    "similar_to": ["cse-4101-final-2024-q2b"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q2b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "2(b)",
    "marks": 4,
    "topics": ["Adversarial Search & Min-Max"],
    "question": "How is a two-player game formulated as a search problem? Explain the roles of terminal test and utility function.",
    "solution": {
      "steps": [
        "1. Formulation components: Initial state $s_0$, $\\text{Player}(s)$, $\\text{Actions}(s)$, Transition model $\\text{Result}(s, a)$, Terminal test, Utility function.",
        "2. Terminal Test: Returns true if game is over (e.g., checkmate, draw), false otherwise.",
        "3. Utility Function (Payoff): Defines numeric value for terminal states (e.g., +1 for win, -1 for loss, 0 for draw)."
      ],
      "answer": "Two-player games formulate search over alternating player turns, evaluated at terminal states via a payoff utility function.",
      "marking_hint": "Award 2 marks for formal game formulation, 1 mark each for terminal test and utility function."
    },
    "similar_to": ["cse-4101-final-2023-q4a"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q2c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "2(c)",
    "marks": 3,
    "topics": ["Adversarial Search & Min-Max"],
    "question": "Explain the Adversarial Search algorithm with an example game tree.",
    "solution": {
      "steps": [
        "1. Minimax recursively evaluates game trees where MAX chooses action with maximum utility and MIN chooses action with minimum utility.",
        "2. $V(s) = \\max_{a} V(\\text{Result}(s, a))$ if Player = MAX; $V(s) = \\min_{a} V(\\text{Result}(s, a))$ if Player = MIN.",
        "3. Backpropagates utility from terminal leaves up to root."
      ],
      "answer": "Minimax backs up terminal values to establish the optimal game-theoretic value against an optimal adversary.",
      "marking_hint": "Award 1.5 marks for algorithm principles, 1.5 marks for game tree diagram."
    },
    "similar_to": ["cse-4101-final-2023-q4c"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q5a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "5(a)",
    "marks": 5,
    "topics": ["Adversarial Search & Min-Max", "Alpha-Beta Pruning"],
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
    },
    "similar_to": ["cse-4101-final-2023-q4b"],
    "verified": False
  },

  # --- GENETIC ALGORITHMS ---
  {
    "id": "cse-4101-final-2023-q5b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "5(b)",
    "marks": 7,
    "topics": ["Genetic Algorithms"],
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
    },
    "similar_to": ["cse-4101-final-2024-q2a"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q2a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "2(a)",
    "marks": 3,
    "topics": ["Genetic Algorithms"],
    "question": "Define Genetic Algorithm and its working principles with a suitable example.",
    "solution": {
      "steps": [
        "1. Genetic Algorithm: A search heuristic inspired by biological natural selection.",
        "2. Principles: Encodes candidate states as strings, evaluates fitness, mates pairs using crossover, and introduces diversity with mutation."
      ],
      "answer": "Evolutionary optimization using reproductive operators to explore complex non-differentiable search landscapes.",
      "marking_hint": "Award 1.5 marks for definition, 1.5 marks for example."
    },
    "similar_to": ["cse-4101-final-2023-q5b"],
    "verified": False
  },

  # --- FIRST-ORDER LOGIC ---
  {
    "id": "cse-4101-final-2023-q6a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "6(a)",
    "marks": 5,
    "topics": ["First-Order Logic"],
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
    },
    "similar_to": [],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q6b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "6(b)",
    "marks": 5,
    "topics": ["First-Order Logic"],
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
    },
    "similar_to": ["cse-4101-final-2024-q4b"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q6c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "6(c)",
    "marks": 4,
    "topics": ["First-Order Logic"],
    "question": "Define Inference and Existential Quantifiers in FOL with example?",
    "solution": {
      "steps": [
        "1. Inference: The process of deriving new logical statements from known axioms using sound inference rules (Modus Ponens, Resolution).",
        "2. Existential Quantifier (∃): Asserts that a predicate holds for at least one entity in domain: ∃x P(x)."
      ],
      "answer": "Inference yields valid conclusions; existential quantifier asserts property holds for at least one domain member.",
      "marking_hint": "Award 2 marks for inference, 2 marks for existential quantifier."
    },
    "similar_to": ["cse-4101-final-2024-q4c"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q4b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "4(b)",
    "marks": 5,
    "topics": ["First-Order Logic"],
    "question": "Convert the following English statement into FOL:\ni. Every man respects his parent\nii. There is somebody whom everybody loves\niii. Not all students like both Mathematics and Science\niv. Mahmud has never sent an e-mail message to Abdullah\nv. Everybody loves somebody",
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
    },
    "similar_to": ["cse-4101-final-2023-q6b"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q4c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "4(c)",
    "marks": 3,
    "topics": ["First-Order Logic"],
    "question": "Write short note on two types of quantifiers in FOL with example?",
    "solution": {
      "steps": [
        "1. Universal Quantifier (∀): 'For all'. Example: ∀x (Human(x) → Mortal(x)).",
        "2. Existential Quantifier (∃): 'There exists'. Example: ∃x (Student(x) ∧ Passed(x))."
      ],
      "answer": "Universal (∀) applies across entire domain; Existential (∃) specifies existence of at least one instance.",
      "marking_hint": "Award 1.5 marks for universal, 1.5 marks for existential."
    },
    "similar_to": ["cse-4101-final-2023-q6c"],
    "verified": False
  },

  # --- NATURAL LANGUAGE PROCESSING ---
  {
    "id": "cse-4101-final-2023-q7a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "7(a)",
    "marks": 4,
    "topics": ["Natural Language Processing"],
    "question": "What is Natural language Processing (NLP)? Explain Phases of NLP.",
    "solution": {
      "steps": [
        "1. Definition: Computational discipline enabling computers to process, understand, and generate human natural languages.",
        "2. Phases: (1) Morphological/Lexical, (2) Syntactic Analysis (Parsing), (3) Semantic Analysis, (4) Discourse Integration, (5) Pragmatic Analysis."
      ],
      "answer": "NLP models human language through five linguistic levels from tokenization to pragmatic context.",
      "marking_hint": "Award 1 mark for definition, 3 marks for describing the phases."
    },
    "similar_to": ["cse-4101-final-2023-q7b"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2023-q7b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "7(b)",
    "marks": 4,
    "topics": ["Natural Language Processing"],
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
    },
    "similar_to": ["cse-4101-final-2023-q7a"],
    "verified": False
  },

  # --- MACHINE LEARNING IN AI & NEURAL NETWORKS ---
  {
    "id": "cse-4101-final-2024-q5b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "5(b)",
    "marks": 4,
    "topics": ["Machine Learning in AI"],
    "question": "What is Reinforcement Learning? Differentiate between Supervised and Unsupervised machine learning.",
    "solution": {
      "steps": [
        "1. Reinforcement Learning: Agent learns optimal policy through trial-and-error interactions with environment, receiving rewards or penalties (Markov Decision Process).",
        "2. Supervised Learning: Trained on labeled data pairs (input, target).",
        "3. Unsupervised Learning: Learns inherent data patterns, clusters, or distributions without labeled targets."
      ],
      "answer": "Supervised uses labels; Unsupervised discovers latent patterns; Reinforcement optimizes reward signals.",
      "marking_hint": "Award 2 marks for RL, 2 marks for Supervised vs Unsupervised comparison."
    },
    "similar_to": [],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q5c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "5(c)",
    "marks": 5,
    "topics": ["Neural Networks & Backpropagation"],
    "question": "Write short note on Neural networks.",
    "solution": {
      "steps": [
        "1. Computational systems inspired by biological neurons, organized in input, hidden, and output layers.",
        "2. Perceptron model: $y = \\sigma(\\sum w_i x_i + b)$.",
        "3. Training via Backpropagation: Computes gradient of loss function via chain rule to update weights."
      ],
      "answer": "Artificial neural networks learn complex non-linear mappings via layered interconnected nodes trained by gradient descent.",
      "marking_hint": "Award 2 marks for architecture, 3 marks for activation and learning mechanism."
    },
    "similar_to": ["cse-4101-final-2024-q6c"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q6a",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "6(a)",
    "marks": 4,
    "topics": ["Machine Learning in AI"],
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
    },
    "similar_to": ["cse-4101-final-2024-q6b"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q6b",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "6(b)",
    "marks": 3,
    "topics": ["Machine Learning in AI"],
    "question": "Write down the equation for Conditional Probability and Bayes Theorem.",
    "solution": {
      "steps": [
        "1. Conditional Probability: $P(A|B) = \\frac{P(A \\cap B)}{P(B)}$, for $P(B) > 0$.",
        "2. Bayes Theorem: $P(A|B) = \\frac{P(B|A)P(A)}{P(B)} = \\frac{P(B|A)P(A)}{\\sum_i P(B|A_i)P(A_i)}$."
      ],
      "answer": "Formal mathematical definitions of conditional likelihood and Bayesian posterior inversion.",
      "marking_hint": "Award 1.5 marks for conditional probability, 1.5 marks for Bayes theorem equation."
    },
    "similar_to": ["cse-4101-final-2024-q6a"],
    "verified": False
  },
  {
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
        "1. Net input: $z = (0.4)(1.0) + (-0.6)(0.5) + 0.1 = 0.20$.",
        "2. Neuron output: $y = \\sigma(0.20) \\approx 0.5498$.",
        "3. MSE Error: $E = \\frac{1}{2}(1 - 0.5498)^2 = 0.1013$.",
        "4. Gradient factor: $\\delta = (t - y)y(1 - y) = (0.4502)(0.5498)(0.4502) = 0.1114$.",
        "5. Weight updates: $\\Delta w_1 = 0.2(0.1114)(1.0) = +0.0223$; $\\Delta w_2 = 0.2(0.1114)(0.5) = +0.0111$; $\\Delta b = +0.0223$."
      ],
      "answer": "z = 0.20, y = 0.5498, Error = 0.1013, new w1 = 0.4223, new w2 = -0.5889, new b = 0.1223.",
      "marking_hint": "Award 2 marks for net input/output, 2 marks for error, 3 marks for updates."
    },
    "similar_to": ["cse-4101-final-2024-q5c"],
    "verified": False
  },

  # --- DECISION TREES ---
  {
    "id": "cse-4101-final-2024-q3c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "3(c)",
    "marks": 6,
    "topics": ["Decision Trees"],
    "question": "Describe the Decision Tree learning algorithm. Explain with proper mathematical example how attribute selection is performed using: i) Information Gain and ii) Gini Index.",
    "solution": {
      "steps": [
        "1. Entropy formula: $H(S) = -\\sum p_i \\log_2 p_i$.",
        "2. Information Gain: $IG(S, A) = H(S) - \\sum \\frac{|S_v|}{|S|} H(S_v)$. Selects attribute maximizing reduction in entropy.",
        "3. Gini Index: $\\text{Gini}(S) = 1 - \\sum p_i^2$. Selects attribute minimizing split impurity."
      ],
      "answer": "ID3 uses Information Gain (Entropy reduction); CART uses Gini Index impurity to perform recursive greedy splitting.",
      "marking_hint": "Award 3 marks for Information Gain derivation, 3 marks for Gini Index derivation."
    },
    "similar_to": [],
    "verified": False
  },

  # --- KNOWLEDGE REPRESENTATION & ONTOLOGY ---
  {
    "id": "cse-4101-final-2023-q5c",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2023,
    "qno": "5(c)",
    "marks": 2,
    "topics": ["Knowledge Representation & Ontology"],
    "question": "What is Ontology in Knowledge Representation?",
    "solution": {
      "steps": [
        "1. An ontology represents knowledge as a formal, explicit specification of shared conceptualization.",
        "2. Defines concepts, classes, attributes, relations, and axioms in a domain to enable semantic interoperability."
      ],
      "answer": "Ontology provides the formal conceptual vocabulary and relational constraints defining an application domain.",
      "marking_hint": "Award 1 mark for conceptualization definition, 1 mark for components."
    },
    "similar_to": ["cse-4101-final-2024-q7d"],
    "verified": False
  },
  {
    "id": "cse-4101-final-2024-q7d",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "7(d)",
    "marks": 2,
    "topics": ["Knowledge Representation & Ontology"],
    "question": "What is an ontology? How does it differ from a taxonomy or a database schema?",
    "solution": {
      "steps": [
        "1. Taxonomy is strictly a hierarchical tree classification (is-a relations only).",
        "2. Database schema defines data structure for storage/retrieval without rich semantic inference logic.",
        "3. Ontology includes complex multi-dimensional relations, axioms, rules, and semantic inference."
      ],
      "answer": "Ontology generalizes beyond taxonomic hierarchies and database tables to support automated semantic reasoning.",
      "marking_hint": "Award 1 mark for definition, 1 mark for distinguishing from taxonomy and database schema."
    },
    "similar_to": ["cse-4101-final-2023-q5c"],
    "verified": False
  },

  # --- ROBOTICS & APPLICATIONS ---
  {
    "id": "cse-4101-final-2024-q4d",
    "course": "CSE-4101",
    "exam": "final",
    "year": 2024,
    "qno": "4(d)",
    "marks": 2,
    "topics": ["Robotics & Applications"],
    "question": "Write down the application of AI in robotics.",
    "solution": {
      "steps": [
        "1. Perception & SLAM (Simultaneous Localization and Mapping) using computer vision and sensor fusion.",
        "2. Path planning and motion control (obstacle avoidance using A* or RRT).",
        "3. Manipulation & Grasping using reinforcement learning."
      ],
      "answer": "AI empowers robotics with autonomous perception, spatial mapping, trajectory planning, and dexterous manipulation.",
      "marking_hint": "Award 1 mark for perception/SLAM, 1 mark for path planning."
    },
    "similar_to": [],
    "verified": False
  }
]

with open(FILE, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Successfully populated {len(questions)} complete questions in cse-4101.json")
