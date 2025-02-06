from idlelib.macosx import hideTkConsole

from main import menu, resources

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01
buy = True

while buy:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0

    if choice == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")

    elif choice == "off":
        buy = False
        break

    elif choice in menu:
        for i in menu[choice]["ingredients"]:
            if menu[choice]["ingredients"][i] > resources[i]:
                print(f"Sorry there is not enough {i}.")
                break
            else:
                pay = menu[choice]["cost"]
                print(f"Your total is: ${pay}")
                user_quarters = int(input("Insert quarters: "))
                user_dimes = int(input("Insert dimes: "))
                user_nickles = int(input("Insert nickles: "))
                user_pennies = int(input("Insert pennies: "))
                total = quarters * user_quarters + dimes * user_dimes + nickles * user_nickles + pennies * user_pennies

                if total < pay:
                    print("Sorry that's not enough money. Money refunded.")
                    break
                elif total == pay:
                    money += total
                elif total > pay:
                    change = total - pay
                    money += pay
                    print(f"Here is ${round(change, 2)} dollars in change.")

                for n in menu[choice]["ingredients"]:
                    resources[n] = resources[n] - menu[choice]["ingredients"][n]
                if total >= pay:
                    print(f"Here is your {choice}. Enjoy!")
                break
