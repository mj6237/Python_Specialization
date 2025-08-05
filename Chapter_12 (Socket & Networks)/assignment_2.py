import urllib
import urllib.request

f = urllib.request.urlopen("http://data.pr4e.org/intro-short.txt ")

for line in f :
    word_count = {}
    print(line.decode().strip())
    for words in line.split():
        word_count[words] = word_count.get(words, 0) +1 
    print(word_count)