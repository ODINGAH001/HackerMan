#python3
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item_name,x,net_price=input().rpartition(' ')
    d[item_name] = d.get(item_name, 0) + int(net_price)
for item_name, net_price in d.items():
    print(item_name, net_price)
