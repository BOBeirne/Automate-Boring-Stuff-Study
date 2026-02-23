# Fix safe temp program, rewrite the code to fix the errors. 
# You may assume the user always enters valid inputs and not, say, X for the scale or hello for the number of degrees.

scale = input('Enter C or F to indicate Celsius or Fahrenheit:\n').upper()
degrees = float(input('Enter the number of degrees:\n'))


if scale == 'C':
    if degrees <= 16 or degrees >= 38:
        print(f'{degrees}{scale} is DANGEROUS')
    else:
        print(f'{degrees}{scale} is Safe')

elif scale == 'F':
    if degrees <= 60.8 or degrees >= 100.4:
        print(f'{degrees}{scale} is DANGEROUS')
    else:
        print(f'{degrees}{scale} is Safe')




# ORIGINAL CODE

"""
print('Enter C or F to indicate Celsius or Fahrenheit:')
scale = input()
print('Enter the number of degrees:')
degrees = int(input())
if scale == 'C':
    if degrees >= 16 or degrees <= 38:
        print('Dangerous')
    else:
        print('Dangerous')
elif scale == 'F':
    if degrees > 60.8 and degrees >= 100.4:
        print('Safe')
    else:
        print('Dangerous')
"""