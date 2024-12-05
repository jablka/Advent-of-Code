import re

s = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

with open('input.txt') as f:
    s = f.read()

pat = r"mul\((\d{1,3}),(\d{1,3})\)"

found = re.findall(pat,s)
# len(found)

res = 0
for i in found:
    res += int(i[0])*int(i[1])
print(res)