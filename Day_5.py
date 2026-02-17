n = int(input("Enter no of elements: "))

weight = []
for i in range(n):
    weight = weight + [int(input("Enter weight: "))]

very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []
affected_weights = []

for i in range(n):
    if weight[i] < 0:
        invalid_entries = invalid_entries + [weight[i]]
    elif 0 <= weight[i] <= 5:
        very_light = very_light + [weight[i]]
    elif 6 <= weight[i] <= 25:
        normal_load = normal_load + [weight[i]]
    elif 26 <= weight[i] <= 60:
        heavy_load = heavy_load + [weight[i]]
    else:
        overload = overload + [weight[i]]

total = n - len(invalid_entries)

name = "Valluru Komal Sivaram"
print("Given name:", name)

slay = ""
for c in name:
    if c != " ":
        slay += c

L = len(slay)
PLI = L % 3

print("Length:", L)
print("PLI:", PLI)

# Apply Rules
if PLI == 0:
    affected_weights = overload
    invalid_entries = invalid_entries + overload
    overload = []
    print("Applied Rule A")

elif PLI == 1:
    affected_weights = very_light
    very_light = []
    print("Applied Rule B")

else:
    affected_weights = very_light + overload
    very_light = []
    overload = []
    print("Applied Rule C")

print("Loading Plan")
print("Very Light:", very_light)
print("Normal Load:", normal_load)
print("Heavy Load:", heavy_load)
print("Overload:", overload)
print("Invalid Entries:", invalid_entries)
print("Total weights which are valid:", total)
print("Affected Number Of Items Due To PLI:", len(affected_weights))
print("Affected Elements:", affected_weights)
