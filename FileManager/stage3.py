import os
import shutil


def change_directory(target):
    try:
        os.chdir(target)
    except FileNotFoundError:
        print('No such directory')
    else:
        print(os.getcwd())


def create_directory(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        print('The directory already exists')


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


def remove(target):
    if os.path.isfile(target):
        os.remove(target)
    elif os.path.isdir(target):
        shutil.rmtree(target)
    else:
        print('No such file or directory')


def rename(source, target):
    if not os.path.exists(source):
        print('No such file or directory')
    elif os.path.exists(target):
        print('The file or directory already exists')
    else:
        shutil.move(source, target)


def main():
    print('Input the command')
    while (command := input()) != 'quit':
        match command.split():
            case ['cd', target]:
                change_directory(target)
            case ['ls']:
                list_contents()
            case ['ls', '-l']:
                list_contents(sizes='bytes')
            case ['ls', '-lh']:
                list_contents(sizes='readable')
            case ['mkdir', path]:
                create_directory(path)
            case ['mkdir']:
                print('Specify the name of the directory to be made')
            case ['mv', source, target]:
                rename(source, target)
            case ['mv', *_]:
                print('Specify the current name of the file or directory and the new name')
            case ['pwd']:
                print(os.getcwd())
            case ['rm']:
                print('Specify the file or directory')
            case ['rm', target]:
                remove(target)
            case _:
                print('Invalid command')


if __name__ == '__main__':
    main()
