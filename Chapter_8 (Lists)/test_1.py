'''
Write the program that prompts the user for a list of numbers and prints out the maximum and 
minimum of the numbers at the end when the user enters “done”. Write the program to store the 
numbers the user enters in a list and use the max() and min() functions to compute the maximum 
and minimum numbers after the loop completes. 
Enter a number: 6 
Enter a number: 2 
Enter a number: 9 
Enter a number: 3 
Enter a number: 5 
Enter a number: done 
Maximum: 9.0 
Minimum: 2.0
'''
numbers =  []
while True :
    user_input = input("Enter a number :").strip()
    if user_input == "done" :
        print("Maximum Number is :" , max(numbers))
        print("Minimum Number is :" , min(numbers))
        break
    else :
        try :
            converted_user_input = float(user_input)
            numbers.append(converted_user_input)
        except :
            print("Enter a valid Number (e,g.  5, 6, 7)")


