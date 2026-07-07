# Write a fn that greets a user.If no name is provided it should greet with a random name

def greet(name = "User"):
    return "Hello " + name+"!"

print(greet("Abhay"))

print(greet())