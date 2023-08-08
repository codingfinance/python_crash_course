pizza = ['basil', 'tomato', 'onion']
pizza2 = ['vegeterian', 'cheese', 'margerita']

if __name__ == '__main__':
    for i in pizza:
        print(f"I love {}i)

    for i in range(len(pizza2)):
        print(f"I love {pizza2[i].title()} pizza!")