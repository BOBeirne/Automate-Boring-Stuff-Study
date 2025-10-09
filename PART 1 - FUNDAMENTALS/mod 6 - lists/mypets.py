my_pets = ['lola', 'katie', 'tj']
name = input('enter a pet name:').lower()
if name not in my_pets:
    print('I dont have pet named' + name)
else:
    print(name + ' is my pet.')