# OX퀴즈
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    cnt = 0
    result = 0
    l = list(sys.stdin.readline())
    for i in l:
        if i == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)


"""
한줄씩 입력 받으면 되는걸 한번에 입력받으려고 해서 엄청나게 헤맸다.

"""