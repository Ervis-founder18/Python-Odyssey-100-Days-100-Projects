# QUESTION : Welcome to Python Pizza Deliveries!
# You’ve just been hired at a pizza company, and your first task is to build an automatic pizza order billing system.
# Your program should ask the customer for their pizza preferences, calculate the total cost, and display the final bill amount.
# 📌 Pizza Menu
# Pizza Size
# Code
# Price
# Small Pizza
# S
# $15
# Medium Pizza
# M
# $20
# Large Pizza
# L
# $25
# 🍕 Additional Toppings
# Pepperoni
# For a Small Pizza (S) → +$2
# For a Medium (M) or Large (L) Pizza → +$3
# Ask the customer:
# Plain text
# Do you want pepperoni? (Y/N)
# 🧀 Extra Cheese
# For any pizza size, extra cheese costs:
# +$1
# Ask the customer:
# Plain text
# Do you want extra cheese? (Y/N)
# ✅ Your Task
# Ask the user for the pizza size (S, M, or L)
# Ask if they want pepperoni (Y/N)
# Ask if they want extra cheese (Y/N)
# Calculate the final bill
# Display the result
print("Welcome to python Pizza Deliveries 🍕") # 🍕i created this using unicode : print("\U0001F355" On the console if u type this then pizza logo will appear )
print("HERE IS OUR MENU :\n" \
"------------------------\n"
" |Small Pizza(S) : $15 | \n" \
" |Medium Pizza(M): $20 | \n" \
" |Large Pizza(M) : $25 | \n" \
"------------------------\n")
size=input("Enter the size of the Pizza you want? S,M or L :")
P=input("Enter is You want additional Pepporoni For S its $2 for M,L its $3 , type Y/N :")
C=input("Enter is You want additional Cheese For any size it is $1, type Y/N :")
bill=0

if size=="S":
    bill=bill+15
elif size=="M":
    bill=bill+20
elif size=="L":
    bill=bill+25
else:
    print("you have chosen wrong size")

# Let's ask the user about addons 1) Pepporoni

if P=="Y" :
    if size=="S":
        bill = bill + 2
    else:
        bill = bill + 3

# TO ask is they need any extra cheese
if C=="Y":
    bill=bill+1


print("YOUR FINAL BILL IS : \n $",bill)



# SUMMARY : we have learned about if, elif,else, nested if , multiple if , logical operators And mainly we learned where to apply what
