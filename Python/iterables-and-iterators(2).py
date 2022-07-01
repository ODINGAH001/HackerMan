#python3

from itertools import combinations

N = int(input())
L = input().split()
K = int(input())

C = list(combinations(L, K))

F = filter(lambda c: 'a' in c, C)
print(round(len(list(F))/len(C),3))
