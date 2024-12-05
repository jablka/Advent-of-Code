from itertools import combinations

with open('input.txt') as f:
    s = f.read()

rules , data = s.split('\n\n')

rules = rules.splitlines()
bag = []
for rule in rules:
    l = rule.split('|')
    l = (int(l[0]),int(l[1]))
    bag.append(l)
rules = bag

data = data.splitlines()
bag = []
for d in data:
    l = d.split(',')
    l2 = []
    for number in l:
        l2.append(int(number))
    bag.append(l2)
data=bag

### Part1:
###
res = 0
# poďme všetky riadky:
for dat in data:
    # poďme porovnať prvý data riadok
    flag = True
    for n,i in combinations(dat,2):
        for r in rules:
            if (n in r) and (i in r):
                n_index = dat.index(n)
                i_index = dat.index(i)
                if (n_index<i_index):
                    if r.index(n)<r.index(i):
                        ...
                    else:
                        flag = False
    # print(flag)
    if flag:
        # print(dat[(len(dat)//2)])
        res+=dat[(len(dat)//2)]
print('Part1:',res)

### Part2:
###
zle = [] # zlé si vyfiltrujeme
# poďme všetky riadky:
for dat in data:
    # poďme porovnať prvý data riadok
    flag = True
    for n,i in combinations(dat,2):
        for r in rules:
            if flag==True:
                if (n in r) and (i in r):
                    n_index = dat.index(n)
                    i_index = dat.index(i)
                    if (n_index<i_index):
                        if r.index(n)<r.index(i):
                            ...
                        else:
                            flag = False
                            zle.append(dat)
                            break

def procedura(zle_c):
    # poďme porovnať prvý data riadok
    flag = True
    for n,i in combinations(zle_c,2):
        for r in rules:
            if flag==True:
                if (n in r) and (i in r):
                    n_index = zle_c.index(n)
                    i_index = zle_c.index(i)
                    if (n_index<i_index):
                        if r.index(n)<r.index(i):
                            ...
                        else:
                            flag = False
                            swap1 = zle_c[i_index]
                            swap0 = zle_c[n_index]
                            zle_c[n_index] = swap1
                            zle_c[i_index] = swap0
                            procedura(zle_c)
                            return
    # print(flag, zle_c)
    bag.append(zle_c)
    return

# ideme riešiť zlé:
bag = []
for c in range(len(zle)):
    procedura(zle[c])

res = 0
for dat in(bag):
    res+=dat[(len(dat)//2)]
print('Part2:',res)