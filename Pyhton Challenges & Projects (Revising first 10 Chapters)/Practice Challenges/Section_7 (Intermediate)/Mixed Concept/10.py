'''

'''

contacts = [
    {"name": "Alice", "phone": "111-2222"},
    {"name": "Bob", "phone": "333-4444"},
    {"name": "Charlie", "phone": "555-6666"},
    {"name": "David", "phone": "777-8888"},
    {"name": "Eve", "phone": "999-0000"}
]

def find_contact(contact_list, search_name):
    for contact in contact_list:
        if contact["name"].lower() == search_name.lower():
            return contact["phone"]
    return "Contact not found."

def add_contact(contact_list, name, phone):
    new_contact = {"name": name, "phone": phone}
    contact_list.append(new_contact)
    print(f"Contact '{name}' added.")

result_alice = find_contact(contacts, "Alice")
print(f"Phone number for Alice: {result_alice}")

result_david = find_contact(contacts, "David")
print(f"Phone number for David: {result_david}")

result_frank = find_contact(contacts, "Frank")
print(f"Phone number for Frank: {result_frank}")

result_bob_lower = find_contact(contacts, "bob")
print(f"Phone number for bob: {result_bob_lower}")

result_charlie_upper = find_contact(contacts, "CHARLIE")
print(f"Phone number for CHARLIE: {result_charlie_upper}")

print("\n--- Adding new contacts ---")
add_contact(contacts, "Grace", "123-1234")
add_contact(contacts, "Heidi", "567-5678")

print("\n--- Searching for newly added contacts ---")
result_grace = find_contact(contacts, "Grace")
print(f"Phone number for Grace: {result_grace}")

result_heidi = find_contact(contacts, "Heidi")
print(f"Phone number for Heidi: {result_heidi}")

print("\n--- Current contacts list ---")
for contact in contacts:
    print(f"Name: {contact['name']}, Phone: {contact['phone']}")
