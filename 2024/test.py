import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "day2.txt")) as f:
    data = f.read().splitlines()


total_safe = 0

for line in data:
    line = [int(x) for x in line.split()]
    safe = True
    damper = 0
    if line[1] < line[0]: # decreasing
        for i in range(1, len(line)):
            if not line[i-1] - line[i] in (1, 2, 3):
                damper += 1
                if damper > 1:
                    safe = False
                    break
                

    elif line[1] > line[0]: # increasing
        for i in range(1, len(line)):
            if not line[i] - line[i-1] in (1, 2, 3):
                damper += 1
                if damper > 1:
                    safe = False
                    break
                
    else:
        safe = False
                
    if safe: 
        total_safe += 1
print(total_safe)