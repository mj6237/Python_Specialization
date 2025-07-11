# Take 3 numbers, check if all are different, and print the highest 

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))

if num1 != num2 and num2 != num3 and num1 != num3 :
    print ("Numbers are different")
else:
    print("All or may two of them are same")

if num1 > num2 and num1 > num3 :
    print(f"{num1} is Highest number")
elif num2 > num1 and num2 > num3 :
    print(f"{num2} is highest number")
else :
    print(f"{num3} is highest number")
