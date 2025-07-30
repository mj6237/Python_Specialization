'''
1. Create a dictionary: sales_data = {"Jan": 150, "Feb": 200, "Mar": 180, "Apr": 220}. 
2. Find the month (key) that had the maximum sales (value). 
3. Print the month and its sales figure.
'''
sales_data = {"Jan": 150, "Feb": 200, "Mar": 180, "Apr": 220}

max_month = ""
max_value = 0

for key, value in sales_data.items():
    if value > max_value:
        max_value = value
        max_month = key

print(f"Highest Sales: {max_month} with {max_value}")
