#  Ask for a float and check if it's a whole number (like 7.0) 
try:
    num = float(input("Enter a float number :"))
    if num.is_integer():
        print(f"{num} is a whole number")
    else :
        print(f"{num} is not whole number")
except ValueError:
    print("Please enter a float number (e.g , 5.4 , 2.3)")