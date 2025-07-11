'''   Ask user to enter a number from 1 to 7 and print the corresponding day name 
 1 = Monday, 7 = Sunday, others = invalid  
'''
try:
    user_inp = int(input("Enter number from 1-7 :"))
    if user_inp == 1 :
        print("Monday")
    elif user_inp == 2 :
        print("Tuesday")
    elif user_inp == 3 :
        print("Wednesday")
    elif user_inp == 4 :
        print("Thursday")
    elif user_inp == 5 :
        print("Friday")
    elif user_inp == 6 :
        print("Saturday")
    elif user_inp == 7 :
        print("Sunday")
    else :
        print("Invalid Number")
except ValueError :
    print("Enter valid number from 1-7")