today_is_opposite_day = True

#Set say_it_is_opposite_day based on today_is_opposite_day
if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False
    
    
# IF IT IS THE OPPOSITE DAY, TOGGLE say_it_is_opposite_day
if today_is_opposite_day == True:
    say_it_is_opposite_day = not say_it_is_opposite_day
    
print(say_it_is_opposite_day)
    
# Say what day it is 
if say_it_is_opposite_day == True:
    print('Today is opposite day')
else:
    print("Today is not opposite day")