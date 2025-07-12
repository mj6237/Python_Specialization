'''
ATM Withdrawal Validator 
Ask user to enter withdrawal amount: 
 Must be multiple of 500 
 Must not exceed balance (assume balance = 50,000) 
 If valid, show remaining balance 
 Else, show appropriate error
'''
try:
    balance = 50000
    print("Please Enter amount which must be multiple of 500")
    amount = int(input("Enter amount :"))
    if amount % 500 == 0 and amount <= balance:
        remaining_amount = balance - amount
        print(f"Your remaining amount is : Rs.{remaining_amount}/-")
    else :
        print("Enter amount multiple of 500 and within range of your balance")
except ValueError :
    print("Invalid input Please Enter Correct amount( e.g , 5000 , 17000) !")
