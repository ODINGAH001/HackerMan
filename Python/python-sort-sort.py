import operator
n,m=map(int,input().split())
x=[]
for _ in range(n):
    x.append(list(map(int,input().split())))
#sorted(x, key=operator.itemgetter(int(input())))
c=int(input())
sorted(x, key=lambda a: a[c], reverse=False)
print(x)
