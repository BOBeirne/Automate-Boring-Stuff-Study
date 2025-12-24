# calculate product of first 100k nrs

import time
def calc_product():
	# calculate product of first 100k nrs
	product = 1
	for i in range (1, 100001):
		product = product * i
	return product

start_time = time.time()
result = calc_product()
end_time = time.time()
print(f'It took {end_time - start_time} s to run this program')
# It took 4.307938814163208 s to run this program