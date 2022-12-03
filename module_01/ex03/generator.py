import random

def __transformText(text, option):
    """
    This function is used to transform the text according to the option value.
    """
    if option == "shuffle":
        # Fisher–Yates shuffle Algorithm
        for i in range(len(text)):
            j = random.randint(0, i)
            text[i], text[j] = text[j], text[i] # this is a pythonic way to swap two values
    elif option == "unique":
        text = set(text)
    elif option == "ordered":
        text = sorted(text)
    return text

def __treatErrors(text, option):
    """
    This function is used to treat the errors.
    """
    if not isinstance(text, str): exit("ERROR")
    if not option in ["shuffle", "unique", "ordered", None]: exit("ERROR")

# function prototype
def generator(text, sep=" ", option=None):
    """
    Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """
    __treatErrors(text, option)
    text = text.split(sep)
    text = __transformText(text, option)
    for word in text:
        yield word

    

if __name__ == '__main__':

    print()

    # text = "Le Lorem Ipsum est simplement du faux texte."
    # for word in generator(text, sep=" "):
    #     print(word) # Le Lorem Ipsum est simplement du faux texte. (one word per line)

    # for word in generator(text, sep=" ", option="shuffle"):
    #     print(word) # text shuffled -> No apparent order. (one word per line)

    # for word in generator(text, sep=" ", option="ordered"):
    #     print(word) # Ipsum Le Lorem du est faux du simplement texte. (one word per line)

    # text = "Lorem Ipsum Lorem Ipsum"
    # for word in generator(text, sep=" ", option="unique"):
    #     print(word) # Ipsum Lorem | Lorem Ipsum (one word per line)