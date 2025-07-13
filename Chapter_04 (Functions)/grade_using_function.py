'''
Rewrite the grade program from the previous chapter using a function 
called computegrade that takes a score as its parameter and returns a grade as a string.
'''
try :
    def computegrade (score) :
        if score >= 0.0 and score <= 1.0 :
            if score >= 0.9 :
                return "A"
            elif score >= 0.8 :
                return "B"
            elif score >= 0.7 :
                return "C"
            elif score >= 0.6 :
                return "D"
            else :
                return "F"
            return score
        else :
            return("Please , Enter a number in range !")

    score = float(input("Enter your score :"))
    grade =computegrade(score)
    print(grade)
except ValueError :
    print("Invalid input. Please, enter score as (0.9 , 0.7)")