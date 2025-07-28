'''
Ask the user for two numbers. 
2. Ask the user for an operation ("add", "subtract", "multiply", "divide"). 
3. Perform the chosen operation and print the result. 
4. If the operation is not recognized, print "Invalid operation."
'''

num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))

operation = input(" Enter (+, -, *, /) for get relevant results :")

if operation == "+" :
    print(num1 + num2)
elif operation == "-" :
    print(num1 - num2)
elif operation == "*" :
    print(num1 * num2)
elif operation == "/" :
    if num2 == 0 :
        print("ERROR! Division by Zero(0)")
    else:    
        print(num1 / num2)
else :
    print("Invalid operation")
