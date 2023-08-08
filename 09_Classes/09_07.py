# Admin

class User:

    def __init__(self, first: str, last: str, email: str, zip: int):

        self.first = first
        self.last = last
        self.email = email
        self.zip = zip

    def describe_user(self):

        print(f"The user has following attributes:\n"
              f"Name: {self.first} {self.last}\n"
              f"Email: {self.email}\n"
              f"ZipCode: {self.zip}")

class Admin(User):

    def __init__(self, first: str, last: str, email: str, zipcode: int):

        super().__init__(first, last, email, zipcode)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):

        for i in self.privileges:
            print(f"The Admin {self.first} {self.last} {i}.")

u1 = User("Tom", "Hanks", "th@me.com", 90210)
a1 = Admin("Joe", "Hanks", "jh@me.com", 90210)

u1.describe_user()
a1.show_privileges()
