import sys

n = int(sys.stdin.readline())


result = 0
if n == 1:
    print(1)


else:
    for i in range(1, n):
        result += 6*i
        if result >= n - 1:
            print(i+1)
            break

