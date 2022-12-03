# krkolomne, ale predsa

mustra = {
    'Rock' : 1,
    'Paper' : 2,
    'Scissors' : 3
}

round_result = {
    'loss' : 0,
    'draw' : 3,
    'win' : 6
}

# following is a test string in case you need it:
data="""
A Y
B X
C Z
"""

# or get the data straight from the file:
with open('input.txt', encoding="utf-8") as f:
    data = f.read()

data = data.strip().splitlines()
data = [e.replace(' ', '') for e in data]
data = [tuple(e) for e in data]

score = []
for e in data:
    if e[0]=='A':
        # print("A-Rock vs ", end='')
        if e[1]=='X':
            point1 = mustra["Rock"]
            point2 = round_result["draw"]

        if e[1]=='Y':
            point1 = mustra["Paper"]            
            point2 = round_result["win"]

        if e[1]=='Z':
            point1 = mustra["Scissors"]            
            point2 = round_result["loss"]

        score.append(point1+point2)

    if e[0]=='B':
        # print("B-Paper vs ", end='')
        if e[1]=='X':
            point1 = mustra["Rock"]            
            point2 = round_result["loss"]

        if e[1]=='Y':
            point1 = mustra["Paper"]   
            point2 = round_result["draw"]

        if e[1]=='Z':
            point1 = mustra["Scissors"]    
            point2 = round_result["win"]

        score.append(point1+point2)

    if e[0]=='C': 
        # print("C-Scissors vs ", end='')       
        if e[1]=='X':
            point1 = mustra["Rock"]   
            point2 = round_result["win"]

        if e[1]=='Y':
            point1 = mustra["Paper"]   
            point2 = round_result["loss"]

        if e[1]=='Z':
            point1 = mustra["Scissors"]    
            point2 = round_result["draw"]

        score.append(point1+point2)

print('Part1. Score summed:', sum(score))

# part 2
'''
    'X': 'loss', 
    'Y': 'draw', 
    'Z': 'win'
'''

score = []
for e in data:
    if e[0]=='A':
        # print("A-Rock vs ", end='')
        if e[1]=='X': # prehra
            point1 = mustra['Scissors']
            point2 = round_result["loss"]

        if e[1]=='Y': # remíza
            point1 = mustra['Rock']
            point2 = round_result["draw"]

        if e[1]=='Z': # výhra
            point1 = mustra['Paper']
            point2 = round_result["win"]

        score.append(point1+point2)

    if e[0]=='B':
        # print("B-Paper vs ", end='')
        if e[1]=='X':
            point1 = mustra["Rock"] 
            point2 = round_result["loss"]

        if e[1]=='Y':
            point1 = mustra["Paper"]   
            point2 = round_result["draw"]

        if e[1]=='Z':
            point1 = mustra["Scissors"]  
            point2 = round_result["win"]

        score.append(point1+point2)

    if e[0]=='C': 
        # print("C-Scissors vs ", end='')       
        if e[1]=='X':
            point1 = mustra["Paper"]
            point2 = round_result["loss"]

        if e[1]=='Y':
            point1 = mustra["Scissors"]   
            point2 = round_result["draw"]

        if e[1]=='Z':
            point1 = mustra["Rock"] 
            point2 = round_result["win"]

        score.append(point1+point2)

print('Part2. Score summed:', sum(score))
