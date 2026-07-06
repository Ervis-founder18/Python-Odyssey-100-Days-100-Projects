#                  DAY- 3
# TASK -1 (ROLLER COASTER RIDE)
# QUESTION:Ravi has recently started working at a theme park called Sky Adventure Land. On his first day, the manager gives him an important task: “The roller coaster is dangerous for small children. Only visitors who are 120 cm or taller are allowed to ride. Your job is to check the visitor’s height before giving them a ticket.” Ravi is tired of checking heights manually and wants a small computer program to help him.
# Your Task :
# Write a program that: asks for the visitor’s height in centimeters checks whether the visitor is eligible prints the correct message
#
# ALGORITHM :
"""1. START
 2. TAKE THE HEIGHT FROM THE USER
 3. IF HEIGHT IS > 120 , then print he can ride on the roller coaster
 4. ELSEIF (OTHERWISE) Height==120 then he needs to grow little more to ride
 5. Else print he is not eligible to ride on the roller coaster"""
# CODE :

print("Welcome to the roller coaster ride :)")
H=int(input("Enter Your  Height(in cm) : "))
if H>120:
    print("You can ride on  the roller coaster")
elif H==120:
    print("You need to grow a little taller to  ride on  the roller coaster")
else:
    print("You are not eligible to ride on the roller coaster")

# Summary : we have learned about conditional statement(if, elif, else)
#and Comparison operators (>,<, >=, <= , !=(it means not equal to), == (it means checking LHS = RHS or not, ))
# "=" means assigning the value to the variable

# MULTIPLE IF STATEMENT AND ELIF USECASE

# A roller coaster company wants to automate its ticket booth system.
# Before riding, a person must meet the minimum height requirement of 120 cm.
# Rules:
# If the person's height is less than 120 cm, they cannot ride the roller coaster.
# If the person is allowed to ride, the ticket price depends on age:
# Age less than or equal to 12 → Ticket price is $5
# Age less than or equal to 18 → Ticket price is $7
# Otherwise → Ticket price is $12
# After calculating the ticket price, ask the customer whether they want a photo taken during the ride.
# If the customer enters "Y", add $3 to the current bill.
# If the customer enters "N", no extra charge is added.
# Finally, display the total bill amount.

print ("Welcome to the roller coaster ride :)")
H=int(input("Enter Your  Height(in cm) : "))
age=int(input("Enter your age : "))
want_photo=input("Enter do u want a photo ? additionally $3 ? please type Y/N : ")
bill=0 # bill is the short form of ticket price
if H>=120:
    print("You can ride on  the roller coaster")
    if age<=12:
        bill=5
        print("The children ticket price is $5")
    elif age<=18:
        bill=7
        print("The Youth  ticket price is $7")
    else:
        bill=12
        print("Adult ticket price is $12")
    if want_photo=="Y":
        bill=bill+3
        print("Final ticket price of yours is $ ",bill)
else:
    print("You are not eligible to ride on the roller coaster")

