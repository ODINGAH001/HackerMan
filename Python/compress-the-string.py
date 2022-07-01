#python3

from itertools import groupby
chars = input()
lst = [list(g) for k,g in groupby(chars)]
for i in lst:
    print(tuple((len(i),int(i[0]))), end = ' ')
