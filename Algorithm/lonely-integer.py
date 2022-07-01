#python2

from collections import defaultdict

input()
L = list(map(int, raw_input().split(" ")))

d = defaultdict(int)
for i in L:
    d[i] += 1
result = min(d.iteritems(), key=lambda x: x[1])
print result[0]


#python3

