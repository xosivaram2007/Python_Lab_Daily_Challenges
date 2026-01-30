student_id=input("ID: ")
email_id=input("Email: ")
password=input("Password: ")
ref=input("Referral: ")
choice = True
if len(student_id)!=7:
    choice = False
elif student_id[0:3]!="CSE":
    choice = False
elif student_id[3]!="-":
    choice = False
elif student_id[4:7].isdigit()==False:
    choice = False
if choice:
    if "@" in email_id and "." in email_id==False:
        choice = False
    elif email_id[0]=="@" or email_id[-1]=="@":
        choice = False
    elif email_id.endswith(".edu")==False:
        choice = False
if choice:
    if len(password)<8:
        choice = False
    elif password[0].isupper()==False:
        choice = False
    elif password[0].isdigit()==False and password[1].isdigit()==False and password[2].isdigit()==False and password[3].isdigit()==False and password[4].isdigit()==False and password[5].isdigit()==False and password[6].isdigit()==False and password[7].isdigit()==False:
        choice = False
if choice:
    if len(ref)!=6:
        choice = False
    elif ref[0:3]!="REF":
        choice = False
    elif ref[3:5].isdigit()==False:
        choice = False
    elif ref[-1]!="@":
        choice = False
if choice:
    print("APPROVED")
else:
    print("REJECTED")

