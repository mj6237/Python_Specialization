'''
1. Define a list of words: word_list = ["apple", "banana", "apricot", "grape", "avocado"]. 
2. Define a target letter: target_letter = "a". 
3. Create an empty list filtered_words. 
4. Loop through word_list. If a word starts with target_letter (case-insensitive), add it to filtered_words. 
5. Print filtered_words. 
'''
word_list = ["apple", "banana", "apricot", "grape", "avocado"]
target_letter = "a"
filtered_words = []

for l in word_list :
    if l.lower().startswith(target_letter.lower()) :
        filtered_words.append(l)
print(filtered_words)

