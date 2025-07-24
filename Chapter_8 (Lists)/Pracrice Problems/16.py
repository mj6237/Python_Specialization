'''
Simple IP Address Validator 
o Write a function called is_valid_ip that takes a string as input, representing an IP address (e.g., 
"192.168.1.1"). 
o Use string methods to check if the string consists only of digits and dots. (You don't need to validate the full IP 
structure yet, just basic character types). 
o Use an if-else condition to return True if it seems to be an IP (only digits and dots), otherwise False. 
o Call the function with a few test cases and print the results.
'''

def is_valid_ipv4(ip_address):
    parts = ip_address.split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if not part:
            return False
        
        if not part.isdigit():
            return False

        num = int(part)
        if not (0 <= num <= 255):
            return False

    return True

ip_address = input("Enter  Ipv4 address :")
check = is_valid_ipv4(ip_address)
print(check)