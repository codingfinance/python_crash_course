# Restaurant

class Restaurant:

    def __init__(self, name: str, cuisine: str):

        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):

        print(f"The {self.name} restaurant serves {self.cuisine} food!")

    def open_restaurant(self, status: bool):

        if status:
            print(f"The {self.name} restaurant is open!")

        else:
            print(f"The {self.name} restaurant is closed!")


def main():
    r1 = Restaurant("Nico", "Greek")

    print(r1.name)
    print(r1.cuisine)
    r1.describe_restaurant()
    r1.open_restaurant(status=False)


if __name__ == '__main__':
    main()
