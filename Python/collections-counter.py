#python3

from collections import Counter

input()
X=Counter(list(map(int,input().split())))
price=0
n=int(input())
for _ in range(n):
    size,p=map(int,input().split())
    if(X[size]!=0):
        X[size]-=1
        price+=p
print(price)
