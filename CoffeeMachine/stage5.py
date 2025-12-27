machine = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}

espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4}
latte = {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7}
cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}


def display_state():
    print(f'''
The coffee machine has:
{machine['water']} ml of water
{machine['milk']} ml of milk
{machine['beans']} g of coffee beans
{machine['cups']} disposable cups
${machine['money']} of money''')


def can_brew(coffee):
    for resource in ['water', 'milk', 'beans']:
        if machine[resource] < coffee[resource]:
            print(f'Sorry, not enough {resource}!')
            return False
    if machine['cups'] == 0:
        print('Sorry, out of cups!')
        return False
    return True


def brew(coffee):
    machine['water'] -= coffee['water']
    machine['milk'] -= coffee['milk']
    machine['beans'] -= coffee['beans']
    machine['cups'] -= 1
    machine['money'] += coffee['cost']


def sell():
    selection = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    if selection == 'back':
        return
    coffee = [espresso, latte, cappuccino][int(selection) - 1]
    if can_brew(coffee):
        print("I have enough resources, making you a coffee!")
        brew(coffee)


def fill():
    machine['water'] += int(input('\nWrite how many ml of water you want to add: '))
    machine['milk'] += int(input('Write how many ml of milk you want to add: '))
    machine['beans'] += int(input('Write how many grams of coffee beans you want to add: '))
    machine['cups'] += int(input('Write how many disposable cups you want to add: '))


def give():
    money = machine['money']
    machine['money'] = 0
    print(f'\nI gave you ${money}')


def main():
    actions = {'buy': sell, 'fill': fill, 'take': give, 'remaining': display_state}
    while (selection := input("\nWrite action (buy, fill, take, remaining, exit): ")) != 'exit':
        actions[selection]()


if __name__ == '__main__':
    main()
