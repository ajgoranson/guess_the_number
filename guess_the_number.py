import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    '''Set the high and low values for the random number'''
    return 1, 1000


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high

# Validation Branch here it is
def validation():
    while True:
        try:
            userinput = int(input('Guess the secret number'))
        except ValueError:
            print('This is not an integer, try again')
            continue
        else:
            return userinput
            break
  
        
        


def main():

    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = validation()
        result = check_guess(guess, secret)
        guesses = guesses + 1
        print('The number of guesses youve tried is' + guesses)
        print(result)

        if result == correct:
            break


if __name__ == '__main__':
    main()
