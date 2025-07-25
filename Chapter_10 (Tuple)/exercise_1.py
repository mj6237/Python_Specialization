'''
Task: Ek function banao get_device_info(device_name, ip_address, status) jo teen inputs legi:
device_name (string, e.g., "Router1")
ip_address (string, e.g., "192.168.1.1")
status (string, e.g., "Online" or "Offline")
Is function ka kaam hai in teeno values ko ek single tuple mein pack kar ke return karna.
Phir, function ko call karo aur returned tuple ko print karo.
Example Output: ('Router1', '192.168.1.1', 'Online')
Concepts: Functions, Tuples.
'''
def get_device_info(device_name, ip_address, status) :
    tpl = (device_name,ip_address,status)
    return tpl

device_name = input("Enter device name :")
ip_address = input("Enter Ip_address :")
status = input("Enter status :")

op = get_device_info(device_name,ip_address,status)
print(op)


    

