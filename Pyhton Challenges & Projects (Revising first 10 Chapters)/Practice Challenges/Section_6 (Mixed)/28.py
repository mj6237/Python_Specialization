'''
1. Define a function update_user_age(user_db, username, new_age) that takes a dictionary user_db, a 
username, and a new_age. 
2. Use a try-except block. 
3. Inside try: 
 Convert new_age to an integer. 
 Check if username exists in user_db. 
 If it exists, update the user's age. Print "Age updated successfully." and return True. 
 If username does not exist, print "User not found." and return False. 
4. In except ValueError, print "Error: Invalid age format. Please enter a number." and return False. 
5. Initialize a sample user_db = {"Alice": {"age": 25}, "Bob": {"age": 30}}. 
6. Call the function with various inputs (e.g., ("Alice", 26), ("Charlie", 30), ("Bob", "twenty")) and 
print the return values and the updated user_db.
'''
def update_user_age(user_db, username, new_age):
    try :
        new_age = int(new_age)
        if username in user_db :
            user_db[username]["age"] = new_age
            print("Age updated successfully.")
            return True
        else :
            print("User not found.")
            return True
    except ValueError :
        print("Invalid age format, Enter a number.")

user_db = {"Alice": {"age": 25}, "Bob": {"age": 30}}
print(user_db)

result = update_user_age(user_db,"Alice", 24)
print(user_db)
print(result)