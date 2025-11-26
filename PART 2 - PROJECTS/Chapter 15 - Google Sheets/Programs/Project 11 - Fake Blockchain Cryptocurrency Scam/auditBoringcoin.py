# program examines all the transactions and generates a dictionary of all accounts and their current balance

import ezsheets

ss = ezsheets.Spreadsheet('https://autbor.com/boringcoin')
accounts = {} # keys are names, and values are amounts

for row in ss.sheets[0].getRows(): # Each row is a transaction. 
	sender, recipient, amount = row[0], row[1], int(row[2]) # Loop over each one assuming each one is a transaction and contains 3 values: sender, recipient, amount
	if sender == 'PRE-MINE': # PRE-MINE is the first transaction, which is the genesis transaction (infinite supply of coins)
			accounts.setdefault(recipient, 0)
			accounts[recipient] += amount
	else:
		accounts.setdefault(sender, 0) # set to 0 if it doesn't exist
		accounts.setdefault(recipient, 0) # set to 0 if it doesn't exist
		accounts[sender] -= amount # decrease the sender's balance
		accounts[recipient] += amount # increase the recipient's balance
print(accounts)

"""
lets go through this dictionary and add up the totals of everyone's balance to find out how many Boringcoins are in the entire network. 
Start a total variable at 0, and then have a for loop go through each value in the key-value pairs of the accounts dictionary. 
After adding each value to total, we can print the total amount of Boringcoins:
"""

total = 0 # start at 0
for amount in accounts.values(): # for each value in the dictionary (each value is a balance)
	total += amount # add it to the total
print(f'Total Boringcoins in the network: {total}') # print the total amount


"""results:
{'Al Sweigart': 999058553, 'Miles Bron': 38283, 'not_a_scammer': 48441, 'some hacker': 44429, 'Tech Bro': 53424, 'Claire Debella': 54443, 'Credulous Journalist': 50408, 'Birdie Jay': 36832, 'Carol': 82867, 'Mark Z.': 68650, 'Bob': 37920, 'Andi Brand': 57218, 'Eve': 88296, 'Al Sweigart sock #27': 78080, 'Tax evader': 40937, 'Duke Cody': 17544, 'Lionel Toussaint': 54650, 'some scammer': 2694, 'Alice': 44503, 'David': 41828}
Total Boringcoins in the network: 1000000000
"""