import SocketManager as SM
import sys







if __name__ == "__main__":
    #get interface 
    can_name=input("Enter CAN interface: ")
    #initialize socket
    socket=init_Socket(can_name)

    #get message to send
    can_id=input("Enter CAN_ID: ")
    data = input("Enter Data: ")
    data_len = len(data)
    SM.SendMessage(mesg)
:wq

