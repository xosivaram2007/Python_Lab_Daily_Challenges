n = int(input("Enter no of elements: "))

weight = []
for i in range(n):
    weight = weight + [int(input("Enter weight: "))]

very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []

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

print("Very Light:", very_light)
print("Normal Load:", normal_load)
print("Heavy Load:", heavy_load)
print("Overload:", overload)
print("Invalid Entries:", invalid_entries)
