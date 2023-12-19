# improved by using enumerate(), 
# and novel use of set() inspired by https://github.com/oliver-ni/advent-of-code/blob/master/py/2022/day06.py

# example string
s = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

# or input file
with open("input.txt", encoding="utf-8") as f:
    s = f.read()

# part1
for t,_ in enumerate(s):
    myset = set(s[t:t+4])
    if len(myset) == 4:
        print("máme:", t+4 ,myset)
        break

# part2
for t,_ in enumerate(s):
    myset = set(s[t:t+14])
    if len(myset) == 14:
        print("máme:", t+14 ,myset)
        break
