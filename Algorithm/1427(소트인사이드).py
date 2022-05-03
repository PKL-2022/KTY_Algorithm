import sys

n = (list(sys.stdin.readline().rstrip()))
r= []
for i in n:
    r.append(i)

r.sort(reverse=True)

for i in r:
    print(i, end='')