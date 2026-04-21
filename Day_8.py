import random
import pandas as pd
import numpy as np
import math
def make_data():
    d = []
    for i in range(1, 18):
        temp = {
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        }
        d.append(temp)
    d.append({"zone": 18, "traffic": 0, "air_quality": 40, "energy": 120})
    d.append({"zone": 19, "traffic": 95, "air_quality": 270, "energy": 430})
    d.append({"zone": 20, "traffic": 100, "air_quality": 300, "energy": 500})
    return d
def cat(z):
    if z["air_quality"] > 200 or z["traffic"] > 80:
        return "High Risk"
    elif z["energy"] > 400:
        return "Energy Critical"
    elif z["traffic"] < 30 and z["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"
def risk(z):
    s = (z["traffic"] * 0.35 + z["air_quality"] * 0.45 + z["energy"] * 0.2)
    return math.sqrt(s)
def sort_it(x):
    for i in range(len(x)):
        for j in range(len(x) - 1):
            if x[j]["risk_score"] < x[j + 1]["risk_score"]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x
def decide(a):
    if a < 10:
        return "City Stable"
    elif a < 15:
        return "Moderate Risk"
    elif a < 20:
        return "High Alert"
    else:
        return "Critical Emergency"
data = make_data()
roll = 764
if roll % 3 == 0:
    random.shuffle(data)
else:
    data = sorted(data, key=lambda k: k["traffic"])
for i in data:
    i["category"] = cat(i)
    i["risk_score"] = risk(i)
df = pd.DataFrame(data)
arr = df[["traffic", "air_quality", "energy"]].values
mean = np.mean(arr, axis=0)
sorted_data = sort_it(data.copy())
top = sorted_data[:3]
r = df["risk_score"].values
mx = np.max(r)
av = np.mean(r)
mn = np.min(r)
tup = (mx, av, mn)
th = 18
high = df[df["risk_score"] > th]
var = np.var(df["traffic"])
res = decide(av)
print(df)
print("\nmeans:", mean)
print("\ntop 3:")
for i in top:
    print(i)
print("\ntuple:", tup)
print("\nhigh risk:")
print(high)
print("\nvar:", var)
print("\nfinal:", res)