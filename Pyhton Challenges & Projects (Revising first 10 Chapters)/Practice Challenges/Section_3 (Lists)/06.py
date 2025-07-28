'''
What the Question Demands: 
1. Use the fruits list (after Problem 3.4). 
2. Check if "apple" is in the list. Print "Apple is in the list." or "Apple is NOT in the list." accordingly. 
3. Check if "kiwi" is in the list. Print "Kiwi is in the list." or "Kiwi is NOT in the list." accordingly. 
'''
fruits = ["Mango", "Apple", "Gava", "Banana"]

search_fruit = input("Enter fruit name to search :")
if search_fruit in fruits :
    print(f"{search_fruit} is in the list.")
else :
    print(f"{search_fruit} is not in the list.")