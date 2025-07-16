'''
Show a menu:
1. Say Hello
2. Say Salam
3. Exit
Keep showing menu until user chooses 3.
Use while True and break.

'''
while True :
    
    print("1. Say Hello \n2. Say Salam \n3. Exit")
    choicee = int(input("Enter regarding number to show regarding msg  :"))
    if choicee == 1 :
        print("Hello")
    elif choicee == 2 :
        print("Salam")
    elif choicee == 3 :
        print("Aasta Lavista Baby")
        break
    else :
        print("Enter number form given menu")