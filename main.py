from string import digits

_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
_from_ten_to_twenty = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'] 
_hundredths = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
_num_orders = ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion']

_symb_to_word = {"+":"plus", "-":"minus", "=":"equals", "/":"divide", "%":"percent", "*":"multiplicate", "(":"left bracket", ")":"right bracket", "^":"raise to the power of"}

def is_valid(exp: str) -> bool:
    '''Checks validity of a full math expression'''
    return (set(exp).issubset(f"{digits} {''.join(_symb_to_word.keys())}") and 
            all(elem.isdigit() or not set(elem).intersection(f"{digits}") for elem in exp.split()))

def concat_order(ord_num: int, order: str) -> str:
    """Converts order of a number to words 
    (12_345_678 -- orders between underscores)

    Params:
    ord_num (int): position of order in the number
                   (e.g. '345' in '12345678' - position of thousands -- ord_num=1 in _num_orders)
    order (str): 1|2|3 digit|s -- order of the number -- part of the string
                 (e.g. '12' or '345' or '678' in '12345678')

    Returns:
    str: order of the number in words
         (e.g. '12' in '12345678' -- 'twelve million, ',
               '678' -- 'six hundred and seventy-eight')

    """
    res = ''
    ord_len = len(order)
    if ord_len == 1:
        res += _digits[int(order[0])]
    elif ord_len == 2 or ord_len == 3:
        if ord_len == 3 and order[0] != '0':
            res += f'{_digits[int(order[0])]} hundred'
            if order[1] != '0' or order[2] != '0':
               res += ' and '
        if order[-2] == '1':
            res += _from_ten_to_twenty[int(order[-1])]
        elif order[-2] == '0' and order[-1] != '0':
            res += _digits[int(order[-1])]
        elif order[-2] not in '01':
            res += _hundredths[int(order[-2])-2]
            if order[-1] != '0':
                res += f'-{_digits[int(order[-1])]}'
    if ord_num and set(order) != {'0'}:
        res += f' {_num_orders[ord_num-1]}'
    return res

def orders_split(num: str) -> list:
    """Converts number to order list

    Example:
    num='12345678' --> return ['12','345','678']

    """
    l = [num[i-3:i] for i in range(len(num),0,-3)]
    if len(num)%3:
        l[-1] = num[:len(num)%3]
    return l


def math_to_str(expression: str) -> str:
    '''Converts math expression to words'''
    if not is_valid(expression):
        return "invalid input"
    res = ''
    for elem in expression.split():
        if res:
            res += ' '
        if elem.isdigit():
            ord_elem = orders_split(elem.lstrip("0"))
            res_dig_elem = '' if ord_elem else 'zero'
            for num,el in enumerate(ord_elem):
                c_o = concat_order(num,el)
                if c_o:
                    res_dig_elem = f'{c_o}, {res_dig_elem}' if num and res_dig_elem else c_o + res_dig_elem
            res += res_dig_elem
        else:
            res += _symb_to_word[elem]
    return res

