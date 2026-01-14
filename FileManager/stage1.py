import os

while (command := input('Input the command ')) != 'quit':
    match command.split():
        case ['pwd']:
            print(os.getcwd())
        case ['cd', target]:
            try:
                os.chdir(target)
            except FileNotFoundError:
                print('No such directory')
            else:
                print(os.getcwd())
        case _:
            print('Invalid command')
