import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}
cnt = 0
for _ in range(n):
    i= input().strip()
    dict[i] = dict.get(i, 0)

for _ in range(m):
   cnt += input().strip() in dict


print(cnt)