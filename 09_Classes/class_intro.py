class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initializ name and age attributes"""

        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""

        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""

        print(f"{self.name} rolled over.")


class Car:

    def __init__(self, make: str, model: str, year: int):
        """Initialize a attributes to describe a car."""

        self.make: str = make
        self.model: str = model
        self.year: int = year

        self.odometer = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name: str = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer} miles on it.")

    def update_odometer(self, mileage):

        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print(f"You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""

        self.odometer += miles


# Inheritance
# Inherit Electric Car from Car class

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            battery_range = 150
        elif self.battery_size == 65:
            battery_range = 225

        print(f"This car can go about {battery_range} miles on full charge.")


class ElectriCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print(f"This car doesn't have a gas tank!")


elec_car = ElectriCar("tesla", "roadster", 2008)
elec_car.battery.describe_battery()
elec_car.battery.get_range()