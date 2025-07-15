'''
 Problem 8 - Is Leap Year 
Define a function is_leap(year) that returns: 
 True if year is leap year 
 False otherwise 

� Hint: Leap year rule = divisible by 4, but not by 100 unless divisible by 400. 
'''

def is_leap(year) :
    if (year %4 == 0 and year %100 != 0) or year %400 == 0 :
        return True
    else :
        return False
year = int(input("Enter year :"))
ly = is_leap(year)
print(ly)
