# Make a program that takes a string S and an integer N as argument and print the list
# of words in S that contains more than N non-punctuation characters.

from sys import argv
import string

def check_argv_specs(argv):
    if (len(argv) != 2) or (argv[0].isdigit() == True or argv[1].isdigit() == False):
        raise Exception()

if __name__ == '__main__':
    try:
        argv = argv[1:]
        check_argv_specs(argv)
        argv[0] = argv[0].translate(str.maketrans('', '', string.punctuation))
        new_list = [x for x in argv[0].split() if len(x) > int(argv[1])]
        print(new_list)
    except Exception as error:
        print('ERROR')
