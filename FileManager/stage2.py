import os


def list_contents(sizes=None):
    contents = os.listdir()
    directories = [d for d in contents if os.path.isdir(d)]
    files = [f for f in contents if os.path.isfile(f)]
    directories.sort()
    files.sort()
    for d in directories:
        print(d)
    if sizes == 'bytes':
        for f in files:
            print(f, os.stat(f).st_size)
    elif sizes == 'readable':
        for f in files:
            print(f, _readable_size(os.stat(f).st_size))
    else:
        for f in files:
            print(f)


def _readable_size(bytes):
    KB = 1024
    MB = 1024 * KB
    GB = 1024 * MB
    units = {'GB': GB, 'MB': MB, 'KB': KB}
    for unit, value in units.items():
        if bytes >= value:
            return f'{round(bytes / value)}{unit}'
    return f'{bytes}B'


def main():
    print('Input the command')
    while (command := input()) != 'quit':
        match command.split():
            case ['cd', target]:
                try:
                    os.chdir(target)
                except FileNotFoundError:
                    print('No such directory')
                else:
                    print(os.getcwd())
            case ['ls']:
                list_contents()
            case ['ls', '-l']:
                list_contents(sizes='bytes')
            case ['ls', '-lh']:
                list_contents(sizes='readable')
            case ['pwd']:
                print(os.getcwd())
            case _:
                print('Invalid command')


if __name__ == '__main__':
    main()
