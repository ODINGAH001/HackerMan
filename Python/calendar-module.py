#python3
import calendar
import sys
m,d,y=sys.stdin.readline().split()
print(calendar.day_name[calendar.weekday(int(y),int(m),int(d))].upper())
