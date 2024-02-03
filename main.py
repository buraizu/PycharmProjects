from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def resource_checker(selection):
    """If adequate resources are available, returns True. Otherwise returns False."""
    if selection == 'espresso':
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            return True
        else:
            print("Inadequate resources available")
            return False
    elif selection == 'latte':
        if resources["water"] >= 200 and resources["milk"] >= 150 and resources["coffee"] >= 24:
            return True
        else:
            print("Inadequate resources available")
            return False
    elif selection == 'cappuccino':
        if resources["water"] >= 250 and resources["milk"] >= 100 and resources["coffee"] >= 24:
            return True
        else:
            print("Inadequate resources available")
            return False


def money_checker(s):
    """Allows user to input coins, checks the total, provides change or refund"""
    cost = MENU[s]["cost"]

    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    entered_sum = (quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)

    if entered_sum < cost:
        print(f"Insufficient funds, {entered_sum} refunded")
        return False
    else:
        resources["money"] += cost
        entered_sum -= cost

        if entered_sum > 0:
            print(f"Here's ${entered_sum - cost} in change")
        return True


def decrement_resources(selection):
    menu_item = MENU[selection]
    for key in menu_item["ingredients"].keys():
        resources[key] -= MENU[selection]["ingredients"][key]


def coffee_machine():
    """Returns coffee if sufficient resources are available and sufficient funds provided"""
    selection = input("What would you like? (espresso, latte, or cappuccino): ").lower()

    if selection == 'report':
        print(f"Resource report: {resources}")
    else:
        if resource_checker(selection):
            if money_checker(selection):
                decrement_resources(selection)
                print(f"Here's your {selection}")
            else:
                print("Money issue, exiting")
        else:
            print(f"Insufficient resources for {selection}")

    continue_choice = input("Would you like to make another selection? 'Yes' or 'No': ")
    if continue_choice.lower() == 'yes':
        coffee_machine()
    else:
        print("Thanks, exiting")


coffee_machine()
