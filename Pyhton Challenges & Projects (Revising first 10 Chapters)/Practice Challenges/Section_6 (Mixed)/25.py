'''
1. Define a function perform_operation(num1, num2, operation) that takes two numbers and an operation 
string ("add", "subtract", "multiply", "divide"). 
2. Use if-elif-else to perform the correct arithmetic operation. 
3. Return the result. If the operation is invalid, return "Invalid Operation". 
4. Call the function with various inputs (e.g., (10, 5, "add"), (8, 2, "divide"), (4, 3, "power")) and 
print results. 
'''

def perform_operation(num1, num2, operation) :
    if operation == "+" :
        return (num1 + num2)
    elif operation == "-" :
        return (num1 - num2)
    elif operation == "*" :
        return (num1 * num2)
    elif operation == "/" :
        try :
            return (num1 / num2)
        except ZeroDivisionError:
            print("Error!, Divide by zero.")
    else :
        return "Invalid operation !"

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
operation =input("Press (+, -, *, ?) to get desired results:")
result = perform_operation(num1, num2, operation)
print(result)
    