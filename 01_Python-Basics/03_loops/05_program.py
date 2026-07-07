# Find the first non repeated character of a string

string = str(input("Enter a string:-"))

for char in string:
    print(char)
    if string.count(char)==1:
        print("1st non repeated character is:-",char)
        break
    