#python3

import numpy
n, m = map(int, input().split())

A = numpy.array([input().split() for _ in range(n)], int)
B = numpy.array([input().split() for _ in range(n)], int)

for op in (A+B, A-B, A*B, A//B, A%B, A**B):
    print(op)
