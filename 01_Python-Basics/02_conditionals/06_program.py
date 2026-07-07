#Choose mode of transportation based on distance

dis = int(input("Enter the distance:-"))
if(dis<3):
    print("Take a walk")

elif(dis<15):
    print("Go by a bike")

elif(dis>=15):
    print("Go by a car")

else:
    print("Wrong distance entered")
                