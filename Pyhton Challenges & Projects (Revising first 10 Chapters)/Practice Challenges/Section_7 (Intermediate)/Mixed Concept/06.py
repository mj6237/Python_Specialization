'''
1. Define a function char_to_ascii(char_map, char) that takes a dictionary char_map (mapping characters 
to their ASCII values) and a char (single character string). 
2. If char is in char_map, return its ASCII value. 
3. Otherwise, return "Character not found." 
4. Create a sample ascii_lookup = {"A": 65, "B": 66, "C": 67}. 
5. Call the function for "A" and "D" and print results.
'''

def char_to_ascii(char_map, char) :
    if char in char_map :
        return char_map[char]
    return "Character not found."

char_map = {"A": 65, "B": 66, "C": 67}

result = char_to_ascii(char_map,"C")
print(result)