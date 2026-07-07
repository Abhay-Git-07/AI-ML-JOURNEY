# Recommend type of pet food based on pet's species and age

pet = input("What's your pet? dog or cat?:-")

age = int(input("Enter age of dog or cat:-"))
if pet == "dog":
    if age<2:
        print("Puppy food")
    else:
        print("Senior dog food")

elif pet == "cat":
    if age<2:
        print("Kitten food")
    else:
        print("Senior Cat food")
