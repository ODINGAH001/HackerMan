input(),
A=set(map(int,input().split()))

for _ in range(int(input())):
    command=input().split()[0]
    B=set(map(int,input().split()))
    getattr(A, command)(B)
    
print(sum(A))
