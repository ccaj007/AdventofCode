#with open("day1-test.txt") as f:
with open("day1.txt") as f:
    lines = f.read().splitlines()

nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
p1 = p2 = 0

def translate(value):
    for num, name in enumerate(nums):
        value = value.replace(name, f"{name}{num}{name}")
    return value

# for s in lines:
#     good = []
#     for i in s:
#         if i.isnumeric():
#             good.append(i)
#     p1 += (int(good[0]+good[-1]))

# for s in lines:
#     good = []
#     new = translate(s)
#     for i in new:
#         if i.isnumeric():
#             good.append(i)
#     p2 += (int(good[0]+good[-1]))        

for s in lines:
    good = [i for i in s if i.isnumeric()]
    p1 += (int(good[0]+good[-1]))
    good2 = [i for i in translate(s) if i.isnumeric()]
    p2 += (int(good2[0]+good2[-1]))
print(p1)
print(p2)

