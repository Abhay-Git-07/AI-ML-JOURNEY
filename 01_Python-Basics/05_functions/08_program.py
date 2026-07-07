#Create a fn that accepts any no of keyword arguments and prints them in the format key:value
                          # use of **kwargs or KEYWORD ARGUMNTS

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_kwargs(Name = "Ash")
print_kwargs(Name = "Ash", Pokemon = "Pikachu")
print_kwargs(Name = "Ash", Pokemon = "Pikachu", Ace_pokemon = "Greyninja")
