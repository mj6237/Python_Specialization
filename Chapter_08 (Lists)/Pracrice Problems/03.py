'''
 Login Count by User 
Function Name: count_user_logins(username) 
Task: 
 Open log.txt 
 Count how many lines contain "User 'username' logged in" 
(e.g., "User 'admin' logged in.") 
 Return the count 
Concepts: File reading, string formatting, .count(), loops
'''

def count_user_login(username) :
    count = 0
    with open(r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\log.txt", 'r') as file :
        for line in file :
            if f"User '{username}' logged in" in line :
                count += 1
    return count  
username = input("Enter user name :")
result = count_user_login(username)
print("The user", username, "logged in",result, "times.")
#print(counter)
