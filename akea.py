import numpy as np
import base64

base64lookuptable = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encodeData(keyinput,sizeOfEncoding):
	if isinstance(keyinput,str)==True:
		#process for the string
		temp=str(keyinput)                                #i dont know why i am doing this
		temp=temp.encode()
		temp = base64.b64encode(temp)
		temp=temp.decode()

		#empty list to be appended on
		convertedData = list()

	#rejecting the padding "="
		for temp1 in temp:
			if temp1 != "=":
				convertedData.append(base64lookuptable.index(temp1))
	
	#accepting only string data type
	else:
		raise Exception("invalid data type or invalid format entered")
	return convertedData


def decodeData(keyinput):
	#work on converting the data back to str form number array
	if isinstance(keyinput,str)==True:
		temp = str(keyinput)        #i dont know why i am doing this but just sanity check
		paddingLenght = 4-(len(temp)%4)
		padding = "="*paddingLenght
		temp += padding
		print(temp)

	else:
		raise Exception("invalid data type or invalid format entered")
	return temp




def test():
	#simple naughty string test
	string1 = "hell my name is __🐛🐛 1 aGFzT3duUHJvcGVydHk="
	temp = encodeData(string1,10)
	temp = str(temp)
	print(decodeData(temp))
test()