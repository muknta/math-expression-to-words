import inflect
from string import digits


_symb_to_word = {"+":"plus", "-":"minus", "=":"equals", "/":"divide", "%":"percent", "*":"multiplicate", "(":"left bracket", ")":"right bracket", "^":"raise to the power of"}

def is_valid(exp_list):
    if (set(exp_list).issubset(f"{digits} {''.join(_symb_to_word.keys())}") and 
            all(elem.isdigit() or not set(elem).intersection(f"{digits}") for elem in exp_list)):
        return True
    else:
        return False
    
def math_to_str(expression):
    exp_lst = expression.split()
    if not is_valid(exp_lst):
        return "invalid input"
    eng = inflect.engine()
    return ' '.join([eng.number_to_words(elem) if elem.isdigit() else _symb_to_word[elem] for elem in exp_lst])

