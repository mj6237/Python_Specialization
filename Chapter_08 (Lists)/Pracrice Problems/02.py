'''
Function Name: clean_log_file(input_file, output_file) 
Task: 
 Open and read each line of input_file 
 Skip any line containing "DEBUG" or "TRACE" 
 Write remaining lines to output_file 
Concepts: File I/O, conditions, in keyword, loops
'''
def clean_log_file(input_file, output_file):
    # Open both input and output files using with-statement
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            # Check if the line contains "DEBUG" or "TRACE"
            if "DEBUG" in line or "TRACE" in line:
                print("Skipped:", line.strip())
            else:
                outfile.write(line)

    # Display the cleaned content from output file
    print("\n✅ Cleaned Log Content:")
    with open(output_file, 'r') as cleaned_file:
        for line in cleaned_file:
            print(line.strip())

# Provide the full (raw string) absolute paths
input_file = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\system_log.txt"
output_file = r"E:\Python Specialization  By Michigan University\Python_Specialization\Files\cleaned.txt"

# Call the function
clean_log_file(input_file, output_file)
