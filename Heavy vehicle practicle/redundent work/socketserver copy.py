import socket

#create socket server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#get host
host = '10.84.130.170'

port = 1024

print(host)

#setup port
serversocket.bind((host,port))

#setup maximum connections, moore than the nummbe need to wait

serversocket.listen(5)

while True:
    #create client port
    clientsocket, addr = serversocket.accept()
    
    print('address: %s' %(str(addr)))
    
    msg= ' Ｈellow Word! ' + '\r\n'
    
    clientsocket.send(msg.encode())
    clientsocket.close()



