'''
1. Define a list: items = ["apple", "banana", "apple", "cherry", "banana", "apple"]. 
2. Create an empty dictionary item_counts. 
3. Loop through items. For each item, update its count in item_counts. 
4. Print item_counts.
'''
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
item_count = {}

for item in items :
    item_count[item] = item_count.get(item, 0) +1
print(item_count)