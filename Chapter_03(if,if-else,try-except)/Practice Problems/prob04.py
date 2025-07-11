 # Check if a number is divisible by 2 OR 3 but not both 
num = int(input("Enter a number :"))

if (num %2 == 0) ^ (num %3 == 0)  : #True only when one of them is true
# if (num % 2 == 0 and num % 3 != 0) or (num % 3 == 0 and num % 2 != 0):
    print("The number is divisible by 2 or 3, but not both")
else :
    print("The number is either divisible by both or neither")