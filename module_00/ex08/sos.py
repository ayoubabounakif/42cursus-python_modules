from sys import argv

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ':'/' 
}

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += '/ '
    return cipher

def handle_error(argv):
    if len(argv) < 1:
        raise Exception('usage:\n\tpython3 sos.py [args -- { alphanumeric or space characters }]')
    new_list = [x for x in argv if x.replace(' ', '').isalnum()]
    if len(new_list) != len(argv):
        raise Exception('Error')
    return new_list

def concatenate_arguments(list):
    return ' '.join(list)

if __name__ == '__main__':
    argv = argv[1:] 
    try:
        new_list = handle_error(argv)
        s = concatenate_arguments(new_list)
        print(encrypt(s.upper()))
    except Exception as error:
        print(error)
