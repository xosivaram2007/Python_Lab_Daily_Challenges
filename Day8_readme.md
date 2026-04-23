# 🌆 Autonomous Smart City Data Intelligence System

## 📌 Overview

This project simulates a smart city system that collects and analyzes data from multiple sources such as traffic, air quality, and energy consumption. The system processes this data to identify risk zones and determine the overall condition of the city.

---

## ⚙️ Features

* Random data simulation for multiple city zones
* Data stored using list of dictionaries
* Conversion to Pandas DataFrame
* NumPy-based analysis (mean, variance)
* Custom risk score calculation
* Zone classification (Safe, Moderate, High Risk, Energy Critical)
* Manual sorting to identify top risky zones
* Final system decision based on risk levels

---

## 🧠 Technologies Used

* Python
* Pandas
* NumPy
* Math module
* Random module

---

## 📊 Data Parameters

Each zone contains:

* Traffic (0–100)
* Air Quality Index (0–300)
* Energy Consumption (0–500)

---

## 🚦 Risk Classification

* High Risk → AQI > 200 or Traffic > 80
* Energy Critical → Energy > 400
* Safe Zone → Traffic < 30 and AQI < 100
* Moderate → All other cases

---

## 🔢 Risk Score Formula

Risk score is calculated using a custom formula:

* Traffic (35%)
* Air Quality (45%)
* Energy (20%)
* Final score is transformed using square root

---

## 🧪 Test Cases

The system includes:

* Zero traffic scenario
* Extreme pollution case
* Maximum spike values

---

## 📈 Output

The program displays:

* Complete DataFrame
* Mean values
* Top 3 risky zones
* Risk tuple (max, avg, min)
* High-risk zones
* Traffic variance
* Final system decision

---

## 🏙 Final Decision Categories

* City Stable
* Moderate Risk
* High Alert
* Critical Emergency

---

## 🎯 Personalization

* Dataset is shuffled or sorted based on roll number
* Custom risk formula implemented

---

## 📚 Learning Outcome

This project helped in understanding data simulation, analysis using Pandas and NumPy, and applying logic to detect patterns and make decisions in a smart city environment.

---

## ▶️ How to Run

```bash
python your_file_name.py
```

---

## 👤 Author

SRM University–AP
Department of Computer Science and Engineering
