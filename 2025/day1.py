dial = 50
p1 = 0
p2 = 0
# formula = 100 - (n % 100 )

#with open("d:/repos/adventofcode/2025/day1-test.txt") as f:
with open("d:/repos/adventofcode/2025/day1.txt") as f:
    lines = f.read().splitlines()

for line in lines:
    v = int(line[1:])
    if line[0] == "L":
        v = -v
    dial_old = dial
    dial = (dial + v ) % 100
    if dial == 0:
        p1 += 1

    if line[0] == "L":
        if dial < dial_old:
            p2 += 1
    else:
        if dial > dial_old:
            p2 += 1
    dial_old = dial
print(p1)
print(p2)