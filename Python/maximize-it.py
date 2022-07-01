#python3

from itertools import product
K,M = map(int,input().split())
LL = list()
for i in range(K):
    L=list(map(int,input().split()))
    L = [int(x)**2 for x in L[1:]]#find square of each element in i'th list
    LL.append(L)
    
P = list(product(*LL))#produce permutations
SS = list()
for j in P:
    S = sum(j) % M#find S
    SS.append(S)#make a list of solutions of max S
print(int(max(SS))) # select one of max S
