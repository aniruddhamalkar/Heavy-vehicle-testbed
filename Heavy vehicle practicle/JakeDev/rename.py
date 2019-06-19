#Jake Walker
import SocketManager as SM
import sys

#multiprocessing queue stuff
# ~ #First startup the whole process
# ~ startup_dict = __import__(config.get('Programs','startup').strip()).communicate({'input_filename':"state_defs/" + config.get('General','state_def_filename')})

# ~ #define process out_queues. Note here the visualizer does not need an output queue.
	# ~ reader_out_q = mul.Queue()
	# ~ J1939_Interpreter_out_q = mul.Queue()
	
# ~ #create processes
	# ~ signal.signal(signal.SIGINT, signal.SIG_IGN) #A ignore interupt is required, otherwise child processes will inherit the interupt.
	# ~ inp = mul.Process(target=reader.get_data,args=(reader_out_q,))
	# ~ p1 = mul.Process(target=__import__(config.get('Programs','J1939_Interpreter').strip()).communicate,args=(reader_out_q,J1939_Interpreter_out_q,{'startup':startup_dict['to_J1939_Interpreter']},))
	# ~ p1.start()
	# ~ inp.start()	
	# ~ signal.signal(signal.SIGINT, signal_term_handler)


if __name__ == "__main__":
        can_name=input('Enter Can Name: \n')
        #set up socket
        socket = SM.SocketManager(can_name)
        get_messages(socket,can_name)

def get_messages(socket,can_name):
        while (1<2):
                print (socket.GetMessage(can_name))

