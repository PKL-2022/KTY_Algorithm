import sys

n = int(sys.stdin.readline().rstrip())
arr = [[sys.stdin.readline().rstrip().split(), i] for i in range(n)]


arr.sort(key=lambda x: (int(x[0][0]), x[1]))

for i in arr:
    print(*i[0])