'''
1. Define a function calculate_factorial(n) that takes a non-negative integer n. 
2. If n is 0, return 1 (base case for factorial). 
3. Otherwise, use a loop to calculate the factorial (product of all integers from 1 to n). 
4. Return the factorial. 
5. Call the function with 5 and 0 and print the results. 
'''
def calculate_factorial(n):
    if n == 0:
        return 1  # base case
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the function
print(calculate_factorial(5))  # Output: 120
print(calculate_factorial(0))  # Output: 1
