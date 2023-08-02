def greet(name: str, last:str):

    var1 = (f"\n\n\n\t\t\t{name}\t\t{last}")

    print(var1.rstrip())
    print(var1.lstrip())
    print(var1.strip())

if __name__ == '__main__':
    greet("Frank", "Wheeler")