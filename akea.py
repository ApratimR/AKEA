import numpy as np
import base64

base64lookuptable = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def keyexpand(keyinput,sizeOfEncoding):
	if isinstance(keyinput,str)==True:
		#process for the string
		temp=str(keyinput)
		temp=temp.encode()
		temp = base64.b64encode(temp)
		temp=temp.decode()
		keyinput=temp
		convertedData = list()
		while (current := temp)!= "=":
			#work here now
			pass


	else:
		raise Exception("invalid data type or invalid format entered")
	return keyinput


def test():
	#simple naughty string test
	string1 = "hell my name is __🐛🐛  aGFzT3duUHJvcGVydHk="
	print(keyexpand(string1,10))

test()