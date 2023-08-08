class Restaurant:

    def __init__(self, name, cuisine):

        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):

        print(f"{self.name} restaurant serves {self.cuisine} food!")

    def open_restaurant(self, status: bool):

        if status:

            print(f"{self.name} restaurant is now open!")

        else:
            print(f"{self.name} restaurant is now closed!")

r1 = Restaurant("Nico", "Greek")
r2 = Restaurant("Amore", "Italian")
r3 = Restaurant("The Great Wall", "Chinese")

r_list = [r1, r2, r3]

[i.describe_restaurant() for i in r_list]