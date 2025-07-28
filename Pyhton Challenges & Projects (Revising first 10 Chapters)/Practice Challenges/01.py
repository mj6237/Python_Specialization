# Problem 1.1: Even or Odd Checker 
'''
What the Question Demands: 
1. Ask the user to input an integer. 
2. Check if this number is even. 
3. If it's even, print "The number is Even." 
4. Otherwise (if it's odd), print "The number is Odd."
'''

num = int(input("Enter a number :"))

if num %2 == 0 :
    print(f"{num} : is Even ")
else :
    print(f"{num} : is Odd ")