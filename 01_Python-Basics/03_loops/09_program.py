# Check if all items in loop are unique,if duplicate is found print it and exit the loop.

items = ["apple", "banana", "orange", "apple", "mango"] 

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate :",item)
        break
    else:
        unique_item.add(item)
        
