# the data is actually in CSV format, 
# so we can read it easier with 'csv.reader'

import csv

with open('input.txt', encoding="utf-8") as f:
    data = csv.reader(f)
    splitted_lines = list(data)

pocet_part1 = 0
pocet_part2 = 0
for elf in splitted_lines:
    
    # and again, using csv.reader to split, based on '-' delimiter
    more_split = list(csv.reader(elf, delimiter='-'))

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
