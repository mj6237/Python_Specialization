# Take two numbers and print the result of all arithmetic operations (+, -, *, /, //, %, **). 

num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))

add = num1 + num2
sub = num1 - num2
multi = num1 * num2
divi = num1 / num2
output_without_float = num1 // num2
modu = num1 % num2
expo = num1 ** num2

print(f"Addition = {add}\nSubtraction = {sub}\nMultiplicaton = {multi}\nDivision = {divi:.2f} \nFloor Division = {output_without_float} \nModulus = {modu}\nExponential Power = {expo}")
