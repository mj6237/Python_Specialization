'''
1. Define a function remove_char(text, char_to_remove) that takes a string text and a character 
char_to_remove. 
2. Return a new string with all occurrences of char_to_remove removed from text. 
3. Call the function with ("Hello World", "o") and print the result. 
'''
def remove_char(text, char_to_remove) :
    result = text.replace(char_to_remove, "")
    return result


output = remove_char("Hello World", "o")
print(output)