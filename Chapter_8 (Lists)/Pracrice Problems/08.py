'''
Function Name: search_in_file(filename, keyword) 
Task: 
 Print all lines from the file that contain the keyword 
Concepts: File reading, in keyword, search, conditions
'''

def search_in_file(filename, keyword):
    with open(filename, 'r') as file :
        for line in file :
            line = line.rstrip()
            if keyword.lower() in line.lower() :
                print(line)
            else :
                continue

keyword = input("Enter word to find :")
filename  = (r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\log.txt")
updated_file = search_in_file(filename,keyword)