import time, sys
indent = 0 # var for how many spaces to indent
indent_increasing = True # switch for increasing or not

try:
    while True: # main loop
        print(' '* indent, end='')
        print('*****')
        time.sleep(0.1) # pause for 1/10th sec
        
        if indent_increasing:
            # increase nr of spaces
            indent += 1
            
            if indent == 20:
                #change direction
                indent_increasing = False
                
        else:
            #decrease nr of spaces:
            indent -= 1
            if indent == 0:
                # change direction again
                indent_increasing = True
                
except KeyboardInterrupt:
    sys.exit()
        
