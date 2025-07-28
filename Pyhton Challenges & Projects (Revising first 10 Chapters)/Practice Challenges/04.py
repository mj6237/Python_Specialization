'''
What the Question Demands: 
1. Ask the user to input an integer. 
2. If the number is greater than 0, print "The number is Positive." 
3. Else if the number is less than 0, print "The number is Negative." 
4. Otherwise (if it's neither positive nor negative), print "The number is Zero."
'''

num = int(input("Enter a number :"))

if num > 0 :
    print("Number is Positive.")
elif num < 0 :
    print("Number is Negative")
else :
    print("Number is Exactly Zero(0).")