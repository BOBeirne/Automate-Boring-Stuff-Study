import random 
pets = ['dog', 'cat', 'moose']
print(random.choice(pets)) #returns randomly selected item

# random.choice() is shortened version of
# some_list[random.randint(0, len(some_list) -1)]

random.shuffle(pets)
print(pets)