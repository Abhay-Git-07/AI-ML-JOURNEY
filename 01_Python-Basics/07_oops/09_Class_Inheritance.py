# Demonstrate the use of isinstance() to check if my_ElectricCar is an instance of Car and ElectricCar

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_car += 1     

    def full_name(self):
        return f"{self.brand} {self.model}" 
    
    def fuel_type(self):
        return "Petrol or Diesel"

class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size 

    def fuel_type(self):
        return "Electric Charge"
    
my_ElectricCar = Electric_Car("Tesla", "S", "85kWh")
print(isinstance(my_ElectricCar,Electric_Car))
print(isinstance(my_ElectricCar,Car))  # THis checks and give True or Flase after checking





#print(my_ElectricCar.fuel_type())

# my_car = Car("Tata", "Safari")
# print(my_car.fuel_type())
# print(Car.total_car)