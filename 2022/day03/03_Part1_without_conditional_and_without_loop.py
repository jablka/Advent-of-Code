# Day03 Part1 solution
# experimental version 
# without any conditional
# without any loop
#

import string

# following is a test string in case you need it:
data = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

# or get the data straight from the file:
with open('input.txt', encoding="utf-8") as f:
    data = f.read()

data = data.strip().splitlines()

# mapa:
mydict = { j:i for i,j in enumerate(string.ascii_letters, 1) }

# pole riadkov rozdelených na dve časti
pole = [ ((line[:(len(line)//2)]), (line[(len(line)//2):])) for line in data ]

# pole prienikov dvoch častí 
pole2 = [ ''.join(set(line[0]).intersection(set(line[1]))) for line in pole]

# číselná reprezentácia prienikov
pole3 = [ mydict[n] for n in pole2 ]

# sumár číselnej reprezentácie prienikov
print(sum(pole3))
