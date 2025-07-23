'''
 Count Passwords Containing Digits 
Function Name: count_digit_passwords(passwords) 
Task: 
 Count how many passwords in the list contain at least one digit 
 Return the count 
Concepts: Lists, string iteration, .isdigit(), any() 

'''

def count_digit_passwords(passords) :
    with open(passords, 'r') as file :
        count = 0
        for line in file :
            line = line.rstrip()
            if any(char.isdigit() for char in line):
                count += 1
        return count
    
passwords = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\passwords.txt"
total = count_digit_passwords(passwords)
print(total)
