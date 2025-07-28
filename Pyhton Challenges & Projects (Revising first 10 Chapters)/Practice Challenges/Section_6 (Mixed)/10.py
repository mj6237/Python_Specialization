'''
1. Use the people_data list from Problem 6.9. 
2. Use a for loop with two iteration variables to unpack each tuple directly into name and age. 
3. Inside the loop, print a message like "Name: [name], Age: [age]". 
'''
people_data = [("Alice", 30), ("Bob", 24), ("Charlie", 24)]

for name, age in people_data :
    print(f"Name : {name}, Age : {age}")
    