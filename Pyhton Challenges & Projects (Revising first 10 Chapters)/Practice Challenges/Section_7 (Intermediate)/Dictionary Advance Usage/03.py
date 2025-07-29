'''
1. Use the student_scores dictionary from Problem 2.1. 
2. Use a for loop with two iteration variables to iterate through both keys and values simultaneously. 
3. Inside the loop, print a message like "Student: [Name], Score: [Score]".
'''

student_scores = {"Alice": 95, "Bob": 88, "Charlie": 72}

for name, score in student_scores.items() :
    print(f"Name :{name} , Score :{score}")