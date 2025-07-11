'''
Marksheet generator (5 subjects): 
 Take 5 marks 
 Calculate total and percentage 
 Show grade using if-elif-else 
 Use try-except for input
'''
try:
    total_marks = 500
    sub1 = int(input("Enter marks of subject 1:"))
    sub2 = int(input("Enter marks of subject 2:"))
    sub3 = int(input("Enter marks of subject 3:"))
    sub4 = int(input("Enter marks of subject 4:"))
    sub5 = int(input("Enter marks of subject 5:"))
    obtained_marks = sub1 + sub2 + sub3 + sub4 + sub5
    if obtained_marks >= 450 :
        percent = (obtained_marks / total_marks) * 100
        print(f"Grade 'A' with {percent:.2f}%")
    elif obtained_marks >= 350:
        percent = (obtained_marks / total_marks) * 100
        print(f"Grade 'B' with {percent:.2f}%")
    elif obtained_marks >= 300:
        percent = (obtained_marks / total_marks) * 100
        print(f"Grade 'C' with {percent:.2f}%")
    else :
        percent = (obtained_marks / total_marks) * 100
        print(f"Grade 'F' with {percent:.2f}%")
except ValueError:
    print("Enter valid values :")
