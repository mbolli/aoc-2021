import sys
data = sys.stdin.readlines()
print ("Counted", len(data), "lines.")
lastValue = 0
counter = 0
for i in data:
    if int(i) > lastValue and lastValue > 0: counter += 1
    lastValue = int(i)

print ("Part One: Counted", counter, "increases")

lastValue = 0
counter = 0
lastSum = 0

for i in range(len(data)):
    if i < 3: continue

    lastSum = int(data[i-2]) + int(data[i-1]) + int(data[i])
    if lastSum > lastValue: counter += 1
    lastValue = lastSum
       
print ("Part Two: Counted", counter, "increases")

