from random import randint
from os import system

def welcome(name):
    name = (f'Hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play.')
    return name

def load_game():
    go = False
    while not go:
        print(f'Please choose a game to play:\n'
              f'  1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n'
              f'  2. Guess Game - guess a number and see if you chose like the computer \n'
              f'  3. Currency Roulette - try and guess the value of a random amount of USD in ILS')
        print(':', end='')
        choose1 = int(input())
        if choose1 not in range(1, 4):
            print("Error try again:")
        else:
            go = True

    system('cls')
    go = False
    while not go:
        print('Please choose game difficulty from 1 to 5:')
        print(':', end='')
        choose2 = int(input())
        if choose2 not in range(1, 6):
            print("Error try again:")
        else:
            go = True
    return (choose1,choose2)

def generate_number(n):
    result = randint(1,n)
    return result

def get_guess_from_user(x):
    print('Please guess a number:')
    choose = int(input())

    if generate_number(choose) == x:
        return f"I also chose:{x} well done !!!"
    else:
        return f"I chose:{x} you did not succeed ... Too bad"
