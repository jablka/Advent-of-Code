# improved, elegant version
# thanks to @JakubDotPy for inspiration:
# implemented: regex search, map(), and enumerate()

import re

with open('input.txt', encoding="utf-8") as f:
    data = f.read()

# rozdelíme na data[0] a data[1]
data = data.split('\n\n')

# first part of the data
s_lines = data[0].splitlines()

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# 'number_of_stacks' is the second character from the end, in the last line.
number_of_stacks = int(s_lines[-1][-2])

# 'stacks' will be a list of lists
stacks = [ [] for i in range(number_of_stacks) ]

# let's fill our stacks
for riadok in s_lines:
    for i,pismeno in enumerate(riadok[1::4]):
        if pismeno.isalpha():
            stacks[i].append(pismeno)

# =======
# moves
# =======

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2

# data[1] # second part of the data... contains 'moves data'
moves = data[1].strip().splitlines() # list of moves 

# moves_mustra - will contain just the numbers, something like: [3,2,1]
moves_mustra = [ ]
for e in moves:
    najdene = re.findall('\d+', e)
    moves_mustra.append( list(map(int, najdene)) ) # [howmany, from, to]

# ======================================
# máme mustry: 'stacks' & 'mustra_moves'
# teraz už len vykonať pohyby
# ======================================

# stacks need to be reversed, because we have read them from top-to-bottom
for stack in stacks:
    stack.reverse()

for line in moves_mustra: # [3,2,1]
    howmany = line[0] # line[0] stands for 'how many'
    for h in range(howmany):  
        # line[1] stands for 'what' (or from), but its content needs to be decremented because our lists have zero-based indexing
        # line[2] stands for 'where' (or to), but its content needs to be decremented because our lists have zero-based indexing
        stacks[line[2]-1].append( stacks[line[1]-1].pop() ) 

vysledok = ''
for e in stacks:
    vysledok += e.pop()
    # print(e.pop())

print(vysledok)
# HOTOVO!
