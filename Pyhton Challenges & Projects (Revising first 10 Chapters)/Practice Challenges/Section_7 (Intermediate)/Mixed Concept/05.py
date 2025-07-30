'''
1.Define a function get_total_sales_for_product(records, product) that takes the sales_records list 
and a product name (string). 
2. Inside the function, initialize total_sales = 0. 
3. Loop through each record tuple in records. 
4. Unpack the record tuple into p_name, qty, price. 
5. If p_name matches the product (case-insensitive), calculate qty * price and add it to total_sales. 
6. Return total_sales.
'''
def get_total_sale_for_product(records, product):
    total_sales = 0
    for p_name, qty, price in records :
        if p_name.lower() == product.lower() :
            total_sales += qty * price
    return total_sales

records = [ 
("Laptop", 2, 1200),
("Mouse", 5, 20), 
("Laptop", 1, 1200), 
("Keyboard", 3, 75), 
("Mouse", 10, 20) ] 

result1 = get_total_sale_for_product(records, "Laptop")
print(f"Total sales for Laptop :{result1}")
result2 = get_total_sale_for_product(records, "Mouse")

print(f"Total sales for Mouse :{result2}")
