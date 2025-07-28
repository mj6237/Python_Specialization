'''
What the Question Demands: 
1. Define a variable secret_word = "python". 
2. Ask the user to input a guess for the secret word. 
3. If the user's guess exactly matches the secret_word, print "Access Granted!". 
4. Otherwise, print "Access Denied!".
'''

sec_code = input("Enter secret code to enter :")

if sec_code == "python" :
    print("Access grandted, your welcome.")
else :
    print("Access Denied ! Try Again.")