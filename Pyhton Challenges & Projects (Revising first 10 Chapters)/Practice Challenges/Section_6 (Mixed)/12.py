'''
1. Define a list with duplicates: items = ["apple", "banana", "apple", "cherry", "banana", 
"date"]. 
2. Create a new empty list unique_items. 
3. Loop through items. If an item is NOT already in unique_items, add it. 
4. Print unique_items.
'''
items = ["apple", "banana", "apple", "cherry", "banana", 
"date"]
unique_items = []
for item in items :
    if item not in unique_items :
        unique_items.append(item)
print(unique_items)