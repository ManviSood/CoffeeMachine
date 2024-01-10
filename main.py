from menu import resources, MENU
# TODO: 2. Turn Off Coffee machine


def turn_off_coffee_machine():
    return False


# TODO: 3. Print report of all the coffee machine resources


def report():
    return [resources['water'], resources['milk'], resources['coffee']]


# TODO: 4. Check sufficient resources to make drink order


def check_sufficient_resources(type_of_coffee):
    """Returns True when order can be made, False if ingredients are insufficient"""
    water = MENU[type_of_coffee]['ingredients']['water']
    coffee = MENU[type_of_coffee]['ingredients']['coffee']
    if type_of_coffee == "espresso":
        milk = 0
    else:
        milk = MENU[type_of_coffee]['ingredients']['milk']

    if resources['water'] < water:
        print("Sorry there is not enough water.")
        return False
    elif resources['milk'] < milk:
        print("Sorry there is not enough milk.")
        return False
    elif resources['coffee'] < coffee:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


# TODO: 5. Process coins to make drink order


def process_coins():
    """Returns the total_cost calculated from coins inserted """
    print("Please insert coins.")
    quarters = (int(input("how many quarters?: ")) * 0.25)
    dimes = (int(input("how many dimes?: ")) * 0.10)
    nickles = (int(input("how many nickles?: ")) * 0.05)
    pennies = (int(input("how many pennies?: ")) * 0.01)
    total_cost = round((quarters + dimes + nickles + pennies), 2)
    return total_cost


# TODO: 6. Check Transaction
def check_transaction_successful(money_received, drink_cost):
    """Returns True when the money is accepted or False if money is insufficient"""
    coffee_cost = MENU[coffee_type]['cost']
    if money_received < coffee_cost:
        print("Sorry that's not enough money.Money refunded.")
        return drink_cost, False

    change = round((cost - coffee_cost), 2)
    drink_cost += coffee_cost
    # print(f"Money made:{drink_cost}, Change: {change} ")
    print(f"Here is ${change} dollars in change.")
    return drink_cost, True


# TODO: 7. Make coffee
def make_coffee(coffee_order):
    if coffee_order == 'espresso':
        resources['water'] -= MENU[coffee_order]['ingredients']['water']
        resources['coffee'] -= MENU[coffee_order]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[coffee_order]['ingredients']['water']
        resources['coffee'] -= MENU[coffee_order]['ingredients']['coffee']
        resources['milk'] -= MENU[coffee_order]['ingredients']['milk']
    return


should_continue = True
money = 0
while should_continue:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_type == 'report':
        ingredients = report()
        print(f"Water: {ingredients[0]}ml\nMilk: {ingredients[1]}ml\nCoffee: {ingredients[2]}g\nMoney: ${money}")
    elif coffee_type == 'off':
        should_continue = turn_off_coffee_machine()
    elif coffee_type in ['latte', 'espresso', 'cappuccino']:
        value = check_sufficient_resources(coffee_type)
        if value:
            cost = process_coins()
            money, status = check_transaction_successful(cost, money)
            if status:
                make_coffee(coffee_type)
                print(f"Here is your {coffee_type} ☕. Enjoy!")
    else:
        print("Oops! You did some mistake ☹️")
