import sys

n = int(sys.stdin.readline())

r = list(sys.stdin.readline().split() for _ in range(n))


for i in range(n):
    for j in r[i][1]:
        print(j * int(r[i][0]), end='')
    print()


