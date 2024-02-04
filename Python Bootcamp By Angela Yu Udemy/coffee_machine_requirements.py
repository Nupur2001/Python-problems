'''
Coffee Machine Program Requirements
1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “off” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “Sorry there is not enough water.”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “Sorry that's not enough money. Money refunded.”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
'''

class CoffeeMachine:
    def __init__(self):
        self.water = 300
        self.milk = 200
        self.coffee = 100
        self.money = 0

    def prompt_user(self):
        return input("What would you like? (espresso/latte/cappuccino): ").lower()

    def turn_off(self):
        return input("Enter 'off' to turn off the Coffee Machine: ").lower() == 'off'

    def print_report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money}")

    def check_resources(self, drink):
        return (
            self.water >= drink["water"]
            and self.milk >= drink["milk"]
            and self.coffee >= drink["coffee"]
        )

    def process_coins(self):
        quarters = int(input("Enter number of quarters: "))
        dimes = int(input("Enter number of dimes: "))
        nickels = int(input("Enter number of nickels: "))
        pennies = int(input("Enter number of pennies: "))

        return (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)

    def check_transaction(self, drink, inserted_money):
        if inserted_money < drink["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            change = round(inserted_money - drink["cost"], 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            self.money += drink["cost"]
            return True

    def make_coffee(self, drink):
        self.water -= drink["water"]
        self.milk -= drink["milk"]
        self.coffee -= drink["coffee"]
        print(f"Here is your {drink['name']}. Enjoy!")

    def run(self):
        while True:
            user_input = self.prompt_user()

            if user_input == 'off':
                break
            elif user_input == 'report':
                self.print_report()
            else:
                drink = None
                if user_input == 'espresso':
                    drink = {"name": "espresso", "water": 50, "milk": 0, "coffee": 18, "cost": 1.5}
                elif user_input == 'latte':
                    drink = {"name": "latte", "water": 200, "milk": 150, "coffee": 24, "cost": 2.5}
                elif user_input == 'cappuccino':
                    drink = {"name": "cappuccino", "water": 250, "milk": 100, "coffee": 24, "cost": 3.0}

                if drink and self.check_resources(drink):
                    inserted_money = self.process_coins()
                    if self.check_transaction(drink, inserted_money):
                        self.make_coffee(drink)


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    coffee_machine.run()

