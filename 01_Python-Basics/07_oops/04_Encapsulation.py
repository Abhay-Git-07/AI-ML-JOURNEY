# Modify the Car class to encapsulate the brand attribute,making it private,
                    # and provide a getter method for it

class Car:
    def __init__(self,brand,model):
        self.__brand = brand       # Yha __ lgane se ye private ho gya(Isko class ke andr access kr skte hain pr bahar nhi)
        self.model = model     
                                                    
    def get_brand(self):            #Ye hai getter method bahar access krne ke liye get_brand use kr lenge
        return self.__brand + "!"
                                                    
    def full_name(self):
        return f"{self.__brand} {self.model}"    #Hr gjh __brand use ho gya hai class ke andr kyuki wrna access nhi kr payenge

class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size  

my_tesla = Electric_Car("Tesla", "Model S", "85kWh")

#print(my_tesla.brand)              #Ye dikhane ke liye ki ab access nhi kr pare hain
print(my_tesla.get_brand())



# Just to understand something better myself


# class bike:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def double_name(self):
#         return self.brand*2

# class ElecrticBike(bike):
#     def __init__(self,brand,model,cc):
#         super().__init__(brand,model)
#         self.cc = cc

# my_bike = ElecrticBike("Pulsar", "2021", "150")
# print(my_bike.brand) 
# print(my_bike.model)   
# print(my_bike.cc)  
# print(my_bike.double_name())  