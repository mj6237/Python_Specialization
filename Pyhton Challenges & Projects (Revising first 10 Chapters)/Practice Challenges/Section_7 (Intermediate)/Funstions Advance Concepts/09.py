'''
1. Define a function all_even(numbers_list) that takes a list of integers. 
2. Loop through the list. If you find any number that is odd, immediately return False. 
3. If the loop completes without finding any odd numbers, return True. 
4. Call the function with [2, 4, 6] and [1, 2, 3] and print the results. 
'''

def all_even(number_list): 
    for n in number_list:
        if n % 2 != 0:  # if number is odd
            return False
    return True  # all numbers were even

# Testing
print(all_even([2, 4, 6]))  # True
print(all_even([1, 2, 3]))  # False
