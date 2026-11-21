import json
from pathlib import Path

DATA_DIR = Path("data")
COURSE_FILES = [
    "cse-4101.json",
    "cse-4102.json",
    "cse-4125.json",
    "cse-4126.json",
    "ss-4103.json"
]

TARGET_COLLEGES = {"MEC", "FEC", "NITER"}

removed_count = 0
question_count = 0

for filename in COURSE_FILES:
    filepath = DATA_DIR / filename
    if not filepath.exists():
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        questions = json.load(f)
    
    for q in questions:
        college = q.get("college")
        is_term = q.get("exam") == "term"
        if college in TARGET_COLLEGES or (is_term and college in TARGET_COLLEGES):
            question_count += 1
            if "solution" in q:
                del q["solution"]
                removed_count += 1
            if "subparts" in q and isinstance(q["subparts"], list):
                for sub in q["subparts"]:
                    if "solution" in sub:
                        del sub["solution"]
                        removed_count += 1
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Updated {filename}")

# Rebuild codex_data.js
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

print(f"Rebundled codex_data.js. Processed {question_count} term questions, removed solutions from {removed_count} fields.")
