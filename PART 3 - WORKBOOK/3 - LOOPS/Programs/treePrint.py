# Use a for loop to print a triangular pine tree of a size the user asks for. 
# The tree branches should be printed as a number of rows of ^ characters, while the trunk should always be two # characters. 


width = input('>how wide should the tree be?\n')
width = int(width) # convert to int

for layer in range(1,width+2,2):  # skip every 2 branches, start from 1 and compensate for missing layer
    nrOfSpaces = (width -  layer) // 2 # calculate the number of spaces per layer
    print(' ' * (nrOfSpaces) + '^' * layer) # for each layer print branches

print(f' '* (width // 2) + '#')
print(f' '* (width // 2) + '#')

