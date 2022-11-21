import sys

try:
    if (len(sys.argv) - 1 == 1):
        num = int(sys.argv[1])
        outputs = ['Even', 'Odd', 'Zero']
        print("I'm " + outputs[2] + '.' if int(num) == 0 else "I'm " + outputs[0] + '.' if int(num) % 2 == 0 else ("I'm " + outputs[1] + '.'))
    else:
        print("AssertionError: more than one argument are provided" if len(sys.argv) - 1 > 1 else "Arguments expected\nusage: python3 whois.py [numeric_arg]")
except:
    print("AssertionError: argument is not an integer")
