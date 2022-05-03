import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
    l.append(int(sys.stdin.readline().rstrip()))


for index in range(len(l)-1):
    for index2 in range(len(l)-index-1):
        if l[index2] > l[index2+1]:
            l[index2], l[index2+1] = l[index2+1], l[index2]


for i in l:
    print(i)



