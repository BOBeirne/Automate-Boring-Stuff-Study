def spam():
    global eggs
    eggs = 'spam' # this is a global var
    
def bacon():
    eggs = 'bacon' # this is local var
    
def ham():
    print(eggs) # this is global var
    
eggs = 'global'
spam()
print(eggs) # print 'spam' from spam()
    

