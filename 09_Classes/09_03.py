# Users

class Users:

    def __init__(self, first: str, last: str, email: str, zip: int):

        self.first: str = first
        self.last: str = last
        self.email: str = email
        self.zip: int = zip


    def describe_user(self):

        print(f"""The User's name is {self.first} {self.last}. 
The User's email address is {self.email}.
The User's zip code is {self.zip}.""")


u1 = Users("Tom", "Hanks", "tom.hanks@me.com", "90210")

u1.describe_user()


