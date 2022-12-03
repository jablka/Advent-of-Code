
# following is a test string in case you need it:
data='''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

# or get the data straight from the file:
with open('input.txt', encoding="utf-8") as f:
    data = f.read()

data = data.splitlines()

elfs = list()
elf_particular = list()
for line in data:
    if line != '':
        elf_particular.append(int(line))
    else:
        elfs.append(elf_particular)
        elf_particular = list()
elfs.append(elf_particular)

# elfovia
print("počet elfov:", len(elfs))
# print("elfovia:", elfs)

# zosumované
elfs_summed = [ sum(e) for e in elfs ]
# print("zosumované:", elfs_summed)

# najviac nesie:
print("najviac nesie:", max(elfs_summed), "kalórií")

# zoradenie:
elfs_summed.sort(reverse=True)

# top3
print("top3 nesú:", sum(elfs_summed[:3]), "kalórií")
