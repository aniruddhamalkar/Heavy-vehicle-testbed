import socket


#create socket server


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#""TODO: get host ### need to provide your own IP for server for client you need to provide ip of server with same port""
#TODO: https://gist.github.com/BenKnisley/5647884/revisions
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
#host = '10.0.0.44'

port = 1024

print(hostname, IP)

#setup port
serversocket.bind((IP, port))

#setup maximum connections, moore than the nummbe need to wait

serversocket.listen(5)

while True:
   print("Listening to the socket.....")
   #create client port
   clientsocket, addr = serversocket.accept()
   print("Connected to client at {}".format(IP))
   print('address: %s' %(str(addr)))

   # msg = input("Type to write in client") + '\r\n'

   msg = input("Type to write in client") + '\r\n'
   clientsocket.send(msg.encode())
   msg = ''

   # clientsocket.close()

# serversocket.send(EOF)

import socket
import subprocess
import os

# create socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host name
# host = '10.83.140.12'
# hostname = socket.gethostname()
# IP = socket.gethostbyname(hostname)
# port
# port = 1024

# set up connection
# s.connect((IP, port))

# recieve msg
while True:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host name
#     host = '10.0.0.44'
   hostname = socket.gethostname()
   IP = socket.gethostbyname(hostname)

# port
   port = 1024
   s.connect((IP, port))
   msg = s.recv(1024)

   # s.close()

   print(msg.decode())
