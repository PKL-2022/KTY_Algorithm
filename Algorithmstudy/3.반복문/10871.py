# X보다 작은수
import sys
n, x = map(int, sys.stdin.readline().split())
A = list(map(int, input().split()))
for i in A:
    if i<x:print(i, end=" ")