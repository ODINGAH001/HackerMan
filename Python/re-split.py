#python3

import re
x=re.split(r",|\.",input())
print(*[item for item in x if len(item.strip())>0],sep='\n')
