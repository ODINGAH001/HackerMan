#python3

import itertools

n=int(input())
S=list(input().split())#sequence of characters
chars = list(range(1,n+1))#creating list of numbers
k=int(input())

indices = [i+1 for i, x in enumerate(S) if x == "a"]#getting the list of index of 'a' in S

chars=list(itertools.combinations(chars, k))
#[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
count=0
#This will check if combinations have 'a' index
for t in chars:#traverse one by one tuple combination in list
    for i in range(len(indices)):#check all the indices with tuple till it found
        if indices[i] in t:
            count+=1#count all the tuple which contains 'a'
            break#if any index is found in tuple 
print(round(count/len(chars),3))
