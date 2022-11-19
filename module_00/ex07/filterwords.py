# Make a program that takes a string S and an integer N as argument and print the list
# of words in S that contains more than N non-punctuation characters.

from sys import argv

def check_argv_specs(args):
    if len(args) == 2:
        return
    try:
        # s
    except:
        raise 'ERROR'
    

if __name__ == '__main__':
    try:
        check_argv_specs(argv[1:])
    except Exception as error:
        print(error)
    arg_check = True if len(argv) != 2 else True if argv[0].isdigit() == False and argv[1].isdigit() else False
    print('ERROR' if arg_check else '')
