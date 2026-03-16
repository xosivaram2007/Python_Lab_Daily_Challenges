data=input("Enter the energy readings: ")
values=data.split()
reading=[]
for v in values:
    reading.append(int(v))
table = {
    "efficient":[],
    "moderate":[],
    "high":[],
    "invalid": []
}
for i in reading:
    if i<0:
        table["invalid"].append(i)
    elif i<=50:
        table["efficient"].append(i)
    elif i<=150:
        table["moderate"].append(i)
    else:
        table["high"].append(i)
valid=[x for x in reading if x>=0]
total=sum(valid)
buildings=len(reading)
summary=(total, buildings)
if len(table["high"])>3:
    result="Overconsumption"
elif abs(len(table["efficient"])-len(table["moderate"])) <=1:
    result="Balanced Usage"
elif total>600:
    result="Energy Waste Detected"
else:
    result="Efficient Campus"
green=False
for i in range(len(reading)-2):
    if reading[i]<=50 and reading[i+1]<=50 and reading[i+2]<=50:
        green=True
        break
if green:
    result+="/ Green Hour Detected !!"
print("\n=====ENERGY REPORT=====")
print("Efficiency:", table["efficient"])
print("Moderate:", table["moderate"])
print("High:", table["high"])
print("Invalid:", table["invalid"])
print("Total Consumption:", summary[0])
print("Number of Buildings:", summary[1])
print("Efficiency Result:", result)
print("===========")

