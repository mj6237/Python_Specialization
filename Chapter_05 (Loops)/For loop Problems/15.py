'''
Print numbers from 1 to 10, but stop the loop if the number is 5 using break.
🧠 Output:
CopyEdit
1
2
3
4
Stopped at 5

'''

for i in range (1,11) :

    if i == 5 :
        print("Stopped at 5")
        break
    print(i)