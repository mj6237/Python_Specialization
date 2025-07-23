'''
11. Sanitize Log Messages 
Function Name: sanitize_logs(filename) 
Task: 
 Read file line-by-line 
 Replace banned words like: 
o "hack" → "[REDACTED]", "virus" → "[REDACTED]", etc. 
 Print cleaned lines 
Concepts: File I/O, .replace(), string processing, lists
'''
def sanitized_logs(filename):
    with open(filename, 'r') as file :
        for line in file:
            line = line.rstrip()
            #lines = line.split()
            if "hack" in line or "virus" in line :
                replaced = line.replace("virus", "REDACTED")
                replaced = line.replace("hack", "REDACTED")
                print(replaced)

filename = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\logs_to_clean.txt"
op = sanitized_logs(filename)
print(op)