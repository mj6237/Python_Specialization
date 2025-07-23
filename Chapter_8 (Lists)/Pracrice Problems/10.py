'''
Function Name: sum_numbers_in_file(filename) 
Task: 
 File contains numbers, one per line 
 Return their total sum
'''

def sum_numbers_in_file(filename):
    total = 0
    with open(filename, 'r') as file :
        for line in file :
            line = line.rstrip()
            total += int(line)
        return total
filename = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\numbers.txt"
final_total = sum_numbers_in_file(filename)
print(final_total)


