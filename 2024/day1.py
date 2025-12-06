import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, "day1.txt")) as f:
    lines = f.read().splitlines()

list1, list2 = [], []
total = 0

for i in lines:
    j = i.split()
    list1.append(int(j[0]))
    list2.append(int(j[1]))

list1.sort()
list2.sort()

total = sum(abs(l - r) for l, r in zip(list1, list2))
print(total)

# part 2

with open(os.path.join(__location__, "day1-2.txt")) as f:
    lines = f.read().splitlines()

list1=[]
list2=[]
part2 = 0
for i in lines:
    j = i.split()
    list1.append(int(j[0]))
    list2.append(int(j[1]))

for i in list1:
    count = 0
    for j in list2:
        if i == j:
            count += 1
    part2 += count*i

print(part2)

from collections import Counter

total2 = 0
right_counter = Counter(list2)
# print(right_counter)
# for left_value in list1:
#     total2 += left_value * right_counter[left_value]
total2 = sum(left_value * right_counter[left_value] for left_value in list1)

print(total2)