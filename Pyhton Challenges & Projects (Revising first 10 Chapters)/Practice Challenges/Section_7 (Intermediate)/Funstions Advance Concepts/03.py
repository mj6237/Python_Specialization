'''
1. Define a function get_min_max(numbers_list) that takes a list of numbers. 
2. Inside the function, find the minimum and maximum numbers in the list. 
3. Return both the minimum and maximum numbers. 
4. Call the function with [5, 1, 9, 3, 7]. 
5. Use tuple unpacking to store the returned values into two separate variables (min_val, max_val) and print 
them. 
'''

def get_min_max(numbers_list) :
    maxi = max(numbers_list)
    mini = min(numbers_list)

    print(f"Maximum: {maxi} \nMinimum: {mini}")

numbers_list = [5, 1, 9, 3, 7]
get_min_max(numbers_list)
