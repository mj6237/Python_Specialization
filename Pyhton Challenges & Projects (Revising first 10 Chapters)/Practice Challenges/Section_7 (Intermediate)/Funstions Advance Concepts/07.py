'''
1. Define a function sort_words_by_length(words_list) that takes a list of strings. 
2. Return a new list containing the words sorted from shortest to longest. 
3. Call the function with ["apple", "banana", "cat", "dog", "elephant"] and print the result. 
'''
def sort_words_by_length(words_list):
    return sorted(words_list, key=len)

# Call the function with the given list
words_list = ["apple", "banana", "cat", "dog", "elephant"]
result = sort_words_by_length(words_list)
print(result)
    

