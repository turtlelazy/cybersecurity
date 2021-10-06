from sys import argv
from io import StringIO


def incrementLetter(increment, letter):
    letterAsc = ord(letter.lower()) - 97
    shiftAsc = ord(increment.lower()) - 97

    shifted = (letterAsc + shiftAsc) % 26

    if letter.isalpha():
        return chr(shifted + 65)
    else:
        return letter

def decrementLetter(decrement,letter):
    letterAsc = ord(letter.lower()) - 97
    shiftAsc = ord(decrement.lower()) - 97

    shifted = (letterAsc - shiftAsc) % 26

    if letter.isalpha():
        return chr(shifted + 65)
    else:
        return letter

def encode(key,input):
    encodedMessage = ""
    keyRotation = 0

    #print(range(len(input)))
    for character in range(len(input)):
        #print(incrementLetter(key[0],input[character]))
        encodedMessage += incrementLetter(key[keyRotation],input[character])

        if input[character].isalpha():
            keyRotation+=1
        if(keyRotation==len(key)):
            keyRotation = 0
    
    return encodedMessage


def decode(key, input):
    encodedMessage = ""
    keyRotation = 0

    #print(range(len(input)))
    for character in range(len(input)):
        #print(incrementLetter(key[0],input[character]))
        encodedMessage += decrementLetter(key[keyRotation], input[character])

        if input[character].isalpha():
            keyRotation += 1
        if(keyRotation == len(key)):
            keyRotation = 0

    return encodedMessage


textfile = open(argv[2]).read()
keyfile = open(argv[3]).read()

if argv[1] == "decode":
    print(decode(keyfile,textfile))
elif argv[1] == "encode":
    print(encode(keyfile,textfile))

    #print(incrementLetter(argv[1], argv[2]))




#function that spits out letter after shifting it


#print(incrementLetter("b","z"))
