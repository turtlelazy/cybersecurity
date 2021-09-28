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
    for rotate in range(26):
        print()


#Process input
input = argv[1]
file = open(input)
inputtext = file.read()

counterTable = counters(inputtext)
fileFrequencyPercentages = frequencyTable(counterTable)

printFrqPcnt(fileFrequencyPercentages)

#Sample Data to Compare
sampleFile = open("sample.txt").read()
sampleFrequencyPercentages = frequencyTable(counters(sampleFile))

print(euclideanDistance(fileFrequencyPercentages,sampleFrequencyPercentages,3))