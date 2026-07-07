#Assign grages on the basis of marks:-
#A(90-100),B(80-89),C(70-79),D(60-69),E(Below 60)

marks = float(input("Enter your marks:"))
if (marks>100):
    print("Wrong Marks entered")
    exit()

if (marks>=90):
    print("Your grade is A") 

elif (marks>=80):
    print("Your grade is B")

elif (marks>=70):
    print("Your grade is C")

elif (marks>=60):
    print("Your grade is D")

else:
    print("Your grade is E")  
