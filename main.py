from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()



other_client = True

while other_client:
    choice = menu.get_items()
    coffee_choise = input(f"What would you like {choice} :")
    if coffee_choise == "off":
        other_client = False
    elif coffee_choise == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(coffee_choise)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


