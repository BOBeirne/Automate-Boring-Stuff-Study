# Fizz Buzz is a common programming challenge
# If the integer is divisible by 3, the program should print Fizz.
# If the integer is divisible by 5, the program should print Buzz
# If the integer is divisible by 3 and 5, the program should print Fizz Buzz
# Otherwise, the program should print the number the user entered


def fizzbuzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        print('Fizz Buzz!')
    elif number % 3 == 0:
        print('Fizz!')
    elif number % 5 == 0:
        print('Buzz!')
    else:
        print(number)


print('***** F I Z Z   B U Z Z   C H A L L E N G E *****\n')
number = int(input('Provide a number for a Fizz Buzz Challenge:\n'))
fizzbuzz(number)