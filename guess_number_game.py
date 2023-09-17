secret_number = 88
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count += 1
    if guess == secret_number:
        print('Congratulations, you guessed it.')
        break;
    elif guess > secret_number:
        print('Your number is greater than secret number')
    elif guess < secret_number:
        print('Your number is less than secret number')    
else:
    print (f'You have used all your attempts. The correct answer was {secret_number}')