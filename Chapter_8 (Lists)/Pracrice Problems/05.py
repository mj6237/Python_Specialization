'''
 Extract Domains from Email List 
Function Name: extract_domains(email_list) 
Task: 
 Input: ["admin@gmail.com", "bob@yahoo.net"] 
 Output: ["gmail.com", "yahoo.net"] 

'''
import re
innput = ["admin@gmail.com", "bob@yahoo.net"] 
string = ",".join(innput)
#print(string)
domains = re.findall(r"@([\w.-]+)", string)
print(domains)


