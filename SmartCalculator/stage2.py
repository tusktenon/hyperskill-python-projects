while True:
    match input().split():
        case [a, b]:
            print(int(a) + int(b))
        case ['/exit']:
            print('Bye!')
            break
        case [a]:
            print(a)
        case _:
            pass
