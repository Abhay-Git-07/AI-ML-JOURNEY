#Divide different age groups in child,teenager,adult and senior.

age = int(input("Provide the age :"))
if (age<13):
    print("You are a child")

elif (age<20):
    print("You are a teenager")

elif(age<60):
    print("You are an adult")

else:
    print("You are a senior")
