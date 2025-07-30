'''
1. Initialize an inventory = {"Laptop": 10, "Mouse": 50, "Keyboard": 20}. 
2. Define a function sell_item(inventory_dict, item_name, quantity): 
 Use try-except ValueError for quantity input (assume it's given as a string that needs conversion). 
 If item_name is not in inventory_dict, print "Item not found." 
 Else if quantity is greater than available stock, print "Insufficient stock." 
 Else, reduce the stock and print "Sale successful." 
 Print the updated inventory_dict after each attempt. 
3. Call sell_item with various scenarios: 
 sell_item(inventory, "Mouse", 5) 
 sell_item(inventory, "Laptop", 15) 
 sell_item(inventory, "Monitor", 2) 
 sell_item(inventory, "Mouse", "abc") 
'''

def sell_item(inventory, item_name, quantity) :
    try :
        int_quant = int(quantity)
        if item_name not in inventory :
            print("Item not found")
        elif int_quant > inventory[item_name] :
            print("Insufficient stock.")
        else :
            inventory[item_name] -= int_quant
            print("Sale successful.")
        print(inventory)
    except :
        print("Invalid quantity. Please enter a number")

inventory = {"Laptop": 10, "Mouse": 50, "Keyboard": 20}

sell_item(inventory, "Mouse", 5)
sell_item(inventory, "Laptop", 15)
sell_item(inventory, "Monitor", 2)
sell_item(inventory, "Mouse", "abc")
