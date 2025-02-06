import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play = input("Do you want to play a game of blackjack? 'y' or 'n': ")

def pick_card():
    return random.choice(cards)

while play == "y":
    your_cards = []
    comp_cards = []
    for i in range(2):
        your_cards.append(pick_card())
        comp_cards.append(pick_card())
    your_score = sum(your_cards)
    print("Your cards: ", your_cards, "current score: ", your_score)
    comp_score = sum(comp_cards)
    print("Computer's first card: ", comp_cards[1])

    while comp_score < 17:
        card = random.choice(cards)
        comp_cards.append(card)
        comp_score = sum(comp_cards)

    another_card = "y"
    while another_card == "y":
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            card = random.choice(cards)
            your_cards.append(card)
            your_score = sum(your_cards)
            print("Your cards: ", your_cards, ",current score: ", your_score)
            print("Computer's first card: ", comp_cards[1])
            if 11 in your_cards:
                if your_score > 21:
                    your_cards.remove(11)
                    your_cards.append(1)
                    your_score = sum(your_cards)
            if your_score > 21:
                print("You went over. You lose! 😭")
                play = "n"
                break
        else:
            print("Your final hand: ", your_cards, ",final score: ", your_score)
            print("Computer's final hand: ", comp_cards, ",final score: ", comp_score)
            play = "n"
            if comp_score > 21:
                print("You win!")
            elif your_score == comp_score:
                print("Draw 🙃")
            elif your_score < comp_score <= 21:
                print("You lose!")
            elif comp_score < your_score <= 21:
                print("You win!")
