'''
1. Define a function is_palindrome(word) that takes a string word. 
2. Inside the function, convert the word to lowercase. 
3. Check if the lowercase word is the same as its reversed version. 
4. Return True if it's a palindrome, False otherwise. 
5. Call the function with "Madam" and "Python" and print results.
'''

def is_palindrome(word) :
    word = word.lower()
    if word == word[::-1] :
        return True
    else :
        return False

word = input("Enter a word :")
result = is_palindrome(word)
print(result)