#!/bin/python3

n,k = map(int,input().split())
a = list(map(int,input().split()))
count=0
for i in range (n):
    for j in range(i+1,n):
        if((a[i]+a[j])%k==0):
            #print(a[i],a[j])
            count+=1
print(count)
