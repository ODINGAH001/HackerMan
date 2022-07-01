#python3

t=int(input())
for _ in range(t):
    n,m,s=map(int,input().split())
    if(m+s > n):
        p=(m+s)%n-1
    else:
        p=m+s-1
    print(n) if p==0 else print(p)
