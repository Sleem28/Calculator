import Operations as oper

def calculate(first_num, sign: str, sec_num):
    match sign:
        case '+':
            return oper.sum(first_num, sec_num)
        case '-':
            return oper.sub(first_num, sec_num)
        case '*':
            return oper.mult(first_num, sec_num)
        case '/':
            return oper.div(first_num, sec_num)
