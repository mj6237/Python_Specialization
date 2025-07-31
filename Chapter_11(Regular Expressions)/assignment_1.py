import re

filename = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\assignment_chap_11.txt"
with open(filename, 'r' ) as file :
    file_content = file.read()
    numbers = re.findall("[0-9]+", file_content)
    str_numbers = numbers
    #print(str_numbers)
    int_numbers = [int(num_str) for num_str in str_numbers] # using list comprehension
    total = sum(int_numbers)
    print(f"Sum of all numbers appeared: {total}")
    

