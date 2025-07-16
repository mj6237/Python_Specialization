''' Let user guess a secret number (e.g. 7) 
 If guess is too low: print "Too low" 
 If too high: print "Too high" 
 If correct: print "Correct! You guessed it!" and stop 
�
� Use: while, if-elif-else '''
secret_number = 7
while True:
    num = int(input("Guess Number :"))
    if num == 7 :
        print("Correct ! You Guessed it !")
        break
    elif num < secret_number :
        print("Too Low")
    else :
        print("Too High")