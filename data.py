from GetValue import InputValues as get_val
from GetSign import InputSign as get_sign

def calc_on(num_sign: tuple) -> tuple:
    ffinish = False
    isNumber = 0
    while not ffinish:
        val = get_val if isNumber == 0 else get_sign
        tuple.__add__(val)
        
expression_tuple = tuple()