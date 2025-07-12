'''
Ask for age: 
 Age < 5 or age > 60 → Free 
 Age 5-18 → Rs. 250 
 Age 19-59 → Rs. 500 
Also, ask if it's the weekend (yes/no): 
 If weekend, add Rs. 100 extra
'''

age = int(input("Enter your age :"))
weekend = int(input("If its weekend press 1 if not press 0:"))
ticket_price = 0
if age < 5 or age > 60 :
    print("You can enter free :")
elif age >= 5 and  age <= 18 :
    ticket_price += 250 
    if weekend == 1 :
        ticket_price += 100
        print(f"Your ticket price is : Rs.{ticket_price}/-")
    else :
        print(f"Your ticket price is : Rs.{ticket_price}/-")
elif age >18 and age <= 60 :
    ticket_price += 500
    if weekend == 1 :
        ticket_price += 100
        print(f"Your ticket price is : Rs.{ticket_price}/-")
    else :
        print(f"Your ticket price is : Rs.{ticket_price}/-")