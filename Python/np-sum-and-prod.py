#python

import numpy
a=[]
m,n=map(int,input().split())
for i in range(m):
    row=list(map(int,input().split()))
    a.append(row)
my_array = numpy.array(a)
print(numpy.prod(numpy.sum(my_array, axis = 0)))
