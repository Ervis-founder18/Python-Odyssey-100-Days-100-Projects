# type report to get to get the current status of the machine ingredients and money earned
# Type OFF to turn off the machine


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


# Machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Total money earned
money = 0


print("Welcome to Coffee Machine :)")

print("""
Here's the Menu :)

Espresso : $1.5
Latte : $2.5
Cappuccino : $3.0
""")


machine = True

while machine:

    order = input("What would you like? : ").lower()

    # ------------------------------------------------
    # TURN OFF MACHINE
    # ------------------------------------------------

    if order == "off":
        print("Coffee machine shutting down..Zzzz.")
        machine = False

    # ------------------------------------------------
    # REPORT
    # ------------------------------------------------

    elif order == "report":                             # Added at the end of code actually
        print("\n------ CURRENT REPORT ------")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money:.2f}")
        print("----------------------------\n")

    # ------------------------------------------------
    # INVALID ORDER
    # ------------------------------------------------

    elif order not in MENU:
        print("Sorry, that's not a valid choice.")

    # ------------------------------------------------
    # CHECK RESOURCES
    # ------------------------------------------------

    else:

        drink = MENU[order]

        ingredients = drink["ingredients"]

        # Check whether enough resources exist
        resource_available = True

        for item in ingredients:

            if resources[item] < ingredients[item]:
                print(f"Sorry, there is not enough {item}.")
                resource_available = False

        # If resources are insufficient, go back to beginning
        if not resource_available:
            continue

        # ------------------------------------------------
        # INSERT COINS
        # ------------------------------------------------

        print("\nPlease insert the coins 🪙")

        quarter = int(input("Insert quarter coins (1q = 25 cents): "))
        dime = int(input("Insert dime coins (1d = 10 cents): "))
        nickel = int(input("Insert nickel coins (1n = 5 cents): "))
        penny = int(input("Insert penny coins (1p = 1 cent): "))

        paid = (
            quarter * 0.25
            + dime * 0.10
            + nickel * 0.05
            + penny * 0.01
        )

        cost = drink["cost"]

        # ------------------------------------------------
        # CHECK MONEY
        # ------------------------------------------------

        if paid < cost:

            print(
                f"Sorry, that's not enough money. "
                f"You inserted ${paid:.2f}. "
                f"The drink costs ${cost:.2f}."
            )

            print("Money refunded.")

        else:

            # Calculate change
            change = paid - cost

            print(f"Here is your change: ${change:.2f}")

            # ------------------------------------------------
            # DEDUCT RESOURCES
            # ------------------------------------------------

            for item in ingredients:
                resources[item] -= ingredients[item]

            # Add money to machine
            money += cost

            # ------------------------------------------------
            # SERVE DRINK
            # ------------------------------------------------

            print(f"Here is your {order} ☕")
            print("Enjoy your drink! :)")
