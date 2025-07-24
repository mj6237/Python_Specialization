'''
Function Name: has_duplicates(usernames) 
Task: 
 Return True if any username appears more than once in the list 
 Else return False
'''
def has_duplicates(usernames):
    if len(set(usernames)) < len(usernames):
        return True
    else:
        return False
usernames = ["admin", "bob", "charlie", "admin"]
op = has_duplicates(usernames)
print(op)