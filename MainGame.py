from Live import load_game, welcome
from GuessGame import get_guess_from_user
from MemoryGame import Memory_game
from CurrencyRouletteGame import Currency_RouletteGame
from time import sleep
from os import system

# Run this from the command line  "python MainGame.py" !!!

system('cls')
print(welcome("Doron"))
data = load_game()

while True:
    if data[0] == 1:
        system('cls')
        print('You chose: Memory Game')
        sleep(2)
        Memory_game(data[1])
    elif data[0] == 2:
        system('cls')
        print('You chose: Guess Game')
        sleep(2)
        print(get_guess_from_user(data[1]))
    else:
        system('cls')
        print('You chose: Currency Roulette')
        sleep(2)
        Currency_RouletteGame(data[1])
    print('Do you want to play again? \ny/n ?')
    if input() != 'y':
        system('cls')
        break