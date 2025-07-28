'''
What the Question Demands: 
1. Define a main string: sentence = "The quick brown fox jumps over the lazy dog.". 
2. Define a substring to search for: search_word = "fox". 
3. Check if search_word is present in sentence. 
4. Print "Word found!" if it is, otherwise print "Word not found."
'''
sentence = "The clever brown fox quickly jumps over the lazy dog."
search_word = input("Enter a word to search :")

if search_word.lower() in sentence.lower() :
    print("Word found!")
else :
    print("Word not found.")