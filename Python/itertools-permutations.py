#python3

from itertools import permutations
string,p=input().split()
lex=sorted(list(permutations(string,int(p))))
for i in lex:
    print("".join(i))

#Sample Input

#HACK 2

#Sample Output

#AC
#AH
#AK
#CA
#CH
#CK
#HA
#HC
#HK
#KA
#KC
#KH

