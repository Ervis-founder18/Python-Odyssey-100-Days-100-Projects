# #TODO: Write out the other 3 functions - subtract, multiply and divide.
#
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1-n2
#
# def multiply(n1, n2):
#     return n1*n2
#
# def divide(n1, n2):
#     return n1/n2
#
# #TODO-2: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
#
#
# operations={
#     "+":add,           # WHY NOT add()?? why we not called function ??
#     "-":subtract,     #Remember Not to trigger the fuctions because we are STORING IT
#     "*":multiply,     #and we are not Using It so don't put parentheses to call function
#     "/":divide,       # and use it bcoz we not using it just storing it
# }
#
# #TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
#
#
# # Now :
# print(operations["*"])    # here we tried to take value of that key (*)
#                         # But Output is not as expected so we do something new
#
# #New-Stuff :
#
# print(operations["*"](4,8)) # Look at here by accessing that value i added a parenthesis
#                                     # It became a function and been called a fuction
#
# #how it worked ??
# # operations[s.t] will give you value here # multiply (is our value ) when i print it comes
# # if i add the () then see:
# # multiply () , eventually we called the function and function is been executed triggered there

# LOGIC BE EXPLAINED IN A WAY AND FLOW CHART IS UPLOADED ON FOLDER
#----------------------------LEARNING NOTES ----------------------------------------------------------------------------

def calculator():  # I created this because of final 'n' part because to restart everything i just need to call everything again thats it , we learnes from reborks world game
                    # if i created another while loop that also completely acceptable

    import art
    print("Welcome to Py CALCULATOR :)")
    print(art.logo)

    def add(n1,n2):
        return n1+n2

    def subtract(n1,n2):
        return n1 -n2
    def multiply(n1,n2):
        return n1 *n2
    def divide(n1,n2):
        return n1/n2

    operations={
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide

    }

    # PART -1
    should_accumulate=True      # After part -2 only we can realize this step to add while loop bcoz that step after if condition repeats as long as user type y (so do trail and error)
    n1=eval(input("Enter your first number: "))
    while should_accumulate:



        for i in operations:
            print(i)
        operator=input("Pick an Operator :")
        n2=eval(input("Enter your next number: "))
        result=operations[operator](n1,n2)
        print("The Result of ",n1,operator,n2,"=",result)

        # Part-2 of calculator (is user want to continue calculating with previous result or start new calculation)

        choice=input(f"Type 'y' to continue with {result} OR Type 'n' to restart calculation :").lower()

        if choice=="y":
            n1=result           #result=n1 is mistake i did a complete logic mistake
            #After the process is same we ask the user to pick up the operation and to calculate stuff same way loops through
            # BUT RATHER THAN COPY PASTING IT , WE JUST LOOP THROUGH THIS WHOLE PART 1 AND 2 ? go and add while loop
            should_accumulate=True

        else:
            should_accumulate=False
            print("\n"*20)# note: I added this to create a new page illusion so user don't see the previous calculation and it looks like a new page
            calculator()

calculator()

