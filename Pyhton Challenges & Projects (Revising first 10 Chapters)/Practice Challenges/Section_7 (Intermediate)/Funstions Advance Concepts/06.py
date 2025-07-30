'''
1. Define a function get_valid_integer_input(prompt) that takes a prompt string (e.g., "Enter your age: "). 
2. Inside the function, use a while True loop. 
3. Inside the loop, use a try-except ValueError block to: 
 Ask the user for input using the prompt. 
 Attempt to convert the input to an integer. 
 If successful, return the integer. 
 If ValueError occurs, print "Invalid input! Please enter a whole number." and continue the loop. 
4. Call the function with a prompt and print the returned valid integer
'''
def get_valid_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            int_value = int(user_input)
            return int_value
        except ValueError:
            print("Invalid input! Please enter a whole number.")

# Call the function with a prompt
result = get_valid_integer_input("Enter your age: ")
print(result)
