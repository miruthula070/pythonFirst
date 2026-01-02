import random

find_number = random.randint(1, 100)
while True:
    try:
        number = int(input("Guess the number between 1 and 100:"))
        if number == find_number:
            print("Congratulations! You guessed the number.")
            break
        elif 1 <= number < find_number:
            print("Too low!")
        elif find_number < number <= 100:
            print("Too high!")
        else:
            print("Please enter the valid number!")

    except ValueError:
        print("Please enter the valid number!")
