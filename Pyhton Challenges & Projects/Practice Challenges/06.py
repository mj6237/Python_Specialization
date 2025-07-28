'''
What the Question Demands: 
1. Ask the user to input the current day of the week (e.g., "Monday", "Saturday"). 
2. If the day is "Saturday" or "Sunday", print "It's the Weekend!". 
3. Otherwise, print "It's a Weekday.".
'''

day = input("Enter name of the day :").lower()

if day == "saturday" or day == "sunday" :
    print("It's Weekend dude, Chill out...!!")
else :
    print("It's working Jaano, Kaam pe Jao.")