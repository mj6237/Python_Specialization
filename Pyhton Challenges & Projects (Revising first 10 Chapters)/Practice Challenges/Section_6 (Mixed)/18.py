'''
1. Define a function calculate_average(numbers_list) that takes a list of numbers. 
2. Inside the function, calculate the sum of the numbers and divide by the count of numbers. 
3. Return the calculated average. 
4. Call the function with [10, 20, 30, 40] and print the result.
'''
def calculate_average(number_list) :
    if number_list :
        avg = sum(number_list) / len(number_list)
        return avg
    else :
        input("You entered nothing !")

average = calculate_average([10, 20, 30, 40])
print(average)