'''
1. Define a list of emails: emails = ["user1@example.com", "user2@gmail.com", 
"user3@example.com", "user4@outlook.com", "user5@gmail.com"]. 
2. Create an empty dictionary domain_counts. 
3. Loop through each email in the emails list. 
4. For each email, extract the domain (the part after @). 
5. Update domain_counts: if the domain is already a key, increment its count; otherwise, add it with a count of 1. 
6. Print the domain_counts dictionary. 
'''
emails = ["user1@example.com", "user2@gmail.com", 
"user3@example.com", "user4@outlook.com", "user5@gmail.com"]

domain_count = {}
for mails in emails :
    mail = mails.split("@")
    count_domain = mail[1]
    #print(mail)
    domain_count[count_domain] = domain_count.get(count_domain, 0) +1
print(domain_count)
