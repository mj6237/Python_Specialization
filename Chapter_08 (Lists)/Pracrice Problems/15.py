'''
Forbidden Username Checker 
o Create a list of forbidden usernames (e.g., ["admin", "root", "test", "guest"]). 
o Ask the user to enter a desired username using input(). 
o Use a condition to check if the entered username is present in the list of forbidden usernames. 
o Print "Username available" or "Username taken (forbidden)" accordingly.
'''

forbidden_usernames = ["admin", "root", "test", "guest"]

user_input = input("Enter username :")
if user_input.lower() in forbidden_usernames :
    print("username is taken (forbidden), Try another one !")
else :
    print("username available")