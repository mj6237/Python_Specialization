# File  Word Counter

def count_words_in_file(filename) :
    try :
        counted_words = {}
        with open(filename, 'r') as file :
            for words in file :
                words = words.strip().lower()
                word = words.split()
                for w in word :
                    counted_words[w] = counted_words.get(w, 0) +1
        return counted_words
    except FileNotFoundError:
        return {}

file_path = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\sample.txt"

result = count_words_in_file(file_path)
print(result)

