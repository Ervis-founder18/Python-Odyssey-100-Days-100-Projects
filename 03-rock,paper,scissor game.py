import random
print("Welcome to rock paper scissors game")
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
          )

user_input=int(input("CHOOSE WHT U WANT press 0 for rock, 1 for paper, 2 for scissors : \n"))
choice1=[rock,paper,scissors]
computer_choice=random.choice(choice1)

if user_input==0:
    print(rock)
    print("Computer choice :",computer_choice)
    if computer_choice==rock:
        print("Game is TIE ")
    elif computer_choice==paper:
        print("You lose")
    elif computer_choice==scissors:
        print("You win")
elif user_input==1:
    print(paper)
    print("Computer choice :", computer_choice)
    if computer_choice==paper:
        print("Game is TIE ")
    elif computer_choice==scissors:
        print("You lose")
    elif computer_choice==rock:
        print("You win")
elif user_input==2:
    print(scissors)
    print("Computer choice :", computer_choice)
    if computer_choice==scissors:
        print("Game is TIE ")
    elif computer_choice==rock:
        print("You lose")
    elif computer_choice==paper:
        print("You win")
else:
    print("Invalid choice")
