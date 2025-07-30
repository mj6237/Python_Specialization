'''
1. Define a function count_vowel_start_words(sentence) that takes a string. 
2. Define a string of vowels: vowels = "aeiou". 
3. Split the sentence into words. 
4. Initialize count = 0. 
5. Loop through each word. Convert the word to lowercase. 
6. If the word is not empty and its first letter is in vowels, increment count. 
7. Return count. 
8. Call the function with "Apple is an awesome orange" and print the result.
'''

def count_vowel_start_word(sentence) :
    vowels = "aeiou"
    words = sentence.split()
    count = 0
    for word in words :
        word = word.lower()
        if  word and word[0] in vowels :
            count += 1
    return count

result = count_vowel_start_word("Apple is an awesome orange")
print(result)

