import json
import re

# 1. Load data/cse-4101.json
with open('data/cse-4101.json', 'r', encoding='utf-8') as f:
    sets = json.load(f)

# Find 2024 Set 6 (Neuron gap fix)
for s in sets:
    if s.get('id') == 'cse-4101-final-2024-set6':
        old_q = s['question']
        # Replace the multiple $$ lines with single aligned block
        target_old = r"""$$\text{Inputs: } x_1 = 1.0, \; x_2 = 0.5$$  
$$\text{Weights: } w_1 = 0.4, \; w_2 = -0.6$$  
$$\text{Bias: } b = 0.1$$  
$$\text{Activation function: Sigmoid}$$  
$$\text{Target output: } t = 1$$  
$$\text{Learning rate: } \eta = 0.2$$"""
        
        replacement = r"""$$\begin{aligned}
\text{Inputs: } & x_1 = 1.0, \; x_2 = 0.5 \\
\text{Weights: } & w_1 = 0.4, \; w_2 = -0.6 \\
\text{Bias: } & b = 0.1 \\
\text{Activation function: } & \text{Sigmoid} \\
\text{Target output: } & t = 1 \\
\text{Learning rate: } & \eta = 0.2
\end{aligned}$$"""
        if target_old in old_q:
            s['question'] = old_q.replace(target_old, replacement)
            print("✓ Fixed 2024 Set 6 neuron parameters math block alignment.")
        else:
            print("⚠ Warning: target_old not found in Set 6 question. Checking regex...")

# Find 2024 Set 4 (Bold FOL statements)
for s in sets:
    if s.get('id') == 'cse-4101-final-2024-set4':
        s['question'] = s['question'].replace("i. Every man respects his parent", "i. **Every man respects his parent**")
        s['question'] = s['question'].replace("ii. There is somebody whom everybody loves", "ii. **There is somebody whom everybody loves**")
        s['question'] = s['question'].replace("iii. Not all students like both Mathematics and Science", "iii. **Not all students like both Mathematics and Science**")
        s['question'] = s['question'].replace("iv. Mahmud has never sent an e-mail message to Abdullah", "iv. **Mahmud has never sent an e-mail message to Abdullah**")
        s['question'] = s['question'].replace("v. Everybody loves somebody", "v. **Everybody loves somebody**")
        print("✓ Bolds applied to 2024 Set 4 question.")
        for sub in s.get('subparts', []):
            if sub.get('id') == 'cse-4101-final-2024-q4b':
                sub['question'] = sub['question'].replace("i. Every man respects his parent", "i. **Every man respects his parent**")
                sub['question'] = sub['question'].replace("ii. There is somebody whom everybody loves", "ii. **There is somebody whom everybody loves**")
                sub['question'] = sub['question'].replace("iii. Not all students like both Mathematics and Science", "iii. **Not all students like both Mathematics and Science**")
                sub['question'] = sub['question'].replace("iv. Mahmud has never sent an e-mail message to Abdullah", "iv. **Mahmud has never sent an e-mail message to Abdullah**")
                sub['question'] = sub['question'].replace("v. Everybody loves somebody", "v. **Everybody loves somebody**")
                print("✓ Bolds applied to 2024 Subpart 4(b) question.")

with open('data/cse-4101.json', 'w', encoding='utf-8') as f:
    json.dump(sets, f, indent=2, ensure_ascii=False)
print("Updated cse-4101.json successfully.")
