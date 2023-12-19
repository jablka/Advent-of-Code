# First I wanted to adjust my original code and replace "if" statements with "match~case" statements.
# But it turned out it can be made without any conditional ever!
#
# I think it's called functional programming, right? :)
# Let's go!

# following is a test string in case you need it:
data="""
A Y
B X
C Z
"""

# or get the data straight from the file:
with open('input.txt', encoding="utf-8") as f:
    data = f.read()

# savvy idea, to use string.translate()
mytable = ''.maketrans("AXBYCZ", "RRPPSS", " ")
data = data.translate(mytable)
data = data.strip().splitlines()

# points for particular "round entry"
mustra = {
    'Rock' : 1,
    'Paper' : 2,
    'Scissors' : 3
}

# points for particular round result
round_result = {
    'loss' : 0,
    'draw' : 3,
    'win' : 6
}

truth_table = {
    'RR': round_result['draw'] + mustra['Rock'],
    'RP': round_result['win'] + mustra['Paper'],
    'RS': round_result['loss'] + mustra['Scissors'],

    'PR': round_result['loss'] + mustra['Rock'],
    'PP': round_result['draw'] + mustra['Paper'],
    'PS': round_result['win'] + mustra['Scissors'],

    'SR': round_result['win'] + mustra['Rock'],
    'SP': round_result['loss'] + mustra['Paper'],
    'SS': round_result['draw'] + mustra['Scissors']    
    }

points = [truth_table[e] for e in data]
print('Part1:', sum(points))

# part 2
''' second letter now means the round outcome
    'X': 'loss', 
    'Y': 'draw', 
    'Z': 'win'
'''

# so we modify our truth table
truth_table = {
    'RR': round_result['loss'] + mustra['Scissors'],
    'RP': round_result['draw'] + mustra['Rock'],
    'RS': round_result['win'] + mustra['Paper'],

    'PR': round_result['loss'] + mustra['Rock'],
    'PP': round_result['draw'] + mustra['Paper'],
    'PS': round_result['win'] + mustra['Scissors'],

    'SR': round_result['loss'] + mustra['Paper'],
    'SP': round_result['draw'] + mustra['Scissors'],
    'SS': round_result['win'] + mustra['Rock']    
    }

points = [truth_table[e] for e in data]
print('Part2:', sum(points))
