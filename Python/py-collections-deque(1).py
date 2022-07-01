#python3

from collections import deque
d=deque()
for _ in range(int(input())):
    op=input().split()
    getattr(d,op[0])(*[op[1]] if len(op) > 1 else [])
print(*[item for item in d])
