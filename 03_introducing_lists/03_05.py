guests = ['Ben', 'Tom', 'Alex']

if __name__ == '__main__':
    for i in range(len(guests)):
        print(f"Hello {guests[i]}, can you come to the house party on August 2nd in Washington!")

    print(f"The invited guest list is {guests}")

    print(f"Unfortunately {guests[1]} cannot come to the party.")
    guests.remove('Tom')

    print("Hello Cindy!, can you come to the house party on August 2nd in Washington!")

    guests.insert(1, 'Cindy')

    print(f"The new guest list is {guests}.")

