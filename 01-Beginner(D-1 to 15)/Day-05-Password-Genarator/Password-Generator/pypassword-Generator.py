#PROJECT: PASSWORD GENERATOR

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] # This is the symbols usually accepted by Website for passwords

print("Welcome to the PyPassword Generator! (HARD VERSION)")
no_letters = int(input("How many letters would you like in your password?\n"))
no_symbols = int(input(f"How many symbols would you like?\n"))
no_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Version :
password=""
# First , Lets do for the letter and then number and symbols and then we just add up all those strings
for i in range(1,no_letters+1):
    random_letter=random.choice(letters) # I GUESSED ON MY OWN also here if i put no_letters=4 then for each iteration it runs on letters here i=1 , for this password=password("")+ random.choice(letters) ("L") then password="L" this will continue until i=4 that chooses the random letter as per iteration it picks up with its hand and check
    password=password+random_letter
for i in range(1,no_symbols+1):
    random_symbol=random.choice(symbols)
    password=password+random_symbol
for i in range(1,no_numbers+1):
    random_number=random.choice(numbers)
    password=password+random_number
print(password)

# PROBLEM WITH EASY VERSION; the problem is that if the hacker knew that you always set a password in a sequnce
#like ; that you always put numbers first , symbols in middle and numbers in the end
# To tackle that we use complete random sequence password hard level


# HARD VERSION:
# ER: here same code but at password place we going to use the random.shuffle(password)
# To shuffle the order of the whole string is not possible BECAUSE : The problem is that strings are immutable (they cannot be changed in place). so to use shuffle we need to use LIST

password=""
# First , Lets do for the letter and then number and symbols and then we just add up all those strings
for i in range(1,no_letters+1):
    random_letter=random.choice(letters) # I GUESSED ON MY OWN also here if i put no_letters=4 then for each iteration it runs on letters here i=1 , for this password=password("")+ random.choice(letters) ("L") then password="L" this will continue until i=4 that chooses the random letter as per iteration it picks up with its hand and check
    password=password+random_letter
for i in range(1,no_symbols+1):
    random_symbol=random.choice(symbols)
    password=password+random_symbol
for i in range(1,no_numbers+1):
    random_number=random.choice(numbers)
    password=password+random_number

# Update that Easy version thats it:

password_list=list(password) # We created a list because string are immutable so
random.shuffle(password_list) # To shuffle this PASSWORD in string it is not possible because it is immutable so that only we take up extra step to change this password as string to list and simply we again convert back to string once work is done thats our logic. In above that random.choice(letter) we already manually created the list so

password="".join(password_list) # agian we convert back to string
password = "".join(password_list)

print("YOUR PASS WORD IS :",password)

# Explanation:(What is "".join()function )
#
# join() is used to combine all the elements of a list into a single string.
#
# Syntax:
# separator.join(list)
#
# The string before .join() is called the separator.
#
# Examples:
#
# "".join(["A", "B", "C"])
# Output:
# ABC
#
# "-".join(["A", "B", "C"])
# Output:
# A-B-C
#
# " ".join(["A", "B", "C"])
# Output:
# A B C
#
# In the password generator:
#
# Suppose after shuffling,
#
# password_list = ['@', '4', 'b', 'A', '!', '5', 'C', 'd']
#
# Then,
#
# password = "".join(password_list)
#
# Python joins every character together with an empty string ("") between them.
#
# Internally, it is like:
#
# "@" + "" + "4" + "" + "b" + "" + "A" + "" + "!" + "" + "5" + "" + "C" + "" + "d"
#
# Result:
#
# @4bA!5Cd
#
# So, "".join(password_list) converts the list of characters back into one complete string, which is why we can print it as the final password.
