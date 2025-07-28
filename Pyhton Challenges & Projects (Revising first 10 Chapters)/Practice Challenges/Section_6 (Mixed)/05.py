'''
1. Define an inventory dictionary: inventory = {"Laptop": 5, "Mouse": 10, "Keyboard": 0}. 
2. Ask the user for an item_name they want to check. 
3. If the item_name exists in inventory AND its stock quantity is greater than 0, print "Item is in stock!". 
4. Else if the item_name exists but its stock quantity is 0, print "Item is out of stock.". 
5. Otherwise (item not found), print "Item not found in inventory."
'''
inventory = {"Laptop": 5, "Mouse": 10, "Keyboard": 0}

item_name = input("Enter name to check if it is available :")
#print(inventory[item_name])

if item_name in inventory :
    quantity = inventory.get(item_name)
    print(quantity)
    if quantity > 0 :
        print("Item is in stock.")
    elif quantity == 0 :
        print("Item is out of stock.")  
else :
    print("Item not found !, Item is not in inventory.")  