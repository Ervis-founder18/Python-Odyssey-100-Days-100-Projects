# TASK-2: To check the given number is ODD or EVEN
# ALGORITHM:
#1.Take N as input from the User
#2. formula for even number we know any even number divided by 2 will perfectly divide
# 3. N%2==0 it means an number that divisible by 2 which perfectly gives 0 it means its a even number other wise its a odd
# we use divided by 2 for the sake of human simplicity to half anything will be more easy than messy numbers
#CODE:

N=int(input("Enter a number: "))
if N%2==0:                     # Since the remainder of even number will always is 0 when divide by 2, universally acceptable
    print("This number is even")
else:
    print("This number is odd")

# # OR we can use this method
# N=int(input("Enter a number: "))
# if N%2==1:                    # Since the remainder of odd number will always is 1 when divide by 2, universally acceptable
#     print("This number is odd")
# else:
#     print("This number is even")
