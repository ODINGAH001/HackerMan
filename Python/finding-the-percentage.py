#python3
import sys
n=int(input())
i=0
dict={}
while i<n:
	name,math,physics,chemistry = sys.stdin.readline().split()	
	math=float(math)
	physics=float(physics)
	chemistry=float(chemistry)
	dict[name]={}
	dict[name]={'math':math,'physics':physics,'chemistry':chemistry}
	i+=1

#print(dict)
student=input()
i=0
while i<n:
	if(student in dict.keys()):
		print("%.2f"%((dict[student]['math']+dict[student]['physics']+dict[student]['chemistry'])/3))
		break;	
	i+=1
