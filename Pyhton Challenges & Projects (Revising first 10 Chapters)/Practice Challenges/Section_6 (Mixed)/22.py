'''
1. Define a list of (key, value) tuples: data_pairs = [("name", "Alice"), ("age", 30), ("city", 
"New York")]. 
2. Create an empty dictionary result_dict. 
3. Loop through data_pairs. For each tuple, add its first element as a key and its second element as a value to 
result_dict. 
4. Print result_dict.
'''
data_pairs = [("name", "Alice"), ("age", 30), ("city", 
"New York")]

result_dict = {}
for key, value in data_pairs :
    result_dict[key] = value
print(result_dict)