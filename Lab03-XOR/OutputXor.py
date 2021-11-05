from sys import argv

debug = False
#Read in binary
def xorBinary(text,key):
    xorBinary = []
    for letter in range(len(text)):
        c1 = ord(text[letter])
        c2 = ord(key[letter%len(key)])
        xorBinary.append(c1 ^ c2)
        if(debug):
            print(hex(c1))
            print(hex(c2))
    
    return xorBinary


def compileString(xorBinary):
    returnString = ""

    for ascii in range(len(xorBinary)):
        returnString += chr(xorBinary[ascii])

    return returnString


def compileHexCode(xorBinary):
    returnString = ""

    for ascii in range(len(xorBinary)):
        returnString += hex(xorBinary[ascii])[2:]
        if ascii != len(xorBinary) - 1:
            returnString += " "

    return returnString


mode = argv[1]
keyfile = argv[2]
message = argv[3]

# removes the mandatory \n at the end of the file to support one line messages.
keyfile = open(keyfile, "rb").read()#[:-1]
# removes the mandatory \n at the end of the file to support one line messages.
message = open(message, "rb").read()#[:-1]

if(debug):
  print("mode:"+mode)
  print("key: "+keyfile)
  print("inp: "+message)

if(mode == "numOut"):
    print(compileHexCode(xorBinary(message, keyfile)))
elif(mode == "human"):
    result = compileString(xorBinary(message, keyfile))
    outfile = open("output", "wb")
    outfile.write(result)
    outfile.close()



#print(compileHexCode(xorBinary('hello','A')))

#result = 5
#f.write(result.to_bytes(1,byteorder="little"))
