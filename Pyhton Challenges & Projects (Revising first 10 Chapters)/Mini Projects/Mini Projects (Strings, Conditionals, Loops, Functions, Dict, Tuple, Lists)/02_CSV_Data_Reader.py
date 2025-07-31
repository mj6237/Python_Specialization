def read_csv_data(filepath):
    processed_data = []
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

            if not lines:
                return []

            for line in lines[1:]:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(',')

                if len(parts) >= 3:
                    name = parts[0].strip()
                    age_str = parts[1].strip()
                    city = parts[2].strip()

                    age = None
                    try:
                        age = int(age_str)
                    except ValueError:
                        age = "Invalid"

                    row_dict = {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                    processed_data.append(row_dict)
                else:
                    print(f"Warning: Skipping malformed line in CSV: '{line}'")

        return processed_data
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'.")
        return []

file_path_relative = "data.csv"
result_relative = read_csv_data(file_path_relative)
print(f"Processed data (relative path): {result_relative}")

file_path_absolute = r"E:\Python Specialization By Michigan University\Python_Specialization\Files\data.txt"
result_absolute = read_csv_data(file_path_absolute)
print(f"Processed data (absolute path): {result_absolute}")


non_existent_file = "non_existent_data.csv"
result_non_existent = read_csv_data(non_existent_file)
print(f"Processed data (non-existent file): {result_non_existent}")
