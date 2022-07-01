#python3
import re

emails=[]

for _ in range(int(input())):
    x= input()
    if re.match(r"^[A-Za-z][-\w]*@[A-Za-z0-9]+\.[A-Za-z]{1,3}$",x):
        emails.append(x)
emails.sort()        
print(emails)
