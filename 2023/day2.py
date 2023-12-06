with open('day2.txt') as f:
    lines = f.read().splitlines()

p1 = 0
p2 = 0

class cubeSet:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __str__(self):
        return str((self.r, self.g, self.b))
    def __repr__(self):
        return str((self.r, self.g, self.b))
    
    def isSubset(self, other):
        return (self.r <= other.r
                and self.g <= other.g
                and self.b <= other.b)
    
    def max(self, other):
        self.r = max(self.r, other.r)
        self.g = max(self.g, other.g)
        self.b = max(self.b, other.b)

    def power(self):
        return self.r * self.g * self.b 

def parse(reveal):
    colors = ["red", "green", "blue"]
    values = [0]*3
    # 3 red, 5 green, 4 blue
    for token in reveal.split(","):
        # ["3 red", "5 green", "4 blue"]
        for i, color in enumerate(colors):
            if color in token:
                values[i] += int(token.split()[0])
    #return cubeSet(values[0], values[1], values[2])
    return cubeSet(*values)

total = cubeSet(12, 13, 14)
#print(parse("3 blue, 4 red, 15 green"))
p1 = p2 = 0

for line in lines:
    g, x = line.split(":")
    g = int(g.split()[1])
    sets = []
    for reveal in x.split(";"):
        sets.append(parse(reveal))
    if all(s.isSubset(total) for s in sets):
        p1 += g

    maxCubes = cubeSet(0,0,0)
    for s in sets:
        maxCubes.max(s)
        
    p2 += maxCubes.power()
print(p1)
print(p2)

