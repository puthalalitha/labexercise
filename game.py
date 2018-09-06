"""A number-guessing game."""

# Put your code here
import random
name = input("What is your name? ")
print("Hello, {}".format(name))
print("{}, I'm thinking of a number between 1 and 100".format(name))
print("Try to guess my number: ")
def guessing_game():
    random_num = random.randint(1, 5)
    count = 0
    score = []
    while True:
        guess = input("Your guess between 1 - 100: ")

        
        if not guess.isdigit():
            print("Enter  a number only ")
            continue

        guess = int(guess)

        if guess not in range(1,5):

            print("Enter a valid number: ")
            continue
       
        elif guess != random_num:
            
            if guess > random_num:
                print("Your number is too high, try again")

            elif guess < random_num:
                print("Your number is too low, try again")

        elif guess == random_num:
            print("Well done, {}! You found my number in {} tries.".format(name, count))
            again = input("You want to play again?:")
            score.append(count)
            print(score)

            if again.startswith("y"):
                guessing_game()
                
                # score.append(count)
                # print(score)
                # count = 0

            else:
                break
        
        count += 1
    # print(score)
guessing_game()
