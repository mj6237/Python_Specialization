'''
Write a program to open the file romeo.txt and 
read it line by line. For each line,
 split the line into a list of words using the split function.
For each word, check to see if the word is already in the list of unique words.
If the word is not in the list of unique words, add it to the list.
When the program completes, sort and print the list of unique words in alphabetical order.
'''
f = open("romeo.txt", "r")
for l in f :
    l = l.rstrip()
    #print(l)
l = l.split()

words = l
#print(words)


while True :
    user_input = input("Enter a word to search :")
    if user_input in words :
        print("Already in the list at ")
        break
    else :
        words.append(user_input)
        #print("Added to list !")
    words.sort()
    print(words)