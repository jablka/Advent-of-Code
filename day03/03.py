import string

# following is a test string in case you need it:
data = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''

# we already tested it, so let's get the data from file:
with open('input.txt', encoding="utf-8") as f:
    data = f.read()

# we adjust the data:	
data = data.strip().splitlines()

# PART1:
vysledok = 0
for line in data:

    velkost = len(line)
    sl1 = slice(0, velkost//2 )
    sl2 = slice(velkost//2 , velkost)

    for letter in line[sl1]: 
        if (letter in line[sl2]): 
            vysledok += (string.ascii_letters.index(letter)+1)
            break

print(vysledok)

# PART2:
# let's group the data to new list, for better orientation:
grouped = [ ]
for i in range(0, len(data), 3):
    grouped.append( [ data[i], data[i+1], data[i+2] ] )

# let's count the result:
vysledok = 0
for e in grouped:
    for letter in e[0]:
        if (letter in e[1]) and (letter in e[2]):
            vysledok += (string.ascii_letters.index(letter)+1)
            break

print(vysledok)
