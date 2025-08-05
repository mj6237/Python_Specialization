# Creating and calling methods

class Student :
    
    def __init__(self, name , sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def avg (self, avg, sub1, sub2, sub3) :
        self.avg = (sub1 + sub2 + sub3) / 3
        return self.avg

s1 = Student("Khurram" , 88, 98, 67)
print(s1.avg("Khurram" , 88, 98, 67))
