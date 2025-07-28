'''
1. Define a sentence: text = "This is a sample sentence for filtering words.". 
2. Define a minimum length: min_length = 4. 
3. Split the sentence into words. 
4. Create an empty list long_words. 
5. Loop through each word. If its length is greater than min_length, add it to long_words. 
6. Print long_words. 
'''

text = "This is a sample sentence for filtering words."
min_length = 4
words = text.split()
long_words = []

for w in words :
    if len(w) > min_length :
        long_words.append(w)
print(long_words)