def blackjack():




    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_cards = random.choices(cards, k=2)
    computer_cards = random.choices(cards, k=2)   # look for notes and i searched this on google and learned

    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    print(f"YOUR CARDS ARE : {user_cards}, Your Current Score :{user_score}")
    print(f"Computer First Card : {computer_cards[0]}")
    #------------------------------------------------------------------------------------- (From here onward follow flowchart+solution output reference i solved)
    # 1) Check Black-Jack

    if 11 in user_cards and 10 in user_cards:
        print("USER HAS BLACK JACK, You win")

    elif 11 in computer_cards and 10 in computer_cards:
        print("COMPUTER HAS BLACK JACK, You Lose")

    else:

        # 2) User Ace handling for initial cards

        while user_score > 21 and 11 in user_cards:
            user_score = user_score - 10


        # 3) User plays

        while user_score < 21:

            ask = input("Do u want to get another card? (y/n) (Hit/Stand): ").lower()

            if ask == "y":

                new_card = random.choice(cards)
                user_cards.append(new_card)
                user_score = sum(user_cards)
                print(f"Your Cards {user_cards}, Current Score :{user_score}") # written on my own

                # Ace handling after getting a new card

                while user_score > 21 and 11 in user_cards:
                    user_score = user_score - 10

            elif ask == "n":
                print(f"Your final hand: {user_cards}, Final Score :{user_score}")

                break


        # 4) Check if user lost

        if user_score > 21:

            print("YOU LOSE")

        else:

            # 5) Computer draws while score is less than 17

            while computer_score < 17:

                new_comp_card = random.choice(cards)
                computer_cards.append(new_comp_card)
                computer_score = sum(computer_cards)
                print(f"Computer's First Card : {computer_cards[0]}")
                # Computer Ace handling

                while computer_score > 21 and 11 in computer_cards:
                    computer_score = computer_score - 10
            print(f"Computer final hand: {computer_cards}, Final Score :{computer_score}")

            # 6) Final result

            if computer_score > 21:
                print("YOU WIN")

            elif user_score > computer_score:
                print("YOU WIN")

            elif computer_score > user_score:
                print("COMPUTER WIN")

            else:
                print("DRAW")

#-----------------------------------------------------------------------------------------------
import art
import random

opening = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if opening == "y":
    print("\n" * 20)
    print("Welcome to Blackjack Game :) ")
    print(art.logo)
    blackjack()

# Fully own logic and code is written by me, i just referred to flowchart and solution output reference to understand the logic and then i wrote my own code and logic