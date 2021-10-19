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


mode = argv[1]
keyfile = argv[2]
message = argv[3]

# removes the mandatory \n at the end of the file to support one line messages.
key = open(keyfile, "rb").read()[:-1]
# removes the mandatory \n at the end of the file to support one line messages.
inp = open(message, "rb").read()[:-1]
debug = True

if(debug):
  print("mode:"+mode)
  print("key: "+key)
  print("inp: "+inp)

if(mode == "numOut"):
    print(compileHexCode(xorBinary(message, keyfile)))
elif(mode == "human"):
    print(compileString(xorBinary(message, keyfile)))
