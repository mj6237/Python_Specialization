'''
Print numbers from 1 to 10, but skip the number 7 using continue.
🧠 Output:

1
2
...
6
8
...
10

'''
for i in range (1,11) :
    if i == 7:
        print("Skipped")
        continue
    print(i)