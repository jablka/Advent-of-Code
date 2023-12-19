# example string
s = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

# or input file
with open("input.txt", encoding="utf-8") as f:
    s = f.read()

# part1
times = len(s)-4
for t in range(times):
    buffer = s[t:t+4]
    myset = { p for p in buffer }
    if len(myset) == 4:
        print("máme:", t+4 ,myset)
        break

# part2
times = len(s)-14
for t in range(times):
    buffer = s[t:t+14]
    myset = { p for p in buffer }
    if len(myset) == 14:
        print("máme:", t+14 ,myset)
        break
