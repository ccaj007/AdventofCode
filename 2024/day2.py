import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "day2.txt")) as f:
    data = f.read().splitlines()

total_safe = 0
for i, line in enumerate(data):
    line = [int(x) for x in line.split()]
    safe = True
    damper = 0
    if line[1] < line[0]: # decreasing
        for j in range(1, len(line)):
            #if j > 0:
            if not ((line[j] - line[j-1]) in [-1, -2, -3]):
                damper += 1
                if damper > 1:
                    safe = False
                    break
                
    elif line[1] > line[0]: # increasing
        for j in range(1, len(line)):
            if not((line[j] - line[j-1]) in [1, 2, 3]):
                damper += 1
                if damper > 1:
                    safe = False
                    break
    else: # this means the second and first number are the same
        safe = False

    if safe:
        total_safe += 1


print(total_safe)
        