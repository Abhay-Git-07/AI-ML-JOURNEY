# reverse a string using a loop

string = str(input("Enter your string:-"))
reversed_str = ""

for char in string:
    reversed_str = char + reversed_str

print(reversed_str)
    