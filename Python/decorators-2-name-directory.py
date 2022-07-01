#python3

from operator import itemgetter
data = [input().split() for _ in range(int(input()))]
data.sort(key=itemgetter(2))

for name in data:
    if(name[3]=='M'):
        print('Mr.',name[0], name[1])
    else:
        print('Ms.',name[0], name[1])
