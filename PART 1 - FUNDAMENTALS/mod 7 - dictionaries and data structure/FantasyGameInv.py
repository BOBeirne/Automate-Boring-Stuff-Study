#Fantasy Game Inventory

inventory = { 'rope' : 1,
              'torch' : 6,
              'gold' : 42,
              'dagger' : 1,
              'arrow' : 12
            }

#Dragon loot

loot = ['gold','dagger','gold','gold','ruby']

#Display inventory function

def display_inv(inv):
    print('Inventory:')
    item_total = 0
    for key, value in inv.items():
        print(str(value) + ' ' + str(key))
        item_total += value
    print("Total inv items: " + str(item_total))


#Add list to dictionary function

def add_to_inv(inv, loot):
    for item in loot:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1
    # DEBUG: print('Updated inventory: ' , inv)
    return inv 

    



inventory = add_to_inv(inventory, loot)    
display_inv(inventory)
