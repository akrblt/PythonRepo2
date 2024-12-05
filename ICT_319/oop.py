class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True

class Driver:
    def __init__(self, name):
        self.name = name

    def take_vehicle(self, vehicle):
        if vehicle.is_running:
            raise Exception("The vehicle is not available for a ride.")
        vehicle.start()

# Example usage:
car = Vehicle("Toyota", "Corolla")
car1=Vehicle("Toyota","Prius")
car2=Vehicle("Honda","Insight")
car3=Vehicle("Honda","Civic ")
driver = Driver("Alice")
driver1=Driver("Tom")
driver2=Driver("Jerry")
driver3=Driver("Barny ")

# The driver takes the vehicle and starts it
driver.take_vehicle(car)

# Testing the behavior when trying to take the same vehicle again
try:
    driver.take_vehicle(car)
except Exception as e:
    print(e)  # Output: "The vehicle is not available for a ride."