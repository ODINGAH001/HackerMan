#python3

n = int(input())
s = set(map(int, input().split()))
N=int(input())

i=0
op_list=[]#op_list=list()
while i<N:
	x=input().split()
	if(x[0]=='remove'):
		s.remove(int(x[1]))
	elif(x[0]=='discard'):
		s.discard(int(x[1]))
	elif(x[0]=='pop'):
		s.pop()
	i+=1
#print(', '.join(str(number) for number in s))
print(sum(s))
