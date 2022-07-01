#python3
import string

size = int(input())
alphabet = string.ascii_lowercase

def part():
    row = ["-"] * (size * 2 - 1)
    for j in range(0, size - i):
        row[size - 1 - j] = alphabet[j + i]
        row[size - 1 + j] = alphabet[j + i]
    print("-".join(row))
    return

for i in range(size - 1, 0, -1):
    part()

for i in range(0, size):
    part()
