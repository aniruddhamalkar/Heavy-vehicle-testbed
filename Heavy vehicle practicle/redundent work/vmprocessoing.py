#vmprocessing
import socket
import sys
import multiprocessing as mp

#receiving msg from Pi
def vmrecv(port):
   
    # create socket client
    try:
        vmrecv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        # setup host 
        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)
        # request connection to Pi
        vmrecv.connect((IP, port))
        
    except socket.error as error_msg:
        print(error_msg)
        sys.exit(1)
        
        # start receiving msg from Pi
    while 1:
        recv_msg = vmrecv.recv(1024).decode()
        print('{0} client sends data is {1}'.format(IP,recv_msg))
        #Check if receive msg
        if recv_msg != 'exit'+'\r\n':
            recv_msg = ' '
            send_msg = 'Data is received.'
            vmrecv.send(send_msg.encode())
            print('Waiting for typing')
        #If receive exit, stop connection
        elif recv_msg == 'exit'+'\r\n' or not recv_msg:
            print('{0} connection closes.' .format(IP))
            end_msg = 'Connection is closed'
            vmrecv.send(end_msg.encode())
            break
    vmrecv.close()
    

    
    
#sending msg to Pi
def vmsend(port):
    # create socket client 
    
    try:
        vmsend = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        # setup host
        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)
        # request connection to Pi
        vmsend.connect((IP, port))
        
    except socket.error as error_msg:
        print(error_msg)
        sys.exit(1)
    
    # start sending msg to Pi
    while 1:
        send_msg = input('please input work: ')+ '\r\n'
        
        vmsend.send(send_msg.encode())
        print(vmsend.recv(1024).decode())
        #If send exit, stop connection
        if send_msg == 'exit'+'\r\n':
            recv_msg = vmsend.recv(1024)
            print(recv_msg.decode())
            break
        
    vmsend.close()

if __name__ == '__main__':
    p1 = mp.Process(target=vmrecv, args=(1024,))
    p2 = mp.Process(target=vmsend, args=(2048,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()