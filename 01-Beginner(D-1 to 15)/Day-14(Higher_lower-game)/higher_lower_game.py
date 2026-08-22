import game_data
import art
import random
print("Welcome to Higher Lower Game!")
score=0
random_indexA=random.randint(0,len(game_data.data)-1)  # I googled and learned this logic
should_continue=True
while should_continue:


    print(art.logo)
  #  random_indexA=random.randint(0,len(game_data.data)-1)  # I googled and learned this logic

    random_nameA = game_data.data[random_indexA]['name']
    random_descriptionA=game_data.data[random_indexA]['description']
    random_countryA = game_data.data[random_indexA]['country']

    print(f" Compare A: {random_nameA},  {random_descriptionA},From {random_countryA}")

    print(art.vs)
#-------------------------------------------------------------------------------------------
    random_indexB=random.randint(0,len(game_data.data)-1)  # I googled and learned this logic

    random_nameB = game_data.data[random_indexB]['name']
    random_descriptionB=game_data.data[random_indexB]['description']
    random_countryB = game_data.data[random_indexB]['country']

    print(f" Against B: {random_nameB},  {random_descriptionB},From {random_countryB}")
#-----------------------------------------------------------------------------------------------------------
    choose=input("Who has more followers? Type 'A' or 'B':").lower()


    if choose=='a':
        if game_data.data[random_indexA]["follower_count"] > game_data.data[random_indexB]["follower_count"]:    # See this logic data[index][key] to access the value simple no complex thing here i done myself
            score=score+1
            print(f" THAT IS CORRECT :  Your current score is : {score} ")
            random_indexA=random_indexB
            should_continue=True
        else:
            print(f" THAT IS WRONG TRY AGAIN BY RESTART GAME . YOUR Final score :{score} \n :) BYE !!")
            should_continue=False
    elif choose=='b':
        if game_data.data[random_indexB]["follower_count"] > game_data.data[random_indexA]["follower_count"]:
            score=score+1
            print(f"THAT IS CORRECT :  Your current score is : {score}")
            random_indexA = random_indexB
            should_continue=True
        else:
            print(f"THAT IS WRONG TRY AGAIN BY RESTART GAME . YOUR Final score :{score} \n :) BYE !!")
            should_continue = False

# Above first version is written completely by me with own logic of learning

# Let's write this using functions :


# import game_data
# import art
# import random
#
# score = 0
# should_continue = True
#
#
# def get_person(index):
#     name = game_data.data[index]['name']
#     description = game_data.data[index]['description']
#     country = game_data.data[index]['country']
#
#     return name, description, country
#
#
# random_indexA = random.randint(0, len(game_data.data) - 1)
#
# while should_continue:
#
#     print(art.logo)
#
#     nameA, descriptionA, countryA = get_person(random_indexA)
#
#     print(f"Compare A: {nameA}, {descriptionA}, From {countryA}")
#
#     print(art.vs)
#
#     random_indexB = random.randint(0, len(game_data.data) - 1)
#
#     while random_indexB == random_indexA:
#         random_indexB = random.randint(0, len(game_data.data) - 1)
#
#     nameB, descriptionB, countryB = get_person(random_indexB)
#
#     print(f"Against B: {nameB}, {descriptionB}, From {countryB}")
#
#     choose = input("Who has more followers? Type 'A' or 'B': ").lower()
#
#     followersA = game_data.data[random_indexA]["follower_count"]
#     followersB = game_data.data[random_indexB]["follower_count"]
#
#     if choose == 'a':
#
#         if followersA > followersB:
#             score += 1
#             print(f"You're Right! Your current score is {score}")
#             random_indexA = random_indexB
#         else:
#             print(f"Sorry, That's wrong. Final score: {score}")
#             should_continue = False
#
#     elif choose == 'b':
#
#         if followersB > followersA:
#             score += 1
#             print(f"You're Right! Your current score is {score}")
#             random_indexA = random_indexB
#         else:
#             print(f"Sorry, That's wrong. Final score: {score}")
#             should_continue = False




# Whatever way you write the code is correct it is just that presence of mind to think the logic on spot thats what separate from man and machine
# So yeah i guess i'm getting it slowly and steadily a gradual growth i did it :)) hooray !!
