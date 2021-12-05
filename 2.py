import sys
data = sys.stdin.readlines()
print ("Counted", len(data), "lines.")

horizontal = 0
depth = 0
for i in data:
    op, num = i.split()
    if op == "forward": horizontal += int(num)
    if op == "down": depth += int(num)
    if op == "up": depth -= int(num)

print ("Day 2/1: Horizontal position", horizontal, "depth", depth, "result", horizontal*depth)

aim = 0
horizontal = 0
depth = 0

for i in data:
    op, num = i.split()
    if op == "forward":
        horizontal += int(num)
        depth += aim*int(num)
    if op == "down": aim += int(num)
    if op == "up": aim -= int(num)

print ("Day 2/2: Horizontal position", horizontal, "depth", depth, "result", horizontal*depth)
