#piprocessing
import socket
import sys
import multiprocessing as mp


#sending masg from Pi
def pisend(port):
    
    # create socket server for sending 
    
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # prevent socket.error:[Errno 98] Address already in use
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # setup host
        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)
        
        print('\nServer address is: %s' %(str(IP)))
        
        # setup bind
        serversocket.bind((IP,port))
        
        # setup maximum connections, moore than the nummbe need to wait
        serversocket.listen(5)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
        
    print('Waiting for connection')
    
    # start connecting to VM
    
    while 1:
        # accept connection from VM
        pisend, addr = serversocket.accept()
        
        
        print('Accept new connection from {0}\nWaiting for typing\n' .format(IP))
        
        # start sending msg to VM
    
        while 1:
            send_msg = input('please input work: ')+ '\r\n'
            
            pisend.send(send_msg.encode())
            print(pisend.recv(1024).decode())
            #send exit to stop connection
            if send_msg == 'exit'+'\r\n':
                recv_msg = pisend.recv(1024)
                print(recv_msg.decode())
                break
            
        pisend.close()

#receiveing msg from VM
def pirecv(port):
    # create socket server for receiveing
    try:
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # prevent socket.error:[Errno 98] Address already in use
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # setup host
        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)
        
        print('\nServer address is: %s' %(str(IP)))
        
        # setup bind
        serversocket.bind((IP,port))
        
        # setup maximum connections, moore than the nummbe need to wait
        serversocket.listen(5)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
        
    print('Waiting for connection')
    
    while 1:
        # accept connection from VM 
        pirecv, addr = serversocket.accept()
        
        
        print('Accept new connection from {0}\nWaiting for typing\n' .format(addr))
        #clientsocket.send('Welcome to the server!\n'.encode())
        
        # start receive msg from VM
        while 1:
            recv_msg = pirecv.recv(1024).decode()
            print('{0} client sends data is {1}'.format(addr,recv_msg))
            if recv_msg != 'exit'+'\r\n':
                recv_msg = ' '
                send_msg = 'Data is received.'
                pirecv.send(send_msg.encode())
                print('Waiting for typing')
            # If receive exit. stop the connection
            elif recv_msg == 'exit'+'\r\n' or not recv_msg:
                print('{0} connection closes.' .format(addr))
                end_msg = 'Connection is closed'
                pirecv.send(end_msg.encode())
                break
        pirecv.close()

if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=pisend, args=(1024,))
    p2 = mp.Process(target=pirecv, args=(2048,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()