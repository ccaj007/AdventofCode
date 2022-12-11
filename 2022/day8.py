visible = 0
#
# # test
#
# raw_data = """
# 30373
# 25512
# 65332
# 33549
# 35390
# """
# test = []
# for row in raw_data.split():
#     r = []
#     for x in row:
#         r.append(int(x))
#     test.append(r)
#
# test2 = list(zip(*test))
#
# for i in range(len(test[0])):
#     for j in range(len(test)):
#         tree = test[i][j]
#         if all(x < tree for x in test[i][0:j]) or \
#             all(x < tree for x in test[i][j+1:]) or \
#             all(x < tree for x in test2[j][0:i]) or \
#             all(x < tree for x in test2[j][i+1:]):
#             visible += 1
#
# print(visible)

with open("day8-input.txt") as f:
    data = f.read().splitlines()

forest = [[int(x) for x in row.strip()] for row in data]
forest2 = list(zip(*forest))

for x in range(len(forest[0])):
    for y in range(len(forest)):
        tree = forest[x][y]
        if all(x < tree for x in forest[x][0:y]) or \
            all(x < tree for x in forest[x][y+1:]) or \
            all(x < tree for x in forest2[y][0:x]) or \
            all(x < tree for x in forest2[y][x+1:]):
            visible += 1

print(visible)