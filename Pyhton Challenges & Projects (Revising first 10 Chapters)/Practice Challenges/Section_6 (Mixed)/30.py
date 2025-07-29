'''
1. Define a function tuple_to_sentence(words_tuple) that takes a tuple of strings (words). 
2. Return a single string where the words are joined by spaces. 
3. Call the function with ("This", "is", "a", "tuple", "sentence") and print the result.
'''

def tuple_to_sentence(words_tuple) :
    sentence = " ".join(words_tuple)
    return sentence
    
words_tuple = ("This", "is", "a", "tuple", "sentence")
result = tuple_to_sentence(words_tuple)
print(result)
