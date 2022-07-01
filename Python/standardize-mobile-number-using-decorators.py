#python3

data = [input()[-10:] for _ in range(int(input()))]
data.sort()
for mob in data:
    print('+91', mob[0:5], mob[5:])
