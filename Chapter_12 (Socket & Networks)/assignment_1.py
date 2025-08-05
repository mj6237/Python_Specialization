
# Creating Socket
import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Done.")
# Establish Connection with Server
try :
    my_socket.connect(('data.pr4e.org', 80))
    print("Connection Established.")
except :
    print("Connection Failed.")
# Sending Request to Server
try :
    cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
    my_socket.send(cmd)
    print("Request Successfully sended.")
except :
    print("Request Sending Failed.")
# Receiving Response from Server
try :
    while True :
        data = my_socket.recv(512)
        if len(data) < 1 :
            break
        print(data.decode(), end='')
    print("Data Received.")
    my_socket.close()
except :
    print("No Data Received")
    
    


'''import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
'''
