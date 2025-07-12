'''
Ask user's age and print: 
 Age < 13 → "Child" 
 13-19 → "Teenager" 
 20-59 → "Adult" 
 60+ → "Senior Citizen" 
'''

age = int(input("Enter your age :"))
if age < 13 :
    print("Child")
elif age >= 13 and age <= 19 :
    print("Teenager")
elif age >= 20 and age <=59 :
    print("Adult")
else :
    print("Senior Citizen")