'''

'''

def count_vowel_start_word(sentence) :
    vowels = "aeiou"
    words = sentence.split()
    count = 0
    for word in words :
        word = word.lower()
        if not word and word.startswith(vowels) :
            count += 1
    return count

result = count_vowel_start_word("Apple is an awesome orange")
print(result)

