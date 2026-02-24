# Instead of creating a plain tree like the one in the previous project, 
# write a program that prints a Christmas tree with o ball ornaments randomly replacing ^ branch characters


import random

#width = 15 # testing
width = input('>how wide should the tree be?\n')
width = int(width) # convert to int



for layer in range(1,width+2,2):  # skip every 2 branches, start from 1 and compensate for missing layer
    nrOfSpaces = (width -  layer) // 2 # calculate the number of spaces per layer
    layerChars = []
    for i in range(layer): # loop through each branch in layer
        if random.randint(1, 4) == 1:
            layerChars.append('o')
            #print('o')
        else:
            layerChars.append('^')
            #print('^')
    
    print(' ' * nrOfSpaces + ''.join(layerChars)) # for each layer print branches

print(f' '* (width // 2) + '#')
print(f' '* (width // 2) + '#')


