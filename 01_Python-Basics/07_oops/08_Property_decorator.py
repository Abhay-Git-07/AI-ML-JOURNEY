# Use the property decorator in the class to make the model attribute read only

class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.brand = brand
        self.__model = model
        Car.total_car += 1     

    def full_name(self):
        return f"{self.brand} {self.__model}" 
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @property            # YE use krenge agr kisi ki value fix rkhni ho to
    def model(self):
        return self.__model

class Electric_Car(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size 

    def fuel_type(self):
        return "Electric Charge"
    
my_car = Car("Tata", "Safari")
#my_car.model = "City"               # Hum chate hai modal ki value ab change na ho 
print(my_car.model)
