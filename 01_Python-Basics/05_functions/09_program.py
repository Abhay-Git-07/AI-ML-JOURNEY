# Write a generator fn that yeilds even numbers upto a specified limit

limit = int(input("Enter a number : "))
def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield(i)

for num in even_generator(limit):
    print(num)
