water_per_cup = 200
milk_per_cup = 50
beans_per_cup = 15

water = int(input("Write how many ml of water the coffee machine has: "))
milk = int(input("Write how many ml of milk the coffee machine has: "))
beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
cups_requested = int(input("Write how many cups of coffee you will need: "))
cups_available = min(water // water_per_cup, milk // milk_per_cup, beans // beans_per_cup)

if cups_available > cups_requested:
    print(f"Yes, I can make that amount of coffee (and even {cups_available - cups_requested} more than that)")
elif cups_available == cups_requested:
    print("Yes, I can make that amount of coffee")
else:
    print(f"No, I can make only {cups_available} cups of coffee")
