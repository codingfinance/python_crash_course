# Privileges

class User:

    def __init__(self, first: str, last: str, email: str, zipcode: int):
        self.first: str = first
        self.last: str = last
        self.email: str = email
        self.zipcode: int = zipcode

    def describe_user(self):
        print(f"The User has following attributes.\n"
              f"Name: {self.first} {self.last}\n"
              f"Email: {self.email}\n"
              f"Zipcode: {self.zipcode}")


class Privileges:

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"The Admin has the following privileges")

        for i in self.privileges:
            print(f"{i}")


class Admin(User):

    def __init__(self, first: str, last: str, email: str, zipcode: int):
        super(Admin, self).__init__(first, last, email, zipcode)

        self.privileges = Privileges()


u1: User = User("Tom", "Hanks", "th@me.com", zipcode=90210)
u1.describe_user()

a1: Admin = Admin("Joe", "Biggs", "jb@me.com", zipcode=90210)

a1.privileges.show_privileges()
