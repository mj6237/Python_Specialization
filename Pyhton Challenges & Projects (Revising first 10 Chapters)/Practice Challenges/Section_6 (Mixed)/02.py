'''
1. Start with a list: all_numbers = [1, 5, 8, 12, 15, 20, 23]. 
2. Create an empty list even_numbers. 
3. Loop through all_numbers. If a number is even, add it to even_numbers. 
4. Print even_numbers. 
'''
all_numbers = [1, 5, 8, 12, 15, 20, 23]

even_numbers = []

for n in all_numbers :
    if n %2 == 0 :
        even_numbers.append(n)
print(even_numbers)