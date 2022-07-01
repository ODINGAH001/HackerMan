#python3

import numpy
a = numpy.array(input().split(),float)
for e in ['floor','ceil','rint']:
	print(getattr(numpy,e)(a))
