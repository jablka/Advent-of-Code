
# following is a test string in case you need it:
data='''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''

# or get the data straight from the file:
with open('input.txt', encoding="utf-8") as f:
    data = f.read()

data = data.strip().splitlines()

line_splitted = [ ]
for e in data:
    line_splitted.append(e.split(','))

pocet_part1 = 0
pocet_part2 = 0
for elf in line_splitted:
    more_split = [ ]    
    more_split.append(elf[0].split('-'))
    more_split.append(elf[1].split('-'))

    rozsah1 = range( int(more_split[0][0]), int(more_split[0][1])+1 )
    rozsah2 = range( int(more_split[1][0]), int(more_split[1][1])+1 )

    mn1 = set ( [ x for x in rozsah1 ] )
    mn2 = set ( [ x for x in rozsah2 ] )

    # calculation of Part1
    if mn1.issubset(mn2) or mn1.issuperset(mn2):
        pocet_part1 += 1

    # calculation of Part2
    if mn1.intersection(mn2):
        pocet_part2 +=1

print(pocet_part1)
print(pocet_part2)
