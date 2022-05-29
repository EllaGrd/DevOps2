def welcome(name):
    print(f'Hello {name} and welcome to the World of Games (WoG).')
    print('Here you can find many cool games to play.')

def load_game():
    print('Please choose a game to play:')
    print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back')
    print('2. Guess Game - guess a number and see if you chose like the computer')
    print('3. Currency Roulette - try and guess the value of a random amount of USD in ILS')

    game = int(input('Please choose your game '))
    while game < 1 or game > 3:
        print('Game number must be between 1 and 3')
        game = int(input('Please choose your game '))

    diff = int(input('Please choose game difficulty from 1 to 5 '))
    while diff < 1 or diff > 5:
        print('Difficulty should be a number between 1 to 5')
        diff = int(input('Please choose game difficulty from 1 to 5 '))

    print(f'Your game {game}')
    if game == 1:
        print("Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    elif game == 2:
        print("Guess Game - guess a number and see if you chose like the computer")
    elif game == 3:
        print("Currency Roulette - try and guess the value of a random amount of USD in ILS")
    print(f'Your diificulty level {diff}')

