with open("day3-test.txt") as f:
    lines = f.read().splitlines()

P = complex
adj = [P(-1,1), P(0,1), P(1,1),
       P(-1,0),         P(1,0),
       P(-1,-1), P(0,-1), P(1,-1)]

def getAdjParts(grid, pos):
    for d in adj:
        print(pos+d)

grid = {}
symbols = []

for y, line in enumerate(lines):
    for x, v in enumerate(line):
#        print(x, y, v)
        if v != '.':
            grid[P(x,y)] = v
            if not v.isnumeric():
                symbols.append(P(x,y))



#print(grid)
#print(symbols)
getAdjParts(grid, P(3,1))