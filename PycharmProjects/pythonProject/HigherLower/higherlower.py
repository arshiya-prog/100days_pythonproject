import art_hl
from hl_data import data
import random

print(art_hl.logo)
first = random.choice(data)
first_followers = first["follower_count"]

second = random.choice(data)
second_followers = second["follower_count"]

score = 0
var = "y"
while var == "y":
    if first != second:
        print(f"Compare A: {first["name"]}, a {first["description"]}, from {first["country"]}")
        print(art_hl.vs)
        print(f"Against B: {second["name"]}, a {second["description"]}, from {second["country"]}\n")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if guess == "a":
            if first_followers > second_followers:
                first = second
                first_followers = first["follower_count"]

                second = random.choice(data)
                second_followers = second["follower_count"]

                score += 1
            else:
                print(f"Sorry that's wrong. Final score: {score}")
                break

        elif guess == "b":
            if first_followers < second_followers:
                first = second
                first_followers = first["follower_count"]

                second = random.choice(data)
                second_followers = second["follower_count"]

                score += 1
            else:
                print(f"Sorry that's wrong. Final score: {score}")
                break
    else:
        first = random.choice(data)
        first_followers = first["follower_count"]

        second = random.choice(data)
        second_followers = second["follower_count"]
