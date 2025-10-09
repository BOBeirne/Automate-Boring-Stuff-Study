import random, sys
nr_of_streaks = 0
HT = []


    
try:
    for experiment_nr in range(1000): 
    #create 100 tails and heads
        for x in range(100):
            if random.randint(0, 1) == 1: # 0 is tails 1 is heads
                HT.append('H')
                #print('H')
            else:
                HT.append('T')
                #print('T')
                
    #check if there is streak of 6 of heads or tail in a row
    list_length = len(HT)
    #print(list_length)
    random_index = random.randint(0, list_length - 1)
    for i in range(random_index):
        if HT[i:i + 6] == ['H', 'H', 'H', 'H', 'H', 'H']:
            nr_of_streaks += 1
            #print('streak found for H')
        elif HT[i:i + 6] == ['T', 'T', 'T', 'T', 'T', 'T']:
            nr_of_streaks += 1
            #print('streak found for T')

    
    print('chance of streak: %s%%' % (nr_of_streaks /100))
except KeyboardInterrupt:
    sys.exit() #end program using ctrl+C