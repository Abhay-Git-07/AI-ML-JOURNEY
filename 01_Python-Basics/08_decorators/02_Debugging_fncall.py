# Create a decorator to print a fn name and values of its arguments every time the fn is called

def Ash(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs) 
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k} = {v}" for k,v in kwargs.items())
        print(f"Function name = {func.__name__} and it's args are {args_value} and kwargs are {kwargs_value} ")
        return result    
    return wrapper

@Ash
def greet(name,greeting):
    print(f"{greeting} {name}")

greet("Ash", "Hello")
greet("Ash", greeting = "Hii")    
