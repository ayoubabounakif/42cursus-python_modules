from random import randint

TRIAL = 0

__doc__ = '''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n'''

GUESS_MESSAGE = "What's your guess between 1 and 99?\n>> "
INPUT_ERROR = "That's not a valid number!"
EXIT_GAME_MESSAGE = 'Goodbye!'
DOUGLAS_ADAMS_REF = 'The answer to the ultimate question of life, the universe and everything is 42.'
FIRST_TRY_MESSAGE = 'Congratulations! You got it on your first try!'

SECRET_NUMBER = randint(1, 99)

def init_game():
    print('SN -> ' + str(SECRET_NUMBER))
    while True:
        inp = input(GUESS_MESSAGE)
        global TRIAL
        TRIAL += 1
        if ((inp == 'exit') or (inp.isdigit()) and (int(inp) > 0 and int(inp) < 100)):
            start_game(inp)
            break
        print(INPUT_ERROR)

def start_game(inp):
    if inp == 'exit':
        exit(EXIT_GAME_MESSAGE)
    global SECRET_NUMBER
    if int(inp) == SECRET_NUMBER:
        if SECRET_NUMBER == 42:
            print(DOUGLAS_ADAMS_REF)
        print(FIRST_TRY_MESSAGE if TRIAL == 1 else 'You won in {} attempts!'.format(TRIAL))
    else:
        init_game()

if __name__ == '__main__':
    print(__doc__)
    init_game()
