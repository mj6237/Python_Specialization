'''
1. Define a function filter_above_threshold(numbers_list, threshold) that takes a list of numbers and 
a threshold value. 
2. Return a new list containing only the numbers from numbers_list that are strictly greater than threshold. 
3. Call the function with ([10, 5, 20, 15, 30], 15) and print the result. 
'''
greater_numbers = []
def filter_above_threshold(numbers_list, threshold) :
    for n in numbers_list :
        if n > threshold :
            greater_numbers.append(n)


filter_above_threshold([10, 5, 20, 15, 30], 15)
print(greater_numbers)