from sys import argv

def operations(first, second):
    ops = ["Sum", "Difference", "Product", "Quotient", "Remainder"]
    longest_string_len = len(max(ops, key=len))
    print(ops[0] + ":" + " " * (longest_string_len - len(ops[0])), first + second)
    print(ops[1] + ":" + " " * (longest_string_len - len(ops[1])), first - second)
    print(ops[2] + ":" + " " * (longest_string_len - len(ops[2])), first * second)
    print(ops[3] + ":" + " " * (longest_string_len - len(ops[3])), first / second if second != 0 else "ERROR (division by zero)")
    print(ops[4] + ":" + " " * (longest_string_len - len(ops[4])), first % second if second != 0 else "ERROR (modulo by zero)")


if __name__ == '__main__':
    argv = argv[1:]
    if (len(argv) != 2):
        print("AssertionError: too many arguments" if len(argv) > 2 else "Usage: python operations.py <number1> <number2>")
        exit()
    try:
        first = int(argv[0])
        second = int(argv[1])
        operations(first, second)
    except:
        print("AssertionError: only integers")