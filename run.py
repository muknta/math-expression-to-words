from main import math_to_str


def start():
    print("Hi! This programm does convert math expression to words.\n")

    while(True):
        exp = input("Math-master, type your math-string (q - to quit)\n")
        if exp == "q":
            return
        else:
            print(math_to_str(exp))


if __name__ == "__main__":
    start()

