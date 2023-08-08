# Login Attempts

class User:

    def __init__(self, first, last, email, zip):

        self.first = first
        self.last = last
        self.email = email
        self.zip = zip
        self.login_attempts = 0

    def describe_user(self):

        print(f"{self.first} {self.last} {self.email} {self.zip} LoginAttempts={self.login_attempts}")

    def increment_login_attempts(self, login_attemts):

        self.login_attempts += login_attemts

    def reset_login_attempts(self):
        self.login_attempts = 0



u1 = User("Alex", "Mac", "alex.mac@me.com", 90210)
u1.describe_user()
print("-" * 50)

u1.increment_login_attempts(10)
u1.describe_user()

print("-" * 50)

u1.login_attempts = 5
u1.describe_user()
u1.increment_login_attempts(100)
u1.describe_user()
u1.reset_login_attempts()
u1.describe_user()


