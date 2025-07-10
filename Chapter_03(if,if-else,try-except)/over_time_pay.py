'''  Rewrite your pay computation to give the employee 1.5 times the hourly rate for 
hours worked above 40 hours. '''

try:
    hours = float(input("Enter hours you worked :"))
    rate = float(input("Enter rate per hour :"))
    pay = hours * rate

    if hours > 40 :
        regular_pay = 40 * rate
        over_time_hours = hours - 40
        over_time_pay = over_time_hours * rate * 1.5
        final_pay = regular_pay + over_time_pay
        print(f"Your pay is : Rs.{final_pay}/-")

    else :
        print(f"Your pay is : Rs.{pay}/-")

except:
    print("Enter a valid number !")