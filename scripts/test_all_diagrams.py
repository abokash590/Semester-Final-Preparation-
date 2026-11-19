import json
import glob
import os
from playwright.sync_api import sync_playwright

def test():
    diagrams = []
    for f in glob.glob("data/*.json"):
        if "manifest" in f: continue
        data = json.load(open(f, encoding="utf-8"))
        for q in data:
            if "```mermaid" in q.get("question", ""):
                parts = q["question"].split("```mermaid")
                for p in parts[1:]:
                    code = p.split("```")[0].strip()
                    diagrams.append((f, q["year"], q["qno"], code))

    print(f"Found {len(diagrams)} Mermaid diagrams.")
    for d in diagrams:
        print(f"Diagram in {d[0]} {d[1]} {d[2]}: {d[3].splitlines()[0]}")

if __name__ == "__main__":
    test()
