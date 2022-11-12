from string import punctuation
from sys import argv

def text_analyzer(text = None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if text == None:
        text = input("What is the text to analyze?\n>> ")
    if isinstance(text, str):
        print("The text contains", str(len(text)), "character(s):")
        print("-", sum(1 for char in text if char.isupper()), "upper letter(s)")
        print("-", sum(1 for char in text if char.islower()), "lower letter(s)")
        print("-", sum(1 for char in text if char in punctuation), "punctuation mark(s)")
        print("-", sum(1 for char in text if char.isspace()), "space(s)")
    else:
        print("AssertionError: argument is not a string")

if __name__ == '__main__':
    argv = argv[1:]
    # print(arg)
    print("AssertionError: more than one argument are provided") if len(argv) > 1 else text_analyzer(None if len(argv) == 0 else ''.join(argv))
