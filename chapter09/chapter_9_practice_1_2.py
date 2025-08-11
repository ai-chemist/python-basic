class User:
    """User class docstring"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = ''
        self.login_attempts = 0

    def describe_user(self):
        self.full_name = self.first_name + ' ' + self.last_name
        print(self.full_name)

    def greet_user(self):
        print(f"Hello {self.full_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_0 = User("Apple", "mac")
user_1 = User("Bob", "Smith")

user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

# practice 9-5
user_2 = User("Adam", "Roses")

print(user_2.login_attempts)

user_2.increment_login_attempts()
print(user_2.login_attempts)

user_2.increment_login_attempts()
print(user_2.login_attempts)

user_2.increment_login_attempts()
print(user_2.login_attempts)

user_2.increment_login_attempts()
print(user_2.login_attempts)

user_2.reset_login_attempts()
print(user_2.login_attempts)