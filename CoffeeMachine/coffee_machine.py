machine = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}

espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cost': 4}
latte = {'water': 350, 'milk': 75, 'beans': 20, 'cost': 7}
cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}


def display_state():
    print(f'''The coffee machine has:
{machine['water']} ml of water
{machine['milk']} ml of milk
{machine['beans']} g of coffee beans
{machine['cups']} disposable cups
${machine['money']} of money''')


def brew(coffee):
    machine['water'] -= coffee['water']
    machine['milk'] -= coffee['milk']
    machine['beans'] -= coffee['beans']
    machine['cups'] -= 1
    machine['money'] += coffee['cost']


def sell():
    number = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: '))
    selection = [espresso, latte, cappuccino][number - 1]
    brew(selection)


def fill():
    machine['water'] += int(input('Write how many ml of water you want to add: '))
    machine['milk'] += int(input('Write how many ml of milk you want to add: '))
    machine['beans'] += int(input('Write how many grams of coffee beans you want to add: '))
    machine['cups'] += int(input('Write how many disposable cups you want to add: '))


def give():
    money = machine['money']
    machine['money'] = 0
    print(f'I gave you ${money}')


def main():
    display_state()
    actions = {'buy': sell, 'fill': fill, 'take': give}
    selection = input("\nWrite action (buy, fill, take): ")
    actions[selection]()
    print()
    display_state()


if __name__ == '__main__':
    main()
