with open("day2-test.txt") as f:
    lines = f.read().splitlines()

class cubeSet():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __str__(self):
        return str((self.r, self.g, self.b))
    
maxCubes = cubeSet(12, 13, 14)

def getCubes(value):
    pass

def parse(value):
    colors = ['red', 'green', 'blue']
    values = [0]*3
    for attempt in value.split(","):

        for n, c in enumerate(colors):
            if c in attempt:
                values[n] += int(attempt.split()[0])
    print(values)
    

for pick in lines:
    n, rhs = pick.split(":")
    n = int(n[-1])
    i = rhs.split(";")
    for g in i:
        parse(g)


