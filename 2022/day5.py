c1 = ['Z','J','G']
c2 = ['Q','L','R','P','W','F','V','C']
c3 = ['F','P','M','C','L','G','R']
c4 = ['L','F','B','W','P','H','M']
c5 = ['G','C','F','S','V','Q']
c6 = ['W','H','J','Z','M','Q','T','L']
c7 = ['H','F','S','B','V']
c8 = ['F','J','Z','S']
c9 = ['M','C','D','P','F','H','B','T']
containers = {1:c1, 2:c2, 3:c3, 4:c4, 5:c5, 6:c6, 7:c7, 8:c8, 9:c9}

with open("day5-input.txt") as f:
    data = f.read().splitlines()
# num = []
# source = []
# destin = []

def pop_crate(n,orig, dest):
    for i in range(n):
        push_crate(dest, orig.pop())

def push_crate(dest, orig):
    dest.append(orig)

for i in data:
    cmd = i.split()
    # num.append(cmd[1])
    # destin.append(cmd[5])
    # source.append(cmd[3])
    num = cmd[1]
    destin = containers[int(cmd[5])]
    source = containers[int(cmd[3])]
    pop_crate(int(num), source, destin)

print(c1[-1],c2[-1], c3[-1], c4[-1], c5[-1], c6[-1], c7[-1], c8[-1], c9[-1])

#part 2

c1 = ['Z','J','G']
c2 = ['Q','L','R','P','W','F','V','C']
x = (c2[-2:])
print(x)
print(c1.append(x))
print(c1)
print(c1[-1])