f = open("day1.txt")
depths = [int(x) for x in f]
increases = sum(x < y for x, y in zip(depths, depths[1:]))
print(increases)

# for i, j in zip(depths, depths[1:]):
#    print(i)
#    print(j)

# part 2

# We don't need to sum the elements, because comparing:
#  depths[i] + depths[i+1] + depths[i+2] < depths[i+1] + depths[i+2] + depths[i+3]
# has the same resuts as comparing:
#  depths[i] < depths[i+3]
# sliding window algorithm; the only differences are i and i+3; i+1 and i+2 are common

increase2 = sum(x < y for x, y in zip(depths, depths[3:]))
print(increase2)