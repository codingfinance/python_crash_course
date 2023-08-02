def greet(first: str, last: str) -> str:

    print(f"Hello {first.lower()} {last.lower()}")

    print(f"Hello {first.upper()} {last.upper()}")

    print(f"Hello {first.title()} {last.title()}")


if __name__=='__main__':
    greet(first="Kaa", last="Tail")