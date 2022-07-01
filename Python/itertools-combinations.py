#python3
from itertools import combinations

S,k=input().split()
x=[]
S = sorted(S)

for i in range(1,int(k)+1):
    x=x+sorted(combinations(S,int(i)))    

for i in x:
    print("".join(i))
