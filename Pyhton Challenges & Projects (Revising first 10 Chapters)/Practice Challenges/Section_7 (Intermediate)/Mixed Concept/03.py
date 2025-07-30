'''
1. Initialize an empty list students = []. 
2. Define a function add_student(student_list, name, age, grade): 
 Creates a dictionary {"name": name, "age": age, "grade": grade}. 
 Appends this dictionary to student_list. 
 Prints a confirmation. 
3. Define a function view_students(student_list): 
 If student_list is empty, print "No students enrolled." 
 Else, loop through student_list and print each student's details (name, age, grade). 
4. Call add_student multiple times to add a few students. 
5. Call view_students.
'''
student_list = []

def add_student(student_list, name, age, grade) :
    data_dict = {"name" : name, "age" : age, "grade" : grade}
    student_list.append(data_dict)
    print(f"Student {name} added successfully.")
def view_students(student_list) :
    if not student_list :
        print("No students enrolled.")
    else :
        for student in student_list :
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
add_student(student_list, "Alice", 25, "A")
add_student(student_list, "Bob", 27, "B")
add_student(student_list, "Charlie", 23, "C")
print("--- Student List---")
view_students(student_list)