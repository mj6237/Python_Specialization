'''
1. Define a string: text = "hello world". 
2. Create an empty dictionary char_counts. 
3. Loop through each character in text. 
4. For each character, update its count in char_counts. 
5. Print char_counts.
'''

text = "hello world"
char_count = {}
for char in text :
    char_count[char] = char_count.get(char, 0) +1
print(char_count)