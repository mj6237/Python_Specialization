'''
Define a function greet_time(hour): 
o If hour < 12 → return "Good morning" 
o If hour < 18 → "Good afternoon" 
o Else → "Good evening"
'''

def greet_time(hour) :
    if hour < 12 :
        return "Good Morning !"
    elif hour < 18 :
        return "Good Afternoon !"
    else :
        return "Good Evening !"

hour = int(input("Enter Current Time :"))
greet = greet_time(hour)
print(greet)