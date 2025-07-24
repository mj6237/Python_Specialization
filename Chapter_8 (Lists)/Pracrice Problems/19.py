'''
Password List Filter 
o You have a list of passwords: passwords = ["password123", "securePWD", "12345", "MySecretPass", 
"abc"]. 
o Create a new empty list called long_passwords. 
o Use a for loop to iterate through the passwords list. 
o Inside the loop, use a condition to check if a password's length is greater than 7 characters. 
o If it is, add that password to the long_passwords list. 
o Finally, print the long_passwords list.
'''
passwords = ["password123", "securePWD", "12345", "MySecretPass", "abc"]
long_passwords = []

for p in passwords :
    if len(p) > 7 :
        long_passwords.append(p)
print(long_passwords)