# Check if a number is a multiple of both 3 and 5.

num = int(input("Enter a number :"))

if num % 3 == 0 and num % 5 == 0 :
    print(f"{num} : is Multiple of both 3 & 5.")
else:
    print(f"{num} : is not multiple of 3 or 5.")