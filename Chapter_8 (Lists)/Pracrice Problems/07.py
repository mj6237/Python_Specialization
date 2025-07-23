

def secure_rename(file):
    secure_file = []
    for line in file :
        cleaned = line.replace(" ","_")
        for char in "@#!%" :
            cleaned = cleaned.replace(char, "")
        secure_file.append(cleaned)
    return secure_file

            
file = ["my_file.txt", "databackup.csv", "secure_log.log"]
secure_file = secure_rename(file)
print(secure_file)