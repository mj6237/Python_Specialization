'''
1. Define a function increase_prices(product_prices, percentage_increase) that takes a dictionary 
(product names as keys, prices as values) and a percentage_increase (e.g., 10 for 10%). 
2. Inside the function, create a new dictionary updated_prices. 
3. Loop through product_prices. For each product, calculate its new price by increasing it by the given 
percentage. 
4. Add the product and its new price to updated_prices. 
5. Return updated_prices. 
6. Call the function with {"Laptop": 1000, "Mouse": 20} and 10 (for 10% increase) and print the result.
'''
def increase_prices(product_prices, percentage_increase) :
    updated_prices = {}
    for key, value in product_prices.items() :
        incr_value = (value / 100) * percentage_increase
        new_value = value + incr_value
        updated_prices[key] = new_value
    return updated_prices

print(increase_prices({"Laptop": 1000, "Mouse": 20}, 10))
