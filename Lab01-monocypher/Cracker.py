from sys import argv
input = argv[1]
file = open(input)

text = file.read()

#print(text)

#65 and 97 are A and a respectively

counters = {}

for letter in range(26):
    count = text.count(chr(letter + 65)) + text.count(chr(letter + 97))
    counters[chr(letter+65)] = count
print(counters)