class CoffeeMachine:
    class State:
        MAIN = 0
        BUY = 1
        FILL_WATER = 2
        FILL_MILK = 3
        FILL_BEANS = 4
        FILL_CUPS = 5
        EXIT = 6

    class Coffee:
        def __init__(self, water, milk, beans, cost):
            self.water = water
            self.milk = milk
            self.beans = beans
            self.cost = cost

    ESPRESSO = Coffee(250, 0, 16, 4)
    LATTE = Coffee(350, 75, 20, 7)
    CAPPUCCINO = Coffee(200, 100, 12, 6)

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.state = CoffeeMachine.State.MAIN

    def process_input(self, input_str):
        if self.state == CoffeeMachine.State.MAIN:
            return self._handle_main(input_str)
        elif self.state == CoffeeMachine.State.BUY:
            if input_str == 'back':
                self.state = CoffeeMachine.State.MAIN
                return None
            coffee = [CoffeeMachine.ESPRESSO, CoffeeMachine.LATTE, CoffeeMachine.CAPPUCCINO][int(input_str) - 1]
            return self._handle_buy(coffee)
        elif self.state == CoffeeMachine.State.FILL_WATER:
            self._handle_fill_water(int(input_str))
        elif self.state == CoffeeMachine.State.FILL_MILK:
            self._handle_fill_milk(int(input_str))
        elif self.state == CoffeeMachine.State.FILL_BEANS:
            self._handle_fill_beans(int(input_str))
        elif self.state == CoffeeMachine.State.FILL_CUPS:
            self._handle_fill_cups(int(input_str))
        return None

    def _handle_main(self, command):
        if command == 'buy':
            self.state = CoffeeMachine.State.BUY
            return None
        if command == 'fill':
            self.state = CoffeeMachine.State.FILL_WATER
            return None
        if command == 'take':
            money = self.money
            self.money = 0
            return f'\nI gave you ${money}'
        if command == 'remaining':
            return self._status()
        # command == 'exit':
        self.state = CoffeeMachine.State.EXIT
        return None

    def _check_resources(self, coffee):
        if self.water < coffee.water:
            return False, 'Sorry, not enough water!'
        if self.milk < coffee.milk:
            return False, 'Sorry, not enough milk!'
        if self.beans < coffee.beans:
            return False, 'Sorry, not enough coffee beans!'
        if self.cups == 0:
            return False, 'Sorry, out of cups!'
        return True, "I have enough resources, making you a coffee!"

    def _handle_buy(self, coffee):
        can_brew, message = self._check_resources(coffee)
        if can_brew:
            self.water -= coffee.water
            self.milk -= coffee.milk
            self.beans -= coffee.beans
            self.cups -= 1
            self.money += coffee.cost
        self.state = CoffeeMachine.State.MAIN
        return message

    def _handle_fill_water(self, amount):
        self.water += amount
        self.state = CoffeeMachine.State.FILL_MILK

    def _handle_fill_milk(self, amount):
        self.milk += amount
        self.state = CoffeeMachine.State.FILL_BEANS

    def _handle_fill_beans(self, amount):
        self.beans += amount
        self.state = CoffeeMachine.State.FILL_CUPS

    def _handle_fill_cups(self, amount):
        self.cups += amount
        self.state = CoffeeMachine.State.MAIN

    def _status(self):
        return f'''
The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.beans} g of coffee beans
{self.cups} disposable cups
${self.money} of money'''


_state_prompts = {
    CoffeeMachine.State.MAIN: '\nWrite action (buy, fill, take, remaining, exit): ',
    CoffeeMachine.State.BUY: '\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ',
    CoffeeMachine.State.FILL_WATER: '\nWrite how many ml of water you want to add: ',
    CoffeeMachine.State.FILL_MILK: 'Write how many ml of milk you want to add: ',
    CoffeeMachine.State.FILL_BEANS: 'Write how many grams of coffee beans you want to add: ',
    CoffeeMachine.State.FILL_CUPS: 'Write how many disposable cups you want to add: '
}


def main():
    machine = CoffeeMachine(400, 540, 120, 9, 550)
    while machine.state != CoffeeMachine.State.EXIT:
        input_str = input(_state_prompts[machine.state])
        message = machine.process_input(input_str)
        if message is not None:
            print(message)


if __name__ == '__main__':
    main()
