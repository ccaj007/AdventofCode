horizontal = 0
depth = 0

f = open("day2.txt")
f = [x.split() for x in f]
commands = [(x[0], int(x[1])) for x in f]
for cmd, val in commands:
    if cmd == "forward":
        horizontal += val
    if cmd == "down":
        depth += val
    if cmd == "up":
        depth -= val

print(horizontal * depth)

# part 2
horizontal = 0
depth = 0
aim = 0

for cmd, val in commands:
    if cmd == "forward":
        horizontal += val
        depth += aim * val
    if cmd == "down":
        aim += val
    if cmd == "up":
        aim -= val

print(horizontal * depth)



