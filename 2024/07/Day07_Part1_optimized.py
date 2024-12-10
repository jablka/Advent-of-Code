import itertools
import operator

with open('input.txt') as f:
    s = f.read()

s = s.replace(':','')

lines = s.splitlines()

arr = []
for line in lines:
    li = line.split()
    li = [ int(i) for i in li ]
    arr.append(li)

def my_eval(arr,my_list): # [11,6,16,20], ['+','*','+',]
    index = 0
    accum = arr[0]
    while index<len(my_list):
        if my_list[index]=='+':
            oper = operator.add
        else:
            oper = operator.mul
        accum = oper(accum,arr[index+1])
        index +=1
    return accum

# # celý cyklus
result = 0
for index in range(len(arr)):
    eval_against = arr[index][0]
    this_array = arr[index][1:]
    how_many = len(arr[index][1:])-1  
    for prip in itertools.product(['+','*'],repeat=how_many):
        my_list = [ p for p in prip ]
        if my_eval(this_array,my_list)==eval_against:
            result += eval_against
            break        

print(result)