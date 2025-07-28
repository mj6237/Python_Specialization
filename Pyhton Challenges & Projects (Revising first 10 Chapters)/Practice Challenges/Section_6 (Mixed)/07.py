'''
Define a function safe_divide(numerator, denominator) that takes two parameters. 
2. Inside the function, use a try-except block. 
3. Attempt to convert numerator and denominator to floats and perform division. 
4. If ValueError occurs (invalid input), print "Error: Invalid number input." and return None. 
5. If ZeroDivisionError occurs, print "Error: Cannot divide by zero." and return None. 
6. Otherwise, return the result of the division.
'''
def safe_divide(numerator, denominator) :
    try :
        nom = float(numerator)
        den = float(denominator)
        return nom / den
    except ValueError:
        print("Error !, Invalid numberinput")
    except ZeroDivisionError :
        print("Error !, Cannot divide by zero")

numerator = input("Enter numerator value :")
denominator = input("Enter demoninator value :")

result = safe_divide(numerator, denominator)
print(result)
       
