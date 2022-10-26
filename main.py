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

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 500,
}

def check_resources(drink):
    if resources['water'] < MENU[drink]['ingredients']['water']:
        print('Not enough water to make ', drink)
        return False
    elif resources['coffee'] < MENU[drink]['ingredients']['coffee']:
        print('Not enough coffee to make ', drink)
        return False
    if drink == 'latte' or drink == 'cappuccino':
        if resources['milk'] < MENU[drink]['ingredients']['milk']:
            print('Not enough milk to make ', drink)
            return False        
    return True

def substract_resources(drink):
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    if drink == 'latte' or drink == 'cappuccino':
        resources['milk'] -= MENU[drink]['ingredients']['milk']
        
def payment():
    print('Please insert coins.')
    quarters = input('How many quarters?: ')
    dimes = input('How many dimes?: ')
    nickles = input('How many nickles?: ')
    pennies = input('How many pennies?: ')
    total = (float(quarters) * 0.25) + (float(dimes) * 0.10) + (float(nickles) * 0.05) + (float(pennies) * 0.01)
    print('Total: {0}$'.format(total))
    return total

def check_payment(payment, drink):
    if payment >= MENU[drink]['cost']:
        if payment > MENU[drink]['cost']:
            print('Here is your change of {0}$.'.format(payment - MENU[drink]['cost']))
        substract_resources(drink)
        print('Here is your {0}, enjoy!.'.format(drink))
    else:
        print('Not enough coins here is your refund of {0}$.'.format(payment))

def coffee_machine():
    profit = 0
    while(True):
        user_input = input('What would you like? Espresso | Latte | Capuccino: ')
        if user_input == 'off': exit()
        
        elif user_input.lower() == 'espresso':
            if check_resources('espresso'):
                paying = payment()
                check_payment(paying, 'espresso')
                profit += MENU['espresso']['cost']
            
        elif user_input.lower() == 'latte':
            if check_resources('latte'):
                paying = payment()
                check_payment(paying, 'latte')
                profit += MENU['latte']['cost']
            
        elif user_input.lower() == 'cappuccino':
            if check_resources('cappuccino'):
                paying = payment()
                check_payment(paying, 'cappuccino')
                profit += MENU['cappuccino']['cost']
            
        elif user_input.lower() == 'report':
            print('Water:', resources['water'])
            print('Milk:', resources['milk'])
            print('Coffee:', resources['coffee'])
            print('Profit:', profit)
            
        else:
            print('Please choose between Espresso | Latte | Capuccino.')
            print()
            
if __name__ == '__main__':
    coffee_machine()