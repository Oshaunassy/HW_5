from settings_ini import MY_MONEY
from hw_5 import numbers, lucky

def play_game():
    capital = MY_MONEY

    while True:
        if capital == 0:
            break
        print(f'You capital is {capital}')

        while True:
            try:
                bet = int(input('Сделайте ставку: '))
                if bet > 30 or bet < 1:
                    print('your bet false, enter correct number')
                else:
                    break
            except:
                ValueError
                print('this number is not correct')
        rate_bet = int(input('enter the rate of bet: '))
        winning_number = numbers()
        if lucky(winning_number, bet):
            capital += rate_bet * 2
            print(f'{winning_number}, you won!!!')
        else:
            capital -= rate_bet
            print(f'You lost!!! {winning_number}')
        new_game = input(f'do you want to continue the game?: your capital is: {capital} y/n')
        if new_game.lower() != 'y':
            break
    print('GAME OVER!!!')

play_game()
