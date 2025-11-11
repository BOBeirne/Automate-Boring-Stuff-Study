import random

messages = ['certainly',
            'decidedly so',
            'yes definitely',
            'hazy try again',
            'try again later',
            'ask again']
input('ask yes or no question:')
#print(messages[random.randint(0, len(messages) -1)])
print(random.choice(messages))