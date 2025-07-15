'''
Define a function grade(score) 
Return: 
 "A" if score ≥ 90 
 "B" if 80-89 
 "C" if 70-79 
 "D" if 60-69 
 "F" if below 60 
Add a range check (0-100), and return "Invalid score" if the value is outside. 
'''

def grade(score) :
    if score >= 0 and score <= 100 :
        if score >= 90 :
            return "A"
        elif score >= 80 and score <= 89 :
            return "B"
        elif score >= 70 and score <= 79 :
            return "C"
        elif score >= 60 and score <= 69 :
            return "D"
        else :
            return "F"
    return "Invalid score"
score = int(input("Enter your score here :"))
result = grade(score)
print(f"Your grade is : {result}")