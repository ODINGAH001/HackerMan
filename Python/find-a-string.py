#python3

import re
str=input()
substr=input()
print(len(re.findall('(?='+substr+')', str)))
