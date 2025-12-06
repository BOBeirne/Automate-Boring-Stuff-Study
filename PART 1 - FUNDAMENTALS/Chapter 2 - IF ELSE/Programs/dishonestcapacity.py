print('Enter TB or GB for the advertised unit:')
unit = input('>')

#calculate the amount that the advertised capapcity lies
if unit == 'TB' or unit == 'tb':
	discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb':
	discrepancy = 1000000000 / 1073741824
	
print('enter advertised capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

# calc real capacity and round up to nearest hundreths and convert to a str so it can be concantenated
real_capacity = str(round(advertised_capacity * discrepancy, 2))
#
print(' The actual capacity is ' + real_capacity + ' ' + unit)


# Gemini's suggestion
''' print('Enter TB or GB for the advertised unit:')
unit = input('>').lower()

# Define byte conversion factors
# Decimal (base-10) used by manufacturers
DECIMAL_GB = 10**9
DECIMAL_TB = 10**12

# Binary (base-2) used by operating systems
BINARY_GB = 2**30  # Gibibyte (GiB)
BINARY_TB = 2**40  # Tebibyte (TiB)

#calculate the ratio between decimal (advertised) and binary (actual) values
if unit == 'tb':
	discrepancy_ratio = DECIMAL_TB / BINARY_TB
elif unit == 'gb':
	discrepancy_ratio = DECIMAL_GB / BINARY_GB
else:
	print(f"Error: Invalid unit '{unit}'. Please enter 'TB' or 'GB'.")
	exit()

print('Enter advertised capacity:')
advertised_capacity = float(input('>'))

# The actual capacity is the advertised amount multiplied by the discrepancy ratio
real_capacity = round(advertised_capacity * discrepancy_ratio, 2)

print(f'The actual capacity is {real_capacity} {unit.upper()}')

'''