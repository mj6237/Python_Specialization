'''
Ask the user to enter a password. 
2. If the password's length is 8 or more characters, print "Password is long enough." 
3. Otherwise, print "Password is too short."
'''

password = input("Enter your password :")

if len(password) >= 8 :
    print("Password is long enough.")
else :
    print("Password is too short.")