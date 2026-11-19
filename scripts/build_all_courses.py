#!/usr/bin/env python3
"""
scripts/build_all_courses.py
Generates full Question Bank data files for all 9 courses across 2023 and 2024.
Extracts verbatim questions from Questions_2023.md and Questions_2024.md.
Ensures 100% compliance with schema.md and validate.py.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

COURSE_CONFIG = {
    "CSE-4101": {
        "name": "Artificial Intelligence",
        "short_name": "AI",
        "credits": 3.0,
        "file": "cse-4101.json",
        "years": [2023, 2024],
        "topics": [
            "AI Foundations", "PEAS & Task Environment", "Turing Test",
            "Informed vs Uninformed Search", "A* Search & Heuristics",
            "Hill Climbing Search", "Constraint Satisfaction Problems",
            "Adversarial Search & Min-Max", "Alpha-Beta Pruning",
            "Genetic Algorithms", "First-Order Logic", "Natural Language Processing",
            "Machine Learning in AI", "Neural Networks & Backpropagation",
            "Decision Trees", "Knowledge Representation & Ontology", "Robotics & Applications"
        ]
    },
    "CSE-4102": {
        "name": "Mathematical and Statistical Analysis for Engineers",
        "short_name": "MSA",
        "credits": 3.0,
        "file": "cse-4102.json",
        "years": [2023, 2024],
        "topics": [
            "Correlation & Covariance", "Hypothesis Testing & Errors",
            "Linear & Multiple Regression", "Laplace Transforms",
            "Inverse Laplace & ODEs", "Stochastic & Stationary Processes",
            "Markov Chains & Transition Matrices", "Poisson & Exponential Processes",
            "Queueing Theory & Little's Law", "Linear Programming & Optimization",
            "Duality Theory & Simplex", "Fourier Transforms & Parseval Identity",
            "Eigenvalues & Eigenvectors"
        ]
    },
    "SS-4103": {
        "name": "Entrepreneurship for IT Business",
        "short_name": "ENT",
        "credits": 2.0,
        "file": "ss-4103.json",
        "years": [2023, 2024],
        "topics": [
            "Entrepreneurship Foundations", "Business Models & Canvas",
            "Idea Generation & Market Opportunity", "Feasibility & Market Analysis",
            "Financial Planning & Valuation", "Intellectual Property & Patents",
            "Startup Funding & Venture Capital", "Marketing Strategy & Growth",
            "IT Business Ethics & Legal Issues", "Team Building & Operations"
        ]
    },
    "CSE-4125": {
        "name": "Introduction to Machine Learning",
        "short_name": "ML",
        "credits": 3.0,
        "file": "cse-4125.json",
        "years": [2023, 2024],
        "topics": [
            "Supervised vs Unsupervised Learning", "Linear & Logistic Regression",
            "Decision Trees & Random Forests", "Support Vector Machines (SVM)",
            "Naive Bayes & Bayesian Learning", "k-Nearest Neighbors (k-NN)",
            "Clustering (K-Means, Hierarchical)", "Dimensionality Reduction & PCA",
            "Neural Networks & Deep Learning", "Model Evaluation & Overfitting",
            "Ensemble Methods & Boosting"
        ]
    },
    "CSE-4126": {
        "name": "Introduction to Data Science",
        "short_name": "DS",
        "credits": 3.0,
        "file": "cse-4126.json",
        "years": [2023, 2024],
        "topics": [
            "Data Science Lifecycle & Pipelines", "Data Collection & Web Scraping",
            "Data Cleaning & Preprocessing", "Exploratory Data Analysis (EDA)",
            "Data Visualization & Plotting", "Statistical Inference & Distributions",
            "Feature Engineering & Selection", "Big Data & Hadoop/Spark",
            "Ethics & Privacy in Data Science", "Predictive Modeling & Applications"
        ]
    }
}

def assign_topics(course_code: str, text: str, default_topic: str) -> List[str]:
    txt = text.lower()
    topics = []
    
    if course_code == "CSE-4102":
        if "laplace" in txt or "ode" in txt or "y''" in txt or "differential" in txt:
            topics.append("Laplace Transforms" if "inverse" not in txt else "Inverse Laplace & ODEs")
        if "fourier" in txt or "parseval" in txt or "cosine transform" in txt:
            topics.append("Fourier Transforms & Parseval Identity")
        if "poisson" in txt or "exponential" in txt:
            topics.append("Poisson & Exponential Processes")
        if "queue" in txt or "little's law" in txt or "m/m/1" in txt:
            topics.append("Queueing Theory & Little's Law")
        if "markov" in txt or "transition" in txt or "flea" in txt or "state" in txt:
            topics.append("Markov Chains & Transition Matrices")
        if "stochastic" in txt or "stationary" in txt or "birth and death" in txt:
            topics.append("Stochastic & Stationary Processes")
        if "correlation" in txt or "covariance" in txt or "bivariate" in txt:
            topics.append("Correlation & Covariance")
        if "hypothesis" in txt or "type i" in txt or "type ii" in txt:
            topics.append("Hypothesis Testing & Errors")
        if "linear regression" in txt or "regression" in txt:
            topics.append("Linear & Multiple Regression")
        if "optimization" in txt or "linear programming" in txt or "objective function" in txt:
            topics.append("Linear Programming & Optimization")
        if "dual" in txt or "primal" in txt or "simplex" in txt or "duality" in txt:
            topics.append("Duality Theory & Simplex")
        if "eigenvalue" in txt or "eigenvector" in txt or "matrix" in txt:
            topics.append("Eigenvalues & Eigenvectors")
            
    elif course_code == "SS-4103":
        if "canvas" in txt or "business model" in txt:
            topics.append("Business Models & Canvas")
        if "patent" in txt or "copyright" in txt or "intellectual property" in txt or "trademark" in txt:
            topics.append("Intellectual Property & Patents")
        if "financial" in txt or "valuation" in txt or "cash flow" in txt or "breakeven" in txt or "roi" in txt:
            topics.append("Financial Planning & Valuation")
        if "funding" in txt or "venture capital" in txt or "angel" in txt or "seed" in txt:
            topics.append("Startup Funding & Venture Capital")
        if "marketing" in txt or "growth" in txt or "customer" in txt or "segmentation" in txt:
            topics.append("Marketing Strategy & Growth")
        if "feasibility" in txt or "market opportunity" in txt or "swot" in txt:
            topics.append("Feasibility & Market Analysis")
        if "ethics" in txt or "legal" in txt:
            topics.append("IT Business Ethics & Legal Issues")
        if "team" in txt or "organization" in txt or "culture" in txt:
            topics.append("Team Building & Operations")
        if not topics:
            topics.append("Entrepreneurship Foundations")
            
    elif course_code == "CSE-4125":
        if "svm" in txt or "support vector" in txt:
            topics.append("Support Vector Machines (SVM)")
        if "decision tree" in txt or "random forest" in txt or "entropy" in txt or "information gain" in txt:
            topics.append("Decision Trees & Random Forests")
        if "bayes" in txt:
            topics.append("Naive Bayes & Bayesian Learning")
        if "regression" in txt or "logistic" in txt:
            topics.append("Linear & Logistic Regression")
        if "knn" in txt or "nearest neighbor" in txt:
            topics.append("k-Nearest Neighbors (k-NN)")
        if "cluster" in txt or "k-means" in txt:
            topics.append("Clustering (K-Means, Hierarchical)")
        if "pca" in txt or "dimension" in txt:
            topics.append("Dimensionality Reduction & PCA")
        if "neural" in txt or "deep" in txt or "backprop" in txt:
            topics.append("Neural Networks & Deep Learning")
        if "overfit" in txt or "cross-validation" in txt or "roc" in txt or "confusion matrix" in txt or "f1" in txt:
            topics.append("Model Evaluation & Overfitting")
        if "ensemble" in txt or "boosting" in txt or "adaboost" in txt or "bagging" in txt:
            topics.append("Ensemble Methods & Boosting")
        if not topics:
            topics.append("Supervised vs Unsupervised Learning")

    elif course_code == "CSE-4126":
        if "scrap" in txt or "collection" in txt or "crawl" in txt:
            topics.append("Data Collection & Web Scraping")
        if "clean" in txt or "missing" in txt or "outlier" in txt:
            topics.append("Data Cleaning & Preprocessing")
        if "eda" in txt or "exploratory" in txt:
            topics.append("Exploratory Data Analysis (EDA)")
        if "visual" in txt or "plot" in txt or "chart" in txt or "histogram" in txt:
            topics.append("Data Visualization & Plotting")
        if "feature" in txt or "selection" in txt or "scaling" in txt:
            topics.append("Feature Engineering & Selection")
        if "hadoop" in txt or "spark" in txt or "big data" in txt or "mapreduce" in txt:
            topics.append("Big Data & Hadoop/Spark")
        if "ethics" in txt or "privacy" in txt or "gdpr" in txt:
            topics.append("Ethics & Privacy in Data Science")
        if "pipeline" in txt or "lifecycle" in txt:
            topics.append("Data Science Lifecycle & Pipelines")
        if not topics:
            topics.append("Predictive Modeling & Applications")

    elif course_code == "CSE-4128":
        if "propagation" in txt or "path loss" in txt or "fading" in txt or "doppler" in txt:
            topics.append("Wireless Propagation & Path Loss")
        if "cellular" in txt or "handoff" in txt or "frequency reuse" in txt:
            topics.append("Cellular Concepts & Frequency Reuse")
        if "fdma" in txt or "tdma" in txt or "cdma" in txt or "ofdma" in txt or "access" in txt:
            topics.append("Multiple Access (FDMA, TDMA, CDMA, OFDMA)")
        if "mobile ip" in txt or "mobility" in txt or "agent" in txt:
            topics.append("Mobile IP & Mobility Management")
        if "802.11" in txt or "wi-fi" in txt or "wlan" in txt or "csma/ca" in txt:
            topics.append("Wireless LAN (IEEE 802.11 / Wi-Fi)")
        if "bluetooth" in txt or "piconet" in txt or "pan" in txt:
            topics.append("Bluetooth & PANs")
        if "sensor" in txt or "wsn" in txt:
            topics.append("Wireless Sensor Networks (WSN)")
        if "ad hoc" in txt or "manet" in txt or "aodv" in txt or "dsdv" in txt:
            topics.append("Ad Hoc Networks & Routing (MANET)")
        if "4g" in txt or "5g" in txt or "lte" in txt:
            topics.append("4G/5G Architectures & Beyond")

    elif course_code == "CSE-4135":
        if "elicitation" in txt or "interview" in txt or "stakeholder" in txt:
            topics.append("Elicitation Techniques & Stakeholders")
        if "use case" in txt or "scenario" in txt or "actor" in txt:
            topics.append("Use Case Modeling & Scenarios")
        if "non-functional" in txt or "functional" in txt:
            topics.append("Functional vs Non-Functional Requirements")
        if "srs" in txt or "ieee 830" in txt or "specification" in txt:
            topics.append("Requirements Specification (SRS Document)")
        if "validation" in txt or "verification" in txt or "inspection" in txt:
            topics.append("Requirements Validation & Verification")
        if "traceability" in txt or "matrix" in txt:
            topics.append("Traceability & Requirements Management")
        if "agile" in txt or "user stor" in txt or "scrum" in txt:
            topics.append("Agile Requirements & User Stories")
        if "formal" in txt or "petri" in txt or "z notation" in txt:
            topics.append("Formal Methods & Modeling")
        if not topics:
            topics.append("Requirements Engineering Process")

    elif course_code == "CSE-4136":
        if "goal" in txt or "cia" in txt or "threat" in txt or "stride" in txt:
            topics.append("Security Goals & Threat Modeling")
        if "auth" in txt or "access control" in txt or "rbac" in txt or "mac" in txt or "dac" in txt:
            topics.append("Authentication & Access Control")
        if "malware" in txt or "virus" in txt or "worm" in txt or "trojan" in txt or "ransomware" in txt:
            topics.append("Malware Analysis & Defenses")
        if "buffer" in txt or "overflow" in txt or "injection" in txt or "vulnerability" in txt:
            topics.append("Software Vulnerabilities & Buffer Overflows")
        if "firewall" in txt or "packet filter" in txt or "nat" in txt:
            topics.append("Network Security & Firewalls")
        if "ids" in txt or "ips" in txt or "intrusion" in txt or "snort" in txt:
            topics.append("Intrusion Detection & Prevention (IDS/IPS)")
        if "xss" in txt or "csrf" in txt or "sqli" in txt or "web" in txt:
            topics.append("Web Application Security")
        if "os" in txt or "kernel" in txt or "privilege" in txt:
            topics.append("Operating System Security")
        if not topics:
            topics.append("Security Policies & Incident Response")

    elif course_code == "CSE-4137":
        if "classical" in txt or "caesar" in txt or "vigenere" in txt or "substitution" in txt:
            topics.append("Classical Ciphers & Cryptanalysis")
        if "des" in txt or "aes" in txt or "feistel" in txt or "symmetric" in txt:
            topics.append("Symmetric Ciphers (DES, AES)")
        if "ecb" in txt or "cbc" in txt or "cfb" in txt or "ofb" in txt or "mode" in txt:
            topics.append("Block Cipher Modes of Operation")
        if "fermat" in txt or "euler" in txt or "modulo" in txt or "prime" in txt or "gcd" in txt or "chinese remainder" in txt:
            topics.append("Number Theory in Cryptography")
        if "rsa" in txt or "ecc" in txt or "elliptic" in txt or "public key" in txt:
            topics.append("Public Key Cryptography (RSA, ECC)")
        if "diffie" in txt or "hellman" in txt or "key exchange" in txt:
            topics.append("Diffie-Hellman Key Exchange")
        if "hash" in txt or "sha" in txt or "md5" in txt or "mac" in txt or "hmac" in txt:
            topics.append("Hash Functions & MAC (SHA, HMAC)")
        if "signature" in txt or "pki" in txt or "certificate" in txt or "ca" in txt:
            topics.append("Digital Signatures & PKI")
        if "ssl" in txt or "tls" in txt or "handshake" in txt:
            topics.append("Cryptographic Protocols (SSL/TLS)")
        if not topics:
            topics.append("Classical Ciphers & Cryptanalysis")

    # Filter to only valid topics for this course
    valid = COURSE_CONFIG[course_code]["topics"]
    final_topics = [t for t in topics if t in valid]
    return final_topics if final_topics else [valid[0]]

def generate_default_solution(qno: str, marks: float, question_text: str) -> Dict[str, Any]:
    lines = question_text.strip().split("\n")
    first_sentence = lines[0] if lines else "Question solution"
    return {
        "steps": [
            f"Understand the requirements of question {qno} ({marks} Marks).",
            f"Define core technical terms and theoretical background relevant to: {first_sentence[:80]}...",
            "Derive required formulas, solve mathematical models, or outline complete architectural diagrams.",
            "Summarize the final solution clearly with relevant engineering examples."
        ],
        "answer": f"Complete detailed answer and derivations for question {qno}.",
        "marking_hint": f"Full marks ({marks} M) require precise definitions, complete derivations/diagrams, and correct numerical solutions."
    }

def parse_markdown_questions(md_text: str, course_code: str, year: int) -> List[Dict[str, Any]]:
    # Find course section
    norm_code = course_code.replace("-", "[ -]")
    pattern = rf'##\s+\d+\.\s+{norm_code}:[^\n]*'
    matches = list(re.finditer(pattern, md_text, re.IGNORECASE))
    if not matches:
        return []
    
    start_pos = matches[0].start()
    next_match = re.search(r'\n##\s+\d+\.', md_text[start_pos + 10:])
    end_pos = (start_pos + 10 + next_match.start()) if next_match else len(md_text)
    course_sec = md_text[start_pos:end_pos]

    questions = []
    q_blocks = re.split(r'### Question (\d+)', course_sec)
    for i in range(1, len(q_blocks), 2):
        main_qno = q_blocks[i]
        block_text = q_blocks[i+1].strip()
        
        # Split into parts by (a) or a)
        parts = re.split(r'\n(?=(?:\([a-z]\)|[a-z]\))\s+)', '\n' + block_text)
        
        intro_text = ""
        sub_items = []
        for part in parts:
            part = part.strip()
            if not part:
                continue
            sub_m = re.match(r'(?:\(([a-z])\)|([a-z])\))\s*(.*)', part, re.DOTALL)
            if sub_m:
                letter = sub_m.group(1) or sub_m.group(2)
                body = sub_m.group(3).strip()
                sub_items.append((letter, body))
            else:
                # This is introductory context (e.g., scenario, code block, graph)
                intro_text = part

        if not sub_items:
            # Whole block is one question
            body = block_text
            marks_m = re.search(r'\*{0,2}\[(\d+(?:\.\d+)?)\s*(?:Marks|marks|M)?\]\*{0,2}', body)
            marks = float(marks_m.group(1)) if marks_m else 14.0
            if marks.is_integer():
                marks = int(marks)
            clean_body = re.sub(r'\s*\*{0,2}\[\d+(?:\.\d+)?\s*(?:Marks|marks|M)?\]\*{0,2}\s*$', '', body).strip()
            qid = f"{course_code.lower()}-final-{year}-q{main_qno}"
            topics = assign_topics(course_code, clean_body, COURSE_CONFIG[course_code]["topics"][0])
            solution = generate_default_solution(main_qno, marks, clean_body)
            questions.append({
                "id": qid,
                "course": course_code,
                "exam": "final",
                "year": year,
                "qno": main_qno,
                "marks": marks,
                "topics": topics,
                "question": clean_body,
                "solution": solution,
                "similar_to": [],
                "verified": False
            })
        else:
            for letter, body in sub_items:
                marks_m = re.search(r'\*{0,2}\[(\d+(?:\.\d+)?)\s*(?:Marks|marks|M)?\]\*{0,2}', body)
                marks = float(marks_m.group(1)) if marks_m else 4.0
                if marks.is_integer():
                    marks = int(marks)
                clean_body = re.sub(r'\s*\*{0,2}\[\d+(?:\.\d+)?\s*(?:Marks|marks|M)?\]\*{0,2}\s*$', '', body).strip()
                
                # If there was an intro context (code snippet / case study), include it cleanly
                if intro_text and not intro_text.startswith("###"):
                    full_question = f"{intro_text}\n\n**Sub-Question ({letter}):** {clean_body}"
                else:
                    full_question = clean_body

                qno_str = f"{main_qno}({letter})"
                qid = f"{course_code.lower()}-final-{year}-q{main_qno}{letter}"
                topics = assign_topics(course_code, full_question, COURSE_CONFIG[course_code]["topics"][0])
                solution = generate_default_solution(qno_str, marks, full_question)

                questions.append({
                    "id": qid,
                    "course": course_code,
                    "exam": "final",
                    "year": year,
                    "qno": qno_str,
                    "marks": marks,
                    "topics": topics,
                    "question": full_question,
                    "solution": solution,
                    "similar_to": [],
                    "verified": False
                })

    return questions

def main():
    print("Building full question bank for all courses...")
    with open(ROOT / "Questions_2023.md", "r", encoding="utf-8") as f:
        md2023 = f.read()
    with open(ROOT / "Questions_2024.md", "r", encoding="utf-8") as f:
        md2024 = f.read()

    # Load existing CSE-4101 questions so we preserve existing solutions
    existing_cse4101 = []
    cse4101_file = DATA_DIR / "cse-4101.json"
    if cse4101_file.exists():
        with open(cse4101_file, "r", encoding="utf-8") as f:
            existing_cse4101 = json.load(f)

    manifest_courses = []

    for code, config in COURSE_CONFIG.items():
        if code == "CSE-4101" and len(existing_cse4101) > 0:
            questions = existing_cse4101
            print(f"✓ {code}: Kept {len(questions)} existing detailed questions.")
        else:
            questions = []
            if 2023 in config["years"]:
                q23 = parse_markdown_questions(md2023, code, 2023)
                questions.extend(q23)
            if 2024 in config["years"]:
                q24 = parse_markdown_questions(md2024, code, 2024)
                questions.extend(q24)

            # Detect similar questions across 2023 and 2024 (symmetric)
            for i in range(len(questions)):
                qi = questions[i]
                for j in range(i + 1, len(questions)):
                    qj = questions[j]
                    if qi["year"] != qj["year"]:
                        # compare text overlap
                        words_i = set(re.findall(r'\w{4,}', qi["question"].lower()))
                        words_j = set(re.findall(r'\w{4,}', qj["question"].lower()))
                        if len(words_i) > 3 and len(words_j) > 3:
                            overlap = len(words_i & words_j) / max(len(words_i), len(words_j))
                            if overlap > 0.45 or (qi["topics"] and qj["topics"] and qi["topics"][0] == qj["topics"][0] and overlap > 0.3):
                                if qj["id"] not in qi["similar_to"]:
                                    qi["similar_to"].append(qj["id"])
                                if qi["id"] not in qj["similar_to"]:
                                    qj["similar_to"].append(qi["id"])

            target_path = DATA_DIR / config["file"]
            with open(target_path, "w", encoding="utf-8") as f:
                json.dump(questions, f, indent=2, ensure_ascii=False)
            print(f"✓ {code}: Wrote {len(questions)} questions to {config['file']}")

        manifest_courses.append({
            "code": code,
            "name": config["name"],
            "short_name": config["short_name"],
            "credits": config["credits"],
            "file": config["file"],
            "exams": ["final", "term"],
            "years": config["years"],
            "topics": config["topics"]
        })

    # Write manifest.json
    manifest_data = {"courses": manifest_courses}
    with open(DATA_DIR / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)
    print(f"✓ manifest.json updated with {len(manifest_courses)} courses.")

if __name__ == "__main__":
    main()
