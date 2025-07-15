# Ask user for a number; print its multiplication table (e.g. 5 x 1 = 5 ... 5 x 10 = 50)

num = int(input("Enter a number to get it's table :"))
for i in range (1,11) :
    print(f"{num} x {i} = {num*i}")