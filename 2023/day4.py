with open("day4-test.txt") as f:
    lines = f.read().splitlines()

for line in lines:
    cards, rhs = line.split(":")
    cards = int(cards.split()[1])
    win, play = rhs.split("|")
    win = win.split()
    play = play.split()
    
    print(cards, win, play)