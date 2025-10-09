


def collatz(number):
    while number > 2:
        if number % 2 == 0: # if even nr
            number = number // 2
            print(number, end=' ')
            
        if number % 2 == 1: # if odd nr
            number = (number * 3) + 1
            print(number, end=' ')
            
        if number == 1:
            print(number)
            break

    
try:    
    print('enter nr')
    number = int(input('>'))
    collatz(number)
except ValueError:
        print('Enter integer.')
        number = int(input('>'))

