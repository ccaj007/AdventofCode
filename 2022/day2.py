# dict_values = {'X':1, 'Y':2, 'Z':3}
# win = 6
# loss = 0
# tie = 3
# total_score = 0
# total_score_p2 = 0
#
# with open("day2-input.txt") as f:
#     lines = f.read().splitlines()
#
# for turn in lines:
#
#     elf = turn[0]
#     me = turn[2]
#
#     if elf == 'A':
#         if me == 'X':
#             total_score += 4
#         if me == 'Y':
#             total_score += 8
#         if me == 'Z':
#             total_score += 3
#
#     if elf == 'B':
#         if me == 'X':
#             total_score += 1
#         if me == 'Y':
#             total_score += 5
#         if me == 'Z':
#             total_score += 9
#
#     if elf == 'C':
#         if me == 'X':
#             total_score += 7
#         if me == 'Y':
#             total_score += 2
#         if me == 'Z':
#             total_score += 6
#
# # part 2
#
#     if me == 'X':   # need to lose
#         if elf == 'A':
#             total_score_p2 += 3
#         if elf == 'B':
#             total_score_p2 += 1
#         if elf == 'C':
#             total_score_p2 += 2
#
#     if me == 'Y':   # need to TIE
#         if elf == 'A':
#             total_score_p2 += 4
#         if elf == 'B':
#             total_score_p2 += 5
#         if elf == 'C':
#             total_score_p2 += 6
#
#     if me == 'Z':   # need to WIN
#         if elf == 'A':
#             total_score_p2 += 8
#         if elf == 'B':
#             total_score_p2 += 9
#         if elf == 'C':
#             total_score_p2 += 7
#
# print(f"part 1: {total_score}")
# print(f"part 2: {total_score_p2}")

#rounds = open("day2-input.txt").read().split('\n')
with open("day2-input.txt") as f:
    rounds = f.read().splitlines()

# part 1
points = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}
print(f"My score is {sum([points[round] for round in rounds])}.")


# part 2
points = {
    "A X": 0 + 3,
    "A Y": 3 + 1,
    "A Z": 6 + 2,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 0 + 2,
    "C Y": 3 + 3,
    "C Z": 6 + 1,
}
scores = [points[round] for round in rounds]
print(f"My score is {sum([points[round] for round in rounds])}.")