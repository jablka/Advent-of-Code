s = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''

with open('input.txt') as f:
    s = f.read()

lines = s.splitlines()

arr = []
for line in lines:
    my_arr = line.split()
    my_arr = list(map(int,my_arr))
    arr.append(my_arr)
# arr

# len(arr)

if arr[0]==sorted(arr[0]) or arr[0]==sorted(arr[0],reverse=True):
    print("true")

res = 0
for i in range(len(arr)):
    if arr[i]==sorted(arr[i]) or arr[i]==sorted(arr[i],reverse=True):
        styri = []
        for j in range(len(arr[i])-1):
            delta = abs(arr[i][j]-arr[i][j+1])
            if delta>=1 and delta<=3:
                styri.append(True)
            else:
                styri.append(False)
        if all(styri):
            res+=1
print(res)