class Student :
    def __init__(self, name , roll_no):
        print("Student Added.")
        self.name = name
        self.roll_no = roll_no

s1 = Student("Bilal", 45)
print(s1.name)
print(s1.roll_no)

s2 = Student("Ali", 54)
print(s2.name)
print(s2.roll_no)
    