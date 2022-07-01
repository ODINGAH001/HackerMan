#python3

input()
x=list(map(int,input().split()))
o=False
for p in x:
    if(p>0):
        if(p==int(str(p)[::-1])):
            o=True
    else:
        o=False
print(o)
