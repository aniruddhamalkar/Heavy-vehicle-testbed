import socket
import sys

# create socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# host name
host = '10.84.130.170'

# port
port = 1024

# set up connection
s.connect((host, port))

# recieve msg
msg = s.recv(1024)

s.close()

print (msg.decode())
