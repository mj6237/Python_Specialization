'''
1. Define a function register_user(username, password, user_db) that takes a username, password, and 
a dictionary user_db (which stores existing users). 
2. Inside the function, check if the username already exists as a key in user_db. 
3. If it exists, print "Username already taken." and return False. 
4. Otherwise, add the username as a key to user_db with the password as its value. Print "Registration 
successful!" and return True. 
5. Initialize an empty dictionary users = {}. 
6. Call register_user twice: once with a new user, and once trying to register the same user again. Print the users dictionary after each call. 
'''
def register_user(username, password, user_db) :
    if username in user_db :
        print("username already taken !.")
        return False
    else :
        user_db[username] = password
        print("Registration Successful!")
        return True

users = {}

register_user("newuser", "pass123", users)
#print(users)
register_user("newuser", "pass456", users)
print(users)