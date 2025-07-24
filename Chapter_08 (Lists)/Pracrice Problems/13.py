'''
Password Strength Checker (Basic) 
o Create a function called check_password_strength that takes a password (string) as input. 
o Inside the function, use variables to store minimum length requirements (e.g., min_length = 8). 
o Use an if-else condition to check if the password meets the minimum length. 
o If it meets the length, print "Password meets minimum length." Otherwise, print "Password is too short." 
'''
def check_password_strength(password) :
    min_length = 8
    if len(password) >= min_length :
        print("Password meet the minimum length, Strong Password")
    else :
        print("Password is too short ")

password = input("Enter you password :")
check_password_strength(password)