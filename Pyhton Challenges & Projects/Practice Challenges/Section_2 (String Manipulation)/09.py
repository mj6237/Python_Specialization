'''
What the Question Demands: 
1. Ask the user to input an even-length string (e.g., "Python"). 
2. Print the first half of the string. 
'''

user_input = input("Enter a word which has even character in it.").upper()
if len(user_input) %2 == 0 :
    half_length = len(user_input) // 2
    #print(half_length)
    print(user_input[0:half_length])
else :
    print("Invaid input !")