# It’s possible to write the safe temperature logic of the previous program in a single condition. 
# Fill in the blank in the following program with this condition to make it work in the same way as the previous program:


scale = input('Enter C or F to indicate Celsius or Fahrenheit:\n').upper()
degrees = float(input('Enter the number of degrees:\n'))

if (scale == 'C' and (degrees <= 16 or degrees >= 38)) or (scale == 'F' and (degrees <= 60.8 or degrees >= 100.4)):
    print(f'{degrees}{scale} is DANGEROUS')
else:
    print(f'{degrees}{scale} is Safe')


# ORIGINAL CODE

"""
print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input()
print('Enter the number of degrees:')
degrees = int(input())
if ____:
    print('Safe')
else:
    print('Dangerous')
"""