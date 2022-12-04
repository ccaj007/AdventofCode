with open("day3-input.txt") as f:
    data = f.read().splitlines()

def getVal(x):
    return ord(x) - ord('a') + 1 if x.islower() else ord(x) - ord('A') + 27

p1 = 0
for line in data:
    m = len(line) // 2
    l1 = line[:m]
    l2 = line[m:]
    x, = set(l1) & set(l2)
    p1 += getVal(x)

print(p1)

p2 = 0
for i in range(0, len(data), 3):
    line1, line2, line3 = data[i:i+3]
    x, = set(line1) & set(line2) & set(line3)
    p2 += getVal(x)

print(p2)


