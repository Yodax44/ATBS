def displayInventory(inventoryDict):
    print("Inventory:")
    totalItems = 0
    for k,v in inventoryDict.items():
        totalItems += v
        print(str(v) + ' '+  k)
    print("Total number of items: " + str(totalItems))

def addToInventory(inventory, addedItems):
    for k in addedItems:
        if k not in inventory:
            inventory.setdefault(k, 1)
        else:
            inventory[k]+=1
    return inventory

inv = {'gold coin': 42, 'rope': 1, 'ruby': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
