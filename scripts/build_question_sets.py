#!/usr/bin/env python3
"""
scripts/build_question_sets.py
Constructs 7 unified Question Sets per year (2023 & 2024) for each of the 5 core courses:
  - CSE-4101: Artificial Intelligence
  - CSE-4102: Mathematical and Statistical Analysis
  - SS-4103: Entrepreneurship for IT Business
  - CSE-4125: Introduction to Machine Learning
  - CSE-4126: Introduction to Data Science

Each Question Set bundles all subparts (a, b, c, d) and any diagrams/tables together,
followed by individual sub-question solutions with their question titles.
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

COURSE_LIST = [
    {
        "code": "CSE-4101",
        "name": "Artificial Intelligence",
        "short_name": "AI",
        "credits": 3.0,
        "file": "cse-4101.json",
        "years": [2023, 2024]
    },
    {
        "code": "CSE-4102",
        "name": "Mathematical and Statistical Analysis for Engineers",
        "short_name": "MSA",
        "credits": 3.0,
        "file": "cse-4102.json",
        "years": [2023, 2024]
    },
    {
        "code": "SS-4103",
        "name": "Entrepreneurship for IT Business",
        "short_name": "ENT",
        "credits": 2.0,
        "file": "ss-4103.json",
        "years": [2023, 2024]
    },
    {
        "code": "CSE-4125",
        "name": "Introduction to Machine Learning",
        "short_name": "ML",
        "credits": 3.0,
        "file": "cse-4125.json",
        "years": [2023, 2024]
    },
    {
        "code": "CSE-4126",
        "name": "Introduction to Data Science",
        "short_name": "DS",
        "credits": 3.0,
        "file": "cse-4126.json",
        "years": [2023, 2024]
    }
]

def load_json_questions(filename: str) -> List[Dict[str, Any]]:
    path = DATA_DIR / filename
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def extract_set_raw_markdown(md_text: str, course_code: str, set_num: int) -> str:
    norm_code = course_code.replace("-", "[ -]")
    pattern = rf'##\s+\d+\.\s+{norm_code}:[^\n]*'
    matches = list(re.finditer(pattern, md_text, re.IGNORECASE))
    if not matches:
        return ""
    start_pos = matches[0].start()
    next_match = re.search(r'\n##\s+\d+\.', md_text[start_pos + 10:])
    end_pos = (start_pos + 10 + next_match.start()) if next_match else len(md_text)
    course_sec = md_text[start_pos:end_pos]

    q_blocks = re.split(r'### Question (\d+)', course_sec)
    for i in range(1, len(q_blocks), 2):
        if int(q_blocks[i]) == set_num:
            return q_blocks[i+1].strip()
    return ""

def main():
    print("Building unified Question Sets for all 5 courses...")

    with open(ROOT / "Questions_2023.md", "r", encoding="utf-8") as f:
        md2023 = f.read()
    with open(ROOT / "Questions_2024.md", "r", encoding="utf-8") as f:
        md2024 = f.read()

    # Load existing manifest to keep topic taxonomy
    with open(DATA_DIR / "manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)
    
    course_topics_map = {c["code"]: c["topics"] for c in manifest["courses"]}

    for course in COURSE_LIST:
        code = course["code"]
        existing_items = load_json_questions(course["file"])
        course_topics = course_topics_map.get(code, [])

        question_sets = []

        for year in [2023, 2024]:
            year_md = md2023 if year == 2023 else md2024

            for set_no in range(1, 8):
                # Find all subparts for this set from existing items
                # Match e.g. q1a, q1b, q1c, or qno starts with '1(' or '1'
                subparts = []
                for item in existing_items:
                    if item.get("year") == year:
                        qno_str = str(item.get("qno", ""))
                        m = re.match(r'^(\d+)(?:\(([a-z])\)|([a-z]))?$', qno_str)
                        if m and int(m.group(1)) == set_no:
                            label = f"({m.group(2) or m.group(3) or 'a'})"
                            subparts.append({
                                "id": item["id"],
                                "qno": qno_str,
                                "label": label,
                                "marks": item["marks"],
                                "topics": item.get("topics", [course_topics[0] if course_topics else "General"]),
                                "question": item["question"],
                                "solution": item["solution"]
                            })

                # Sort subparts by label
                subparts.sort(key=lambda s: s["label"])

                # Get raw markdown for the full question set (contains all questions and diagrams)
                raw_set_md = extract_set_raw_markdown(year_md, code, set_no)
                if not raw_set_md and subparts:
                    # Fallback reconstruct from subparts
                    parts_text = []
                    for s in subparts:
                        parts_text.append(f"{s['label']} {s['question']} **[{s['marks']}]**")
                    raw_set_md = "\n\n".join(parts_text)

                total_marks = sum(s["marks"] for s in subparts) if subparts else 14
                all_set_topics = []
                for s in subparts:
                    for t in s.get("topics", []):
                        if t not in all_set_topics:
                            all_set_topics.append(t)
                if not all_set_topics:
                    all_set_topics = [course_topics[0]] if course_topics else ["General"]

                set_id = f"{code.lower()}-final-{year}-set{set_no}"
                
                # Composite Solution Summary
                composite_solution = {
                    "steps": [
                        f"See detailed solution breakdowns for sub-questions below."
                    ],
                    "answer": f"Complete solutions for Question {set_no} ({total_marks} Marks total).",
                    "marking_hint": f"Full marks ({total_marks} M): Answer all sub-parts completely."
                }

                question_sets.append({
                    "id": set_id,
                    "course": code,
                    "exam": "final",
                    "year": year,
                    "set_no": set_no,
                    "qno": f"Question {set_no}",
                    "marks": total_marks,
                    "topics": all_set_topics,
                    "question": raw_set_md,
                    "subparts": subparts,
                    "solution": composite_solution,
                    "similar_to": [],
                    "verified": False
                })

        # Save question sets
        with open(DATA_DIR / course["file"], "w", encoding="utf-8") as f:
            json.dump(question_sets, f, indent=2, ensure_ascii=False)
        print(f"✓ {code}: Successfully generated {len(question_sets)} Question Sets (7 for 2023, 7 for 2024).")

    print("\nAll 5 course question set files generated successfully.")

if __name__ == "__main__":
    main()
