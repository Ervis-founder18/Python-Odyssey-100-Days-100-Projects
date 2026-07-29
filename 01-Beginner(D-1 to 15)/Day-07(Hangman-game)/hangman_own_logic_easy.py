# Step-0: Bring the necesary modules and files to the main file.
import random
import hangman_words 
import hangman_art
print(hangman_art.logo)

#------------------------------------------------ Step-1:Put a necessary input and basic word generation from computer side.

word_list = hangman_words.word_list
choose_word=random.choice(word_list)
print(choose_word)


lives=6
#--------------------------------------------------- step-2: (Create a "_" for each letter in the chosen_word and display it to the user.)

placeholder = ""
word_length = len(choose_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

#----------------------------------------- Step-3: Create a while loop to let the user guess the word until he/she runs out of lives or guesses the word correctly.
game_over=False
correct_words=[] # Counter variable we use as list form . To restore the correct word we guessed , otherwise that will be remain a blank and each time it disappear so only we append them(add them) on list to restore again and again and we can use that list to check if the letter is already guessed or not. and print upto date correct words
while not game_over: # As long as game is true.
    print("****************************",lives,"/6 LIVES LEFT****************************")
    guess=input("Guess a word:").lower() #guess again and agian until game finishes we put end condition like game_over=True where the game ends.
    if guess in correct_words:                # Extra to let the user know if he/she has already guessed the letter.we dont need to take lives here just to let them know they already choosen so they cant choose the smae word again like the same hangman game where if i presses "v"that get crossed out agin i cant touch the "V" again
        print("You already guessed this letter: " ,guess)
#---------------------------------------------------------------
    display = ""  # Step-4: Its time to fill that "_" with the correct letter that they typed and also we need to reflect at every correct blanck that needs to run in a loop
    
    for letter in choose_word:      # (letter in guess) there are only two possibility of game that user guess be on the letter and not in the letter like 0 and 1
            if letter in guess:
                display += letter
                correct_words.append(guess) # Counter variable we use as list form . To restore the correct word we guessed , otherwise that will be remain a blank and each time it disappear so only we append them(add them) on list to restore again and again and we can use that list to check if the letter is already guessed or not. and print upto date correct words
            elif letter in correct_words:
                display += letter
            else:
                display += "_"
    
    print("Word to guess: " + display)
    
        
    #------------------------------------------------- (ii) Letter not in guess st
    if guess not in choose_word:
         lives -= 1
         print("You Guessed",guess,"that's not in the word. You lose 1 life")
         if lives == 0:
            game_over = True
            print("IT WAS" ,choose_word, "YOU LOSE **********************")
    
    if "_" not in display: # if that "_" is not then he win right it is simple logic
         game_over = True
         print("****************************YOU WIN****************************")
    
   #------------------------------ Step-5 : we just print stages[0] with that list position        
    print(hangman_art.stages[lives])
    


