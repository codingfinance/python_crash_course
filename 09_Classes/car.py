"""A clas that can be used to represent a car."""

class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self.odometer_reading: int = 0

    def get_descriptive_name(self):
        long_name: str = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"The car has {self.odometer_reading} miles on it.")

    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You cannot roll back the odometer.")

    def increment_odometer(self, miles_added):
        self.odometer_reading += miles_added

class Battery:
    def __init__(self, battery_size = 40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            battery_range = 150
        elif self.battery_size == 65:
            battery_range = 225
        else:
            print("Please enter 40 or 65 for battery range.")

        print(f"This car can go about {battery_range} miles on a full charge.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)

        self.battery = Battery()
