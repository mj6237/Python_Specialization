'''
1. Define a sentence: sentence = "Python programming is fun". 
2. Split the sentence into individual words. 
3. Create an empty list word_lengths. 
4. Loop through each word. For each word, find its length and add it to word_lengths. 
5. Print word_lengths.
'''

sentence = "Python programming is fun"
word_length = []
word = sentence.split()
#print(word)
for w in word :
    word_length.append(len(w))
print(word_length)