lines = open(0).read().split("\n\n")

elf = []
s = [[int(x) for x in y.split("\n")] for y in lines]
for i in s:
    elf.append(sum(i))

#part 1
print(max(elf))

#part 2
print(sum(sorted(elf)[-3:]))