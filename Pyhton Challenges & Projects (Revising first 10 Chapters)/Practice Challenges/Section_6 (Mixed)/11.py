'''
Ask the user to input a sentence. 
2. Initialize a vowel_count variable to 0. 
3. Define a string of vowels: vowels = "aeiou". 
4. Loop through each character in the input sentence. 
5. Convert the character to lowercase. 
6. If the lowercase character is in the vowels string, increment vowel_count. 
7. Print the final vowel_count. 
 Simple Hints: 
o How do you iterate through characters of a string? 
o How do you check if a character is present in another string? 
o Remember to handle case-insensitivity.
'''
sentence = input("Enter a sentence :")
vowel_count = 0
vowel = "aeiou"
for chara in sentence :
    chara = chara.lower()
    if chara in vowel :
        #print(chara)
        vowel_count = vowel_count +1 
print(vowel_count)
 