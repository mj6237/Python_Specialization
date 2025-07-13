# Define a function even_or_odd(n) that returns "Even" or "Odd" 

def even_or_odd(n) :
    if n % 2 == 0 :
        return "Even"
    else :
        return "Odd"
try :
    n = int(input("Enter a number :"))
    if n >= 0 :
        result = even_or_odd(n)
        print(f"{n} is  {result} number ")
    else :
        print("Enter positive number !")
except ValueError :
    print(" Please, Enter valid number ( e.g, 7,6,4 etc)")
        


    