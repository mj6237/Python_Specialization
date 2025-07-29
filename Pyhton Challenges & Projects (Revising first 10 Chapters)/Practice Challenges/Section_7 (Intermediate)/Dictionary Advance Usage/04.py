'''
1. Define a string: sentence = "apple banana apple cherry banana apple". 
2. Split the sentence into words. 
3. Create an empty dictionary word_counts. 
4. Loop through each word. 
5. For each word, update its count in word_counts. If the word is new, add it with a count of 1. If it exists, 
increment its count. 
6. Print the word_counts dictionary.
'''
word_count = {}
sentence = "apple banana apple cherry banana apple"
words = sentence.split()
for word in words :
#print(word)
    word_count[word] = word_count.get(word, 0) +1
print(word_count)