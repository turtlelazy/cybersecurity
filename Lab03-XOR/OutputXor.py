from sys import argv

def xorBinary(text,key):
    xorBinary = []
    for letter in range(len(text)):
        c1 = ord(text[letter])
        c2 = ord(key[letter%len(key)])
        xorBinary.append(c1 ^ c2)
    
    return xorBinary


def compileString(xorBinary):
    returnString = ""

    for ascii in range(len(xorBinary)):
        returnString += chr(xorBinary[ascii])

    return returnString


def compileHexCode(xorBinary):
    returnString = ""

    for ascii in range(len(xorBinary)):
        returnString += hex(xorBinary[ascii])
        if ascii != len(xorBinary) - 1:
            returnString += " "

    return returnString



