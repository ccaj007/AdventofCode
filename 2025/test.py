#ranges = [list(map(int, item.split("-"))) for item in input().split(",")]
count = 0
dial = 50

grid = [for line in open(0)]
print(grid)
# for line in open(0):
#     i = line[0]
#     mov = int(line[1:])
#     dir = 1 if i == "R" else -1
#     new_dial = (dial + (dir * mov)) % 100
#     if i == "R" and new_dial > dial:
#         count += 1
#     if i == "L" and new_dial < dial:
#         count += 1
#     dial = new_dial




# print(count)
