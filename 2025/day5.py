# https://adventofcode.com/2025/day/5

ranges, numbers = open(0).read().split("\n\n")

ranges = [list(map(int, r.split("-"))) for r in ranges.splitlines()]
numbers = list(map(int, numbers.splitlines()))
count = 0
for number in numbers:
    for low, hi in ranges:
        if low <= number <= hi:
            count += 1
            break

print(count)