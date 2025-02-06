import random
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.choice(range(1, 101))
num = 0

if difficulty == "easy":
    turns = 10
else:
    turns = 5
while turns != 0 or num != number:
    num = int(input("Make a guess: "))
    if num > number:
        print("Too high!")
        turns = turns - 1
        print(f"You have {turns} attempts remaining to guess the number.")
    elif num < number:
        print("Too low!")
        turns = turns - 1
        print(f"You have {turns} attempts remaining to guess the number.")
    elif num == number:
        print(f"You got it! The answer was {num}")
        break
