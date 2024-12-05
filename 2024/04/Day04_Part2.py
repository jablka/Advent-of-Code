s = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''

with open('input.txt') as f:
    s = f.read()

lines = s.splitlines()

## PART2:
counter = 0
for o in range(1,len(lines)-1):
    for i in range(1,len(lines[o])-1):
        if lines[o][i]=='A':
            my_string1 = lines[o-1][i-1] + lines[o][i] + lines[o+1][i+1]
            my_string2 = lines[o+1][i-1] + lines[o][i] + lines[o-1][i+1]
            if (my_string1=='MAS' or my_string1[::-1]=='MAS') and (my_string2=='MAS' or my_string2[::-1]=='MAS'):
                counter+=1
print(counter)