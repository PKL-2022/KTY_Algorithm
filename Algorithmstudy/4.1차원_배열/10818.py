import sys
l = [list(map(int,sys.stdin.readline().split())) for _ in range(2)];print(min(l[1]),max(l[1]))


import sys
input = sys.stdin.readline
n = int(input())
m = list(map(int, sys.stdin.readline().split()))
print(min(m), max(m))