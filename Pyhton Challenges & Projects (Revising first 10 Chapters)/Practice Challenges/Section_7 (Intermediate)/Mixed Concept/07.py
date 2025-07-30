'''
1. Import the random module. 
2. Define a function generate_password(length) that takes an integer length. 
3. Define strings for possible characters: letters = "abcdefghijklmnopqrstuvwxyz", numbers = 
"0123456789", symbols = "!@#$%^&*". 
4. Combine these into a single string all_chars. 
5. Initialize an empty string password. 
6. Loop length times. In each iteration, randomly choose a character from all_chars and add it to password. 
7. Return the generated password. 
8. Call the function with length = 8 and print a generated password. 
'''

import random

def generate_password(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_=+[{}];:,.<>/?`~"

    all_chars = letters + numbers + symbols

    password = ""

    for _ in range(length):
        password += random.choice(all_chars)

    return password

password_length = 8
my_generated_password = generate_password(password_length)
print(f"Generated password of length {password_length}: {my_generated_password}")

print(f"Generated password of length 12: {generate_password(12)}")
print(f"Generated password of length 16: {generate_password(16)}")