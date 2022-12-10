with open("day10-input.txt") as f:
    data = f.read().splitlines()

register = 1
cycle = 0
total = 0
check_cycles = [20, 60, 100, 140, 180, 220]

for x in data:
    x=x.split()

    if cycle in check_cycles: total += cycle * register
    if x[0] == 'noop':
        cycle += 1
    elif x[0] == 'addx':
        cycle += 1
        if cycle in check_cycles: total += cycle * register
        cycle += 1
        register += int(x[1])

print(total)


X, part1, part2 = 1, 0, '\n'
for cycle, value in enumerate(open('day10-input.txt').read().split(), 1):
    part1 += cycle * X  if cycle%40==20              else 0
    X += int(value) if value[-1].isdigit()           else 0
print(part1)

for cycle, value in enumerate(open('day10-input.txt').read().split(), 1):
    print(cycle, value)