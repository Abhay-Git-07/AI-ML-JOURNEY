# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes,
                    # but with different behaviours.

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

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
    
my_car = Car("Tata", "Safari")
print(my_car.fuel_type())

my_ElectricCar = Electric_Car("Tesla", "S", "85kWh")
print(my_ElectricCar.fuel_type())
