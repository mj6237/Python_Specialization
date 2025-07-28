'''
1. Define a function square_numbers(numbers_list) that takes a list of numbers. 
2. Inside the function, create an empty list squared_list. 
3. Loop through numbers_list, calculate the square of each number, and append() it to squared_list. 
4. Return squared_list. 
5. Call the function with [1, 2, 3, 4] and print the result. 
'''
def square_numbers (numbers_list) :
    squared_list = []
    for n in numbers_list :
        square = n **2
        squared_list.append(square)
    return squared_list

numbers_list = [ 1, 2, 3, 4]
result = square_numbers(numbers_list)
print(result)