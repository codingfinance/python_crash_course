# Numbers Served

class Restaturant:

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

        self.numbers_served = 0

    def describe_restaurant(self):
        print(f"{self.name} {self.cuisine} restaurant has served: {self.numbers_served} customers.")

    def set_numbers_served(self, customers):

        self.numbers_served = customers

    def increment_number_served(self, customers):

        self.numbers_served += customers


r1 = Restaturant("Nico", "Greek")
r1.numbers_served = 10
r1.describe_restaurant()

print("-" * 50)

r1.set_numbers_served(100)
r1.describe_restaurant()

print("-" * 50)

r1.set_numbers_served(100)
r1.describe_restaurant()
r1.increment_number_served(20)
r1.describe_restaurant()

