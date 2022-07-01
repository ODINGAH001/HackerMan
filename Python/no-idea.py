#python2

from collections import Counter
nm= map(str,raw_input().split())
arr=map(str,raw_input().split())
A=set(map(str,raw_input().split()))
B=set(map(str,raw_input().split()))
t=Counter(arr)
c=0
for k in set(arr).intersection(A):
    c+=t[k]

for k in set(arr).intersection(B):
    c-=t[k]
print c
