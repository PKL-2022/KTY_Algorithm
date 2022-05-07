import sys

n = int(sys.stdin.readline().rstrip())

arr = (list(map(int, sys.stdin.readline().rstrip().split())))

arr2 = sorted(set(arr))

d = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(d[i], end=' ')

# 시간초과
# for i in range(n):
#     for j in range(m):
#         if arr[i] > arr2[j]:
#             result[i] += 1


