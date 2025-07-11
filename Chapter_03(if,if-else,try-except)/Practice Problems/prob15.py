'''
 Login system (single attempt): 
 Username = "admin", password = "1234" 
 If wrong, print “Access Denied”, else “Welcome!”

'''
username = input("Enter username :")
passwd = input("Enter password :")

if username == "admin" and passwd == "1234" :
    print ("Welcome")
else :
    print("Access Denied")
