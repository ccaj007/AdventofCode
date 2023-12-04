with open('day2-test.txt') as f:
    lines = f.read().splitlines()

p1 = 0
p2 = 0
for line in lines:
    ok = True
    #print(line)
    game, line = line.split(":")
    game = int(game.split(" ")[1])
    #print(game, line)

    c_dict = {}
    for event in line.split(';'):
        for balls in event.split(','):
            n, color = balls.split()
            n = int(n)
            if n > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                ok = False
            
            if color not in c_dict:
                c_dict[color] = n
            c_dict[color] = max(c_dict[color], n)
    print(c_dict)
    for i in c_dict.values():
        # multiply all values in dictionary
        pass
        
    if ok:
        p1 += game

print(p1)
print(p2)