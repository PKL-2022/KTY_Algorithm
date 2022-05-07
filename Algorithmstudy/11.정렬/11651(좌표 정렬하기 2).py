import sys

n = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
arr2=[]


for i in arr:
    arr2.append(i[::-1])

arr2.sort()
arr3=[]
for i in arr2:
    arr3.append(i[::-1])

for i,j in arr3:
    print(i, j)


