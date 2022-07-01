#python3
A=set(map(int,input().split()))
flag=0
for i in range(int(input())):
    B=set(map(int,input().split()))
    if(B<A and len(B)!=len(A))==0:
        flag=1
        break
if(flag==1):
    print('False')
else:
    print('True')
