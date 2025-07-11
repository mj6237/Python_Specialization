'''
. Electricity bill calculator 
 Units <= 100 → Rs.5/unit 
 101–300 → Rs.8/unit 
 Above 300 → Rs.10/unit 
Add 18% tax at end
'''

units = int(input("Enter units you have consumed :"))
bill = 0
tax = 0

if units <= 100 :
    bill = units * 5
    tax = (18 / 100) * bill
    total_bill = bill + tax
    print(f"Your total bill is :Rs.{total_bill}/-")
elif units >= 101 and units <= 300 :
    bill = units * 8
    tax = (18 / 100) * bill
    total_bill = bill + tax
    print(f"Your total bill is :Rs.{total_bill}/-")
elif units > 300 :
    bill = units * 10
    tax = (18 / 100) * bill
    total_bill = bill + tax
    print(f"Your total bill is :Rs.{total_bill}/-")