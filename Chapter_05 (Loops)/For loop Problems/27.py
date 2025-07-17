'''
Add pattern program to print right-angled triangle using nested loops

*
* *
* * *
* * * *
* * * * *
'''
n = 5
for i in range(n):
    s = 1
    for p in range (i+1) :
        print("*",end=" ")
    print()
