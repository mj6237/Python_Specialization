'''
Ask the user for a number and print its factorial. 
(e.g. 5 → 5 * 4 * 3 * 2 * 1 = 120) 
�
� Use: for or while, multiplication loop 
'''

factorial = 1
num = int(input("Enter a number :"))
for i in range(1,num+1) :
    factorial *= i # factorial = factorial * i
print(factorial)


    
