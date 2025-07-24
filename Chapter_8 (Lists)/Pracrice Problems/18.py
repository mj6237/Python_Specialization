'''
User List Generator 
o Create an empty list called users. 
o Use a while loop that continues to ask the user to enter new usernames. 
o The loop should stop when the user types "done". 
o After the loop, print all the usernames collected in the users list.
'''

users = []
while True :
    user_input = input("Enter user name :")
    if user_input in users :
        print("This user already exist !")
    elif user_input == "done" :
        break
    else :
        users.append(user_input)

print(users)