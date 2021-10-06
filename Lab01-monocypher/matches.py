import Cracker

file = open("ving.txt").read()

#print(file)

length = 3

"""
for i in range(len(file)-1):
    if(file.find(file[i:i+length], 0, i)==-1):
        if file.count(file[i:i+length]) > 2:
            print(file[i:i+length] + " " + "distance of " + str(file.find(file[i:i+length],i+1) - i))
            #print(file[i:i+length] + " " + str(file.count(file[i:i+length])))
"""

#Distances appear to be multiples of 4

wordHeaps = []

heapCount = 4

for i in range(heapCount):
    wordHeaps.append("")

current = 0
for character in range(len(file)):
    wordHeaps[current] += file[character:character+1]
    current+=1
    if current == heapCount:
        current = 0

"""
print(len(wordHeaps))
for i in range(len(wordHeaps)):
    print(wordHeaps[i])
    print("\nYUMMY")
"""
sampleFile = open("alice_in_wonderland.txt").read()
for i in range(len(wordHeaps)):
    counterTable = Cracker.counters(wordHeaps[i])
    fileFrequencyPercentages = Cracker.frequencyTable(counterTable)

    sampleFrequencyPercentages = Cracker.frequencyTable(Cracker.counters(sampleFile))

    key = Cracker.findMatch(fileFrequencyPercentages,sampleFrequencyPercentages)
    print(key)
    wordHeaps[i] = Cracker.decode(wordHeaps[i],key)
    #print(wordHeaps[i])

decodedString = ""
counter = 0
loop = 0
for i in range(len(file)):
    decodedString += wordHeaps[counter][loop]
    counter +=1
    if counter == heapCount:
        counter = 0
        loop+=1

print(decodedString)
#print(len(file))
#print(len(decodedString))