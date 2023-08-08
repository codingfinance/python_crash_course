# Ice Cream Stand

class Restaurant:

    def __init__(self, name, cuisine):

        self.name = name
        self.cuisine = cuisine

class IceCreamStand(Restaurant):

    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        self.flavors = ['Vanilla', 'Mango', 'Strawberry', 'Walnut']

    def show_flavors(self):

        for i in self.flavors:
            print(f"The Ice Cream Restaurant {self.name} has {i} flavor.")

ice1 = IceCreamStand(name="Wally's", cuisine="Ice Cream")

ice1.show_flavors()

