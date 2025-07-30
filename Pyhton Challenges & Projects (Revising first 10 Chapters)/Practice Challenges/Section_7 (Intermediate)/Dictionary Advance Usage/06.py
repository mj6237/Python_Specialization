'''
1. Create a dictionary: products = {"Laptop": 1200, "Mouse": 25, "Monitor": 300, "Keyboard": 
75}. 
2. Create a new empty dictionary affordable_products. 
3. Loop through the products dictionary's items (key-value pairs). 
4. If a product's price (value) is less than 100, add that product (key-value pair) to affordable_products. 
5. Print affordable_products. 
'''
products = {"Laptop": 1200, "Mouse": 25, "Monitor": 300, "Keyboard": 
75}

affordable_products = {}

for key, value in products.items() :
    if value < 100 :
        affordable_products[key] = value

print(affordable_products)
