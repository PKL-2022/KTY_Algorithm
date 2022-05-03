import sys

t = int(sys.stdin.readline())

for _ in range(t):
    f = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    f0 = [x for x in range(1, n+1)]
    for k in range(f):
        for i in range(1, n):
            f0[i] += f0[i-1]
    print(f0[-1])
