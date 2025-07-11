# Check if a number is prime (only check for 2, 3, 5, 7, 11 — no loops)

num = int(input("Enter a number :"))

if num in [2,3,5,7,11]:
    print("Number is prime")
else:
    print("Number is not prime")