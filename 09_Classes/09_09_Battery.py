# Battery Upgrade

class Car:

    def __init__(self, make: str, model: str, year: int):

        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):

        print(f"{self.year} {self.make.title()} {self.model.title()}.")

class Battery:
    def __init__(self, battery_size: int):
        self.battery_size: int = battery_size

    def get_range(self):
        if self.battery_size == 45:
            self.battery_range = 150
            print(f"The car's battery range is {self.battery_range}.")
        elif self.battery_size == 65:
            self.battery_range = 225
            print(f"The car's battery range is {self.battery_range}.")
        else:
            print("Enter a battery size of either 45 or 65 kWh.")

class ElectricCar(Car):

    def __init__(self, make:str, model: str, year: int):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery_size = Battery(battery_size = 45)

    def upgrade_battery(self):
        if self.battery_size.battery_size != 65:
            self.battery_size.battery_size = 65

c1 = Car("ford", "f1", 2020)
e1 = ElectricCar("tesla", "cybertruck", "2024")
e1.describe_car()
e1.battery_size.get_range()
e1.upgrade_battery()
e1.battery_size.get_range()
