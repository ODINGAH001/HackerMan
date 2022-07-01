#python3

from collections import deque
d=deque()
for _ in range(int(input())):
    d.clear()
    n=int(input())
    l=input().split()
    d.extend(l)
    for _ in range(len(l)):
        if(d.pop()==d.popleft()):
            print("NO")
            continue
        else:
            print("NO")
            break
