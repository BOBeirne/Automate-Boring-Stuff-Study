# Write a program that prints a rectangle of capital O characters.

nr = int(input('Enter the desired number of letters: \n'))
#input = 5 # test

def print_square(number):
    sq_height = number # establish height of square
    for sq_height in range(number):
        print('O' * number)    


print_square(nr)