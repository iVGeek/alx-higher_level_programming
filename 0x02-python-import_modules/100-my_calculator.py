#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    def getop(a, op, b):
        if op == "+":
            return (add(a, b))
        if op == "-":
            return (sub(a, b))
        if op == "*":
            return (mul(a, b))
        if op == "/":
            return (div(a, b))

    nb = len(sys.argv)
    arg = sys.argv
    signe = "-+*/"
    if nb == 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if nb == 4:
        if arg[2] not in signe:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        r = getop(int(arg[1]), arg[2], int(arg[3]))
        print("{} {} {} = {}".format(arg[1], arg[2], arg[3], r))
        exit(0)
