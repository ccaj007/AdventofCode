#with open("day4-test.txt") as f:
with open("day4.txt") as f:
    lines = f.read().splitlines()

p1 = p2 = 0

def winner(n):
    _, rhs = line.split(":")
    win, play = rhs.split("|")
    win = win.split()
    play = play.split()
    t = len((set(win) & set(play)))
    return t

for line in lines:
    t = winner(line)
    p1 += int(2**(t-1))

print(p1)

# PART 2 TOO CONFUSING; DIDN'T DO
