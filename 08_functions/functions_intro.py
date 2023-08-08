# passing a list

from typing import List


def greet_users(names: List) -> str:

    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List a function

unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_design:
    current_design = unprinted_design.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# Passing Arbitrary Number of Arguments

def make_pizza(*toppings):
    print("\nMaking Pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza("Basil", "Tomato", "Cheese", "Onion")

# Mixing Positional and arbitrary arguments

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following.")

    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, "Tomato", "Cheese", "Onion")

# Using Arbitrary Keyword Arguments


def build_profile(first, last, **user_info):

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                           location='princeton',
                           field='physics')

print(user_profile)





