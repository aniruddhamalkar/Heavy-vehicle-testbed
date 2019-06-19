#!/usr/bin/python3
import SocketManager as SM
from time import sleep

can_name = "can1"
socket = SM.SocketManager(can_name)

#inject single message function
def injectMsg(can_id,data_len,data):
#Inject function injects a single message to the CAN BUS. Args=can_id, data length, and data)

	"""check input to be correct"""
	socket.SendMessage(can_id,data_len,data)

#loop function
def loop(numLines, numTimes):
#loops a number of lines so many times. Args=numLines (int), numTimes(int)
	if ((numLines<1) or (numTimes<1)):
		print ("Number of lines must be greater than 0 and number of times must be greater than 1")
		

#check message function
def checkMessage(can_id, data_len, data):
	mesg = (can_id, data_len, data)
	data = socket.GetMessage(can_name)
	
	while (1<2):
		if(data==mesg):
			print("TADA!")
		else:
			data=socket.GetMessage(can_name)
		
#wait function
def wait(amount, unit):
#sleeps for given amount. Arguments = time(int) and units ('ms', 's', 'min')
	if (amount>=0):
		if unit=='ms':
			sleep(amount*0.001)
		elif unit=='s':
			sleep(amount)
		elif unit=='min':
			sleep(amount*60)
		else:
			print("Error, given unit not defined")
	else: 
		print("Error, given amount not positive")


