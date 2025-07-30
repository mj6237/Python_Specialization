'''
1. Define a function double_numbers(input_list) that takes a list of numbers. 
2. Inside the function, create a new empty list doubled_list. 
3. Loop through input_list, multiply each number by 2, and append the result to doubled_list. 
4. Return doubled_list. 
5. Call the function with [1, 2, 3] and print the result. 
'''

def double_numbers(input_list) :
    doubled_list = []
    for n in input_list :
        d = n * 2
        doubled_list.append(d)
    return doubled_list
print(double_numbers([1, 2, 3]))

