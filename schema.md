# Question Bank JSON Schema & Data Contract

This document defines the strict specification for all course question data in `data/*.json`. Every file is validated against this contract by `scripts/validate.py`.

---

## 1. File Structure & Organization
* All course question banks reside in `data/[course-code-lowercase].json` (e.g. `data/cse-4101.json`).
* Course metadata, available years, exams, and the **controlled topic whitelist** are defined in `data/manifest.json`.
* Every question file is an array of JSON question objects: `[ { ... }, { ... } ]`.

---

## 2. Field Specifications

| Field | Type | Required | Description | Constraints |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `string` | **Yes** | Globally unique identifier | Format: `^[a-z0-9-]+-(final\|term)-\d{4}-q[a-z0-9]+$` (e.g., `cse-4101-final-2023-q3b`). Must be unique across all files. |
| `course` | `string` | **Yes** | Official course code | Must match the course code in `manifest.json` (e.g., `"CSE-4101"`). |
| `exam` | `string` | **Yes** | Examination type | Enum: `"final"` or `"term"`. |
| `year` | `integer` | **Yes** | Examination year | 4-digit positive integer (e.g., `2023`, `2024`). |
| `qno` | `string` | **Yes** | Question label on exam paper | e.g. `"1(a)"`, `"3(b)"`, `"7"`. |
| `marks` | `number` | **Yes** | Allocated marks | Positive integer or float (e.g. `4`, `5`, `2.5`). |
| `topics` | `array[string]` | **Yes** | Categorization topics | Non-empty array of strings. **Every topic MUST exist in the course's controlled topics list in `manifest.json`.** |
| `question` | `string` | **Yes** | Verbatim question text | May include inline LaTeX `$...$` and display LaTeX `$$...$$` or HTML tables/SVGs. |
| `solution` | `object` | **Yes** | Step-by-step solution | Must contain `steps` (array of strings), `answer` (string), and `marking_hint` (string). |
| `similar_to` | `array[string]` | **Yes** | Related/repeated question IDs | Array of string IDs. Every referenced ID must exist. Symmetrically linked in the UI. |
| `verified` | `boolean` | **Yes** | Review status | Set to `false` until manually verified by student. Shows an unverified badge when `false`. **Never set `true` automatically.** |

---

## 3. Example Valid Entry

```json
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
      "Define PEAS components: Performance measure, Environment, Actuators, Sensors for each agent.",
      "Characterize each along the 6 standard dimensions: Observability, Agents, Determinism, Episodic, Dynamism, Continuity."
    ],
    "answer": "Complete PEAS analysis and 6-dimensional task environment matrix for Taxi, Vacuum Cleaner, and Backgammon.",
    "marking_hint": "Award 3 marks for each environment (1.5 marks for PEAS breakdown, 1.5 marks for dimensional characterization)."
  },
  "similar_to": ["cse-4101-final-2024-q1b"],
  "verified": false
}
```

---

## 4. Validation Rules Enforced by `scripts/validate.py`

1. **Manifest Integrity:** Every course entry in `data/manifest.json` must map to an existing `data/[file]` that is non-empty and valid JSON.
2. **Schema Conformance:** Every question entry must contain all required fields with matching types.
3. **ID Uniqueness:** No two questions across any file in `data/` may share an `id`.
4. **Relational Integrity:** Every ID listed in any `similar_to` array must point to a real, existing question `id`.
5. **Controlled Topic Validation:** Any topic not present in the course's `topics` whitelist in `manifest.json` fails validation immediately.
