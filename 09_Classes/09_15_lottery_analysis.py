# Lottery
from random import choice

options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = ['a', 'c', 2, 6]
counter = 0
while True:
    counter += 1
    lottery_result = []

    for i in range(4):

        pick1 = choice(options)
        lottery_result.append(pick1)
    if set(my_ticket) == set(lottery_result):
        break

print(f"Your ticket {my_ticket} matche in {counter} attempts.")
