print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/__________/____
*******************************************************************************''')

#NOTE : YOU CAN OBSERVE WE DON'T USED DOUBLE QUOTE AT START AND END , Rather we used triple single quote at starting and end to say it has multiple line
print("Welcome to Treasure Island! "
      " Your mission is to find the treasure in island.")
path1=input('You are currently at monkey temple near to the river valley'
            'Type "right" or "left" to Move : ').lower()  # here we learned about lower() fn whatever u type it gets convert to lower
                                                         # \ this mean escape sequence it helps to bypass the quote rule ex: ' You're at skull island "Right" or "left" 'here it raises an error because the string just got end at "you"
                                                         # To avoid that we use \ (backslash),ex: 'You\'re -----> \'re means escape from this like saying leave it
if path1 == "left":
    path2=input('You are now near to the River, Type "swim" To swim in the River, Type "wait" To wait for the Boat to travel : ').lower()
    if path2 == "wait":
        path3=input('You are now standing near the 3 magic doors inside one of the room you have the treasure other you are going to meet the death !! '
                    'Type "red" for the Red door and "yellow" for the Yellow door and "blue" for the Blue door.').lower()
        if path3 == "red":
            print("You were Burned By fire ashes, Game Over!")
        elif path3 == "yellow":
            print("You found the treasure , YOU WIN THE GAME :D HOORAY !!!")
        elif path3 == "blue":
            print("YOU WERE EATEN BY THE BEASTS")
        else:
            print("Game Over!")

    else:
        print("YOU were attacked by Sharks , Game Over! ")
else:
    print("You fall into the Hole , Game over!")




# SUMMARY: Here we learned about escape sequence (\)  and lower() function