# Ask user for a number and print its multiplication table using while

num = int(input("Enter a number :"))
i = 1
while i <= 10 :
    print(f"{num} x {i} =  {i*num}")
    i += 1