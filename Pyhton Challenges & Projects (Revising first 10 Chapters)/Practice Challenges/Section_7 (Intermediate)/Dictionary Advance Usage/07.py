'''
1. Create a nested dictionary: 
2. company = {      
"employees": { 
"Alice": {"age": 30, "department": "HR"}, 
"Bob": {"age": 24, "department": "IT"} 
}, 
"location": "Main Office" }
9. Print Bob's age. 
10. Print Alice's department
'''
company = {      
"employees": { 
"Alice": {"age": 30, "department": "HR"}, 
"Bob": {"age": 24, "department": "IT"}, 
"location": "Main Office" }}

print("Bob's age :",company["employees"]["Bob"]["age"])
print("Alice's depatment :",company["employees"]["Alice"]["department"])