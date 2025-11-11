def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('symbol must be single char str')
    if width <= 2:
        raise Exception('width must be greater than 2')
    if height <= 2:
        raise Exception('Height must be greater than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print (symbol * width)
    
try:
    box_print('*', 4, 4)
    box_print('0', 20, 5)
    box_print('x', 1, 3)
    box_print('ZZ', 3 ,3)
except Exception as err:
    print('an exception happened: ' +str(err))