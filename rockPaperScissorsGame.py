import random

choices = ("r", "p", "s")

while True:
    guess = input("Rock, paper, or scissors? (r/p/s):").lower()

    if guess not in choices:
        print("invalid choice")
        continue 
    com_guess = random.choice(choices)
    print("User guess:", guess)
    print("Computer guess:", com_guess)

    if com_guess == guess:
        print("Draw match")
    elif (com_guess == "r" and guess == "p") or ( com_guess == "s" and guess == "r") or (com_guess == "p" and guess == "s"):
        print("You win")
    elif (com_guess == "p" and guess == "r") or (com_guess == "r" and guess == "s") or (com_guess == "s" and guess == "p"):
        print("You lose")
    else:
        print("Invalid choice!")

    statement = input("Continue or Skip(c/s):").lower()
    if statement == "c":
        continue
    elif statement == "s":
        break
    else:
        print("Invalid choice")   

        
    
    
    
    
        
    
    
