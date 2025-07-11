# Check if a character is a vowel or consonant (single-letter input)

letter = input("Enter an alphabet :")

letter = letter.lower()

if letter in ['a' , 'e' , 'i' , 'o' , 'u'] :
    print("Letter is Vowel")
else:
    print("Letter is consonant")

