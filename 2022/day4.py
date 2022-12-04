with open("day4-input.txt") as f:
    data = f.read().splitlines()

c = 0
d = 0
for line in data:
    a,b = line.split(',')
    a1,a2 = map(int,a.split("-"))
    b1,b2 = map(int,b.split("-"))
    if a1 <= b1 <= b2 <= a2 or (
        b1 <= a1 <= a2 <=b2):
        c += 1
    if a2 >= b1 and a1 <= b2 or (
        b2 >= a1 and b1 <= a2):
        d += 1
print(c)
print(d)



