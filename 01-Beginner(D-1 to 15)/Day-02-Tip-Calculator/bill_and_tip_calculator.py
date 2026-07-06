# Bill and tip calculator
print("Welcome to the Bill Calculator ")
bill=float(input("What is your bill ? $"))
tip=bill* (int(input("Enter the percentage u want to tip 10,12,15 :")))/100
people=int(input("How many people splitting the bill ? "))
x=bill+tip     #Total bill                                    # Look the PEMDAS IS IMPORTANT HERE 
y=x/people
print("The total bill is",round(x,2))
print("Each person should pay : $",round(y,2))

# Summary : here we learned about the Number datatypes ,TYPE CONVERSION, importance of PEMDAS,ROUND FUNCTION round(number, ndigits to round)

