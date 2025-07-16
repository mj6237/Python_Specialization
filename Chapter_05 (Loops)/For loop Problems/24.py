'''
Ask for a number. 
If it reads the same forward & backward (like 121 or 3443), print "Palindrome" 
Else, print "Not a palindrome" 
'''
num = input("Enter a number: ")
#print(num[::-1])
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

