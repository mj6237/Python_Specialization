'''
1. Create two dictionaries: dict1 = {"a": 1, "b": 2} and dict2 = {"b": 3, "c": 4}. 
2. Merge dict2 into dict1 such that dict1 is updated with all items from dict2, and dict2's values override 
any existing keys in dict1. 
3. Print the modified dict1. 
'''


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

dict1.update(dict2)
print(dict1)