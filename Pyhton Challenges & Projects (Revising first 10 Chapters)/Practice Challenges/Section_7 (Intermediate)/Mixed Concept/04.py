'''
1. Define a function parse_logs(logs_list, keyword) that takes the list of logs and a keyword (e.g., 
"ERROR"). 
2. Inside the function, create an empty list filtered_logs. 
3. Loop through logs_list. If the keyword is found in a log entry (case-insensitive), add that entry to 
filtered_logs. 
4. Return filtered_logs. 
5. Call parse_logs to get all "ERROR" logs and print the result. 
'''

def parse_logs(logs_list, keyword) :
    filtered_list = []
    for log in logs_list :
        if keyword.lower() in log.lower() :
            filtered_list.append(log)
    return filtered_list
        
logs_list = [ 
"INFO: User login successful.", 
"ERROR: File not found: config.txt", 
"DEBUG: Processing data.", 
"WARNING: Low disk space.", 
"ERROR: Network connection lost." ]

result = parse_logs(logs_list, "ERROR")
print(result)