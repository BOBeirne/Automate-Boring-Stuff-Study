while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('please enter nr for your age')
    
while True:
    print('Select a new pwd (letters and nrs only!)')
    pwd = input()
    if pwd.isalnum():
        break
    print('Passwords can only have letters and nrs!')