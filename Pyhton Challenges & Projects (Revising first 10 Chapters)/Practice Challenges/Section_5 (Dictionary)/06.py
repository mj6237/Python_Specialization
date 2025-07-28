'''
1. Use the student dictionary (after Problem 5.4). 
2. Try to get the value for the key "phone". If it's not found, return "N/A". Print the result. 
3. Try to get the value for the key "age". Print the result. 
'''

student = {
    "name" : "Muhammad",
    "age" : 24,
    "major" : "Computer Science"

}

print(student.get("phone", "N/A"))
print(student.get("age", "N/A"))
