import random, sys

print('ROCK, PAPER, SCISSORS')
wins = 0
loses = 0
ties = 0

while True: #main loop
    print('%s Wins, %s Loses, %s Ties' % (wins, loses, ties))
    while True: #player input loop
        print('enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        player_move = input('>')
        if player_move == 'q':
            print('exiting...')
            sys.exit() #quit
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break #stop asking for input  
        else:     
            print('Type one of r, p, s or q')    
    # player move
    if player_move == 'r':
        print('ROCK vs...')
    if player_move == 'p':
        print('PAPER vs...')
    if player_move == 's':
        print('SCISSORS vs...')
        
    # computer move
    move_number = random.randint(1,3)
    if move_number == 1:
        computer_move = 'r'
        print('...ROCK')
    if move_number == 2:
        computer_move = 'p'
        print('...PAPER')
    if move_number == 3:
        computer_move = 's'
        print('...SCISSORS')
        
    # display and record win/lose/tie
    if player_move == computer_move:
        print('Tie')
        ties += 1
        
    elif player_move == 'r' and computer_move == 's' or player_move == 'p' and computer_move == 'r' or player_move == 's' and computer_move == 'p':
        print('you win!')
        wins += 1
    else:
        print('You lose')
        loses += 1