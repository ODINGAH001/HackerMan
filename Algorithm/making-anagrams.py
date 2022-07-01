#python3

from collections import Counter
counts = Counter(input())
#print(counts)
counts.subtract(input())
#print(counts)
print(sum(abs(x) for x in counts.values()))



#Input (stdin)

#cde
#abc

#Your Output (stdout)

#Counter({'c': 1, 'd': 1, 'e': 1})
#Counter({'d': 1, 'e': 1, 'c': 0, 'a': -1, 'b': -1})
#4

#Expected Output

#4
