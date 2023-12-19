# solution for Day03, Part1:
#
# using set() and enumerate(),
# and without any 'if' or 'match~case' statement!
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

# adjust the data:
data = data.strip().splitlines()

# enumerate letters
mydict = { j:i for i,j in enumerate(string.ascii_letters, 1) }

pole = [ ]
for line in data:

    # divide the line into two sets
    set1 = set(line[:(len(line)//2)])
    set2 = set(line[(len(line)//2):])

    # if intersection found, map it with the value in our dictionary, and append to array.
    pole.append(mydict[''.join(set1.intersection(set2))]) 

# summarize the array
print(sum(pole))
