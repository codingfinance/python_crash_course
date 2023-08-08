pizza = ['cheese', 'vegan', 'vegeterian']

pizza2 = pizza

pizza3 = pizza[:]

print(pizza)
print(pizza2)
print(pizza3)

pizza2.append('margherita') # This will change the original pizza list
pizza3.append('lactose')

print(pizza)
print(pizza2)
print(pizza3)