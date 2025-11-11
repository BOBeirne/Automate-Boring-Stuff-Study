# example of how to use list in this example
'''
print('enter name of the cat 1:')
cat1 = input()

print('enter name of the cat 2:')
cat2 = input()

print('enter name of the cat 3:')
cat3 = input()

print('enter name of the cat 4:')
cat4 = input()

print('cat names are:')
print(cat1 + ', ' + cat2 + ', ' + cat3 + ', ' + cat4)
'''


names = []
while True:
    print('enter cat\'s name ' + str(len(names) + 1) + ' or enter nothing to stop program')
    name = input()
    if name == '':
        break 
    names = names + [name] #concatenation
print('cat names are:')
for name in names:
    print(' ' + name)