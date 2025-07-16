'''
Keep asking the user to enter numbers and keep adding them.
Stop when the user enters 0, and print the total sum.

'''

total = 0
while True :
    num = int(input("Enter a number :"))
    if num == 0 :
        print("Ye Kia Kr Diya Jaano (-_-) Good_Bye")
        break
    else :
        total += num
print(f"Sum of all numbers : {total}")