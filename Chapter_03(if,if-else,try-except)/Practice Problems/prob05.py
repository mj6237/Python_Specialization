# Take two numbers, print the greater one (without using max() function)

num1 = int(input("Enter first number:"))
num2 = int(input("Enter seconde number:"))
if num1 > num2 :
    print(f"{num1} is greater than {num2}")
elif num2 > num1 :
    print(f"{num2} is greater than {num1}")
else :
    print("Both number are equal")