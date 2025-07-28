'''
What the Question Demands: 
1. Ask the user for a numerical score (integer). 
2. If the score is 90 or above, print "Grade: A". 
3. Otherwise, print "Grade: B or lower". 
'''

score = int(input("Enter your score :"))

if score >= 90 :
    print("Your grade is : A.")
else :
    print("Your grade is B or lower.")