#Keep asking for input from user untill they enter a number b/w 1 and 10

while True:
    num = int(input("Enter a number b/w 1 and 10 :-"))
    if num>=1 and num<=10:
        print("Thanks")
        break
    else:
        print("Invalid no try again")    
