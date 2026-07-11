# TOPIC : BANKER ROULETTE (APPLICATION OF RANDOM , LIST PRACTICE)
# Banker Roulette is a simple program that randomly selects one person from a list of names to pay the bill. It teaches you how to store names in a list and make a random selection using Python.
# 1st method :
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends)) # RECALL : choice() is a built-in function used with module to specifially used for lists

#2nd method:
random_index=random.randint(0,4)
print(friends[random_index]) # here to access the elements from list you always use the square braces[]