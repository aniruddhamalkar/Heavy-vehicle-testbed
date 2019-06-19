import socket
import sys

# create socket client 

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # setup host and port
    host = '127.0.0.1'
    port = 1024
    # setup connection
    server.connect((host, port))
    
except socket.error as error_msg:
    print(error_msg)
    sys.exit(1)

# start communicating with server

recv_msg = server.recv(1024)
print(recv_msg.decode())
while 1:
    send_msg = input('please input work: ')
    print('Waiting for typing')
    
    server.send(send_msg.encode())
    print(server.recv(1024).decode())
    if send_msg == 'exit':
        break
    
server.close()

