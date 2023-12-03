import re

# with open ('day1.txt') as f:
#     data = f.read().splitlines()

# total = 0
# for i in data:
#     nums = re.findall(r'\d', i)
#     combine = int(nums[0] + nums[-1])
#     total += combine

# print(total)

# part 2
numbers = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

if numbers in 'eightwothree':
    print(numbers)
