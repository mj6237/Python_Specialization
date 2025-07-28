'''
1. Define a list of log messages: logs = ["INFO: User logged in.", "ERROR: Disk full.", 
"WARNING: Low memory.", "ERROR: Database disconnected."] 
2. Create an empty list error_messages. 
3. Initialize error_count = 0. 
4. Loop through each log message. 
5. If the string "ERROR" is found in the log message (case-sensitive for this problem), add the log to 
error_messages and increment error_count. 
6. Print error_messages and error_count. 
'''
logs = ["INFO: User logged in.", "ERROR: Disk full.", 
"WARNING: Low memory.", "ERROR: Database disconnected."]
error_messages = []
error_count = 0

for l in logs :
    if "ERROR" in l :
        error_messages.append(l)
        error_count += 1
print(error_messages)
print(error_count)