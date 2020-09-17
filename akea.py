#NOTE delete test() later

import numpy as np
import base64

base64lookuptable = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encodeData(keyinput):
	"""input:(class) string -> output:(calss) list
	
	Takes string as input and encodes it with base64 and converts the encoded string into 
	numbers based on base64 rules
	"""
	if isinstance(keyinput,str)==True:
		#process for the string
		temp=str(keyinput)
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
		temp = str(keyinput)
		paddingLenght = 4-(len(temp)%4)
		padding = "="*paddingLenght
		temp += padding
		temp = temp.encode()
		temp = base64.b64decode(temp)
		temp = temp.decode()
	else:
		raise Exception("invalid data type or invalid format entered")
	return temp


initialVector = [24,39, 3,63, 7,46,16, 3,
				 12,57,18,46,12,55,35,43,
				 15, 6,25,53, 0,45,60,15,
				 50,22,37,41,62,56,29,38,
				  9,15,60, 2,55, 3,18, 8,
				 54,10,28, 0,61,40,14,41,
				 12, 2,40,27,23,43,36,62,
				 32,60,45, 4,17,11,21, 4]

permutations = np.genfromtxt("permutation.csv",delimiter=",",dtype=np.uint8)

combinations = np.genfromtxt("combination.csv",delimiter=",",dtype=np.uint8)

messups = np.genfromtxt("messup.csv",delimiter=",",dtype=np.uint8)

#this is called everytime before a key expansion is under process
def verifyIntegrity():
	status = False


	return status


#the main algorithm
def keyexpander_subroutine2(parameter0):
	for _ in range(64-(len(parameter0)%64)):
		for temp in parameter0:
			pass



def keyexpander_subroutine1(parameter0):
	if verifyIntegrity()==False:
		raise Exception("internal IV data and other constants of Algorithm is tampered")
	else :
		expandedKey=keyexpander_subroutine2(parameter0)
		
	return expandedKey



def keyexpander(keyinput=""):
	if isinstance(keyinput,str)==True:
		if len(keyinput)!=0:
			encodedKey = encodeData(keyinput)
			derivedKey = keyexpander_subroutine1(encodedKey)
		else:
			derivedKey = keyexpander_subroutine1(initialVector)

	else:
		raise Exception("invalid data type or invalid format entered")
	return derivedKey

def test():
	#simple naughty string test
	string1 = "hell my name is __🐛🐛 1 aGFzT3duUHJvcGVydHk="
	string2 = "YXBydGltdGlt"

	#print(permutations)
	#print(combinations)
	#print(initialVector)


if __name__ == "__main__":
	test()