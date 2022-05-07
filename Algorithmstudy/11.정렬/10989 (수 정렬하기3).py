import sys

n = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

arr1 = [0]*n
result = [0]*n

for i in arr:
    arr1[i] += 1

for i in range(1, len(arr1)):
    arr1[i] += arr1[i-1]

for i in arr:
    result[arr1[i]-1] = i
    arr1[i] -= 1

for i in result:
    print(i)
