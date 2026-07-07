# Check if the year is leap year

year = int(input("Enter the year:-"))

if year%400==0:
    print("Leap year")

elif (year%4==0 and year%100!=0):
    print("Leap year")

else:
    print("Not a leap year")
