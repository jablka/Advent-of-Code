import itertools

with open('input.txt') as f:
    s = f.read()

lines = s.strip().splitlines()

my_set = set() # jednotlivé počítače
for line in lines:
    my_set.add(line[:2])
    my_set.add(line[3:])

my_dict = {}
for key in my_set: # ku ktorým je príslušný počítač pripojený
    small_set = set()
    my_dict[key] = small_set
    for line in lines:
        if key in line:
            small_set.add(line[:2])
            small_set.add(line[3:])        
    small_set.remove(key)

trojice = []
for key in my_dict: # hľadanie trojíc
    comb = list(itertools.combinations(my_dict[key],2))
    for a,b in comb:
        if (a in my_dict[b]) or (b in my_dict[a]):
            tr = sorted([key,a,b])
            if tr not in trojice:
                trojice.append(tr)

bag = []
for troj in trojice: # ktoré začínajú na 't'
    for tr in troj:
        if tr.startswith('t'):
            bag.append(troj)
            break

print(len(bag))