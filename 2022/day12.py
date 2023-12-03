
with open("day12-test.txt") as f:
    data = f.read().splitlines()

r = [[x for x in row.strip()] for row in data]
c = list(zip(*r))

print('a' > 'b')
print('x' > 'q')
print('x' )
