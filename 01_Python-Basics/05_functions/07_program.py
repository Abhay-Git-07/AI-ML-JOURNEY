# Write a fn that takes variable number of arguments and returns their sum

def sum_all(*args): #Args ki gjh kuch bhi likhdo pr * jruri hai
    print(*args)    # Prints the arguments 
    print(args)     # Prints the arguments in array form
    for i in args:
        print(i*2)
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7))
