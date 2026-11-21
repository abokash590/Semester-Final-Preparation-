import json
from pathlib import Path

DATA_DIR = Path("data")
with open(DATA_DIR / "cse-4101.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

for q in questions:
    if q.get("id") == "cse-4101-final-2023-set1":
        # 1(a)
        q["subparts"][0]["solution"] = {
            "steps": [
                "**Engineering Goal (Building Intelligent Systems):** To design and develop software/hardware agents capable of mimicking human cognitive faculties—specifically perceiving environments, reasoning logically, learning from data, solving complex problems, and executing rational actions autonomously.",
                "**Scientific Goal (Understanding Intelligence):** To investigate the foundational principles of cognition and rationality by constructing computational models that demonstrate rational thinking (logic-based deduction) and rational acting (maximizing goal achievement under uncertainty)."
            ],
            "answer": "The primary goal of AI is to design and develop rational autonomous agents that can perceive their environment, reason, learn from experience, and take optimal actions to achieve specified objectives.",
            "marking_hint": "Award 1 mark for mentioning the creation of rational/intelligent systems capable of learning, reasoning, and autonomous action."
        }

        # 1(b)
        q["subparts"][1]["solution"] = {
            "steps": [
                "**Definition & Conceptual Difference:** Weak AI (Narrow AI) is designed and optimized for a specific dedicated domain without true consciousness, whereas Strong AI (Artificial General Intelligence - AGI) exhibits generalized human-equivalent cognitive intelligence across any intellectual discipline with genuine self-awareness and reasoning.",
                "**Structured Comparison:**\n\n| Feature / Dimension | Weak AI (Narrow AI / Applied AI) | Strong AI (Artificial General Intelligence - AGI) |\n| :--- | :--- | :--- |\n| **Scope & Objective** | Dedicated to **one specific task** (e.g., playing chess, speech recognition). | Generalized intelligence across **any intellectual task** equivalent to human cognition. |\n| **Consciousness & Mind** | Simulates intelligence **without genuine consciousness**, sentience, or subjective understanding (*Chinese Room Argument*). | Possesses genuine consciousness, self-awareness, emotions, and true intentionality. |\n| **Adaptability** | Cannot transfer or adapt knowledge outside its training domain without reprogramming. | Autonomously transfers learned abstractions across novel and unrelated domains. |\n| **Current Status** | Fully realized and pervasive today (e.g., Siri, AlphaGo, ChatGPT, Tesla FSD). | Purely theoretical today; no true Strong AI/AGI system currently exists. |"
            ],
            "answer": "Weak AI simulates human task performance within a constrained domain without consciousness; Strong AI exhibits generalized, conscious, and autonomous human-equivalent cognition across all domains.",
            "marking_hint": "Award 1 mark for Weak AI definition and concrete examples, 1 mark for Strong AI definition and general cognition characteristics."
        }

        # 1(c)
        q["subparts"][2]["solution"] = {
            "steps": [
                "**Part I — Automated Taxi Driver:**\n\n* **PEAS Description:**\n  * **P (Performance Measure):** Safe trip, compliance with traffic laws, passenger comfort, minimize travel time, minimize operating/fuel cost, maximize profits.\n  * **E (Environment):** Urban streets and freeways, other motorized vehicles, pedestrians, cyclists, road conditions, weather, traffic police, passengers.\n  * **A (Actuators):** Steering wheel, accelerator pedal, brakes, turn signals, horn, communication screen/speaker.\n  * **S (Sensors):** Video cameras, LiDAR, RADAR, ultrasonic rangefinders, GPS receiver, speedometer, accelerometer, engine diagnostic sensors.\n\n* **Task Environment Characterization:**\n\n| Dimension | Classification | Justification |\n| :--- | :---: | :--- |\n| **Observability** | **Partially Observable** | Sensor range is bounded; agent cannot see around blind corners, inside other vehicles, or discern other drivers' intent. |\n| **Determinism** | **Stochastic** | Road friction, weather changes, unexpected vehicle maneuvers, and mechanical faults introduce random outcomes. |\n| **Episodic vs Sequential** | **Sequential** | Present steering and braking decisions directly impact vehicle momentum, safety, and all subsequent states. |\n| **Static vs Dynamic** | **Dynamic** | The environment (traffic and pedestrians) continuously moves and changes while the agent decides its next action. |\n| **Discrete vs Continuous** | **Continuous** | Vehicle speed, steering angle, acceleration, and coordinates vary continuously over real numbers. |\n| **Agent Count** | **Multi-Agent (Cooperative & Competitive)** | Interacts with numerous other rational decision-makers (other motorists, traffic officers, pedestrians). |",
                "**Part II — Vacuum Cleaner:**\n\n* **PEAS Description:**\n  * **P (Performance Measure):** Percentage of floor area cleaned, amount of dirt collected, time elapsed, battery/power efficiency, collision avoidance.\n  * **E (Environment):** Room floor surfaces (carpet, hardwood, tile), walls, furniture legs, obstacles, stairs/drop-offs, dirt/dust particles.\n  * **A (Actuators):** Motorized drive wheels/tracks, suction motor, spinning edge brushes, dirt disposal release valve, indicator LEDs.\n  * **S (Sensors):** Dirt detection sensor (acoustic/infrared), tactile bumper switch, downward infrared cliff sensor, wheel revolution encoders.\n\n* **Task Environment Characterization:**\n\n| Dimension | Classification | Justification |\n| :--- | :---: | :--- |\n| **Observability** | **Partially Observable** *(Standard 2-Tile)* / **Fully Observable** *(Mapped Room)* | In the canonical setup, the agent only senses dirt in its current tile; with a top-down camera/full grid map, it is Fully Observable. |\n| **Determinism** | **Deterministic** | Moving forward consistently advances the agent to the next tile; sucking consistently removes dirt without random error. |\n| **Episodic vs Sequential** | **Sequential** | Cleaning one location changes current battery level and spatial location for subsequent cleaning passes. |\n| **Static vs Dynamic** | **Static** | Furniture and room walls remain stationary while the agent computes its next action. |\n| **Discrete vs Continuous** | **Discrete** | Locations (grid coordinates), percepts (Dirt / No Dirt), and actions (Left, Right, Suck) are discrete finite sets. |\n| **Agent Count** | **Single-Agent** | Operates alone without competing or collaborating agents in the workspace. |",
                "**Part III — Backgammon:**\n\n* **PEAS Description:**\n  * **P (Performance Measure):** Winning the match (first player to bear off all 15 checkers), score points accumulated (Single win, Gammon, Backgammon).\n  * **E (Environment):** 24-point playing board, 15 black checkers, 15 white checkers, doubling cube, pair of 6-sided dice.\n  * **A (Actuators):** Move checkers along points, hit opponent blot to the bar, bear off checkers, propose/accept doubling cube.\n  * **S (Sensors):** Digital board perception (exact location of all 30 checkers and current dice roll numbers).\n\n* **Task Environment Characterization:**\n\n| Dimension | Classification | Justification |\n| :--- | :---: | :--- |\n| **Observability** | **Fully Observable** | All 30 checker positions, dice rolls, and the doubling cube are completely visible to both players at all times. |\n| **Determinism** | **Stochastic** | Dice rolls introduce non-deterministic probabilistic chance into possible state transitions. |\n| **Episodic vs Sequential** | **Sequential** | Early checker placement and building prime defenses directly dictate late-game bearing off success. |\n| **Static vs Dynamic** | **Static** | The board configuration does not change while a player takes time to analyze their move. |\n| **Discrete vs Continuous** | **Discrete** | Finite number of board positions (24 points), discrete dice outcomes (1 to 6), and a finite set of legal moves. |\n| **Agent Count** | **Multi-Agent (Competitive)** | Two agents playing in strict zero-sum adversarial competition where one player's gain is the other's loss. |"
            ],
            "answer": "Automated Taxi: Partially Observable, Stochastic, Sequential, Dynamic, Continuous, Multi-Agent. Vacuum Cleaner: Partially Observable, Deterministic, Sequential, Static, Discrete, Single-Agent. Backgammon: Fully Observable, Stochastic, Sequential, Static, Discrete, Competitive Multi-Agent.",
            "marking_hint": "Award 3 marks per task environment: 1.5 marks for complete PEAS description (0.375 per component), 1.5 marks for 6-dimension characterization with clear justifications (0.25 per dimension)."
        }

        # 1(d)
        q["subparts"][3]["solution"] = {
            "steps": [
                "**Origin & Operational Setup (Alan Turing, 1950):** Proposed in the seminal paper *'Computing Machinery and Intelligence'*, the Turing Test (originally the *Imitation Game*) replaces the subjective philosophical dilemma *'Can machines think?'* with an empirical behavioral evaluation. The experimental setup isolates three entities in separate rooms communicating strictly through a text-only terminal interface: a human interrogator (Judge $C$), a human respondent ($B$), and an AI system ($A$).",
                "**Evaluation Criterion & Significance:** The interrogator freely poses arbitrary questions across any topic to both respondents. If the evaluator cannot reliably determine which respondent is the machine and which is the human (conventionally if the machine misleads the interrogator at least 30% to 50% of the time), the system passes the test. Its historical significance lies in establishing an **operational definition of intelligence** rooted in observable, rational behavior rather than internal biological consciousness."
            ],
            "answer": "The Turing Test is an operational benchmark evaluating artificial intelligence through natural language conversation. A system passes if a human interrogator cannot reliably distinguish its text responses from those of a human.",
            "marking_hint": "Award 1 mark for the experimental setup (isolated rooms, human judge, human respondent, machine, text-only interface), 1 mark for the passing criterion and operational significance."
        }
        print("Updated cse-4101-final-2023-set1 successfully!")
        break

with open(DATA_DIR / "cse-4101.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)
    f.write("\n")

# Rebundle codex_data.js
manifest_path = DATA_DIR / "manifest.json"
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = json.load(f)

courses_dict = {}
for c in manifest.get("courses", []):
    c_file = DATA_DIR / c["file"]
    if c_file.exists():
        with open(c_file, "r", encoding="utf-8") as f:
            courses_dict[c["code"]] = json.load(f)

bundle = {
    "manifest": manifest,
    "courses": courses_dict
}

bundle_js_path = DATA_DIR / "codex_data.js"
with open(bundle_js_path, "w", encoding="utf-8") as f:
    f.write("window.CODEX_DATA = " + json.dumps(bundle, indent=2, ensure_ascii=False) + ";\n")

print("Rebundled codex_data.js successfully!")
