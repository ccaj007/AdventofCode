total = 0

for line in open(0):
    bank2 = (list(map(int, line.strip())))
    jolts = 0
    for index in range(11):
        digit = max(bank2[:index-11])
        bank2 = bank2[bank2.index(digit) + 1:]
        jolts = (jolts * 10) + digit
    jolts = (jolts * 10) + max(bank2)
    total += jolts

print(total)