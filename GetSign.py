oper_list = ['-', '+', '*', '/', '=']

def InputSign () -> str:
    check = False
    while not check:
        sign = input()
        if sign in oper_list:
            check = True
        else:
            check = False
    return sign
