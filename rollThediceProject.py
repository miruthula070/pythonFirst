import random

while True:
    get_input_from_user = input("Roll the dice? (y/n):")
    if get_input_from_user.lower() == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1},{die2})")

    elif get_input_from_user.lower() == "n":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice!")
