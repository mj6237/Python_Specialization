'''
Rewrite your pay computation with time-and-a-half for overtime and create a function 
called computepay which takes two parameters (hours and rate).
'''

def computepay(hours,rate) :
   
    if hours > 40 :
        regular_pay = 40 * rate 
        over_time_hours = hours - 40
        over_time_pay = over_time_hours * rate * 1.5
        final_pay = regular_pay + over_time_pay
        
    else :
        final_pay = hours * rate
    return final_pay

hours = int(input("Enter hours you worked :"))
rate = float(input("Enter rate per hour :"))
pay=computepay(hours,rate)
print(f"Pay {pay}")
