max_elf = 0
current_elf = 0
all_elf = []
with open("day1-data.txt") as f:
    for line in f:
        if line == '\n':
            all_elf.append(current_elf)
            #max_elf = max(max_elf, current_elf)
            current_elf = 0
            continue
        try:
            cals = int(line)
        except Exception:
            raise Exception(f'line {line} not a valid positive number')
        current_elf += cals
#part 1
print(max(all_elf))

# part 2
sorted_elfs = sorted(all_elf)
print(sum(sorted_elfs[-3:]))
