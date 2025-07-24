'''Write a program to read through a file and print the contents of the file (line by line) 
all in upper case.'''
fh = input("Enter name of file :")
fo = open(fh)
for i in fo :
    i = i.rstrip()
    i = i.upper()
    print(i)