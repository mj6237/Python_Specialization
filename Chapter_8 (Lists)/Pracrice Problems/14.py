'''
Log File Line Counter 
o Imagine you have a simple log file named activity.log (you can create this file with a few lines of dummy 
text like "Login successful", "Failed attempt", "User logout"). 
o Write a Python script that opens this file, reads its contents, and uses a loop to count how many lines are in the 
file. 
o Print the total number of lines. 
'''

def line_count(filename) :
    count = 0
    with open(filename, 'r') as file :
        for line in file :
            line = line.rstrip()
            count += 1
    return count

filename = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\activity.log.txt"
total = line_count(filename)
print(total)