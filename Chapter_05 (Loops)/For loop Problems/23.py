# Ask the user for a number (e.g. 5432), and print the reversed number: 2345

num = input("Enter a number :")
length=(len(num))

while length > 0 :
    print (num[length-1],end="")
    length -= 1
    
    
    