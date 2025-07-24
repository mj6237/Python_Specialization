'''
4. Email Format Checker 
Function Name: is_valid_email(email) 
Task: 
 Return True if: 
o Contains exactly one @ 
o Ends with .com or .net 
o Does not contain any space 
 Else return False 
Concepts: Strings, .count(), .endswith(), in, .isspace() 

'''

def is_valid_email(email):
    if  email.count("@") == 1 and " " not in email and (email.endswith(".com") or email.endswith(".net")) :
        return True
    else :
        return False

email = input("Enter your email address :")
result = is_valid_email(email)
print(result)

