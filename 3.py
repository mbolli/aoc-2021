import sys
data = sys.stdin.readlines()
print ("Counted", len(data), "lines.")
testdata = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
length = len(data[0])
gamma = [] 
epsilon = []
for l in range(0, length):
    zeroes = 0
    ones = 0
    for i in data:
        if i[l] == "0": zeroes += 1
        if i[l] == "1": ones += 1
    if zeroes > ones: 
        gamma.append("0")
        epsilon.append("1")
    if ones > zeroes: 
        gamma.append("1")
        epsilon.append("0")

gammaDec = int("".join(gamma), 2)
epsilonDec = int("".join(epsilon), 2)

print ("Day 3/1: Gamma", gammaDec, "Epsilon", epsilonDec, "Result", gammaDec*epsilonDec)

oxygen = 0
co2 = 0

def getOnesAndZeroes(pos, rows, kind):
    zeroesList = []
    onesList = []

    for row in rows:
        if row[pos] == "0": zeroesList.append(row)
        if row[pos] == "1": onesList.append(row)
   
    pos += 1

    if kind == 'oxygen':
        if len(zeroesList) > len(onesList):
            zeroesList = getOnesAndZeroes(pos, zeroesList, kind)
            return zeroesList
        if len(onesList) > len(zeroesList):
            onesList = getOnesAndZeroes(pos, onesList, kind)
            return onesList
        if len(onesList) == len(zeroesList):
            global oxygen
            oxygen = int(onesList[0], 2)
    if kind == 'co2':
        if len(zeroesList) < len(onesList):
            zeroesList = getOnesAndZeroes(pos, zeroesList, kind)
            return zeroesList
        if len(onesList) < len(zeroesList):
            onesList = getOnesAndZeroes(pos, onesList, kind)
            return onesList
        if len(onesList) == len(zeroesList):
            global co2
            co2 = int(zeroesList[0], 2)

getOnesAndZeroes(0, data, 'oxygen')
getOnesAndZeroes(0, data, 'co2')
print ("Day 3/2: Oxygen generator rating:", oxygen, "CO2 scrubber rating:", co2, "Result:", oxygen*co2)
