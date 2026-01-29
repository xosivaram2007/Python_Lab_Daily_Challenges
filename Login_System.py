user_name=str(input("Full Name:"))
email_id=str(input("Email:"))
ph_number=str(input("Mobile:"))
age=int(input("Age:"))
if user_name[0] != " " and user_name[len(user_name)-1] != " " and " " in user_name:
    if email_id[0] != "@" and email_id.count("@") == 1 and "." in email_id:
        if ph_number[0] != "0" and len(ph_number) == 10 and ph_number.isdigit():
            if 18 <=age<= 60:
                print("User Profile is VALID")
            else:
                print("User Profile is INVALID")
        else:
            print("User Profile is INVALID")
    else:
        print("User Profile is INVALID")
else:
    print("User Profile is INVALID")