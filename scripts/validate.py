#!/usr/bin/env python3
"""
scripts/validate.py
Strict JSON schema and relational integrity validator for Question Bank.
Ensures:
  1. Every course in data/manifest.json exists, has a valid file, and passes schema validation.
  2. Every question strictly satisfies the schema.
  3. Every topic in every question is present in the course's controlled topics list.
  4. All question IDs are unique across all files.
  5. Every similar_to target points to a real existing question ID.
Exits with code 1 on any failure.
"""

import sys
import json
from pathlib import Path
from typing import Dict, List, Set, Any

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
MANIFEST_PATH = DATA_DIR / "manifest.json"

REQUIRED_FIELDS = {
    "id": str,
    "course": str,
    "exam": str,
    "year": int,
    "qno": str,
    "marks": (int, float),
    "topics": list,
    "question": str,
    "solution": dict,
    "similar_to": list,
    "verified": bool,
}

REQUIRED_SOLUTION_FIELDS = {
    "steps": list,
    "answer": str,
    "marking_hint": str,
}

VALID_EXAMS = {"final", "term"}


def fail(msg: str) -> None:
    print(f"\n❌ VALIDATION ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def validate() -> None:
    print("🔍 Starting Question Bank validation...")

    if not MANIFEST_PATH.exists():
        fail(f"Manifest not found at {MANIFEST_PATH}")

    try:
        with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception as e:
        fail(f"Failed to parse {MANIFEST_PATH}: {e}")

    courses = manifest.get("courses")
    if not isinstance(courses, list) or len(courses) == 0:
        fail("manifest.json must contain a non-empty 'courses' array.")

    all_questions_by_id: Dict[str, Dict[str, Any]] = {}
    course_topics_map: Dict[str, Set[str]] = {}
    course_files: Dict[str, Path] = {}

    # Step 1: Validate Course Definitions in Manifest
    for idx, c in enumerate(courses):
        code = c.get("code")
        file_name = c.get("file")
        topics = c.get("topics")

        if not code or not isinstance(code, str):
            fail(f"Course #{idx} in manifest is missing valid 'code'.")
        if not file_name or not isinstance(file_name, str):
            fail(f"Course {code} in manifest is missing valid 'file'.")
        if not isinstance(topics, list) or len(topics) == 0:
            fail(f"Course {code} must define a non-empty controlled 'topics' array in manifest.")

        for t in topics:
            if not isinstance(t, str) or not t.strip():
                fail(f"Course {code} contains invalid topic '{t}' in manifest.")

        course_topics_map[code] = set(topics)
        course_file = DATA_DIR / file_name

        if not course_file.exists():
            fail(f"Course file specified in manifest does not exist: {course_file}")

        course_files[code] = course_file

    print(f"✓ Manifest verified ({len(courses)} courses registered).")

    # Step 2: Validate Questions in each course file
    total_questions = 0

    for code, file_path in course_files.items():
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                questions = json.load(f)
        except Exception as e:
            fail(f"Failed to parse JSON file {file_path}: {e}")

        if not isinstance(questions, list):
            fail(f"{file_path} must be a top-level JSON array of questions.")

        allowed_topics = course_topics_map[code]

        for q_idx, q in enumerate(questions):
            total_questions += 1
            if not isinstance(q, dict):
                fail(f"{file_path}: Question #{q_idx} is not a JSON object.")

            q_id = q.get("id")
            if not q_id or not isinstance(q_id, str):
                fail(f"{file_path}: Question #{q_idx} is missing a string 'id'.")

            # Check unique ID
            if q_id in all_questions_by_id:
                fail(f"Duplicate question id detected: '{q_id}' (in {file_path})")

            # Verify field types
            for field, expected_type in REQUIRED_FIELDS.items():
                if field not in q:
                    fail(f"Question '{q_id}' in {file_path} is missing required field '{field}'.")
                if not isinstance(q[field], expected_type):
                    fail(f"Question '{q_id}' field '{field}' must be {expected_type}, got {type(q[field])}.")

            # Validate course match
            if q["course"] != code:
                fail(f"Question '{q_id}' has course '{q['course']}' but is inside {file_path} (expected '{code}').")

            # Validate exam type
            if q["exam"] not in VALID_EXAMS:
                fail(f"Question '{q_id}' has invalid exam '{q['exam']}'. Expected one of {VALID_EXAMS}.")

            # Validate year
            if q["year"] < 1900 or q["year"] > 2100:
                fail(f"Question '{q_id}' has unrealistic year '{q['year']}'.")

            # Validate marks
            if q["marks"] <= 0:
                fail(f"Question '{q_id}' must have positive marks, got {q['marks']}.")

            # Validate controlled topics
            q_topics = q["topics"]
            if len(q_topics) == 0:
                fail(f"Question '{q_id}' topics list cannot be empty.")
            for t in q_topics:
                if not isinstance(t, str):
                    fail(f"Question '{q_id}' topic must be string, got {t}.")
                if t not in allowed_topics:
                    fail(
                        f"Controlled Topic Violation in '{q_id}': topic '{t}' is NOT in manifest for course {code}.\n"
                        f"Allowed topics for {code}: {sorted(list(allowed_topics))}"
                    )

            # Validate solution object
            sol = q["solution"]
            for s_field, s_type in REQUIRED_SOLUTION_FIELDS.items():
                if s_field not in sol:
                    fail(f"Question '{q_id}' solution is missing '{s_field}'.")
                if not isinstance(sol[s_field], s_type):
                    fail(f"Question '{q_id}' solution.{s_field} must be {s_type}.")

            if len(sol["steps"]) == 0:
                fail(f"Question '{q_id}' solution.steps cannot be empty.")

            # Validate similar_to is list of strings
            for sim_id in q["similar_to"]:
                if not isinstance(sim_id, str):
                    fail(f"Question '{q_id}' similar_to entry must be string, got {sim_id}.")

            all_questions_by_id[q_id] = q

        print(f"✓ {file_path.name}: {len(questions)} questions passed schema validation.")

    # Step 3: Validate Relational Integrity (similar_to pointers)
    print("🔍 Checking similar_to reference integrity...")
    missing_links = []
    for q_id, q in all_questions_by_id.items():
        for target_id in q["similar_to"]:
            if target_id not in all_questions_by_id:
                missing_links.append(f"Question '{q_id}' references unknown similar_to target '{target_id}'")

    if missing_links:
        fail("Broken relational links:\n" + "\n".join(f"  • {m}" for m in missing_links))

    print(f"✓ All similar_to references resolved successfully.")
    print(f"\n🎉 ALL CHECKS PASSED: {len(course_files)} courses, {total_questions} questions verified with zero errors.")


if __name__ == "__main__":
    validate()
