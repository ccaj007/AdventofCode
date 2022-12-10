with open("day6-input.txt") as f:
    data = f.read()
#test
#data = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'

for size in (4, 14):
    for i in range(size,len(data)):
        if len(set(data[i - size : i])) == size:
            print(i)
            break

# # part 2
# for i in range(0,len(data)-4):
#     if(len(set(data[i:i+14]))) == 14:
#         print(f"part 1: {i+14}")
#         break


