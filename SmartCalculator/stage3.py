while (user_input := input()) != '/exit':
    if user_input == '/help':
        print('The program calculates the sum of numbers')
    elif user_input:
        numbers = map(int, user_input.split())
        print(sum(numbers))
print('Bye!')
