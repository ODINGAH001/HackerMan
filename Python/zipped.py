#python3

col,row=map(int,input().split())
x=[]
for _ in range(row):
    x.append(list(map(float,input().split())))
for i in range(col):
    sums=0
    for j in range(row):
        sums=sums+x[j][i]
    print(sums/row)
