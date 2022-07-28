from GetValue import InputValues as get_val
from GetSign import InputSign as get_sign

def calc_on() -> list:
    num_sign = list()
    ffinish = False
    isNumber = 0

    while not ffinish:
        val = get_val() if isNumber == 0 else get_sign()
        if val == '=':
            ffinish = True
        else:
            num_sign.append(val)
            isNumber = 1 if isNumber == 0 else 0

    return num_sign
        

