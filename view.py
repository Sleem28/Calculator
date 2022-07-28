from data import calc_on
from calculate import calculate

def get_result():
    oper_list = calc_on()
    result = 0
    sign = ''
    for item in oper_list:
        if item.isdigit():
            if result == 0:
                result += int(item)
            else:
                result = calculate(result, sign, int(item))
        else:
            sign = item
    return result



