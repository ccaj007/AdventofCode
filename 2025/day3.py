p1 = 0

for line in open(0):
    bank = (list(map(int, line.strip())))
    bank2 = (list(map(int, line.strip())))
    tens = max(bank[:-1])
    ones = max(bank[bank.index(tens) + 1:])
    p1 += tens * 10 + ones

# part 2
    jolts = 0
    p2 = 0
    for index in range(11):
        digit = max(bank2[:index-11])
        bank2 = bank2[bank2.index(digit) + 1:]
        jolts = (jolts * 10) + digit
    jolts = (jolts * 10) + max(bank2)
    p2 += jolts

print(p1)
print(p2)