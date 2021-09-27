from sys import argv

A = 65
a = 97

#65 and 97 are A and a respectively
def counters(text):
    counters = {}

    for letter in range(26):
        count = text.count(chr(letter + A)) + text.count(chr(letter + a))
        counters[chr(letter+A)] = count
    #print(counters)
    return counters

def frequencyTable(counterTable):
    total = 0
    percentages = {}
    for letter in range(26):
        total += counterTable[chr(letter + A)]
    for letter in range(26):
        if total != 0:
            percentages[chr(A+letter)] = counterTable[chr(letter + A)] * 1.0 / total

    return percentages
    
        

input = argv[1]
file = open(input)

text = file.read()

counterTable = counters(text)

print(frequencyTable(counterTable))