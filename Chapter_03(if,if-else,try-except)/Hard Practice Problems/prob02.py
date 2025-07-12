'''
Ask the user to enter a number: 
 If between 1 and 100 → “Low range” 
 101 to 1000 → “Mid range” 
 Greater than 1000 → “High range” 
 Anything else → “Invalid range” 
'''
try:
    num = int(input("Enter a number :"))
    if num <= 0 :
        print("0 and negative numbers are not allowed !")
    else :
        print ("Correct input , Lets Proceed")
    if num >= 1 and num <=100 :
        print("Low range")
    elif num > 100 and num <= 1000 :
        print("Mid range")
    elif num > 1000 :
        print("High range")
except ValueError:
    print("Enter only positive number (e.g , 77 , 56 )")