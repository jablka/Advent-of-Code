import re

s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open('input.txt') as f:
    s = f.read()

pat = r"(?:mul\((\d{1,3}),(\d{1,3})\))|(don't\(\))|(do\(\))"

found = re.findall(pat,s)
# found

res = 0
rob = True
for i in found:
    if ("don't()" in i) or ("do()" in i):
        if ("don't()" in i):
            rob = False
        else:
            rob = True
    else:
        multiplied = int(i[0])*int(i[1])
        if rob:
            res += multiplied
print(res)