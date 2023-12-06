with open('day3.txt') as f:
    lines = f.read().splitlines()

P = complex
adj = [P(-1,1), P(0,1), P(1,1),
       P(-1,0),         P(1,0),
       P(-1,-1), P(0,-1), P(1,-1)]

def getNum(grid, pos):
    if pos not in grid or not grid[pos].isnumeric():
        return None
    while pos-1 in grid and grid[pos-1].isnumeric():
        pos -= 1
    start = pos
    num = ""
    while pos in grid and grid[pos].isnumeric():
        num+=grid[pos]
        pos+=1
    return start, int(num)

def getAdjParts(grid, pos):
    parts = set()
    for d in adj:
        parts.add(getNum(grid, pos+d))
        #print(pos+d)
    return parts-{None}

def p1(grid, symbols):
    parts = set()
    for s in symbols:
        parts|=getAdjParts(grid,s)
    p1 = 0
    for p in parts:
        p1+=p[1]
    return p1

def p2(grid, symbols):
    ans = 0
    for s in symbols:
        if grid[s] != '*': continue
        parts = list(getAdjParts(grid, s))
        if len(parts) == 2:
            ans += parts[0][1]*parts[1][1]
    return ans

grid = {}
symbols = []
for y, line in enumerate(lines):
    for x, v in enumerate(line):
    #     print(x,y,v)
        if v != '.':
            grid[P(x,y)] = v
            if not v.isnumeric():
                symbols.append(P(x,y))                    
    # print(y, line)

#print(grid, symbols)
#print(getAdjParts(grid, P(3,1)))
print(p1(grid, symbols))
print(p2(grid, symbols))


