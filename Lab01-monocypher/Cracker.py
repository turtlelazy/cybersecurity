from sys import argv

#65 and 97 are A and a respectively
def counters(text):
    counters = {}

    for letter in range(26):
        count = text.count(chr(letter + 65)) + text.count(chr(letter + 97))
        counters[chr(letter+65)] = count
    #print(counters)
    return counters


input = argv[1]
file = open(input)

text = file.read()

counters = counters(text)