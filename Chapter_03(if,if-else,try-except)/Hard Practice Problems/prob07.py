'''
Ask user for a 3 digit number. If: 
 Sum of digits is 7 or divisible by 7 → "Lucky Number" 
 Else → "Not Lucky"
'''

num = int(input("Enter a number from 1-3 digits :"))
digit1 = num // 100
digit2 = (num % 100) // 10
digit3 = num % 10
sum = digit1 + digit2 + digit3

if sum == 7 or sum % 7 == 0 :
    print("Lucky")
else :
    print ("Not lucky")