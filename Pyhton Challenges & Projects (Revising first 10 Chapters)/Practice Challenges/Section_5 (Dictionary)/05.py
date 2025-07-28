'''
Use the student dictionary (after Problem 5.4). 
2. Check if the key "email" exists in the dictionary. Print "Email key exists." or "Email key does NOT exist." 
accordingly. 
3. Check if the key "name" exists in the dictionary. Print "Name key exists." or "Name key does NOT exist." 
accordingly. 
'''

student = {
    "name" : "Muhammad",
    "age" : 24,
    "major" : "Computer Science"

}

if "email" in student :
    print("Email exists in the student database.")
else :
    print("Email do not exists in student database")

if "name" in student :
    print("Name exists in student database.")
else :
    print("Name do not exists in student database.")