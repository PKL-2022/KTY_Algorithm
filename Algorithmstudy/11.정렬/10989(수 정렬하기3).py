import sys

n = int(sys.stdin.readline().rstrip())


arr = [0] * n

for _ in range(n):
    arr[int(sys.stdin.readline().rstrip())] += 1

for i in range(n):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)












# 메모리 초과
# for i in arr:
#     arr1[i] += 1
#
# for i in range(1, len(arr1)):
#     arr1[i] += arr1[i-1]
#
# for i in arr:
#     result[arr1[i]-1] = i
#     arr1[i] -= 1
#
# for i in result:
#     print(i)
