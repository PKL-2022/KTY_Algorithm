import sys

n = int(sys.stdin.readline().rstrip())

l = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

cnt = {}
l.sort()
result = []

cnt = {l[i] : 0 for i in range(n)}
for i in l:
    cnt[i] += 1

for i,j in cnt.items():
    if j == max(cnt.values()):
        result.append(i)


print(round(sum(l)/n))
print(l[n//2])
print(result[0] if len(result)==1 else result[1])
print(abs(l[-1] - l[0]))