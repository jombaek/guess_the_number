from random import randint

def computer_number(min_number, max_number):
    '''
    function that generates a random number between min_number and max_number.
    returns random int
    '''
    return randint(min_number, max_number)

def player_guess(min_number, max_number):
    '''
    function that asks the player for a number.
    return player int
    '''
    player_input = int(input(f'Guess a number between {min_number} and {max_number}: '))
    return player_input

def play():
    # get range input
    low = int(input('Enter Lower bound: '))
    high = int(input('Enter Upper bound: '))

    # get number from computer and player
    computer_choice = computer_number(low, high)
    player_choice = player_guess(low, high)

    # loop until player guesses the number
    while computer_choice != player_choice:
        if computer_choice > player_choice:
            player_choice = int(input('Your number is too small! Try again: '))
        elif computer_choice < player_choice:
            player_choice = int(input('Your number is too big! Try again: '))

    print('Congratulation! You guessed the number.')

play()