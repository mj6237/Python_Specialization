# Count how many digits are in a number (e.g., 732 has 3 digits)

num = input("Enter a number :")
total_digit = 0
i = 0
while i < len(num) :
    total_digit += 1
    i += 1
print(f"There are {total_digit} digits.")
