# guess the nr game
import random
secret_nr = random.randint(1, 100)
print('Im thinking of nr between 1 and 100')

# ask to guess 6 times
for guesses_taken in range(1, 10):
    print('Take a guess')
    guess = int(input('>'))
    
    if guess < secret_nr:
        print('too low')
    elif guess > secret_nr:
        print('too high')
    else:
        break #this is correct guess

if guess == secret_nr:
    print('congrats, you got it in ' +str(guesses_taken) + ' guesses')
else:
    print('wrong, the nr was ' +str(secret_nr))