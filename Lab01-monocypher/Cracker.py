from io import StringIO
from sys import argv

A = 65
a = 97

#65 and 97 are A and a respectively
def counters(text):
    counters = {}

    for letter in range(26):
        count = text.count(chr(letter + A)) + text.count(chr(letter + a))
        counters[chr(letter+a)] = count
    #print(counters)
    return counters

def frequencyTable(counterTable):
    total = 0
    percentages = {}
    for letter in range(26):
        total += counterTable[chr(letter + a)]
    for letter in range(26):
        if total != 0:
            percentages[chr(a+letter)] = counterTable[chr(letter + a)] * 1.0 / total

    return percentages

def printFrqPcnt(frequencyTable):
    printStr = ""
    for letter in range(26):
        printStr +=  chr(a+letter) + ":" + str(frequencyTable[chr(a+letter)])
        if letter != 25:
            printStr += "\n"
    print(printStr)

def euclideanDistance(input,sample,rotation):
    sum = 0
    for letter in range(26):
        sum += (sample[chr(a+letter)] - input[chr((letter + rotation) % 26 + a)]) ** 2
        #print(chr((letter + rotation) % 26 + a) + str(sample[chr((letter + rotation) % 26 + a)]))
    return sum ** 0.5

def findMatch(input, sample):
    rotation = 0
    distance = 1.0
    for currentRotate in range(26):
        localDistance = euclideanDistance(input,sample,currentRotate)
        if  localDistance < distance:
            rotation = currentRotate
            distance = localDistance
    #print(rotation)
    #print(distance)
    return rotation

def decode(txt_input : str, key : int):
    txt_decoded = list(txt_input)
    for character in range(len(txt_decoded)):

        for letter in range(26):
            if txt_decoded[character] == chr(letter + a):
                txt_decoded[character] = chr((letter - key) % 26 + a)
                break
            elif txt_decoded[character] == chr(letter + A):
                txt_decoded[character] = chr((letter - key) % 26 + A)
                break

    return "".join(txt_decoded)

#Process input
input = argv[1]
file = open(input)
inputtext = file.read()

counterTable = counters(inputtext)
fileFrequencyPercentages = frequencyTable(counterTable)

if argv[2] == "decode":
    sampleFile = open("alice_in_wonderland.txt").read()
    sampleFrequencyPercentages = frequencyTable(counters(sampleFile))
    key = findMatch(fileFrequencyPercentages,sampleFrequencyPercentages)
    print(decode(inputtext, key))

elif argv[2] == "frequency":
    printFrqPcnt(fileFrequencyPercentages)


#printFrqPcnt(fileFrequencyPercentages)

#Sample Data to Compare