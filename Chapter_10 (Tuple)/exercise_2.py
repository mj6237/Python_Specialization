'''
Task: Ek list of strings di jayegi, 
jahan har string ek simplified log entry hai.
 Har log entry ek tuple hai jismein (timestamp, event_type, message) hai.
 Ek function banao filter_error_logs(logs_list) jo yeh logs_list input legi.

Function ke andar, ek new empty list banao error_logs naam ki.
logs_list ke har tuple pe iterate karo using a for loop.
Har tuple ke event_type (jo second item hai, index 1 pe) ko check karo.
Agar event_type "ERROR" hai, toh us poore tuple ko error_logs list mein add kar do.
Finally, error_logs list ko return karo.
Function ko call karo aur returned list ko print karo.
'''
def filter_error_logs(logs_list) :
    error_logs = []
    with open(logs_list, 'r') as file :
        for line in file :
            if "ERROR" in line :
                error_logs.append(line)
        return error_logs

logs_list = "log_entries.txt"
op = filter_error_logs(logs_list)
print(op)