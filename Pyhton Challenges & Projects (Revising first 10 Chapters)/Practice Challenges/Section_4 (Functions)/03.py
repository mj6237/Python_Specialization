'''
Define a function named add_two_numbers that takes two parameters: num1 and num2. 
2. Inside the function, calculate their sum. 
3. Return the sum. 
4. Call the function and store its returned value in a variable, then print the variable.
'''

def add_two_numbers(num1,num2) :
    return (num1 + num2)

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

total = add_two_numbers(num1,num2)
print(total)