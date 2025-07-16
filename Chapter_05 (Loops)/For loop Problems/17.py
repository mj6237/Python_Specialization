'''
Keep asking the user to enter a number until they type 0.
When they do, print "Loop ended."
🧠 Hint: Use while True: and break when input is 0.

'''

while True :
    num = int(input("Enter a number :"))
    if num == 0 :
        print("loop ended")
        break