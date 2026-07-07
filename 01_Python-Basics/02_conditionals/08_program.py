#Check if password is weak,medium or strong

password = input("Enter password :-")
pass_len = len(password)

if pass_len<6:
    print("Weak password")

elif pass_len<=10:
    print("Medium password")

else:
    print("Strong password")
            