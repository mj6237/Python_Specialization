# Take a number; if it’s negative, convert it to positive and show result

num = int(input("Enter a number :"))
if num < 0 :
    num = -num
    #num = (num + (-num)) - num
    print(f"Coverted positive number is {num}")
else :
    print(f"{num} is a positive number")