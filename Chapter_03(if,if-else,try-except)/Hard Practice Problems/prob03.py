'''
 Three Digits Classification 
Ask the user for a 3-digit number. Extract the digits: 
 Count how many of the 3 digits are: 
o Greater than 5 
o Less than or equal to 5 
Hint: Use integer math (//, %) and if statements only.
'''

num = int(input("Enter a three digit number :"))

digit1 = num // 100       # 7 (hundreds place)
digit2 = (num % 100) // 10  # 3 (tens place)
digit3 = num % 10         # 8 (ones place)
print(f"Digit 1 = {digit1}\nDigit 2 = {digit2}\nDigit 3 = {digit3} ")
greater = 0
less_or_equal = 0
if digit1 > 5 :
    greater += 1
else :
    less_or_equal += 1
if digit2 > 5 :
    greater += 1
else :
    less_or_equal += 1
if digit3 > 5 :
    greater += 1
else :
    less_or_equal += 1

print(f"Digits > 5 : {greater}")
print(f"Digits <= 5 : {less_or_equal}")