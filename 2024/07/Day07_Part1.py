import itertools

s = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''

with open('input.txt') as f:
    s = f.read()

s = s.replace(':','')

lines = s.splitlines()

arr = []
for line in lines:
    li = line.split()
    # li = [ int(i) for i in li ]
    arr.append(li)

# # celý cyklus
result = 0
for index in range(len(arr)):
    this_array = arr[index][1:]
    eval_against = int(arr[index][0])
    how_many = len(arr[index][1:])-1  
    for prip in itertools.product(['+','*'],repeat=how_many):
        my_string = ''
        for n,p in enumerate(prip):
            if n==0:
                my_string += '('+this_array[n]+p
            else:
                my_string = '('+my_string+this_array[n]+')'+p
        my_string += this_array[n+1]+')'
        if eval(my_string)==eval_against:
            result += eval_against
            break

print(result)