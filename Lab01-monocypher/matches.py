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
    key = Cracker.findMatch(wordHeaps[i],sampleFile)
    wordHeaps[i] = Cracker.decode(wordHeaps[i],key)

