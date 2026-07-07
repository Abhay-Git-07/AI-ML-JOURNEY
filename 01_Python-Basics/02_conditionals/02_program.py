# To do ticket pricing on the basis of age 12$ for adults and over,8$ for children,
# everyone gets a 2$ discount on wednesday..

age = int(input("Enter your age:"))
day = input("Enter the week day:")

price = 12 if(age>=18) else 8
if day =="wednesday":
    price = price - 2

print("Ticket price is $",price)

