#  Convert minutes to hours and minutes (e.g., 130 minutes → 2 hours, 10 minutes). 

user_min = int(input("Enter minutes :"))
hours = user_min // 60 # using // will give output without floating point number
minutes = user_min % 60
print(f"{hours} hours {minutes} minutes")