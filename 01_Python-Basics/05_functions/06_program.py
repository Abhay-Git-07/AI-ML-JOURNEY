# Create a lambda function to compute the cube of a number

num = int(input("Enter a number : "))

cube = lambda num : num**3
print(cube(num))