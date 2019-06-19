import socket, struct
interface = "can1"
sock = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
try:	
	sock.bind((interface,))
except OSError:
	sys.stderr.write("Could not bind to interface '%s'\n" % interface)

fmt = "<IB3x8s" #This line is required if we are using Python struct to structure CAN messages.
can_pkt = struct.pack(fmt, 0x741, len(b"hello"), b"hello")
sock.send(can_pkt)
