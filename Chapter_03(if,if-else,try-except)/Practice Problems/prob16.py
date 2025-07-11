#  Income Tax Calculator 
'''
 Income <= 5L → 0% 
 5-10L → 10% 
 10-20L → 20% 
 20L+ → 30% '''
tax = 0
income = int(input("Enter Your Income :"))
if income <= 500000 :
    print("No income tax")
elif income >500000 and income <=1000000 :
    tax =  (0.10 * income)
    print(f"Your income tax is : Rs.{tax}")
elif income >1000000 and income <=2000000 :
    tax =  (0.20 * income)
    print(f"Your income tax is : Rs.{tax}")
else :
    tax =  (0.30 * income)
    print(f"Your income tax is : Rs.{tax}")

