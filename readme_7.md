⚡ Smart Campus Energy Analyzer
📌 Overview
The Smart Campus Energy Analyzer is a Python program that analyzes energy usage across different campus buildings. The system accepts energy readings, classifies them based on consumption levels, and generates an efficiency report. This helps detect inefficient energy usage and promotes better energy management in a smart campus environment.

🎯 Problem Statement
Energy readings (in units) are collected from multiple buildings in a smart campus.
The program analyzes these readings and categorizes them into four groups:
Energy Range	Category
< 0	Invalid
0 – 50	Efficient
51 – 150	Moderate
> 150	High Consumption
After classification, the system evaluates the campus energy efficiency and generates a report.

🚀 Features
Accepts multiple energy readings from the user
Classifies readings using a Python dictionary
Uses loops and conditional statements for classification
Uses list comprehension to filter valid energy readings
Stores summary information using a tuple
Generates a final energy efficiency report

🧠 Logic / Approach
The program takes energy readings as input from the user.
The readings are converted into a list of integers.
A dictionary is used to classify each reading into efficient, moderate, high, or invalid categories.
A for loop and conditional statements perform the classification.
List comprehension extracts valid readings to calculate the total energy consumption.
The total consumption and number of buildings are stored in a tuple.
The program evaluates conditions like overconsumption, balanced usage, or energy waste.
A personalization rule detects a Green Hour when three efficient readings occur consecutively.

🌱 Personalization Applied

A custom rule called Green Hour Detection was implemented.
If three consecutive energy readings are efficient (≤ 50 units), the system detects a “Green Hour”.
This represents a period when multiple campus buildings are using energy efficiently at the same time, indicating effective energy management.

💻 Example Input
20 30 40 120 180

📊 Example Output
===== ENERGY REPORT =====
Efficient: [20, 30, 40]
Moderate: [120]
High: [180]
Invalid: []
Total Consumption: 390
Number of Buildings: 5
Efficiency Result: Efficient Campus / Green Hour Detected !!

🧪 Test Cases
| Test Case | Input                  | Efficient        | Moderate      | High      | Invalid | Total Consumption | Buildings | Result                                 |
| --------- | ---------------------- | ---------------- | ------------- | --------- | ------- | ----------------- | --------- | -------------------------------------- |
| 1         | 25 30 45 120 160 40    | [25, 30, 45, 40] | [120]         | [160]     | []      | 420               | 6         | Efficient Campus / Green Hour Detected |
| 2         | 100 120 150 180 200 50 | [50]             | [100,120,150] | [180,200] | []      | 800               | 6         | Energy Waste Detected                  |


📚 Learning Outcome
Through this project, I learned how to apply core Python concepts such as lists, dictionaries, tuples, loops, conditional statements, and list comprehension to analyze and classify data. This exercise also helped improve my logical thinking and problem-solving skills while building a simple real-world analysis program.
