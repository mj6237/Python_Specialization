'''
1. Use a while True loop. 
2. Inside the loop, ask the user to "Enter a command (type 'exit' to quit):". 
3. If the user's input is "exit" (case-insensitive), print "Exiting program." and break the loop. 
4. Otherwise, print "Command received: [user_input]". 
'''

while True :
    command = input("Enter command (type 'exit' to quit) :")
    if command.upper() == "EXIT" :
        print("Exiting program...")
        break
    else :
        print(f"Commad received : {command}")