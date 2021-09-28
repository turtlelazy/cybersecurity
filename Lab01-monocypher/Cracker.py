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

def euclideanDistance(table1,table2):
    sum = 0
    for letter in range(26):
        sum += (table1[chr(a+letter)] + table2[chr(a+letter)]) ** 2
    
    return sum ** 0.5


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

print(euclideanDistance(fileFrequencyPercentages,sampleFrequencyPercentages))