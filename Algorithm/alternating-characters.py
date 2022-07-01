#python3

from itertools import groupby
n=int(input())
for j in range(n):
    chars = input()
    lst = [list(g) for k,g in groupby(chars)]
    count=0
    for i in lst:
        if(len(i)>1):
            count+=len(i)-1
    print(count)            
