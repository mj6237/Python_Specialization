'''
Write a program to read through the mail box data and when you find line that starts with “From”, 
you will split the line into words using the split function. We are interested in who sent the 
message, which is the second word on the From line.
'''

file = open("mailbox.txt", 'r')
for line in file :
    line = line.rstrip()
    if not line.startswith("From ") :
        continue
    words = line.split()
    #print(words)
    print(words[1])
