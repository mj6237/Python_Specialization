'''
Define a function named reverse_string that takes one parameter: word. 
2. Return the word reversed. 
3. Call the function with a word (e.g., "Python") and print the result.
'''

def reverse_string (word) :
    print(word[::-1])

word = input("Enter a word :")

reverse_string(word)