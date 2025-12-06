import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "day3.txt")) as f:
    data = f.read().splitlines()
p1 = 0
p2 = 0

for line in data:
    #for i, j, k in re.findall("(mul\((\d+),(\d{1,3})))", line):
    for i, j, k in re.findall("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", line):
        p1 += int(j) * int(k)

print(p1)
    

