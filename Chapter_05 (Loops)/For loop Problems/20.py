'''
Keep asking the user to enter a password until they enter "open123" 
 If wrong: print "Wrong password. Try again." 
 If correct: print "Access granted!" and end the loop 
�
� Use: while True, break, if-else
'''
while True :
    password = input("Enter password :")
    if password == "open123":
        print("Access granted !")
        break
    else :
        print("Wrong password. Try Again....!!")
