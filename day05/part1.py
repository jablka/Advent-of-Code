#
# prvotné, kostrbaté riešenie.
#

with open('input.txt', encoding="utf-8") as f:
    data = f.read()

# rozdelíme na data[0] a data[1]
data = data.split('\n\n')

s1 = data[0] # first part of the data

# s1='''    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# '''

# data cleaning. 
# replace '[] ' with underscores...
mytable = ''.maketrans("[] ", "___")
s1 = s1.translate(mytable)
# print(s1)

spl = s1.strip().splitlines()

# get the number of stacks
# loop over the the last line. The last digit is 'number_of_stacks'
for i in spl[-1]:
    if i.isdecimal():
        number_of_stacks = int(i) 

# get the number of rows
rows = len(spl)-1 # -1 because the last line is just counter

# 'stacks' will be a list of lists
stacks = [ ]
for i in range(number_of_stacks):
    stacks.append([ ])

# let's fill our stacks
for riadok in range(rows):
    for dalej in range(number_of_stacks):
        dex = 1+(dalej*4)
        if spl[riadok][dex].isalpha():
            # print(" značíme")
            stacks[dalej].append(spl[riadok][dex])
        else:
            # print(" neznačíme")
            pass

# =======
# moves
# =======
s2 = data[1] # second part of the data... contains 'moves data'

# s2='''move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2'''

# data cleaning, so that we get something like this: '3from2to1'
s2 = s2.replace(' ','')
s2 = s2.replace('move','')
moves = s2.strip().splitlines() # list of moves 

# further data cleaning.
# moves_mustra - will contain just the numbers, something like: ['3','2','1']
moves_mustra = [ ]
for e in moves:
    pomocny = ['','',''] # [howmany, from, to]
    ex = e 
    pomocny[2] = ex[-1]
    pomocny[1] = ex[-4]
    pomocny[0] = ex[0]
    if len(ex)==10:
        pomocny[0]=ex[0:2]
        # print(ex[0:2])
    moves_mustra.append(pomocny)

# ======================================
# máme mustry: 'stacks' & 'mustra_moves'
# teraz už len vykonať pohyby
# ======================================

# dôležité otočiť poradie stackov...
for stack in stacks:
    stack.reverse()

for line in moves_mustra: # ['3','2','1']

    howmany = int(line[0]) # line[0] stands for 'how many'
    for h in range(howmany):  

        # line[1] stands for 'what' (or from), but its content needs to be decremented because our lists have zero-based indexing
        tt = stacks[int(line[1])-1].pop() 

        # line[2] stands for 'where' (or to), but its content needs to be decremented because our lists have zero-based indexing
        stacks[int(line[2])-1].append(tt) 

vysledok = ''
for e in stacks:
    vysledok += e.pop()
    # print(e.pop())

print(vysledok)
# HOTOVO!
