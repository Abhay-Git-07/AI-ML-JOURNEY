# Create a fn that returns both area and circumference of a circle ,radius given

import math
radius = int(input("Enter the radius of circle : "))

def circle_stats(radius):
    area = math.pi * radius*radius
    circumference = 2 * math.pi * radius
    return area,circumference

a,c = circle_stats(radius)
print("Area : ",a  ,"Circumference : ",c)