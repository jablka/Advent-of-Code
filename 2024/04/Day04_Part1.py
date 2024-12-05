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

# procedura vpravo_vlavo
def vpravo_vlavo(lines):
    counter = 0
    for line in lines:
        for i in range(len(line)):
            if line[i:i+4] == 'XMAS':
                counter += 1
                
            rev_line = line[::-1]
            if rev_line[i:i+4] == 'XMAS':
                counter += 1
    return counter

# '-' horizontalne:
counter = 0
counter += vpravo_vlavo(lines)

## '|' vertikalne:
# otáčam matrix:
new_lines = []
for o in range(len(lines[0])):
    new_s = ''
    for i in range(len(lines)):
        new_s += lines[i][o]
    new_lines.append(new_s)
counter += vpravo_vlavo(new_lines) # volám procedúru s otočeným matrixom

## šikmo "/" (14~8 hod. ciferník)
for o in range(0,len(lines)-3):
    for i in range(3,len(lines[o])):
        my_string = lines[o][i]+lines[o+1][i-1]+lines[o+2][i-2]+lines[o+3][i-3]
        if my_string=='XMAS' or my_string[::-1]=='XMAS':
            counter+=1

## šikmo "\" (10~16 hod. ciferník)
for o in range(0,len(lines)-3):
    for i in range(0,len(lines)-3): 
        my_string = lines[o][i] +lines[o+1][i+1] +lines[o+2][i+2] +lines[o+3][i+3]
        if my_string=='XMAS' or my_string[::-1]=='XMAS':
            counter+=1
print(counter)
