from sys import argv

def xorBinary(text,key):
    xorBinary = []
    for letter in range(len(text)):
        c1 = ord(text[letter])
        c2 = ord(key[letter%len(key)])
        xorBinary.append(c1 ^ c2)
    
    return xorBinary

