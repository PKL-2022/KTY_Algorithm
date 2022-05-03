import sys

n , m = list(sys.stdin.readline().split())

print(max(int(n[::-1]), int(m[::-1])))
