'''
Create a list: mixed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
2. Create a new empty list called even_list. 
3. Iterate through mixed_numbers. If a number is even, add it to even_list. 
4. Print even_list.
'''
mixed_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = []
for n in mixed_numbers :
    if n %2 == 0 :
        even_list.append(n)
print(even_list)