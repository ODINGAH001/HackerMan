#python3

n=int(input())
numbers = list(map(int, input().split()))
#numbers = [int(n) for n in input().split()]
numbers.sort()
x=numbers.index(numbers[-1])
print(numbers[x-1])
