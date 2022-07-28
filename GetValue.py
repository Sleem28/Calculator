from curses.ascii import isdigit


def InputValues () -> str:
    check = False
    while not check:
        number = input()
        if number.isdigit():
            check = True
    return number
