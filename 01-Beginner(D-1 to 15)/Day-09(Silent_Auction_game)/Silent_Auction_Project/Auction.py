

# print("Hello World")
# print("\n" *2000)  # Note-1 : It is how we create a new page as you seen in solution
#                     # From here there will be huge gap that create a illusion of new page so nobody going to scroll up so
# print("Type your name :")
#------------------------------------------------------------------------------------------------

import art
print("WELCOME TO THE SILENT AUCTION GAME :) ")
print(art.logo)



bids={}  # I created this empty dict because to store the repeated value in dictionary called bids
        #other-wise each time you loop it will get old value be thrown away and only the final value will stay

should_continue=True
while should_continue:
    name = input("What is your name? :")
    price = int(input("What's Your Bid ? : $"))
    bids[name]=price # Here we created and added the key:value 's here in dictionary bids. So each time we loop it will add the new value to the dictionary and not throw away the old value
    bidder=input("Are there any other bidders ? Type 'yes' or 'no' : ").lower()
    if bidder == "yes":
        should_continue=True
        print("\n"*100)
    else:
        should_continue=False
        print("\n"*100)
        winner= max(bids,key=bids.get)
        print("The winner is ",winner,"With a bid of $",bids[winner])


# UNDERSTAND OF COMPARISON with this max(dictionary,key=dictionary.get )?  (REFER TO File max in dict.txt )
