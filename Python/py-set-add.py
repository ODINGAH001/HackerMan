#python3

n=int(input())
country=[]
for _ in range(n):
    country.append(input())
print(len(set(country)))
