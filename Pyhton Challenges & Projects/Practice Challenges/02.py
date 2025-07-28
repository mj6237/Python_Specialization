#Voting Eligibility 

'''
What the Question Demands: 
1. Ask the user to input their age as an integer. 
2. If the age is 18 or greater, print "You are eligible to vote." 
3. Otherwise, print "You are not yet eligible to vote."
'''

age = int(input("Enter your age :"))

if age >= 18 :
    print("You are eligible to vote.")
else :
    print("You are not yet eligible to vote.")