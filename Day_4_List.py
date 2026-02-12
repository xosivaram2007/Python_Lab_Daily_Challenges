slay = input("Enter elements of the list: ")
data = []
word = ""
for ch in slay:
    if ch != " ":
        word = word + ch
    else:
        data = data + [word]
        word = ""
data = data + [word]
num = []
str = []
num_count = 0
str_count = 0
reg_no=input("Enter your registration number: ")
last_digit = 0
for ch in reg_no:
    if ch >= '0' and ch <= '9':
        last_digit=int(ch)
for item in data:
    if item != "":
        if item[0] >= '0' and item[0] <= '9':
            num=num +[int(item)]
            num_count=num_count + 1
        else:
            str= str+[item]
            str_count=str_count+1
if last_digit % 2 == 0:
    num=num[::-1]
else:
    str=str[::-1]
print("Output:")
print("Number List:", num)
print("String List:", str)
print("Total Numbers:", num_count)
print("Total Strings:", str_count)
