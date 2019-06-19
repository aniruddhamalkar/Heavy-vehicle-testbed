import socket
import sys
import csv

# create socket server
try:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # prevent socket.error:[Errno 98] Address already in use
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # setup host and port
    host = '127.0.0.1'
    port = 1024
    
    print('\nServer address is: %s' %(str(host)))
    
    # setup bind
    serversocket.bind((host,port))
    
    # setup maximum connections, moore than the nummbe need to wait
    serversocket.listen(5)
except socket.error as msg:
    print(msg)
    sys.exit(1)
    
print('Waiting for connection')

while 1:
    # accept connection from client 
    clientsocket, addr = serversocket.accept()
    
    #-----------------------check buffer size-----------------------------
    bufsize = serversocket.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print('buffer size is {0}'.format(bufsize))
    #---------------------------------------------------------------------
    
    print('Accept new connection from {0}\nWaiting for typing\n' .format(host))
    clientsocket.send('Welcome to the server!\n'.encode())
    
    # start communication with client
    while 1:
        recv_data = clientsocket.recv(1024).decode()
        #test_data = recv_data.decode()
        print('{0} client sends data is {1}'.format(addr,recv_data))
        if recv_data != 'exit':
            #--------------------------------------------------
            
            if recv_data == 'canbus': 
                with open('All_traffic.csv','r') as myFile:
                    lines=csv.reader(myFile)
                    for line in lines:
                        send_msg = str(line)
                        clientsocket.sendall(send_msg.encode())
                    break
                break
            
            #----------------------------------------------------
            #send_msg = input('please input work: ')
            send_msg = 'Data is received.'
            clientsocket.send(send_msg.encode())
            print('Waiting for typing')
            #print(clientsocket.recv(1024).decode())
        elif recv_data == 'exit' or not recv_data:
            print('{0} connection closes.' .format(addr))
            end_msg = 'Connection is closed'
            clientsocket.send(end_msg.encode())
            break
        
        #send_data = '{0} received.'.format(recv_data)
        #clientsocket.send(send_data.encode())
    clientsocket.close()
