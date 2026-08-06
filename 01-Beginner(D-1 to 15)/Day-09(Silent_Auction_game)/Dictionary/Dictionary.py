# I) WHAT IS DICTIONARY ??

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# Dictionaries have elements which are identified by the Key
# Not like list ie list[0] where you put index and retrive value
# Here you can retrive value only with key not by index
# EXAMPLE:
print(programming_dictionary["loop"])

#-----------------------------------------------------------------------------------------
# II) How can we add/modify the dictionary , Later on in our program?

# REMEMBER: DSL is mutable so we can chnage later
#BY:

# SYNTAX: dictionary_name[(key to add)] = value to be added to this new key

programming_dictionary["Loop"]="A action being done repeatedly over and over again."
print(programming_dictionary)

# TO MODIFY/ EDIT:
programming_dictionary["Bug"]="A moth in your computer" # Just assign(=) the desired value to key
#----------------------------------------------------------------------------------------------------------------

# III ) How to create a empty dictionary ??

# Just like we created empty list : empty_lst=[] we can create:
empty_dict={}
#-------------------------------------------------------------------

# IV ) V.imp :How can we WIPE OUT THE EXISTING DICTIONARY ??

#1) JUST WRITE THE CURRENT DICTIONARY NAME AND EQUAL TO {}
#2) SYNTAX :

# programming_dictionary={}  # IT IS MORE USEFUL : WHEN WE WANTED TO CLEAR OUT A USERS PROGRESS
# print(programming_dictionary)                           # OR IF A GAME RESTARTS IT WILL PROBABLY EMPTY THE DICTIONARY AND AGAIN LOOP STARTS

#----------------------------------------------------------------------------------------------------------------

# V) How can we LOOP THROUGH A DICTIONARY ??

for i in programming_dictionary:
    print(i)

# OUTPUT IS A BIT OF SURPRISE BECAUSE I THOUGHT IT WOULD GIVE COMPLETE KEY: VALUE BUT IT JUST GIVEN THE KEY

#SO

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key]) # This will actually give you the value

#--------------------------------------------------------------------------------------------------------------