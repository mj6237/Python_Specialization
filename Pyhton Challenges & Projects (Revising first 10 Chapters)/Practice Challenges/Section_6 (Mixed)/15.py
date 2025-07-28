'''
Define a function login_user(username, password, user_db) that takes username, password, and the 
user_db dictionary. 
2. Inside the function, check if the username exists in user_db. 
3. If it exists AND the provided password matches the stored password for that user, print "Login successful!" 
and return True. 
4. Otherwise, print "Invalid username or password." and return False. 
5. Initialize a sample user_db = {"admin": "pass123", "guest": "welcome"}. 
6. Call login_user with valid and invalid credentials and print the return value. 
'''
def login_user(username, password, user_db) :
    if username in user_db and user_db[username] == password:
        #print(username)
        print("Login Successful!")
        return True
    else :
        print("Invalid username or password !")
        return False

user_db = {"admin": "pass123", "guest": "welcome"}
result_1 = login_user("admin", "pass123", user_db)
print(result_1)
#login_user("guest", "pass123", user_db)
result_2 = login_user("fozi", "786", user_db)
print(result_2)