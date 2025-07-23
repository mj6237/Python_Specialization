'''
Function Name: is_weak_password(password) 
Task
Return "Weak Password" if: 
o Length is less than 8 characters, OR 
o No uppercase letter, OR 
o No number in the password 
 Otherwise, return "Strong Password" 
Concepts: Strings, len(), .isupper(), .isdigit(), any(), conditions, functions
'''

def is_weak_password(password) :
    if len(password) < 8 :
        return "Too Short, Weak Password"
    if not any(char.isdigit() for char in password):
        return "Weak Password"
    if not any (char.isupper() for char in password):
        return "Weak Password"
    return "Strong Password"
password = input("Enter your password :")
suggestion = is_weak_password(password)
print(suggestion)

    
