"""A number-guessing game."""

# Put your code here
import random
name = input("What is your name? ")
print("Hello, {}".format(name))
print("{}, I'm thinking of a number between 1 and 100".format(name))
print("Try to guess my number: ")
random_num = random.randint(1, 100)
count = 0
while True:
    guess = int(input("Your guess: "))
    if guess != random_num:
        count += 1
        if guess > random_num:
            print("Your number is too high, try again")
        elif guess < random_num:
            print("Your number is too low, try again")
    else:
        print("Well done, {}! You found my number in {} tries.".format(name, count))
        break
