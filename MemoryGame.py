from os import system
from time import sleep
import random
import Score


def Memory_game(x):
    randomlist = random.sample(range(1, 101), x)
    print(f'In three seconds I will now show you {x} numbers try to remember them..')
    sleep(2)
    for i in range(0,4): # Countdown timer for 3 Seconds
        sleep(1)
        system('cls')
        print(3-i)

    for i in randomlist: # Number display
        system('cls')
        print(f'The number is:{i}')
        sleep(0.7)
    system('cls')
    print("OK i hope you remember...")

    for i in range(len(randomlist)+1): # Request the numbers from the user
        system('cls')
        if i == 0:
            print("Please enter the first number")
        elif i == (len(randomlist)):
            print('Well done you won !!!')
            Score.Points_of_winning(x)
            break
        else:
            print('Well done !! please enter the following number..')

        if randomlist[i] != int(input()): # Checking the numbers
            print('Sorry this is not the right number Too bad ..')
            break