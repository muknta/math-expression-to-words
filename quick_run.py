from main import math_to_str
from sys import argv


# call -- input string in quotes like:
# python quick_run.py '1 + 4 = 6'
def start(exp: str):
    print(math_to_str(exp))


if __name__ == "__main__":
    start(argv[1])

