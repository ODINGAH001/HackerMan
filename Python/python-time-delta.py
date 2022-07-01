#python3

from datetime import datetime

format = "%a %d %b %Y %H:%M:%S %z"
for _ in range(int(input())) :
    t1 = datetime.strptime(input(),format)
    t2 = datetime.strptime(input(),format)
    print(abs(int((t1-t2).total_seconds())))
