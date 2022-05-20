import requests
from os import system
import random
import Score

def Currency_RouletteGame(d):
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    dolar = (data["rates"]["ILS"])
    amount = random.sample(range(1, 101), 1)[0]
    t = int(amount * dolar) # int to round the number
    system('cls')
    print(f'Please enter the value of {amount}$:')
    while True:
        try:
            guess = int(input())
            break
        except:
            print('Please enter a number')

    if (t - (5 - d)) < guess < (t + (5 - d)):
        Score.Points_of_winning(d)
        print('This is the correct answer well done !!')
    else:
        print(f'Sorry this is not the answer .. The correct answer is:{t}')
