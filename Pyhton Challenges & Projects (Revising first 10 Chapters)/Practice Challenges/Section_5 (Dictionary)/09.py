'''
1. Use the student dictionary (after Problem 5.4). 
2. Use a for loop with two iteration variables to iterate through both keys and values simultaneously. 
3. Print each key and its corresponding value (e.g., "Key: name, Value: Alice"). 
'''

student  = {
    "name" : "Muhammad",
    "age" : 24,
    "major" : "Computer Science"
}

for k, v in student.items() :
    print(f"Key :{k} Value :{v}")