#fantasy game inventory
#use this program to display a fantasy game player inventory
#captures inventory items as keys and quantities as values
import pprint

inventoryDict =  {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
def displayinventory(inventoryDict):
    
    print("Inventory:")
    totalItems = 0
    for k,v in inventoryDict.items():
        totalItems += v
        print(str(v) + ' '+  k)
    print("Total number of items: " + str(totalItems))

displayinventory(inventoryDict)
