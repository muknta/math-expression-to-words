import inflect
from string import digits


_symb_to_word = {"+":"plus", "-":"minus", "=":"equals", "/":"divide", "%":"percent", "*":"multiplicate", "(":"left bracket", ")":"right bracket", "^":"raise to the power of"}

def is_valid(exp):
    if (set(exp).issubset(f"{digits} {''.join(_symb_to_word.keys())}") and 
            all(elem.isdigit() or not set(elem).intersection(f"{digits}") for elem in exp.split())):
        return True
    else:
        return False
    
def math_to_str(expression):
    if not is_valid(expression):
        return "invalid input"
    exp_lst = expression.split()
    eng = inflect.engine()
    return ' '.join([eng.number_to_words(elem) if elem.isdigit() else _symb_to_word[elem] for elem in exp_lst])

