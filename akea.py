# NOTE delete test() later

import numpy as np
import base64


base64lookuptable = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")


def encodeData(keyinput):
    """input:(class) string -> output:(calss) list

    Takes string as input and encodes it with base64 and converts the encoded
    string into numbers based on base64 rules
    """
    if isinstance(keyinput, str) is True:
        # process for the string
        temp = str(keyinput)
        temp = temp.encode(encoding="UTF-8")
        temp = base64.b64encode(temp)
        temp = temp.decode(encoding="UTF-8")

        # empty list to be appended on
        convertedData = list()

    # rejecting the padding "="
        for temp1 in temp:
            if temp1 != "=":
                convertedData.append(base64lookuptable.index(temp1))

    # accepting only string data type
    else:
        raise Exception("invalid data type or invalid format entered")
    return convertedData


def decodeData(keyinput):
    if isinstance(keyinput, str) is True:
        temp = str(keyinput)
        paddingLenght = 4-(len(temp) % 4)
        padding = "="*paddingLenght
        temp += padding
        temp = temp.encode(encoding="UTF-8")
        temp = base64.b64decode(temp)
        temp = temp.decode(encoding="UTF-8")
    else:
        raise Exception("invalid data type or invalid format entered")
    return temp


initialVector = (24, 39, 3, 63, 7, 46, 16, 3, 12, 57, 18, 46, 12, 55, 35, 43,
                 15, 6, 25, 53, 0, 45, 60, 15, 50, 22, 37, 41, 62, 56, 29, 38,
                 9, 15, 60, 2, 55, 3, 18, 8, 54, 10, 28, 0, 61, 40, 14, 41, 12,
                 2, 40, 27, 23, 43, 36, 62, 32, 60, 45, 4, 17, 11, 21, 4)

permutation_constants_set = np.genfromtxt("permutation.csv", delimiter=",", dtype=np.uint8)

substitution_constatnds_set = np.genfromtxt("substitution.csv", delimiter=",", dtype=np.uint8)

messup_constatns_set = np.genfromtxt("messup.csv", delimiter=",", dtype=np.uint8)

verifyValueForPermutation = (46, 57, 60, 40, 38, 62, 18, 14, 18, 37, 6, 9, 62,
                             23, 45, 21, 3, 55, 32, 15, 3, 45, 54, 8, 40, 10,
                             28, 12, 46, 56, 39, 60, 4, 50, 11, 35, 41, 41, 16,
                             17, 55, 0, 29, 3, 27, 53, 2, 25, 61, 43, 36, 12,
                             22, 24, 4, 63, 60, 7, 0, 15, 2, 43, 15, 12)

verifyValueForSubstitution = (22, 61, 56, 42, 47, 45, 41, 56, 35, 43, 58, 45,
                              35, 20, 17, 19, 52, 21, 5, 46, 27, 55, 59, 52, 18,
                              62, 30, 3, 36, 48, 54, 1, 26, 52, 59, 34, 20, 56,
                              58, 40, 51, 7, 53, 27, 12, 11, 13, 3, 35, 34, 11,
                              15, 14, 19, 50, 36, 8, 59, 55, 2, 37, 33, 31, 2)

verifyValueForMessup = (2, 60, 22, 17, 23, 34, 7, 44, 29, 35, 20, 18, 8, 1, 34,
                        5, 22, 41, 61, 35, 33, 30, 18, 25, 23, 33, 35, 61, 44,
                        14, 45, 27, 12, 48, 53, 24, 61, 50, 47, 6, 9, 15, 21,
                        41, 28, 19, 17, 44, 47, 24, 55, 30, 39, 34, 25, 41, 47,
                        24, 55, 30, 39, 34, 25, 41)


# this is called everytime before a key expansion is under process

# permutation csv check
def verifyIntegrity_subRoutine1():
    status = False
    temp = initialVector[:]
    tempshadow = initialVector[:]
    for temp1 in range(64):
        for temp2 in range(64):
            tempshadow[temp2] = temp[permutation_constants_set[temp1][temp2]]
        temp = tempshadow[:]
    if(temp == list(verifyValueForPermutation)):
        status = True
    else:
        raise Exception("internal constants tampering")
    return status


# substitution csv check
def verifyIntegrity_subRoutine2():
    status = False
    temp = initialVector[:]
    for temp1 in range(64):
        for temp2 in range(64):
            temp[temp2] = substitution_constatnds_set[temp1][(temp[temp2])]
    if (temp == list(verifyValueForSubstitution)):
        status = True
    else:
        raise Exception("internal constants tampering")
    return status


# messup csv check
def verifyIntegrity_subRoutine3():
    status = False
    temp = initialVector[:]
    for temp in range(64):
        temp = (temp + messup_constatns_set[temp][:]) % 64
    if (list(temp) == list(verifyValueForMessup)):
        status = True
    else:
        raise Exception("internal constants tampering")
    return status


def verifyIntegrity():
    status = True and verifyIntegrity_subRoutine1()
    status = status and verifyIntegrity_subRoutine2()
    status = status and verifyIntegrity_subRoutine3()
    return status


def keyexpander_permutation(parameter0, key):
    shadowbox = parameter0[:]
    # exception if length is wrong
    if len(permutation_constants_set) != len(parameter0):
        raise Exception("size data block input is wrong")
    for temp1 in range(len(parameter0)):
        shadowbox[temp1] = parameter0[permutation_constants_set[key][temp1]]
    return shadowbox


def keyexpander_combination(parameter0, key):
    shadowbox = parameter0[:]
    # exception if length is wrong
    if len(substitution_constatnds_set) != len(parameter0):
        raise Exception("size data block input is wrong")
    for temp1 in range(len(parameter0)):
        shadowbox[temp1] = substitution_constatnds_set[key][parameter0[temp1]]
    return shadowbox


def keyexpander_messup(parameter0, key):
    # exception if length is wrong
    if len(messup_constatns_set) != len(parameter0):
        raise Exception("size data block input is wrong")
    parameter0 = (parameter0 + messup_constatns_set[key]) % 64
    return parameter0


# the main algorithm
def keyexpander_subroutine2(parameter0):
    length_left = len(parameter0)
    current_position = 0
    for iteration1 in range((len(parameter0)//64)+1):
        parameter0_start = 1
        parameter0_end = 1 #"1" is a place holder

        for iteration2 in parameter0[(64*(iteration1-1)):(64*iteration1)]:
            pass


def keyexpander_subroutine1(parameter0):
    if verifyIntegrity() is False:
        raise Exception("internal IV data and other constants of Algorithm is tampered")
    else:
        expandedKey = keyexpander_subroutine2(parameter0)
    return expandedKey


def keyexpander(keyinput=""):
    if isinstance(keyinput, str) is True:
        if len(keyinput) != 0:  # if the length of key is 0 the default key is initial vector
            encodedKey = encodeData(keyinput)
            derivedKey = keyexpander_subroutine1(encodedKey)
        else:
            derivedKey = keyexpander_subroutine1(initialVector)
    else:
        raise Exception("invalid data type or invalid format entered")
    return derivedKey


def test():
    # simple naughty string test
    string1 = "hell my name is __🐛🐛 1 aGFzT3duUHJvcGVydHk="
    string2 = "YXBydGltdGlt"


    print(verifyIntegrity())

    # generatedkey = keyexpander("secret key")
    # print(generatedkey)
    # generatedkey = keyexpander("a")#short key test
    # print(generatedkey)

    # print(encodeData(string1))
    # print(decodeData(string2))

    # print(permutation_constants_set)
    # print(combinations)
    # print(initialVector)


if __name__ == "__main__":
    test()
