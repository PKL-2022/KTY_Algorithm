import sys

n = int(sys.stdin.readline().rstrip())
result = 0


if n == 1:
    print('1/1')

else:
    for i in range(1, n+1):

        result += i
        if result >= n:
            if i % 2:
                print(f'{i - (i - (result - n)) + 1}/{i - (result - n)}')
            else:
                print(f'{i - (result - n)}/{i - (i - (result - n)) + 1}')
            break
