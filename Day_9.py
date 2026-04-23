import copy
def generate_data():
    return [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]
def replicate_data(data):
    assigned = data
    shallow = data[:]
    deep = copy.deepcopy(data)
    return assigned, shallow, deep
def modify_data(data, roll):
    for user in data:
        if roll % 2 == 0:
            user["data"]["files"].append(f"extra_{user['id']}.txt")
        else:
            if user["data"]["files"]:
                user["data"]["files"].pop()
        user["data"]["usage"] += 100
def check_integrity(original, shallow, deep):
    leakage = 0
    safe = 0
    overlap = 0
    for i in range(len(original)):
        if original[i]["data"] != deep[i]["data"]:
            leakage += 1
        if deep[i]["data"] != shallow[i]["data"]:
            safe += 1
        s1 = set(original[i]["data"]["files"])
        s2 = set(shallow[i]["data"]["files"])
        overlap += len(s1 & s2)
    return (leakage, safe, overlap)
roll=764
original = generate_data()
assigned, shallow, deep = replicate_data(original)
print("Before:", original)
modify_data(shallow, roll)
print("\nOriginal:", original)
print("\nShallow:", shallow)
print("\nDeep:", deep)
result = check_integrity(original, shallow, deep)
print("\nResult:", result)