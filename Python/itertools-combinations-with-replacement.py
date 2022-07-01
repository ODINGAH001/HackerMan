#python3

from itertools import combinations_with_replacement
S,k=input().split()
S=sorted(S)
x=[]
x=sorted(combinations_with_replacement(S,int(k)))

for i in x:
    print("".join(i))
