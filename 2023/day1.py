#import re
digit_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open ('day1.txt') as f:
    data = f.read().splitlines()

total1 = 0
total2 = 0

def translate(line):
    for num, name in enumerate(digit_names):
        line = line.replace(name, f"{name}{num}{name}")
    return line

# for i in data:
#     nums = re.findall(r'\d', i)    
#     combine = int(nums[0] + nums[-1])
#     total += combine

for line in data:
    # digits = []
    # for char in line:
    #     if char.isnumeric():
    #         digits.append(char)
    digits = [char for char in line if char.isnumeric()]
    total1 += int(digits[0]+digits[-1])

    digits2 = [char for char in translate(line) if char.isnumeric()]
    total2 += int(digits2[0] + digits[-1])
    
print(total1)
print(total2)


