'''
 Extension Cleaner 
Function Name: clean_filename(filename) 
Task: 
 Replace spaces with underscores 
 Remove characters like #, @, %, ! 
 Return the sanitized filename 
Example: "my file@name!.txt" → "my_filename.txt" 
Concepts: Strings, .replace(), loops, string cleanup
'''

def clean_filename(filename):
    cleaned_files = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing spaces/newlines
            # Replace spaces with underscores
            cleaned = line.replace(" ", "_")
            # Remove characters #, @, %, !
            for char in "#@%!":
                cleaned = cleaned.replace(char, "")
            cleaned_files.append(cleaned)
    return cleaned_files


# Path to your input file
filename = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\replace.txt"
cleaned_list = clean_filename(filename)

# Print all cleaned filenames
for clean in cleaned_list:
    print(clean)
