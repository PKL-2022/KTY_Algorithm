import sys

n = int(sys.stdin.readline().rstrip())


arr = set([sys.stdin.readline().rstrip() for _ in range(n)])

result = [[i, len(i)] for i in arr]

result.sort(key=lambda x:(x[1], x[0]))

for i, _ in result:
    print(i)