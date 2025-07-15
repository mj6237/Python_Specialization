# Count how many vowels are in the word "programming"

word = "programming"
number_of_words = 0
for vowel in word :
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u" :
        number_of_words += 1
print(number_of_words)