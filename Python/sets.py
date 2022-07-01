input()
first=set(map(int,input().split()))
input()
second=set(map(int,input().split()))
diff=first.symmetric_difference(second)
for n in sorted(list(diff)):
    print(n)
