# Prompt user for file name
filename = input("Enter the file name: ")

try:
    # Try to open the file
    file = open(filename, 'r')
except:
    print("File cannot be opened:", filename)
    quit()

# Initialize counters
count = 0
total = 0.0

# Read through the file line by line
for line in file:
    line = line.strip()  # Remove whitespace
    if line.startswith("X-DSPAM-Confidence:"):
        # Extract the number after the colon
        value = float(line.split(":")[1])
        total += value
        count += 1

# Compute and print average
if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No matching lines found.")
