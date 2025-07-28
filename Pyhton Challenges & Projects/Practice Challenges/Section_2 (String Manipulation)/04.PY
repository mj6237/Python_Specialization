'''
What the Question Demands: 
1. Ask the user to input a string that might have spaces at its beginning or end (e.g., " hello world "). 
2. Print the string with leading and trailing whitespace removed.
'''

user_input = input("Enter a sentence :")
print(user_input,"=",user_input.strip())