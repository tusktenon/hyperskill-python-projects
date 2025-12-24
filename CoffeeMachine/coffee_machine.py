water_per_cup = 200
milk_per_cup = 50
beans_per_cup = 15

cups = int(input('Write how many cups of coffee you will need: '))

print(f'''For {cups} cups of coffee you will need:
{cups * water_per_cup} ml of water
{cups * milk_per_cup} ml of milk
{cups * beans_per_cup} g of coffee beans''')
