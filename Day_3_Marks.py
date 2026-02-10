number=int(input("Enter number of students: "))
marks=[]
for i in range(number):
    mark=int(input("Enter marks: "))
    marks=marks+[mark]
count=0
fail=0
name="Sivaram"
name_len=0
for ch in name:
    name_len=name_len+1
print("\nResults:")
for n in range(number):
    mark=marks[n]
    if mark<0 or mark>100:
        print(mark, "→ Invalid")
    elif mark==39 and name_len%2!=0:
        print(mark, "→ Border pass")
        count=count+1
    elif mark>=90:
        print(mark, "→ Excellent")
        count=count+1
    elif mark>=75:
        print(mark, "→ Very Good")
        count=count+1
    elif mark>=60:
        print(mark, "→ Good")
        count=count+1
    elif mark>=40:
        print(mark, "→ Not Bad")
        count=count+1
    else:
        print(mark, "→ Fail")
        count=count+1
        fail=fail+1
print("Overview")
print("Total no of Valid Students: ", count)
print("Total no of Failed Students: ", fail)
