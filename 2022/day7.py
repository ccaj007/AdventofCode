from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)

for line in open("day7-input.txt").read().splitlines():
    match line.split():
        case "$", "cd", "/":
            path = ["/"]
        case "$", "cd", "..":
            path.pop()
        case "$", "cd", dir:
            path.append(dir + "/")
        case "$" | "dir", *_:
            continue
        case size, _:
            for p in accumulate(path):
                dirs[p] += int(size)

print(sum(sizd:
e for size in dirs.values() if size <= 100000))