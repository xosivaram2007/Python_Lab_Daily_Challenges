📊 Data Replication & Integrity Analyzer
📌 Overview

This project simulates how data is copied in a cloud system and analyzes issues caused by improper copying methods.

🎯 Objective

To compare assignment, shallow copy, and deep copy and detect:

Data leakage
Consistency
Overlapping data
⚙️ Working
Create nested user data
Replicate using different copy methods
Modify data based on roll number:
Even → Add file
Odd → Remove file
Analyze integrity using conditions and sets
📊 Output
Displays original, shallow, and deep copies

Generates integrity report:

(leakage_count, safe_count, overlap_count)
⚠️ Key Insight

Shallow copy can cause unintended changes in original data, while deep copy keeps data safe.

🚀 Run
python filename.py