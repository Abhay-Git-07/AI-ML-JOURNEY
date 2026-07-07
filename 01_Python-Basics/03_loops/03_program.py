# Print multiplication table of a given no upto 10,skip the 5th iteration

num = int(input("Enter the number to print it's table:-"))

for i in range(1,11):
    if i == 5:     #pucha kyuki jruri tha
        continue   #ye particular condition ko loop se skip krwa dega
    print(num,"x",i,"=",num*i)
