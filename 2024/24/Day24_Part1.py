with open('input.txt') as f:
    s = f.read()

parts = s.strip().split('\n\n')

# parts1:
data = parts[0].splitlines()
tuples = []
for d in data:
    tuples.append(d.split())

values = {}
for tup in tuples:
    values[tup[0][:-1]]=int(tup[1])

# parts2:
data = parts[1].splitlines()
data2 = []
for dat in data:
    # print(dat.split())
    data2.append(dat.split())

def process(dat):
    global values
    if (dat[0] in values) and (dat[2] in values):
        if dat[1]=='AND':
            values[dat[4]] = values[dat[0]] & values[dat[2]]
        if dat[1]=='OR':
            values[dat[4]] = values[dat[0]] | values[dat[2]]
        if dat[1]=='XOR':
            values[dat[4]] = values[dat[0]] ^ values[dat[2]]        
    return 

def check(data2):
    global vsetky
    summa = 0
    for dat in data2:
        if (dat[4] in values) and (dat[0] in values) and (dat[2] in values):
            summa +=1
    if summa == len(data2):
        vsetky = True

vsetky = False
while not vsetky:
    for dat in data2:
        process(dat)
    check(data2)

my_keys = sorted(list(values), reverse=True)

binary_string = ''
for i in my_keys:
    if i.startswith('z'):
        # print(values[i], end='')
        binary_string +=str(values[i])

decimal_number = int(binary_string, 2)
print(decimal_number)
# done!
